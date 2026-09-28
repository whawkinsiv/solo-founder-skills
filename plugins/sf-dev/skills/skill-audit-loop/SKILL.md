---
name: skill-audit-loop
description: Measure whether an existing Claude Code skill actually works, then fix it from evidence instead of by inspection. Use this whenever someone asks if a skill is working, wants to test, audit, benchmark, or evaluate a skill, says a skill is being ignored or fires when it shouldn't, wants an A/B comparison of results with and without a skill, wants to turn a real session where a skill misbehaved into a regression case, or wants to revise a SKILL.md and doesn't want to guess at the edit. Also use when a skill "seems fine" but nobody has actually checked. For drafting a brand-new skill from nothing, use skill-creator instead, then come back here once a draft exists.
---

# Skill audit loop

Skills are prompts, and prompts fail quietly. A skill can look excellent and still be
ignored half the time, or be followed exactly and still produce worse output than no
skill at all. You cannot see either of those by reading the SKILL.md. You see them by
running the skill against fixed tasks, comparing against a run without it, and reading
what the agent actually did.

This skill runs that loop:

1. **Collect cases** — real sessions where the skill was used, plus a few constructed ones.
2. **Write checks** — before touching the skill. The checks are the specification.
3. **Run the matrix** — every case, every arm, several repetitions.
4. **Read the evidence** — pass rates, cost, and the trace of what the agent did.
5. **Revise once, verify, keep or revert** — one hypothesis per round, with the user's sign-off.

The loop is not optional at step 5. A revision that isn't re-measured is just another
guess with more words in it.

## Before running anything

Settle the auth question first, because it decides both what the runs cost and whether
the comparison means anything.

**Pick one of two configurations.** They trade the same thing in opposite directions.

*API key, bare mode* — `"auth": "api_key"`, `"bare": true`. `--bare` skips
auto-discovery of hooks, skills, plugins, MCP servers, memory, and CLAUDE.md, so the
baseline arm is genuinely skill-free and the with-skill arm gets exactly one skill: the
one under test, staged into an `--add-dir` directory. This is the cleanest isolation
available. It bills per token, and bare mode never reads OAuth credentials, the system
keychain, or `CLAUDE_CODE_OAUTH_TOKEN` — so a subscription cannot be used here at all.
Bare sessions also carry a smaller tool set.

*Subscription, dedicated profile* — `"auth": "subscription"`, `"bare": false`,
`"config_dir": "~/.claude-audit"`. `CLAUDE_CONFIG_DIR` gives Claude Code a separate
profile with its own credentials, settings, skills, hooks, and MCP servers. Log into it
once and every run is isolated *and* covered by the subscription:

```bash
CLAUDE_CONFIG_DIR=~/.claude-audit claude auth login
```

Two things to watch. `CLAUDE_CONFIG_DIR` is thinly documented and there are open reports
of it still creating local `.claude/` directories in the workspace, so confirm the
isolation with a smoke run rather than assuming it. And if `ANTHROPIC_API_KEY` is set
anywhere in the environment it takes precedence over a subscription — you can believe
you're spending rate limits and be spending dollars. The harness strips it from the
child environment when `auth` is `subscription`, but check `unset ANTHROPIC_API_KEY` in
your own shell too.

**Either way, it costs something.** A modest suite (5 cases x 2 arms x 3 reps) is 30
agent sessions. On an API key that's a bill; the harness records `total_cost_usd` per
run and reports the total. On a subscription it's rate limits, drawn from the same pool
as your own work, so keep `--jobs` low or you'll spend the afternoon throttled. If the
budget is tight, cut cases before cutting repetitions — see below, because 1 rep is
close to worthless.

**Never run without isolation.** If bare mode is off and no `config_dir` is set, the
baseline arm loads every skill you have installed, and the comparison measures nothing.
The harness warns about this; don't wave it through. At absolute minimum, keep the skill
under test out of `~/.claude/skills` and manage it from a repo directory, so the only
difference between arms is the `--add-dir`.

**Smoke test before spending.** `scripts/run_matrix.py --smoke` runs one case, one arm,
one rep, and prints the tool list from the session's init event. That catches a broken
auth setup and a tool the skill needs but the session doesn't have — bare sessions get
Bash, file read, and file edit, so a skill depending on web fetch or MCP will fail there
for reasons that have nothing to do with the skill. Say which configuration you used in
the report, because it changes how much the numbers mean.

## Running the scripts

Every `scripts/...` path below is relative to the folder that holds this SKILL.md, not to
your project. Resolve it against that folder before you run it. If your agent reports
`No such file or directory`, it used the wrong working directory: prefix the path with the
folder this file was loaded from.

## Stage 1 — Collect cases

Cases from real failures beat cases you invented. An invented case tests whether the
agent can solve a puzzle; a real one tests the thing that actually went wrong.

Start with the field log:

```bash
python3 scripts/scan_field.py --skill <skill-name> --days 30 --out cases/field.md
```

This scans local Claude Code session transcripts for sessions where the skill was
loaded and pulls out every user turn that came after it. Read them with the user. The
turns where they had to correct the agent — "no, put it in the other format", "you
skipped the part where…" — are the highest-value cases available, because each one is a
recorded instance of the skill failing to carry an instruction, with the correct answer
supplied by the user for free.

The script ranks candidates but does not judge them. Ask the user which of those
exchanges were genuine skill failures versus them changing their mind. That distinction
is not recoverable from the text.

Then add constructed cases only to cover gaps: an edge case nobody has hit yet, or a
near-miss prompt that should *not* trigger the skill. Keep the total between 4 and 8.
Bigger suites cost more and rarely change the conclusion.

Cases go in `suite.json` (see `assets/suite.example.json` for the schema). Every case
needs a `fixture` — a directory that gets copied fresh into each run's working
directory. Runs that share state contaminate each other, and an agent that finds last
run's output file will behave differently.

## Stage 2 — Write the checks first

Write checks before you edit the skill, and show them to the user. Writing them forces
you to say what "working" means, and that conversation usually exposes that the skill
was underspecified all along. A skill that passes every check on the first run has weak
checks, not a strong skill.

Two kinds, both needed. Full guidance in `references/judges.md`; the short version:

- **Rule checks** are shell commands run against the finished working directory. Exit 0
  is a pass. Use them for observable side effects: a file exists, has a heading, has no
  placeholder text left in it. Deterministic and free.
- **Judge checks** are questions answered by a separate `claude -p` call reading the
  run's trace. Use them for behavior no rule can express: did the agent verify its
  claims before writing them, did it follow the documented order of operations, did it
  load the skill at all.

Judges read the **trace**, not just the artifact. Most skill failures are invisible in
the output. If the skill says "always check X before writing the report" and the agent
wrote a fine report without checking X, the artifact looks correct and the skill is
broken. Only the sequence of tool calls shows that.

Every judge must return a rationale, not a verdict alone. "No" tells you a check failed.
"The agent wrote the report in turn 3 without ever reading the config file the skill
names as a prerequisite" tells you which sentence of the skill to fix. The rationale is
the entire diagnostic value; a bare boolean gives you nothing to act on.

## Keeping the spend honest

An audit loop wastes money in ways that each feel small. The guardrails below are on
by default; the reason to know them is that turning one off should be a decision, not
an accident.

**Estimate from your own runs, not from a guess.**

```bash
python3 scripts/run_matrix.py --suite suite.json --out runs/iter-1 --smoke   # one run
python3 scripts/run_matrix.py --suite suite.json --out runs/iter-1 --estimate
```

The smoke run establishes a real cost-per-run for *this* suite, and `--estimate`
projects the full matrix from it and exits without spending. Cost per run is dominated
by how much work the cases ask for, which varies by an order of magnitude between
suites, so any general figure would be useless.

**Set a ceiling that stops work.** `"budget_usd"` in the suite, or `--budget`. New runs
stop once it's reached rather than reporting the overrun afterward. Work already in
flight finishes, so with a small `--jobs` the overshoot is a run or two. When the cap
bites, the report says so and warns that the arms aren't comparable — a partial matrix
is not a result.

**Finished runs are never paid for twice.** A run with a completed `meta.json` is
reused. Interrupt the suite, rerun the command, and only the missing runs execute.
`--force` overrides. The same applies to scoring: a run already graded against the same
checks is skipped, and the check set is fingerprinted so editing a criterion
invalidates only what actually changed. `--rescore` overrides.

**Grading is the leak people miss.** 30 runs x 4 judge criteria is 120 model calls, each
reading a trace, and that can cost more than the runs it grades. Three defaults address
it:

- All of a run's judge criteria go in **one call**, not one call each. Roughly 4x
  cheaper. The trade-off is real — criteria graded together can bleed into each other,
  where a bad impression of the run colours every verdict. The prompt pushes against it.
  When a criterion is load-bearing enough that you want it graded alone, `--no-batch`.
- Judges default to a **small model**, because most trace questions are retrieval ("did
  Read on config.yaml appear before Write on report.md"), not judgement. When one
  criterion genuinely needs more, put `"model": "sonnet"` on that check rather than
  raising it for all of them. Repeated `unclear` verdicts on one check are the signal.
- The **trace summary is capped** (`judge_trace_chars`, default 12000). It's what every
  judge call pays to read, so it's the main cost lever. Tool output is truncated hardest
  because it's most of the bytes and least of the signal.

**Cap the matrix size.** `"max_runs"` (default 60) refuses an oversized suite without an
explicit `--yes`. Past a certain point more cases stop changing the conclusion and only
change the bill.

**Runs that hit the turn cap are flagged, not silently counted.** A run that reaches
`max_turns` was looping, and its output isn't evidence about anything. The report calls
these out, because re-running the case unchanged next iteration buys another one exactly
like it.

**A ledger tracks the whole audit.** Every phase appends to `runs/spend.jsonl`, and each
report shows the running total across iterations. The expensive failure here is never
one costly run — it's six rounds nobody re-estimated, each of which felt cheap.

**Don't re-run a suite that can't tell you anything new.** If the SKILL.md hasn't changed
since the last iteration, the matrix will reproduce the last result at full price. And
resist `--case` as a way to iterate cheaply: it's fine for investigating one failure, but
a revision accepted on a single case has not been checked for regressions, which is the
one thing the full suite exists to do.

## Stage 3 — Run the matrix


```bash
python3 scripts/run_matrix.py --suite suite.json --out runs/iter-1
```

Defaults: 3 repetitions per case per arm. **Do not drop below 3.** Agent runs vary
substantially between identical invocations; a single run showing the skill winning is
an anecdote, and single-run comparisons will send you chasing fixes for noise. If the
budget forces a cut, drop to 2 cases at 3 reps rather than 6 cases at 1 rep.

Arms, defined in the suite:

- `with` — the skill under test, staged into an isolated `--add-dir` host.
- `base` — no skill. This is the arm that answers "is the skill earning its keep?"
- `old` — optional, a snapshot of the previous version. Use this when improving an
  existing skill, and snapshot **before** you edit anything.

Each run writes `result.json` (cost, duration, session id), `trace.jsonl` (the full
stream), and `workdir/` (whatever the agent produced).

Then score:

```bash
python3 scripts/score_runs.py --suite suite.json --runs runs/iter-1
python3 scripts/report.py --runs runs/iter-1 --out runs/iter-1/report.md
```

`score_runs.py` grades blind: the judge is given the trace summary and the check
question, never the arm name. Told which arm it is looking at, a judge will find reasons
to favor the one it expects to win. This matters more than usual here, because the
session proposing the skill edits is also the one orchestrating the grading.

## Stage 4 — Read the evidence

`report.md` gives pass rate per check per arm, with cost and turn counts. Interpret it
against these three failure modes, because they have completely different fixes:

| What the evidence shows | What's broken | Where to fix it |
|---|---|---|
| `skill-loaded` judge fails — the skill never got read | Triggering | The `description` frontmatter, not the body. Claude decides from the description alone |
| Skill loaded, but a step it mandates doesn't appear in the trace | The body isn't persuasive or is buried | That section: explain why the step matters, or move it earlier |
| Skill loaded, steps followed, output still bad | The instruction itself is wrong | The substance. Don't add emphasis to a bad instruction |

Then check the two results people skip past:

**No difference between arms.** The skill isn't doing anything. Common and worth
saying plainly: modern models handle a lot unaided, and a skill that restates what the
model would do anyway is pure context cost. The honest recommendation is sometimes
"delete this skill."

**Baseline beats with-skill.** The skill is actively harmful — usually because it
forces a rigid procedure onto tasks that needed judgment. Read those traces closely.

**Cost and turns.** Report them next to quality. A skill that lifts pass rate from 80%
to 85% while doubling tokens and turns is a bad trade, and nobody notices unless it's in
the table.

Show the user the report and the traces for the failures before proposing any edit.
Their read on why something went wrong is usually better than yours, and they are the
one who has to live with the skill.

## Stage 5 — Revise, verify, keep or revert

Group the failures into clusters — several checks failing for the same underlying
reason. Form **one hypothesis per cluster** and make the smallest edit that tests it.
Batching five edits into one round means that when the score moves you won't know which
edit moved it, and you'll keep all five forever.

Detailed guidance in `references/revision.md`. The rules that matter most:

- **Explain why, don't shout.** Reaching for a bold ALWAYS or a ⛔ is a signal that you
  don't know why the agent deviated. Find out from the trace, then write the reason.
  A model that understands the constraint generalizes it; a model that was yelled at
  complies on the cases you tested and nothing else.
- **Fix triggering in the description, everything else in the body.** A dependency or
  precondition the agent must honor before loading the body has to live in the
  description, because that's all it sees at decision time.
- **Watch the line count.** Record SKILL.md length each iteration in the report. Loops
  like this ratchet toward bloat: every round adds a clause, none removes one, and by
  round five the skill is 400 lines of accumulated scar tissue that costs context on
  every invocation. If a round adds words and doesn't move the score, revert it. Revert
  is a normal outcome, not a failure.
- **Never accept a fix that regresses another case.** Re-run the whole suite, not the
  case you were fixing. A fix that overfits to one prompt is worse than no fix, because
  it looks like progress.

Get the user's sign-off on the diff before applying it. Show the diff, the failure
evidence it addresses, and what you expect to change. Then re-run into `runs/iter-2`
and compare. `report.py --previous runs/iter-1` adds the delta column.

Stop when the user is satisfied, when two consecutive rounds fail to improve anything,
or when the remaining failures are cases where the model was right and the skill was
wrong. That last one is a real result — write it down rather than forcing the score up.

## Continuous capture

The batch loop above is for when someone is paying attention. Between rounds, keep
collecting evidence from real use:

```bash
python3 scripts/install_hook.py --skill <skill-name> --scope user
```

This registers a `SessionEnd` hook that appends a one-line record to
`~/.claude/skill-audit/<skill>.jsonl` whenever a session loaded the skill: session id,
transcript path, timestamp, turn count. It records pointers, not content — the
transcripts already exist on disk and copying them around is a needless privacy
liability.

Then `scan_field.py` has a growing pool to draw from, and the next audit round starts
from what actually happened rather than what you imagined might.

Resist the temptation to have the hook rewrite the skill on its own. A single session
is n=1, the evidence is unverified, and a skill that edits itself unattended will drift
somewhere nobody chose and nobody reviewed. Capture is automatic; revision is deliberate
and reviewed. That split is the whole design.

## Reference files

- `references/judges.md` — writing rule checks and judge checks, with worked examples
- `references/revision.md` — diagnosing a failure from a trace and editing the SKILL.md
- `references/field-capture.md` — the hook, the log format, and what it does not store
- `assets/suite.example.json` — the suite schema, annotated

## Scripts

| Script | Does |
|---|---|
| `scan_field.py` | Find real sessions that used the skill; extract post-skill user turns |
| `run_matrix.py` | Run cases x arms x reps headlessly; save traces, artifacts, cost |
| `score_runs.py` | Apply rule checks and blind judge checks; write scores |
| `report.py` | Aggregate into report.md and results.csv, with deltas vs a previous iteration |
| `install_hook.py` | Register the SessionEnd capture hook |
| `trace.py` | Shared: parse stream-json and session transcripts into a compact summary |
| `budget.py` | Shared: spend ceilings and the cross-iteration ledger |
