---
name: validate
description: "Use this skill when the user needs to validate a business idea, test demand before building, run a smoke test, or decide whether an idea is worth pursuing. Also use when the user says \"is this a good idea,\" \"should I build this,\" \"pressure test my idea,\" \"how do I know anyone wants this,\" \"test demand,\" or \"go/no-go.\" For sizing a market or analyzing competitors, see market-research. For interviewing existing customers and building personas, see customer-research. For ranking features you've already decided to build, see prioritize. Four modes — full (default), pressure-test, design, verdict. Outputs a validation brief with a Build / One more experiment / Pivot the angle / No-go verdict and a revisit date."
metadata:
  version: 1.0.1
---

# Validate — Test demand before you build

Runs an idea through a stage-appropriate pressure test, designs the cheapest experiment that would settle it, scores the evidence, and produces a dated go/no-go brief with a revisit date.

The goal is to fail fast and cheap — not to confirm what the founder already believes.

## Mental model

```
pressure-test  →  design       →  run           →  verdict
(is the idea      (what's the      (the founder     (score the
 coherent?)        cheapest test    does this)       evidence,
                   of the gap?)                      make the call)
```

Most founders arrive wanting the verdict without the evidence. The job is to route them back to the earliest incomplete stage, not to score optimism.

## Step 0 — Load context

Read these if they exist, silently — don't narrate what you're reading:

- `${BUSINESS_BRAIN:-$HOME/business-brain}/customer/icp.md` and `customer/jobs-and-pains.md` — who this is for and what already hurts
- `${BUSINESS_BRAIN:-$HOME/business-brain}/customer/evidence.md` — what real people have already said or done
- Project files: CLAUDE.md, README, any founder or product context docs

If the founder mentions an earlier brief for this idea, ask them for it. This run is then a revisit, not a fresh start — say so, and score against what's changed.

## Step 1 — Parse mode

| Invocation | Mode |
|---|---|
| Default, or "validate this idea" | **full** — Steps 2 → 6 |
| "pressure test this," "is this idea any good" | **pressure-test** — Steps 2, 6 |
| "how do I test this," "design an experiment" | **design** — Steps 3, 6 |
| "here's what happened," "score this," "go or no-go" | **verdict** — Steps 4 → 6 |

## Step 2 — Pressure-test the idea

Get the idea in 1–2 sentences and the founder's stage. If either is too vague to work with, ask once and stop — do not pad the brief with assumptions.

Read `references/pressure-test-questions.md`. Ask **only the questions mapped to their stage** — three, not six. Capture answers verbatim; do not paraphrase the optimism out of them.

Mark each answer: ✅ evidenced / 🟡 partial / ❌ none.

Any ❌ is a gap that Step 3 must design an experiment for. Do not proceed to a verdict with a ❌ on the board.

## Step 3 — Design the experiment

Read `references/experiments.md` and pick the cheapest experiment that would close the biggest gap from Step 2. One experiment, not a program.

Specify all four before the founder runs anything:

- **The test** — landing page / fake door / pre-sale / conversations
- **The target metric** — the single number being measured
- **The pass bar** — set now, never after seeing the result
- **The deadline** — a date, usually 2–4 weeks out

If the gap is Q1 (no evidence anyone else wants it), the experiment is always conversations first. A landing page cannot tell you whether a problem is real.

For conversation-based experiments, hand the founder `references/interview-guide.md`.

## Step 4 — Score the evidence

Only with real results in hand. Read `references/scorecard.md` for what each dimension means and what a 1 versus a 5 looks like, then assign all six.

Score from evidence, not belief. A dimension with no evidence scores 1 and becomes an open question. Guessing at one to avoid an awkward number is how a scorecard ends up flattering an idea the founder already wants to build.

Then run the script. The path is relative to the folder that holds this SKILL.md, not to your project:

```bash
python3 scripts/score.py \
    --frequency 3 --intensity 3 --willingness 1 \
    --market 3 --advantage 5 --solutions 3
```

If your agent reports `No such file or directory`, it used the wrong working directory: prefix the path with the folder this file was loaded from.

Take the verdict from the script, not from your own reading of the bands. Summing six numbers is easy and you will get it right; picking the band and applying the override rules is where this step goes wrong in practice. The script encodes both rules:

- **Willingness to pay of 1 is a ceiling.** It drags a "Build" down to "One more experiment". It does not lift anything up — a total of 15 stays "Pivot the angle". The temptation is to read this rule as "willingness of 1 means One more experiment," which quietly upgrades a weak idea and defeats the whole scorecard.
- **A high unique-advantage score gets flagged, not credited.** Expertise is a tiebreaker, never the reason a low total becomes a go.

Report the total, the verdict, and the weakest dimension as the script gives them. A verdict that contradicts its own score is worse than no verdict, because the founder can't tell which half to trust.

Show the six numbers in the brief. A total the founder can't check is a total they have no reason to believe.

## Step 5 — Output the brief

```markdown
# Validation: <idea slug>

**Date:** <YYYY-MM-DD>
**Idea:** <1–2 sentences>
**Stage:** <pre-product / prototype / paying customers>

## Verdict
**Build** / **One more experiment** / **Pivot the angle** / **No-go**

<2–3 sentences. Say why, in plain English.>

## Pressure test

| # | Question | Answer | Evidence |
|---|---|---|---|
| Q1 | Demand reality | … | ✅ |
| Q3 | Desperate specificity | … | ❌ |

## Experiment run
- **Test:** <what> · **Metric:** <number> · **Bar:** <pass bar> · **Result:** <actual>

## Score

| Dimension | Score | Basis |
|---|---|---|
| Problem frequency | 4/5 | … |
| Problem intensity | 3/5 | … |
| Willingness to pay | 2/5 | … |
| Market size | 3/5 | … |
| Unique advantage | 5/5 | … |
| Current solutions | 3/5 | … |
| **Total** | **20/30** | |

## Next experiment
<the single weakest dimension, and the cheapest test that would move it>

## Open questions
<what would change the verdict>

## Revisit
**<YYYY-MM-DD>** — <what to look for on that date>
```

Never soften the verdict. "Leaning towards maybe" wastes the brief — the whole point is to convert a vague feeling into a call the founder can act on.

## Step 6 — Save the brief

Ask the founder how they want the brief saved. The default is a Markdown (`.md`) file in a directory the founder names. Do not choose the directory yourself, because the founder decides where their files live. If the founder does not want it saved, skip this step. Suggest saving a No-go brief too.

## Step 7 — Surface

Show the brief in chat. If the founder saved it, give the file path. Then offer, based on the verdict:

- **Build** → *"Want me to scope the MVP?"* (`plan`) or *"Test willingness-to-pay properly?"* (`pricing`)
- **One more experiment** → *"Want me to set up the landing page for that test?"* (`landing-page`)
- **Pivot the angle** → *"Want to re-run against a different audience?"* (`customer-research`)
- **No-go** → *"Want me to check whether the angle is worth stealing for something you're already running?"*

Always offer: *"Want a reminder to revisit on <date>?"* (`loop`)

## Composes with

- `customer-research` — run before Step 2 when Q1 has no evidence. `Skill({skill: "customer-research"})`
- `market-research` — sizes the market when scorecard dimension 4 is unknown
- `landing-page` — builds the smoke test designed in Step 3
- `pricing` — after a Build verdict, tests willingness-to-pay properly rather than by proxy
- `plan` — turns a Build verdict into a spec
- `translate` and `niche-advantage` — for domain experts, whose own network is the fastest validation lab
- `loop` — schedules the revisit so it actually happens

## Notes on quality

- **The founder's own excitement is never Q1 evidence.** "I'd use this" from the person building it is the most common false positive in this skill. Say so plainly when it happens.
- **Set the pass bar before the experiment, never after.** A founder who sees 3% and decides 3% is encouraging has learned nothing. Write the bar into the brief in Step 3.
- **Route back, don't score forward.** When someone asks for a verdict with no evidence, the answer is "run this experiment first," not a scorecard built on guesses. Refusing to score is the more useful output.
- **Interest is not demand.** Waitlist signups, compliments, and "definitely would pay" are all interest. Only money, time, and switching effort are demand.
- **Save no-go verdicts too.** Killed ideas resurface six months later. The brief with its rationale is what stops the same argument being had twice.
- **One experiment at a time.** A founder running three tests at once learns nothing from any of them and burns four weeks.

## When NOT to use this skill

- The founder already has paying customers and wants to know what to build next — use `prioritize`.
- They want to size a market or map competitors — use `market-research`.
- They're deciding whether an existing activity is still worth their time — use `focus`.
- They've validated and want to scope the build — use `plan`.
- The idea is a small feature inside a working product. Ship it and watch the metric; a validation brief is overkill.
