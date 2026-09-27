---
name: analytics
description: "Use this skill when the user needs to set up analytics, design event tracking, define key metrics, build funnels, or instrument their SaaS product for data-driven decisions. Covers event naming conventions, tracking strategy, funnel analytics, and data quality."
---

# Analytics & Instrumentation

Track decisions, not dashboards. This skill helps you set up analytics that answer the questions that matter — without drowning in data.

## Core Principles

- Every metric should connect to an action you'd take differently based on the result.
- Instrument events at build time, not as an afterthought. It's 10x easier.
- More data ≠ better decisions. Focus on 5-10 key metrics per stage.
- Data quality matters more than data quantity. One clean funnel beats fifty broken ones.

---

## Choosing an Analytics Tool

You don't need to write code to track events. Pick a tool, add the snippet, and configure in the UI.

### Recommended by Stage

| Stage | Tool | Why | Cost |
|-------|------|-----|------|
| Pre-revenue | **PostHog** | Product analytics, funnels, session replay. Built for SaaS. | Free (1M events/mo) |
| Pre-revenue | **Plausible** | Simple, privacy-first traffic analytics. | $9/mo |
| $0-5K MRR | **PostHog** or **Mixpanel** | Deeper funnel analysis, cohort retention | Free tier or ~$200/mo |
| $5K+ MRR | **Amplitude** or **Heap** | Advanced analytics, experimentation | $500+/mo |

**Recommendation for solo founders:** Start with **PostHog** (free tier). It covers product analytics, funnels, session recordings, and feature flags — all things you'll need.

For basic traffic analytics (where visitors come from), add **Plausible** or **Google Analytics 4** (free).

### Setup

**Tell AI:**
```
Set up PostHog analytics:
1. Create a PostHog project and get the API key
2. Add the PostHog JavaScript snippet to our app (in the <head> or layout component)
3. Verify it's tracking page views by checking the PostHog dashboard
4. Configure: exclude admin/test accounts from tracking
```

---

## What to Track (By Stage)

### Pre-Launch (Just These 3)
1. Landing page visits (traffic source)
2. Waitlist/signup conversions
3. Where visitors drop off

### 0-$1K MRR (Add These)
4. Signup → activation rate (completed key action)
5. Time to activate (hours from signup to key action)
6. D7 retention (% returning after 1 week)
7. Free-to-paid conversion

### $1K-$10K MRR (Add These)
8. Feature adoption (% of users using each feature weekly)
9. Cohort retention curves (track each month's signups over time)
10. Expansion revenue triggers (what behavior precedes upgrades)
11. Churn rate and reasons

---

## Event Naming Conventions

Use a consistent schema so events make sense to anyone reading them.

**Format:** [Object] [Action] in past tense, Title Case.

| Event Name | When It Fires |
|------------|--------------|
| Signup Form Submitted | User completes registration |
| Project Created | User creates their first/any project |
| Dashboard Viewed | User visits the main dashboard |
| Report Exported | User downloads or shares a report |
| Subscription Upgraded | User moves to a higher plan |
| Invite Sent | User invites a teammate |

**Rules:**
- Object first, then action (makes grouping in tools easier)
- Past tense (the event already happened)
- Be specific: "Signup Form Submitted" not "Form Submitted"
- Never include personal data in the event name

### Event Properties

Every event should include context:

```
"Project Created"
  template_used: "blank" | "marketing" | "engineering"
  source: "dashboard" | "onboarding" | "api"

"Subscription Upgraded"
  from_plan: "free"
  to_plan: "pro"
  billing_period: "annual"
  trigger: "usage_limit" | "feature_gate" | "self_serve"
```

**Tell AI:**
```
Set up event tracking for our core funnel:
- Track these events: [list your key events from the table above]
- Include these properties with each event: [relevant properties]
- Set user-level properties on identify: plan, signup_date, role
- Verify events are firing correctly in PostHog/Mixpanel
```

---

## Core Metrics Framework

### The 5 Metrics That Matter

| Metric | What It Tells You | How to Calculate |
|--------|------------------|-----------------|
| **Signup rate** | Is your marketing working? | Visitors → Signups |
| **Activation rate** | Is your onboarding working? | Signups → Completed key action |
| **D7 retention** | Does your product deliver ongoing value? | % of users returning 7 days later |
| **Free-to-paid** | Is your product worth paying for? | Free users → Paying users |
| **MRR** | Is your business growing? | Sum of all monthly subscription revenue |

### Setting Up Your Dashboard

**Tell AI:**
```
Create an analytics dashboard with these 5 charts:
1. Daily signups (line chart, last 30 days, by source)
2. Activation rate (% of signups who [completed key action], last 30 days)
3. D7 retention (% of each week's signups who returned 7 days later)
4. Free-to-paid conversion rate (last 30 days)
5. MRR (line chart, all time)

This should be the first thing I see when I open analytics.
```

---

## Funnel Instrumentation

Define your core funnel and track every step:

```
Typical SaaS funnel:
  1. Landing Page Viewed
  2. Signup Form Viewed
  3. Signup Form Submitted
  4. Onboarding Started
  5. [Key Activation Action] Completed
  6. Second Session (returned next day/week)
  7. Upgrade Page Viewed
  8. Subscription Created
```

**The biggest drop-off between steps = your biggest opportunity.** Fix that first.

**Tell AI:**
```
Instrument our conversion funnel:
- Track these events in order: [list your funnel steps]
- Build a funnel visualization showing drop-off between each step
- Set up an alert if any step's conversion drops below [X]% week-over-week
```

---

## Privacy and Compliance

Add these before you launch:

- [ ] Add analytics tool reference to your Privacy Policy
- [ ] Add cookie consent banner if required (depends on tool and geography)
- [ ] Enable "anonymize IP" in your analytics tool
- [ ] Exclude admin/test accounts from tracking
- [ ] Never track PII (email, name) in event properties without consent
- [ ] Allow users to opt out of tracking
- [ ] Respect Do Not Track (DNT) browser settings

**Tell AI:**
```
Add privacy compliance for analytics:
- Add a cookie consent banner that loads analytics only after consent
- Exclude users with DNT enabled
- Add an "opt out of tracking" toggle in account settings
- Ensure no PII is sent in event properties
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Tracking everything from day one | Start with 5 metrics. Add more when you have questions they can't answer. |
| No analytics until post-launch | Add the snippet during build. Track from first user. |
| Dashboard but no actions | Every metric should have an "if this drops, I'll do X" response |
| Ignoring data quality | Check that events are firing correctly once a week for the first month |
| Paying for expensive tools too early | PostHog free tier handles most needs until $5K MRR |

---

## If You Can't Set Up Analytics Right Now

Track these manually in a spreadsheet until you can:

| Week | Signups | Activated | Retained (D7) | Paid | MRR |
|------|---------|-----------|---------------|------|-----|
| Week 1 | | | | | |
| Week 2 | | | | | |

Even rough manual tracking beats flying blind. Graduate to a real tool as soon as you can.
