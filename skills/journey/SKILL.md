---
name: journey
description: "Use this skill when a solo founder does not know where to start or what to do next: 'where do I start,' 'what should I do first,' 'what order do I do things in,' 'what should I work on now,' 'I have an idea, now what,' or 'I don't have an idea yet.' Finds the founder's stage from paying customers, not from code, and names the one next skill to use. Not for judging whether a specific activity or purchase is worth it (use focus)."
metadata:
  version: 1.0.0
---

# Journey

Find the founder's stage and name the one next step. The stage depends on paying customers, not on how much code exists.

## The order

Sell before you build. Get the first 10 paying customers by hand, then grow to 100.

| Stage | The founder says | Use | Gate to pass before the next stage |
|---|---|---|---|
| 0. No idea | "I don't have an idea yet" | **validate** (find the problem) | One problem that people they can name have now |
| 1. Idea | "I have an idea" | **validate**, then **is-this-an-app** | Evidence that strangers have the problem and spend money or time on it |
| 2. Sell by hand | "How do I get my first customers?" | **pricing**, **landing-page**, **email**, **first-customers**, then the manual delivery test in **validate** | 10 paying customers who are not friends or family, and the delivery steps written down |
| 3. Build | "Now I build it" | **build**, **beautify**, **secure** | The step that takes the most time is automated, and customers use it |
| 4. Go live | "Is it ready?" | **go-live**, **payments**, **legal** | go-live passes |
| 5. 10 to 100 | "How do I grow?" | **first-customers** (launch), **content**, **seo**, **retention** | 100 paying customers |

Use these at any stage: **focus** (is this worth my time or money), **finances** (runway and the quit number), **domain-name** (when the founder needs a name), **about-me** and **humanize** (writing in the founder's voice).

## Steps

1. Read the project's CLAUDE.md and README if they exist. Look for how many people pay today and what is built.
2. If you cannot tell, ask two questions in one message:
   - How many people pay you today?
   - What have you built so far?
3. Place the founder at the earliest stage whose gate they have not passed. A founder with a finished app and no paying customers is at stage 2, not stage 4. The code exists, but nobody has paid yet. Say this plainly. It is the most useful thing this skill can tell them.
4. Name one next skill and one next action for this week.

## Rules

- **One recommendation.** A list of five skills is a menu, and a founder who is lost cannot choose from a menu.
- **Do not skip a gate.** Building before stage 2 is the most common way founders lose months. A launch before 10 customers sends strangers to a product nobody has paid for.
- **A product that cannot be delivered by hand** (real-time collaboration, network effects) replaces the manual test with a pre-sale in **validate**. The gate stays at 10 paying customers.
- **Friends and family can buy, but they do not count toward a gate.** They pay to support the founder, not to solve a problem.

## Output

```
Stage: <number and name>
Why: <one sentence, from what the founder said or what the project shows>
Next: <one action for this week>
Skill: <one skill name>
Gate: <what must be true before the next stage>
```

## Example

User says: "My app is finished. Where do I launch it?"

The founder has no paying customers. Result:

```
Stage: 2. Sell by hand
Why: The app works, but nobody has paid for it yet.
Next: Sell it, one person at a time, to 10 people who have the problem.
Skill: first-customers
Gate: 10 paying customers who are not friends or family. Then launch.
```
