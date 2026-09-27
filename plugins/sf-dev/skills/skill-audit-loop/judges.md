# Writing checks

Checks are the specification. Write them before editing the skill, show them to the
user, and expect the conversation to reveal that the skill was underspecified — that
is the point of writing them first.

If every check passes on the first run, the checks are too weak. Tighten them before
concluding the skill works.

## Rule checks

A shell command run in the finished working directory. Exit 0 passes. Deterministic,
free, and the only checks you can fully trust.

```json
{ "id": "report-written",    "type": "rule", "cmd": "test -f report.md" }
{ "id": "has-summary",       "type": "rule", "cmd": "grep -q '^## Summary' report.md" }
{ "id": "no-placeholders",   "type": "rule", "cmd": "! grep -qiE 'TODO|TBD' report.md" }
{ "id": "valid-json",        "type": "rule", "cmd": "python3 -m json.tool out.json >/dev/null" }
{ "id": "tests-pass",        "type": "rule", "cmd": "npm test --silent" }
```

Use a rule wherever one is possible. Anything a rule can decide should not go to a
judge: judges cost money, take time, and occasionally disagree with themselves.

Watch for rules that pass for the wrong reason. `test -f report.md` passes on an empty
file. Pair existence with a content check, or check for a thing that could only be
there if the work was really done.

## Judge checks

A question answered by a separate `claude -p` call reading a summary of the run's
trace. Use them where no rule can reach.

```json
{ "id": "verified-before-claiming", "type": "judge",
  "ask": "Did the agent read the actual config file before describing its contents, or did it describe them from assumption? Point to the specific tool calls." }
```

### Judge the trace, not the artifact

This is the single most useful thing in this file.

Most skill failures leave no mark on the output. A skill says "read the schema before
writing the migration." The agent skips that and writes a migration that happens to be
correct. The artifact is perfect. The skill failed, and it will keep failing on the
cases where guessing doesn't happen to work.

The trace is the only record of what the agent actually did. Judges here get an ordered
account: every user turn, every assistant message, every tool call with its
distinguishing argument. Ask questions about *sequence* and *evidence*, because that is
what the trace can answer and the artifact cannot.

Questions worth asking:

- Did it read X before doing Y?
- Did it verify this claim, or assert it?
- Did it follow the order the skill lays out, or reorder the steps?
- Did it load the skill at all?
- Did it do work the skill does not call for?

### The rationale is the whole point

Every judge returns a verdict and a rationale. Insist on the rationale being specific.
A bare "fail" tells you a check failed. It does not tell you which sentence to change,
so the next step is a guess and you are back to inspection.

Useless: *"The agent did not follow instructions."*

Useful: *"The agent wrote report.md at turn 4. It never called Read on config.yaml,
which the skill names as a prerequisite in step 2. It appears to have inferred the
config values from the directory listing at turn 2."*

The second one names the fix.

### Always include a triggering check

Put a `skill-loaded` judge on every case:

> Did the agent read a SKILL.md file before starting work? Name the file if so.

If this fails, nothing else in the report means anything, and the fix is in the
`description` frontmatter rather than the body. Claude decides whether to open a skill
from the description alone; a perfect body that never gets read is dead weight.

### Include a negative case

At least one case whose prompt sits near the skill's territory but should not trigger
it. Over-triggering is a real cost — the skill burns context and forces its procedure
onto a task that didn't want it — and it never shows up in a suite of prompts you wrote
to make the skill fire.

Make the negative genuinely close. "Write a fibonacci function" as a negative for a PDF
skill tests nothing.

## Blinding, and its limits

`score_runs.py` never tells the judge which arm it is grading. That removes the crudest
bias, where a judge told "this is the with-skill run" finds reasons for it to win.

It does not make grading neutral. A judge reading a trace where the agent loaded
`some-skill/SKILL.md` at turn 1 can infer the arm perfectly well. Treat judge results as
evidence, not as measurement:

- Rule checks are unbiased. Weight them heavily.
- Where a judge and a rule disagree, believe the rule.
- Read failing traces yourself before acting on them. The report ranks and summarises;
  it does not replace looking.

This matters more here than in most eval setups, because the same session proposing the
skill edits is also the one running the grading.

## Unclear verdicts

A judge can answer `unclear`, and should when the trace does not settle the question.
Unclear verdicts are excluded from pass rates rather than counted as failures.

A check that comes back unclear repeatedly is a badly written check. Fix the criterion —
usually it is asking two things at once, or asking about something that never appears in
a trace. Do not fix the skill in response to an unclear verdict.
