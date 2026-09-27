# Validation Scorecard

Six dimensions, scored 1–5 each, 30 points total. Used in `verdict` mode to convert gathered evidence into a call.

**Assign the six numbers from this file, then run `scripts/score.py` to get the total and verdict.** The bands and override rules below are documented here so you can see the reasoning, but the script is what applies them — summing six numbers by eye is how a verdict ends up disagreeing with its own score.

## The dimensions

| # | Dimension | 1 | 3 | 5 |
|---|---|---|---|---|
| 1 | **Problem frequency** | Yearly | Monthly | Daily |
| 2 | **Problem intensity** | Mild annoyance | Costs real time or money | Hair on fire |
| 3 | **Willingness to pay** | Words and clicks — "cool idea", waitlist signups, "I'd definitely pay" | A costly signal short of money — a signed LOI, switching effort, hours they gave you | Money changed hands — a pre-sale, a deposit, a paid pilot |
| 4 | **Market size** | Tiny or unclear | Niche but reachable | >$1B TAM, or a niche you can own entirely |
| 5 | **Your unique advantage** | None | Some domain familiarity | Deep expertise or unfair distribution |
| 6 | **Current solutions** | Strong incumbents | Mediocre options exist | Nothing, or everyone hates what exists |

Score each from evidence, not from belief. A dimension with no evidence scores 1 and gets flagged as a gap — never scored on optimism.

Dimension 3 is the one founders and scorecards both get wrong, so it is worth saying plainly: a waitlist signup costs the person nothing, so it scores 1 here however many you have. It is real evidence of interest and it belongs in dimensions 1 and 2 — but this row asks a narrower question, whether anyone has given up something to get this. A rubric that pays out a 3 for an email address quietly turns interest into demand and hands back a verdict the founder wanted to hear.

## Reading the total

| Total | Verdict | What it means |
|---|---|---|
| 25–30 | **Build** | Strong go. Scope the MVP. |
| 18–24 | **One more experiment** | Promising. Name the weakest dimension and design a test for it. |
| 12–17 | **Pivot the angle** | The problem may be real but this framing isn't working. Change audience or wedge, re-test. |
| < 12 | **No-go** | Find a different problem. Archive the brief and move on. |

## Rules

- **A 1 on willingness to pay is a ceiling, not a floor.** It pulls a "Build" down to "One more experiment". It never lifts a weaker verdict up: a total of 15 is "Pivot the angle" whether willingness scored 1 or 5. Every other dimension can be strong and the business still fails if nobody pays — but a low total already said that, and this rule must not be used to soften it. Reading the ceiling as a floor is the most common way a scorecard flatters a bad idea.
- **A 5 on unique advantage does not rescue a low total.** Founders over-weight their own expertise. It is a tiebreaker, not a foundation.
- **Score dimension 4 for the wedge, not the dream.** "Everyone with a smartphone" is not a market size, it's an evasion.
- **Unknowns score 1 and are listed as open questions.** Never average, never guess, never leave a dimension blank.

## Worked example

An idea with a real daily problem (5), high intensity (4), a waitlist and no payments (1), a reachable niche (3), deep domain expertise (5), and mediocre incumbents (3) scores **21 — One more experiment**. The weakest dimension is willingness to pay, so the next test is a pre-sale, not more interviews. The scorecard's job is to name the next experiment, not just produce a number.

Note what the willingness score is doing there. Five out of six dimensions are strong, and the total still cannot reach "Build", because the one number that tracks money is at the floor. That is the scorecard working. Rescuing that 1 up to a 3 because the waitlist "feels like something" is how a strong-looking total gets built on nothing.
