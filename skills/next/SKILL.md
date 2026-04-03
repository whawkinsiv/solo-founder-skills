---
name: next
description: "Use this skill when the user doesn't know what to work on next, asks 'what should I do?', wants to find high-value opportunities, or needs help deciding where to spend their time. Also use when the user mentions 'what should I do next,' 'what should I work on,' 'where should I focus,' 'find low-hanging fruit,' 'what's the most valuable thing I could do,' or 'I don't know what to do.' Scans the full project — code, infrastructure, marketing, growth, business — and surfaces 3-5 high-impact, low-effort opportunities ranked by value. Routes each recommendation to the right skill."
---

# What To Do Next

You sat down to work and don't know where to start. This skill scans your project — code, infrastructure, marketing, growth, business — and surfaces the 3-5 highest-value things you could do right now.

**This skill is for discovering what to work on when you don't know.** For evaluating whether a specific activity is worth your time, use **focus**. For ranking feature candidates you've already identified, use **prioritize**. For improving code performance, use **optimize**.

## How This Works

1. I read your project context (files, codebase, docs)
2. I ask 1-2 quick questions if I can't figure out your stage
3. I scan for high-value gaps across your whole business
4. You get a ranked list of opportunities with effort estimates and which skill to use

---

## Step 1: Gather Context

Read these files if they exist (silently — don't list what you're reading):
- About-me skill output or any founder context docs
- `product-marketing-context.md` or `.agents/product-marketing-context.md`
- CLAUDE.md, README, package.json
- Any analytics, metrics, or status docs

Scan the codebase for structure:
- What's built, what's missing, what's half-finished
- TODO/FIXME/HACK comments on important code
- Deployment config, monitoring, CI/CD, error tracking
- Marketing pages, analytics integration, SEO setup
- Test coverage, error handling patterns

**Only ask what you can't infer.** If existing context answers these, skip straight to scanning.

Max 2 questions, one message:

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

---

## Step 2: Scan for Opportunities

Look for signals across these categories. Use judgment about which matter based on the founder's stage — don't mechanically check every one.

**Product & Code**
- Critical paths with no error handling or tests
- TODO/FIXME/HACK comments on important code
- Obvious performance issues (missing indexes, N+1 queries)
- Features half-built or abandoned
- Security gaps (unprotected routes, exposed secrets)

**Infrastructure & Ops**
- No error monitoring on a live app
- No analytics on a launched product
- No backups, no CI/CD, manual deploys
- Missing environment variable management

**Marketing & Growth**
- Launched but no landing page (or a bad one)
- No SEO basics on a content-driven product
- Users but no onboarding flow
- Paying users but no retention or churn strategy
- Customers but no social proof anywhere

**Business & Strategy**
- Revenue but no financial tracking
- No terms of service or privacy policy on a live product
- Customers but no feedback collection
- Growing but no docs or support resources

### Stage-Aware Weighting

Don't treat all categories equally:
- **Pre-launch:** Lean heavily on product/code. Marketing and business signals are mostly noise at this stage.
- **Launched, few users:** Shift toward growth/activation. The product exists — now it needs to reach and retain people.
- **Revenue:** Business/strategy signals get real weight. Legal, financial, retention gaps have direct cost.

For each opportunity, assess:
- **Impact:** How much does this move the needle at this stage?
- **Effort:** Can this realistically be done today or this week?

Filter ruthlessly. Only surface opportunities where impact/effort is strongly favorable. If something is high impact but takes a month, it's not a "next" item.

---

## Step 3: Output

Present 3-5 opportunities, ranked by impact/effort ratio.

### Format

```
## What to do next

Based on: [stage summary] — [app name/type]

1. **[Action]** — [Why this matters right now, referencing what you found in their project]
   ~[time estimate] · Use `/[skill]`

2. **[Action]** — [Why this matters]
   ~[time estimate] · Use `/[skill]`

3. **[Action]** — [Why this matters]
   ~[time estimate] · Use `/[skill]`
```

### Output Rules

- **Plain English** — "you're live with no way to know when things break" not "no observability layer"
- **Specific to their project** — reference what you actually found, not generic advice
- **Effort in human time** — "~1 hour" or "~2-3 hours", not "low effort"
- **One skill per item** — if multiple skills apply, pick the starting one
- **3-5 items max** — cut anything that doesn't pass the impact/effort bar
- **No preamble** — no methodology explanation, no "here's what I found" intro. Just the list.

---

## Skill Routing Reference

Route each recommendation to the most relevant skill:

| Domain | Skills |
|--------|--------|
| Build features | **build**, **plan** (for scoping first) |
| Fix bugs | **debug** |
| Performance | **optimize** |
| Monitoring/errors | **monitor** |
| Security | **secure** |
| Testing | **test** |
| Deploy/go live | **deploy**, **go-live** |
| Database | **database** |
| Landing page | **landing-page** |
| Onboarding | **growth** (activation section) |
| SEO | **seo**, **technical-seo**, **seo-content** |
| Email | **email** |
| Analytics | **analytics** |
| Pricing | **pricing** |
| Legal | **legal** |
| Retention | **retention** |
| Payments | **payments** |
| Support/docs | **support** |
| Design/UI | **beautify**, **ux-design** |
| Content/copy | **content**, **copywriting** |
| Ads | **ads** |
| Social media | **social-media** |
| Launch | **launch** |
| Sales | **sales** |
| Customer research | **customer-research** |
| Finances | **finances** |
| Hiring | **hiring** |

---

## Related Skills

- **focus** — Evaluate whether a specific activity is worth your time (kill/refine/pivot)
- **prioritize** — Rank feature candidates with RICE scoring
- **growth** — Design product-led growth strategy and activation funnels
- **validate** — Test demand before building
- **optimize** — Make existing code faster and leaner
