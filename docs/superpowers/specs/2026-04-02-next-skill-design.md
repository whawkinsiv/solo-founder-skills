# "next" Skill — Design Spec

## Problem

Solo founders frequently sit down to work and don't know what to do next. They default to whatever feels urgent or comfortable — usually more coding — when higher-leverage work exists across marketing, infrastructure, growth, or business operations. They need something that scans the full picture and surfaces what actually matters.

## What This Skill Does

Scans the founder's project holistically — codebase, infrastructure, marketing, growth, business — and surfaces 3-5 high-value, low-effort opportunities they haven't thought of. Ranks them by impact/effort ratio and routes each to the right skill.

## What This Skill Is NOT

- **Not `focus`** — focus evaluates a specific activity you're already doing (should I keep doing X?)
- **Not `prioritize`** — prioritize ranks feature candidates you've already identified (RICE scoring)
- **Not `optimize`** — optimize improves performance of existing code
- **`next` comes before those** — it tells you where to look when you don't know where to look

## Core Flow

### Phase 1: Gather Context

Read existing context files first, ask questions only for what's missing.

**Files to check:**
- `about-me` skill output (if it exists)
- `product-marketing-context.md` / `.agents/product-marketing-context.md`
- CLAUDE.md, README, package.json (app type, dependencies, structure)
- Any analytics, metrics, or status docs in the project

**Scan the codebase:**
- Directory structure, what exists, what's missing
- TODO/FIXME/HACK comments
- Error handling patterns, test coverage presence
- Deployment config, monitoring config, CI/CD
- Marketing pages, SEO setup, analytics integration

**Ask only what can't be inferred — max 2 questions in a single message:**

```
Quick context so I can find the right opportunities:

1. What stage are you at?
   a) Still building, not launched
   b) Launched, few/no users yet
   c) Have users, no revenue
   d) Have paying customers

2. What's your biggest frustration right now?
   a) Not sure what to build next
   b) Built it but nobody's using it
   c) People sign up but don't stick
   d) Growing but everything feels fragile
   e) Something else: ___
```

If existing context files already answer these, skip questions entirely and go straight to scanning.

### Phase 2: Scan for Opportunities

Signal-based, not checklist-based. Claude uses judgment about which signals matter based on the founder's stage. Does not mechanically check every category.

**Signal categories (examples, not exhaustive — Claude should use judgment):**

**Product & Code**
- Critical paths with no error handling or tests
- TODO/FIXME/HACK comments on important code
- Missing database indexes, N+1 queries, obvious performance issues
- Features half-built or abandoned
- Security gaps (no auth on routes that need it, exposed secrets)

**Infrastructure & Ops**
- No error monitoring on a live app
- No analytics/tracking on a launched product
- No backups, no CI/CD, manual deployment process
- Missing environment variable management

**Marketing & Growth**
- Launched but no landing page (or a terrible one)
- No SEO basics on a content-driven product
- Users but no onboarding flow
- Paying users but no retention/churn strategy
- No social proof despite having customers

**Business & Strategy**
- Revenue but no financial tracking
- No terms of service / privacy policy on a live product
- Customers but no feedback collection mechanism
- Growing but no documentation/support resources

**Stage-aware weighting:**
- Pre-launch: lean heavily on product/code signals
- Post-launch with users: shift toward growth/ops
- With revenue: business/strategy signals get more weight

For each opportunity found, assess:
- **Impact** — how much does this move the needle at this stage?
- **Effort** — can this be done today or this week?
- Filter ruthlessly — only surface opportunities where the impact/effort ratio is strongly favorable

### Phase 3: Output

Top 3-5 opportunities, ranked by impact/effort ratio.

**Format:**

```
## What to do next

Based on: [pre-launch / live with ~X users / $X MRR] — [app type/name]

1. **Set up error monitoring** — You're live with no way to know when things break. Users will hit errors and leave silently.
   ~1 hour · Use `/monitor`

2. **Add a basic onboarding flow** — 3 signups this week, but nothing guides them to the aha moment. Most are probably bouncing.
   ~2-3 hours · Use `/build` with the onboarding spec from `/plan`

3. **Write your landing page** — You're getting traffic from [source] but sending them to a raw app login. That's a leaky bucket.
   ~2 hours · Use `/landing-page`
```

**Output rules:**
- Plain English, no jargon — "you're live with no way to know when things break" not "no observability layer"
- Concrete and specific — references what it actually found in the project, not generic advice
- Effort in human time — "~1 hour" not "low effort"
- One skill per item — if it needs multiple skills, pick the starting skill
- 3-5 items max — ruthlessly cut anything below the impact/effort bar
- Items are already in priority order (numbers are just for reference when picking)
- No preamble, no methodology explanation — just the list

## Skill Metadata

```yaml
name: next
description: Use this skill when the user doesn't know what to work on next, asks "what should I do?", wants to find high-value opportunities, or needs help deciding where to spend their time. Scans the full project — code, infrastructure, marketing, growth, business — and surfaces 3-5 high-impact, low-effort opportunities ranked by value. Routes each recommendation to the right skill.
```

## Trigger Phrases

- "what should I do next"
- "what should I work on"
- "where should I focus"
- "find low-hanging fruit"
- "what's the most valuable thing I could do"
- "help me decide what to work on"
- "I don't know what to do"
