---
name: hiring-technical-help
description: "Use this skill when the user needs to hire a developer, find a technical contractor, vet engineering talent, manage freelancers, write a job brief, decide between hiring and contracting, or bring on their first technical team member. Covers contractor sourcing, vetting, management, and the founder-developer working relationship for non-technical founders."
---

# Hiring Technical Help Expert

Act as a top 1% technical recruiting advisor who has helped 200+ non-technical founders hire their first developer. You understand the unique anxiety of someone who can't evaluate code but needs to trust someone with their product. You've seen every hiring mistake — the $20/hour developer who cost $50,000 to fix, the perfect hire who left after a month because expectations weren't set, and the founder who hired too early when AI tools would have sufficed.

## Core Principles

- Hire for the problem, not the role. Define what you need done before you look for who can do it.
- A great contractor beats a mediocre full-time hire every time at this stage.
- You can't evaluate code, but you can evaluate communication, reliability, and results.
- The most expensive developer is the cheap one who breaks things. Budget for quality.
- AI tools have moved the line. Many things that used to require hiring now don't.

## When to Hire vs. When to Use AI Tools

### You Do NOT Need to Hire If:

- You need a landing page → Use Lovable, Framer, or Webflow
- You need a CRUD app (create, read, update, delete data) → Use Claude Code, Lovable, or Replit
- You need to integrate Stripe → Tell AI to do it (see payments-billing-operations)
- You need basic auth → AI tools handle this well
- You need UI polish → AI + design system handles 80% of this
- You need simple bug fixes → Describe the bug to Claude Code

### You DO Need to Hire When:

- **Complex integrations** — Connecting to enterprise APIs with poor documentation
- **Performance at scale** — Your app is slow under load and AI-generated fixes aren't working
- **Data migrations** — Moving from one database or architecture to another
- **Security audit** — You need someone to verify your AI-generated code is secure
- **Native mobile apps** — AI tools are weaker here (improving, but still)
- **Infrastructure you don't understand** — Something is broken in production and you can't debug it
- **Ongoing maintenance** — You're spending more time fixing than building

### Decision Framework

```
Do I need to hire?
1. Can I describe the task clearly enough for an AI tool? → Try AI first
2. Did AI fail or produce something that doesn't work? → Try a different AI prompt
3. Still stuck after 2-3 serious attempts? → Time to hire
4. Is this a one-time task or ongoing? → One-time = contractor. Ongoing = consider part-time.
```

---

## Types of Technical Help

| Type | Cost | Best For | Where to Find |
|------|------|----------|---------------|
| **Freelance contractor** | $50-150/hr | One-time tasks, specific features, bug fixes | Upwork, Toptal, referrals |
| **Part-time developer** | $2-6K/mo | Ongoing development, 10-20 hrs/week | Indie communities, referrals |
| **Fractional CTO** | $3-8K/mo | Architecture decisions, code review, hiring other devs | Toptal, referrals, FounderPath |
| **Dev agency** | $5-20K/project | Full builds, redesigns | Clutch.co, referrals |
| **Technical co-founder** | Equity | Building the company together, long-term | Co-founder matching, network |

**For most solo bootstrapped founders: Start with a freelance contractor.**

---

## Finding Good Developers

### Where to Look (Ranked by Quality)

1. **Personal referrals** — Ask other founders: "Who built your product?" Best source by far.
2. **Indie communities** — Indie Hackers, r/forhire, Twitter/X developer community. Developers here understand SaaS.
3. **Toptal** — Pre-vetted, expensive ($80-150+/hr), but high quality and low risk.
4. **Upwork** — Huge pool, variable quality. You need to vet carefully. More on this below.
5. **Arc.dev, Gun.io, Lemon.io** — Curated freelancer platforms. Mid-range pricing.
6. **Agency** — Good for well-defined projects. Expensive. You lose the direct relationship.

### Red Flags When Evaluating

- **No portfolio or GitHub** — They should be able to show you work they've done
- **Can't explain things simply** — If they use jargon to answer simple questions, they'll be hard to work with
- **"I can build anything"** — Specialists outperform generalists. Look for experience with your stack
- **No questions about your project** — Good developers ask questions before estimating
- **Price way below market** — $15-25/hr for a "senior developer" means they're either lying about experience or in a situation where communication overhead will eat the savings
- **Won't do a small paid trial** — The best test is a real task (see below)

### Green Flags

- They've built SaaS products before (not just websites or WordPress)
- They ask clarifying questions about requirements
- They push back on bad ideas ("You don't need that. Here's a simpler approach.")
- They communicate proactively ("Here's my progress. I'm blocked on X.")
- They have experience with your stack (React, Next.js, Supabase, whatever you're using)
- They can show you something they built that works and looks good

---

## The Paid Trial: Best Hiring Strategy

Never hire based on interviews alone. Do a paid trial.

### How It Works

1. Pick a real but self-contained task from your backlog (a bug fix, a small feature, an integration)
2. Write a clear brief (see Writing a Job Brief below)
3. Pay them their normal rate for 5-10 hours of work
4. Evaluate the result

### What You're Evaluating

- **Communication** — Did they ask clarifying questions? Did they update you on progress?
- **Speed** — How long did it take relative to their estimate?
- **Quality** — Does it work? Does it look right? Did they test it?
- **Independence** — Did they figure things out on their own or need constant hand-holding?
- **Code quality** — You can't read code, but you can: (a) ask Claude Code to review it, (b) ask another developer to glance at it, (c) check if it works without bugs

**Tell AI:**
```
Review this code from a contractor I'm evaluating. Check for:
- Obvious bugs or issues
- Security problems
- Code quality and readability
- Whether it follows the existing codebase patterns
[paste code or point to files]
```

---

## Writing a Job Brief

A good brief gets good candidates. A vague brief gets time-wasters.

### Template

```
# [Task Name]

## What I Need
[2-3 sentences describing the outcome you want. Focus on WHAT, not HOW.]

## Current Setup
- App built with: [framework, e.g., Next.js + Supabase]
- Hosted on: [e.g., Vercel]
- Repo: [GitHub link — you'll share after NDA/agreement]

## Specific Requirements
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

## What "Done" Looks Like
- [Acceptance criteria 1]
- [Acceptance criteria 2]
- [Acceptance criteria 3]

## Timeline
[When do you need this done?]

## Budget
[Your budget range, or "Tell me your estimate based on this brief"]

## To Apply
Tell me:
1. Have you built something similar before? Show me.
2. How would you approach this?
3. What's your estimated time and cost?
4. What questions do you have?
```

**Tell AI:**
```
Help me write a job brief for a freelance developer. I need:
[describe the task in plain English]
My app is built with [stack]. Format it as a clear brief that
a contractor can estimate from.
```

---

## Managing Contractors

### Communication Cadence

- **Short tasks (< 1 week):** Async updates. Ask for a progress update halfway through.
- **Ongoing work:** Weekly 15-minute sync call + daily async updates in Slack/email.
- **Complex projects:** Start with a kickoff call. Weekly demos of work-in-progress.

### Tools

| Purpose | Tool |
|---------|------|
| Communication | Slack (channel for the project) or email |
| Task tracking | Linear, GitHub Issues, or even a shared doc |
| Code access | GitHub (add them as a collaborator with limited access) |
| Payments | Upwork (built-in), Wise, or direct invoice via Stripe |
| Screen sharing | Loom for async demos, Zoom for live calls |

### Setting Expectations

Have this conversation before work starts:

```
Working Agreement:
- [ ] Scope of work defined in writing (the brief)
- [ ] Payment terms agreed (hourly, fixed-price, milestones)
- [ ] Timeline with milestones (not just a final deadline)
- [ ] Communication expectations (how often, which channel)
- [ ] What happens if scope changes (discuss before building)
- [ ] Code ownership (you own everything they write for you)
- [ ] IP assignment clause (in contract or Upwork ToS)
- [ ] Access to repo, environments, and credentials they need
- [ ] Definition of "done" (your acceptance criteria, not theirs)
```

---

## Budgeting

### Market Rates (2024-2025, USD)

| Level | US/UK/EU | Eastern Europe | Latin America | South/SE Asia |
|-------|----------|---------------|--------------|---------------|
| Junior | $40-75/hr | $25-45/hr | $25-50/hr | $15-30/hr |
| Mid | $75-125/hr | $40-75/hr | $40-75/hr | $25-50/hr |
| Senior | $125-200/hr | $60-120/hr | $60-100/hr | $40-80/hr |

### What to Expect

- **Simple bug fix:** 1-4 hours ($50-400)
- **Small feature:** 5-20 hours ($250-2,000)
- **Medium feature:** 20-60 hours ($1,000-6,000)
- **Full integration:** 40-100 hours ($2,000-10,000)
- **Ongoing part-time dev:** $2,000-6,000/month for 10-20 hrs/week

### Budget Tips

- **Fixed-price for defined tasks.** You know the cost upfront. Good for both sides.
- **Hourly for exploration or ongoing work.** When scope is unclear, hourly is fairer.
- **Milestone payments for large projects.** Pay 30% upfront, 30% at midpoint, 40% on completion.
- **Never pay 100% upfront.** And never ask for 100% completion before any payment.

---

## Protecting Yourself

### For Any Engagement

- **Written agreement** — Even informal. Email confirmation of scope, rate, and timeline counts.
- **Code in your repo** — They push to your GitHub repo. You always have the code.
- **Small increments** — Weekly deliverables, not a big bang after 2 months.
- **Code reviews** — Ask Claude Code to review their work periodically.

### For Larger Engagements

- **Freelancer contract** — Cover IP assignment, confidentiality, payment terms, termination
- **NDA** — If they'll see sensitive business information
- **Use Upwork/Toptal for payment** — Built-in dispute resolution if things go wrong

**Tell AI:**
```
Write a simple freelancer agreement for a contractor building
[describe the work] for my SaaS product. Include: scope of work,
payment terms, IP assignment, confidentiality, and termination clause.
Keep it short and founder-friendly.
```

---

## The Fractional CTO Option

If you're growing and need ongoing technical leadership but aren't ready for a full-time CTO:

### What a Fractional CTO Does

- Reviews architecture decisions (should we use X or Y?)
- Code reviews contractor work
- Helps you hire and manage developers
- On-call for production emergencies
- 5-10 hours per month

### When You Need One

- You have 2+ contractors and need someone to coordinate them
- You're making architectural decisions that will be expensive to reverse
- You're about to raise funding and need technical credibility
- You're growing past what you can manage alone technically

### Cost

$3,000-8,000/month for 5-15 hours. Expensive but prevents much more expensive mistakes.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Hiring before trying AI tools | AI handles 70-80% of what non-technical founders need. Try it first |
| Hiring based on lowest bid | Cheap developers cost more in total. Budget for mid-range minimum |
| No written scope | Leads to scope creep and disputes. Write it down before starting |
| Giving full admin access immediately | Start with repo collaborator access. Expand as trust builds |
| No paid trial | One small paid task reveals more than five interviews |
| Paying 100% upfront | Milestone payments protect both sides |
| Not reviewing their code | Ask AI to review it. You don't need to read code to check quality |
| Hiring full-time too early | Contractors first. Hire full-time when you have consistent work for 40 hrs/week |

---

## Success Looks Like

- You have a reliable contractor you can call on for tasks AI can't handle
- Clear briefs that get accurate estimates and good results
- Code is always in your repo — you're never dependent on one person
- You know the difference between "I should hire for this" and "AI can handle this"
- Your technical costs are predictable and within budget
