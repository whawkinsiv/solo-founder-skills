---
name: customer-research
description: "Use this skill when the user needs to understand their customers, create personas, conduct user interviews, apply the Jobs-to-be-Done framework, or create an ideal customer profile. Also use when the user says 'ICP,' 'ideal customer,' 'who is my customer,' 'customer profile,' or 'target audience.' Covers JTBD methodology, behavioral personas, interview techniques, and creates MY-ICP.md — a reference file that other skills use to personalize copy with customer language."
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

---

## Capture Your ICP: Create MY-ICP.md

Research is useful in the moment. `MY-ICP.md` makes it useful forever. This file captures who your customer is so every other skill — landing pages, ads, email, pricing copy — can use their language instead of your marketing language.

### When to create it

- After completing interviews and synthesizing findings
- After building behavioral personas above
- Or right now, if you're a domain expert who already knows your customer deeply

### Quick capture for domain experts

If you ARE your customer (or were recently), you can skip interviews and write this directly. But be honest about your blind spots — the "When You ARE the Persona" section above still applies.

> Describe your ideal customer. Be specific about who they are, what frustrates them, what they're trying to accomplish, how they make buying decisions, and what words they actually use when talking about this problem. If you have multiple customer types, describe each one — start with your primary.

### After interviews

Pull from your Interview Analysis above:
- **Exact quotes** become the "Their Language" section
- **Common patterns** become "Their Pain" and "Their Goals"
- **Pain intensity** informs priority within sections

### MY-ICP.md template

```markdown
# My Ideal Customer Profile

## Primary ICP: [Name or label — e.g., "Solo Consultants" or "Marketing Managers at Series A startups"]

### Who They Are
[Role, company size, experience level, relevant demographics.
Not a persona — specific enough that you could find them on LinkedIn.]

### Their Pain
[Primary problems, current workarounds, what frustrates them.
Use THEIR words, not your marketing language.
Example: "I spend 3 hours every Monday pulling reports from 4 different tools"
not "inefficient multi-platform reporting workflows."]

### Their Goals
[What success looks like to them. What they're trying to achieve.
The outcome they'd pay for, in their framing.]

### How They Buy
[Decision process — do they decide alone or need approval?
Common objections. Price sensitivity. What triggers a purchase.
What makes them say no.]

### Their Language
[Actual words and phrases they use to describe the problem.
Pull directly from interviews, Reddit posts, reviews, support tickets.
This section is gold for landing pages, ads, and email subject lines.]

### Where They Are
[Communities, publications, events, Slack groups, subreddits, LinkedIn groups.
Where you can reach them. Where they go for advice.]

---

## Secondary ICP: [Name or label] (if applicable)

[Same sections as above. Only add a secondary if the audiences are
genuinely distinct — different roles, different pains, different language.
If they're similar, one profile is fine.]
```

### What makes a good MY-ICP.md

- **Their words, not yours.** "I waste hours on reporting" not "streamline analytics workflows."
- **Specific enough to find them.** "Marketing managers at B2B SaaS companies with 20-100 employees" not "marketers."
- **Pain described with intensity.** "Hair-on-fire: broken onboarding causes 40% of trials to churn in 3 days" not "onboarding could be improved."
- **Multiple ICPs only if truly distinct.** Don't split into 5 segments. Most early-stage products have 1-2.

---

## Related Skills

- **about-me** — Creates `ABOUT-ME.md`, the companion file. MY-ICP.md is who your customer is. ABOUT-ME.md is who you are. Together they let skills personalize both message and voice.
- **validate** — Validate demand before building (uses similar interview techniques)
- **prioritize** — Turn research insights into feature prioritization
- **copywriting** — Use customer language (from MY-ICP.md) in your marketing copy
- **landing-page** — Uses MY-ICP.md "Their Language" and "Their Pain" sections for copy
- **feedback** — Ongoing feedback collection after launch
