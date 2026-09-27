---
name: prioritize
description: "Use this skill when the user needs to prioritize features, define an MVP, create a roadmap, or decide what to build next. Also use when the user asks 'what should I build first,' 'is this feature worth building,' 'how do I decide between X and Y,' or 'feature prioritization.' Covers RICE prioritization, hypothesis testing, MVP definition, and ruthless feature prioritization for early-stage SaaS."
---

# Product Strategy & Prioritization

The hardest product decision is what NOT to build. This skill helps you evaluate ideas, score features, and decide what to work on next — so you build the thing that matters most.

## Core Principles

- Features don't win markets. Solving a painful problem better than anyone else does.
- Ship the smallest thing that tests the biggest assumption.
- Product work is hypothesis testing, not feature delivery.
- Roadmaps are communication tools, not promises.
- For solo founders: do ONE thing well before adding the next.

---

## Workflow

```
Prioritization Process:
- [ ] List all feature candidates
- [ ] Score each with RICE
- [ ] Cut anything scoring below threshold
- [ ] Define MVP scope for the winner
- [ ] Write the spec (see plan skill)
- [ ] Build it
```

---

## Step 1: List Your Candidates

Gather every idea, request, and "we should build..." into one place.

**Tell AI:**
```
Help me organize feature candidates for prioritization:
- Product: [what it does]
- Current stage: [pre-launch / 0-$1K MRR / $1K-$10K MRR]
- Current pain points: [what users are asking for or struggling with]

Here are my feature ideas:
1. [Feature idea]
2. [Feature idea]
3. [Feature idea]
4. [Feature idea]

For each, identify: what user problem it solves, who it helps, and whether it drives
acquisition, activation, retention, or revenue.
```

---

## Step 2: Score with RICE

| Factor | Question | Scale |
|--------|----------|-------|
| **R — Reach** | How many users will this affect in the next quarter? | Number of users |
| **I — Impact** | How much will it move the key metric? | 3=massive, 2=high, 1=medium, 0.5=low |
| **C — Confidence** | How sure are you about reach and impact? | 100%, 80%, 50% |
| **E — Effort** | Person-weeks of engineering time? | Weeks |

**Score = (Reach x Impact x Confidence) / Effort**

Rank by score, but use judgment — scores are conversation starters, not final answers.

**Tell AI:**
```
Score these features using RICE prioritization:

[Paste your feature list]

For our context:
- Total active users: [number]
- Key metric we're trying to improve: [activation rate / retention / revenue / etc.]
- My capacity: [solo founder / one developer / small team]

Create a table: Feature | Reach | Impact | Confidence | Effort | RICE Score | Rank
Then recommend which to build first and why — don't just go by the numbers.
```

---

## Step 3: Define MVP Scope

For the winning feature, cut scope ruthlessly.

### Five Questions to Cut Scope

1. What is the ONE problem this solves? (Not three. One.)
2. Who is the ONE persona who has this problem most acutely?
3. What is the minimum experience that solves their problem?
4. What can be manual, janky, or behind-the-scenes for v1?
5. What's the fastest path to a real user doing a real task?

The MVP should be:
- Usable by a real person for a real purpose
- Small enough to ship in 2-4 weeks
- Instrumented so you learn whether it works
- Embarrassingly small in scope but surprisingly polished in execution

**Tell AI:**
```
Help me cut scope for this feature:
- Feature: [what you want to build]
- Full vision: [everything you'd ideally include]
- Time budget: [how long you want to spend — 1 week, 2 weeks, etc.]

What's the absolute minimum version that:
1. Solves the core problem
2. Ships within my time budget
3. Lets me learn whether users actually want this

List what's IN v1 and what's explicitly OUT (saved for v2).
```

---

## Saying No to Features

Cut a feature when:
- It serves <10% of your target users
- It adds complexity that affects the other 90%
- It requires ongoing maintenance but doesn't drive retention or revenue
- A workaround exists that's "good enough"
- It's a sales request from one loud customer, not a pattern
- It moves you toward a different product category

**Tell AI:**
```
A user/customer is requesting [feature]. Help me decide:
- What problem are they actually trying to solve?
- How many other users likely have this problem?
- Is there a workaround that's good enough?
- If we build it, what's the maintenance cost?
- Does this align with our core product direction?

Give me a recommendation: build it, defer it, or decline it — with reasoning
I can share with the requester.
```

---

## Feature Spec Template

Once you've decided what to build, spec it before handing it to an AI tool:

```markdown
## [Feature Name]

### Problem
What user problem does this solve? What's the evidence?

### Users
Who specifically needs this? How many?

### Proposed Solution
Describe the experience, not the implementation.

### Success Metrics
How will we know this worked? What moves?

### Scope (v1)
What's in. Be specific.

### Non-Goals (v1)
What's explicitly out. This is the most important section.

### Open Questions
What do we need to answer before building?

### Effort Estimate
T-shirt size: S / M / L / XL
```

See **plan** skill for full spec templates and examples.

---

## Competitive Positioning

Don't try to have more features. Instead:

1. Identify where incumbents are weakest (usually: complexity, speed, price, or audience fit)
2. Be 10x better at ONE thing rather than 10% better at ten things
3. Define your "wedge" — the narrow use case you win decisively
4. Expand from the wedge once you own it

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Building what's loudest, not what's most impactful | Score with RICE. Loud ≠ important. |
| "MVP" that takes 3 months | If it takes more than 2-4 weeks, cut more scope |
| No success metrics defined | Define "how we'll know this worked" before building |
| Building for one customer's request | Look for patterns across 3+ users/requests |
| Adding features to match competitors | Compete on depth in your wedge, not breadth |
| No out-of-scope list | Explicitly define what's NOT in v1 to prevent creep |

---

## Related Skills

- **plan** — Write detailed specs after prioritizing
- **validate** — Validate demand before building
- **analytics** — Set up tracking to measure feature impact
- **growth** — Prioritize features that drive activation and retention
- **build** — Hand your spec to AI tools and build it
