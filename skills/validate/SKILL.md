---
name: validate
description: "Use this skill to test whether an idea is worth pursuing before building it, or to find an idea in the first place: 'is this a good idea,' 'should I build this,' 'pressure test my idea,' 'how do I know anyone wants this,' 'I don't have an idea yet,' 'do it by hand first,' 'concierge MVP,' 'go/no-go,' or 'how big is this market.' Designs the cheapest test, scores the evidence with a script, and returns a dated verdict. Not for choosing what form to build (use is-this-an-app) or for getting customers after a go (use first-customers)."
metadata:
  version: 1.0.0
---

# Validate

Find out whether strangers will pay for this, as cheaply as possible. The goal is to fail fast, not to confirm what the founder already believes.

```
find   →  pressure-test  →  design       →  run            →  verdict
(no idea  (is the idea      (cheapest       (the founder      (score the
 yet?)     coherent?)        test of the     does this)        evidence)
                             biggest gap)
```

Most founders want the verdict without the evidence. Route them back to the earliest stage they have not finished.

## Step 0: Context

Read the project's CLAUDE.md, README, and ABOUT-ME.md if they exist. If the founder mentions an earlier brief for this idea, ask for it, and treat this run as a revisit.

## Step 1: Choose the mode

| The founder says | Mode | Steps |
|---|---|---|
| "I don't have an idea yet" | **find** | 2, then 3 |
| "Validate this idea" (default) | **full** | 3 → 6 |
| "Pressure test this" | **pressure-test** | 3, 6 |
| "How do I test this?" | **design** | 4, 6 |
| "Here's what happened" / "go or no-go" | **verdict** | 5 → 6 |

## Step 2: Find the problem (no idea yet)

Ask the founder to answer in one sentence each:
1. Which groups do you belong to? Think of work, hobbies, online communities, and local groups.
2. In those groups, what do people complain about again and again?
3. What task do you, or people like you, dread or put off?
4. What takes far too long for what it produces?
5. What would you pay \$100 a month to never do again?

Kill a problem early if only the founder has it, if it happens once a year, if a good tool already exists and people know about it, or if every step needs human judgment.

Pick the one problem where the founder can **name a real person** who has it and can reach that person. "Everyone in my field needs this" means they have not found anyone yet. Continue with Step 3.

## Step 3: Pressure-test

Get the idea in 1–2 sentences and the founder's stage. If either is too vague, ask once and stop.

Read `references/pressure-test-questions.md`. Ask only the three questions mapped to the founder's stage. Capture the answers word for word. Mark each one: ✅ evidenced / 🟡 partial / ❌ none. Any ❌ is a gap that Step 4 must test. Do not give a verdict with a ❌ on the board.

## Step 4: Design one test

Read `references/experiments.md`. Pick the cheapest test that closes the biggest gap. Specify all four before the founder runs anything:
- **The test:** conversations, landing page, fake door, pre-sale, or manual delivery
- **The metric:** one number
- **The pass bar:** set now, never after seeing the result
- **The deadline:** a date, usually 2–4 weeks out

If nobody else has shown they want this, the test is conversations first. Hand the founder `references/interview-guide.md`. A landing page cannot tell you whether a problem is real.

## Step 5: Score the evidence

Only with real results in hand. Read `references/scorecard.md` and assign all six scores. A dimension with no evidence scores 1. If market size is unknown, use the bottom-up method in the scorecard.

Run the script. The path is relative to the folder that holds this SKILL.md:

```bash
python3 scripts/score.py \
    --frequency 3 --intensity 3 --willingness 1 \
    --market 3 --advantage 5 --solutions 3
```

Take the verdict from the script, not from your own reading of the bands. The script applies the two override rules: willingness to pay of 1 caps the verdict at "One more experiment", and a high unique-advantage score never rescues a low total. Show all six numbers in the brief.

## Step 6: Write the brief

```markdown
# Validation: <idea>
**Date:** <YYYY-MM-DD> · **Stage:** <idea / prototype / paying customers>

## Verdict
**Build** / **One more experiment** / **Pivot the angle** / **No-go**
<2–3 plain sentences on why.>

## Pressure test
| # | Question | Answer | Evidence |

## Test run
**Test:** … · **Metric:** … · **Bar:** … · **Result:** …

## Score
<the six scores and the total, from the script>

## Next test
<the weakest dimension, and the cheapest test that would move it>

## Revisit
**<YYYY-MM-DD>**: <what to look for>
```

Never soften the verdict. "Leaning towards maybe" wastes the brief.

Ask how the founder wants the brief saved. The default is a Markdown file in a folder the founder names. Do not choose the folder yourself. Suggest saving a No-go brief too: killed ideas come back, and the brief stops the same argument from happening twice.

Then offer the next step:
- **Build:** "Build" means the idea has earned a first version, and that first version is done by hand. Run the manual delivery test (`references/experiments.md`, Level 5). Use **pricing** and **first-customers** to get 10 paying customers before writing code.
- **One more experiment:** design that test. Use **landing-page** if it needs a page.
- **Pivot the angle:** re-run with a different customer or a narrower wedge.
- **No-go:** save the brief and return to Step 2.

## Rules

- **The founder's own excitement is never evidence.** "I'd use this," said by the founder, is the most common false positive.
- **Interest is not demand.** Signups, compliments, and "I'd definitely pay" are interest. Money, time, and switching effort are demand.
- **One test at a time.** Three tests at once teach nothing and burn a month.
- **Refusing to score is a valid output.** With no evidence, the answer is "run this test first," not a scorecard built on guesses.
