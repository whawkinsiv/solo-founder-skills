---
name: customer-research
description: "Use this skill when the user needs to understand their customers, create personas, conduct user interviews, or apply the Jobs-to-be-Done framework. Covers JTBD methodology, behavioral personas, interview techniques, and extracting actionable insights."
---

# Customer Research & Personas

Personas based on demographics are useless. Personas based on behaviors, goals, and constraints drive decisions. This skill helps you run interviews, apply Jobs-to-be-Done, and build personas that actually inform your product.

## Core Principles

- Personas based on demographics are useless. "34-year-old male marketer" tells you nothing about product design.
- Personas based on behaviors, goals, and constraints drive decisions.
- The goal of research is to discover what users DO, not what they SAY they want.
- Five good interviews reveal 80% of usability issues.
- Jobs-to-be-Done > traditional personas for SaaS product decisions.

## Jobs-to-be-Done Framework

A "job" is the progress a user is trying to make in a specific circumstance.

**Job statement format:**
"When I [situation], I want to [motivation], so I can [desired outcome]."

**Examples:**
- "When I'm preparing for a board meeting, I want to pull together our key metrics quickly, so I can spend my time on the narrative, not the data."
- "When a new developer joins our team, I want to get them productive on day one, so I can maintain our shipping velocity."

**Discover jobs by asking:**

1. "Walk me through the last time you [did the thing]."
2. "What were you trying to accomplish?"
3. "What did you try first? What happened?"
4. "What was frustrating about that?"
5. "What would 'good enough' look like?"
6. "What would 'amazing' look like?"

## Behavioral Persona Template

```markdown
## [Persona Name] — [One-line role description]

### Behavioral Segment
What behavior defines this group? (e.g., "Uses the product daily for team
coordination" or "Evaluates tools quarterly for the team")

### Primary Job
[Job statement in JTBD format]

### Context
- Role and responsibilities (relevant to product usage)
- Team size and structure
- Tools they use alongside yours
- Technical sophistication level
- Decision-making authority (buyer, influencer, user)

### Current Workflow (without your product)
Step-by-step: How do they accomplish this job today?
Where are the friction points?

### Key Pain Points
1. [Specific, observed pain — not assumed]
2. [Another specific pain]
3. [Another specific pain]

### Success Criteria
How do they measure whether the job is done well?
What would make them say "this is working"?

### Objections / Barriers to Adoption
What would prevent them from trying or buying?

### Trigger Events
What circumstances push them to seek a new solution?
(Team growth, tool sunset, new mandate, frustration peak)
```

## User Interview Guide

**Before the interview:**
- Define your learning goal: What decision will this inform?
- Recruit based on behavior, not demographics.
- 5-8 interviews per persona segment is usually sufficient.

**Opening (2 min):**
"Thanks for joining. I'm trying to understand how people [do X]. There are no right answers — I'm learning from your experience. Can I ask you some questions about how you currently handle [topic]?"

**Core questions (25 min):**

1. "Tell me about your role. What does a typical week look like?"
2. "When was the last time you [relevant task]? Walk me through it."
3. "What tools do you use for this? How did you end up with those?"
4. "What's the most frustrating part of this process?"
5. "If you could wave a magic wand and fix one thing, what would it be?"
6. "Have you tried other solutions? What happened?"
7. "Who else is involved in this process?"
8. "How do you decide when to invest in a new tool for this?"

**Closing (3 min):**
"Is there anything about [topic] I should have asked but didn't?"
"Would you be open to trying an early version and giving feedback?"

## When You ARE the Persona

If you're building for your own profession, you have a unique advantage and a unique blind spot.

**The advantage:** You understand the pain deeply. You don't need to "discover" the problem — you've lived it.

**The blind spot:** You assume everyone does the job the way you do. They don't. After 20 years, your workflow is optimized. A 3-year practitioner's workflow is different. A solo practitioner's is different from someone at a large firm.

**How to correct for this:**
- Interview people at different experience levels (junior, mid, senior)
- Interview people at different organization sizes (solo, small firm, large firm)
- When they describe their process and it's different from yours, don't correct them. That's data.
- Ask: "What tools do you actually use?" — not "Would you use a tool that does X?"
- The question isn't "Do I have this pain?" — it's "Do enough OTHER people have it, and will they pay?"

---

## Interview Analysis

After interviews, synthesize:

1. **Common patterns:** What did 3+ people say independently?
2. **Surprising insights:** What contradicted your assumptions?
3. **Exact quotes:** Capture the user's words, not your interpretation.
4. **Pain intensity:** Rate each pain point (annoying vs. hair-on-fire).
5. **Willingness to pay:** Would they pay to solve this? How much?

## Turning Research into Action

Research is only valuable if it changes decisions:

- **Feature prioritization:** "Persona A's #1 pain is X, which maps to feature Y."
- **Messaging:** Use their exact words in marketing copy.
- **Onboarding:** Design the first-run experience around their primary job.
- **Pricing:** Align tiers with persona segments.
- **Roadmap:** Sequence features by persona priority.

## Related Skills

- **validate** — Validate demand before building (uses similar interview techniques)
- **prioritize** — Turn research insights into feature prioritization
- **copywriting** — Use customer language in your marketing copy
- **feedback** — Ongoing feedback collection after launch
