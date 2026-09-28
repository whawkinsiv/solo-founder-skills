# Revising a skill from evidence

The reason this loop exists is that improving a skill by inspection does not work.
Reading a SKILL.md tells you what it says. It does not tell you which sentence the model
ignored, which one it followed into a bad outcome, or which one it never saw. Only the
trace tells you that.

So: diagnose from the trace, form one hypothesis, make the smallest edit that tests it,
re-run the whole suite.

## Diagnose first

Every failure lands in one of four buckets, and the fixes have nothing in common. Get
the bucket right before writing anything.

**1. The skill never loaded.**
The `skill-loaded` check fails. The body is irrelevant — the model never saw it. Fix
the `description` frontmatter, which is the only thing available at the moment the model
decides. Add the phrasings real users actually use, including the casual and misspelled
ones. If the skill has a prerequisite the model must honor before opening the body — a
dependency on another skill, a precondition — that fact has to live in the description
too, because the body is too late.

**2. The skill loaded and a mandated step is absent from the trace.**
The model read the instruction and did something else. Almost always this is because the
instruction reads as ceremony: it does not say why it matters, so the model routed around
it in favour of the goal it inferred. Explain the consequence of skipping it. A model
that understands the constraint applies it to cases you never tested; a model that was
shouted at complies on your cases and nothing else.

Also check whether the step is simply buried. Long skills get skimmed. If a critical step
is in paragraph nine, move it.

**3. The skill loaded, the steps happened, and the output is still wrong.**
The instruction itself is wrong or incomplete. This is the bucket people misdiagnose most
often, because the reflex is to add emphasis. Adding **ALWAYS** to a bad instruction
produces a reliably bad result. Fix the substance.

**4. It fails in the baseline too.**
Not a skill problem. Either the task is unreasonable or the check is wrong. Fix the case,
not the skill.

## Editing

**One hypothesis per round.** Batch five edits and a score change tells you nothing about
which edit caused it, so all five stay forever, including the four that did nothing. Slow
is faster here.

**Explain why, don't shout.** Reaching for `ALWAYS`, `NEVER`, `⛔`, or bold caps is a
signal that you don't know why the model deviated. Go back to the trace and find out,
then write the reason. Emphasis is what you use when you have run out of understanding.

Weak:
> **ALWAYS read the config file first. DO NOT skip this.**

Better:
> Read `config.yaml` before writing anything. It carries the field names the rest of the
> project uses, and a report written from guessed names is worse than no report — it
> reads as authoritative and sends the reader looking for fields that don't exist.

**Don't overfit to the case you're fixing.** You are iterating on four to eight examples
to make something that will run hundreds of times. An edit that names the specific file,
company, or phrasing from a test case will pass that case and generalise to nothing. If
you find yourself writing the fixture's filename into the skill, stop.

**Prefer removing to adding.** If the trace shows the model spending turns on something
unproductive, look for the instruction that sent it there and delete it. Deletions are
underused and they are the only edit that makes the skill cheaper.

**Bundle repeated work as a script.** If every run independently writes a similar helper
— the same parsing, the same conversion — that is a strong signal the skill should ship
it in `scripts/`. Write it once. Every future invocation stops reinventing it.

## The bloat ratchet

Loops like this drift toward bloat by default. Each round adds a clause; no round removes
one; by round five the skill is four hundred lines of accumulated scar tissue, most of it
addressing failures that stopped happening three rounds ago, all of it costing context on
every single invocation.

Defenses:

- `report.py --skill-md <path>` records SKILL.md line count each iteration. Watch it.
- If a round adds words and does not move any score, revert it. Reverting is a normal
  outcome, not an admission of failure.
- Every two or three rounds, try deleting the oldest additions and re-running. If nothing
  regresses, they were never doing anything.

## Verify, then keep or revert

Re-run the **entire suite**, not the case you were fixing. A fix that repairs one case
and quietly breaks another is worse than no fix, because it looks like progress.

`report.py --previous runs/iter-N/scores.json` adds a delta column.

Accept the change when the target cluster improved and nothing else regressed. Otherwise
revert and form a different hypothesis. Two consecutive rounds without improvement means
stop: either the remaining failures are cases where the model was right and the skill was
wrong, or the skill isn't the lever.

## When the answer is "delete it"

If the arms come out within noise of each other, the skill is not doing anything, and the
honest recommendation is to delete it rather than tune it. Modern models handle a great
deal unaided, and a skill that restates what the model would have done anyway is pure
context cost with a maintenance burden attached.

Say this plainly when the numbers say it. It is a genuinely useful result and nobody
wants to hear it, which is exactly why it needs saying rather than hinting.
