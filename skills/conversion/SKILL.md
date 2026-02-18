---
name: conversion
description: "Use this skill when the user needs to improve conversion rates, reduce funnel drop-off, optimize signup flows, or increase trial-to-paid conversion. Covers funnel analysis, friction reduction, behavioral psychology, social proof, and A/B testing strategies."
---

# Conversion Rate Optimization

Every page has one job. If you can't name it, the page is broken. This skill helps you find where users drop off and fix it.

## Core Principles

- Friction is the enemy. Every field, click, and decision point costs conversions.
- Don't guess — measure. But don't measure everything — measure what drives revenue.
- Social proof is the most underused conversion lever in SaaS.
- Speed is a feature. Every 100ms of load time costs ~1% conversion.
- The best optimization is often removal, not addition.

---

## Finding Your Biggest Bottleneck

Before optimizing, find where users actually drop off.

### Step 1: Map Your Funnel

```
Typical SaaS funnel:
  Landing page visit → Signup page viewed → Account created →
  Onboarding started → Key action completed → Returned next week →
  Upgrade page viewed → Subscription created
```

### Step 2: Measure Drop-Off

**Tell AI:**
```
Analyze our conversion funnel:
- Pull the number of users at each step: [list your funnel steps]
- Calculate the drop-off % between each step
- Identify the step with the biggest drop-off — that's our priority
- Show results in a table: Step | Users | Drop-off %
```

**If you don't have analytics yet:** Set them up first (see analytics-instrumentation skill). In the meantime, track manually: count signups, count activations, count paying customers. Even rough numbers reveal the biggest leak.

### Step 3: Diagnose Why

For the biggest drop-off, evaluate the page/flow using this framework:

1. **CLARITY:** Does the user know what to do and why?
2. **MOTIVATION:** Is the value of completing this step obvious?
3. **FRICTION:** What's making this harder than it needs to be?
4. **ANXIETY:** What fears or objections might stall the user?
5. **DISTRACTION:** What elements compete with the primary action?

---

## Signup & Registration

- Minimize fields. Email + password is ideal. Email-only or SSO is even better.
- Defer everything else to onboarding (company name, role, team size).
- Show password requirements before the user types, not after they fail.
- Social login (Google, GitHub) should be visually prominent if your audience uses them.
- Post-signup, go DIRECTLY to value — not a "check your email" dead end.

**Tell AI:**
```
Simplify our signup flow:
- Reduce to email + password (or email-only with magic link)
- Add Google Sign-In as the most prominent option
- After signup, redirect directly to onboarding (not "check your email")
- Defer all profile questions (name, company, role) to later
```

---

## Pricing Page Optimization

- Always include a recommended/highlighted tier.
- Show annual pricing by default with monthly as a toggle.
- Use price anchoring: show the most expensive plan first or feature the mid-tier.
- "Free forever" converts better than "free trial" for hesitators.
- Add FAQ section: "Can I cancel anytime?", "What happens to my data?", "Is there a setup fee?"

**Tell AI:**
```
Optimize our pricing page:
- Highlight the recommended tier with a visual badge ("Most Popular")
- Default to annual pricing (show monthly as toggle)
- Add a comparison table showing features by tier
- Add FAQ section below pricing addressing common objections
- Add social proof near the CTA: "[X] teams already use [Product]"
```

---

## Trial-to-Paid Conversion

- **Reverse trial:** Give full access, then downgrade — users feel loss aversion.
- Show usage vs. plan limits: "You've used 847 of 1,000 API calls this month."
- Trigger upgrade prompts at the moment of value, not on a timer.
- Frame limits as growth: "Your team is growing! Upgrade to add unlimited members."

**Tell AI:**
```
Improve trial-to-paid conversion:
- Show usage meters on the dashboard: "X of Y [resource] used"
- When user hits 80% of a limit, show a gentle prompt: "You're growing! Upgrade for unlimited [resource]"
- 3 days before trial ends, show banner: "Your trial ends [date]. Keep everything by upgrading."
- After trial ends, downgrade features but keep their data intact
```

---

## Form Optimization

- Multi-step forms convert 20-40% better than single long forms.
- Show progress: "Step 2 of 3"
- Start with easy/engaging questions (not name/email).
- Use smart defaults: pre-select the most common option.
- Inline validation on blur. Show checkmarks for completed fields.

**Tell AI:**
```
Convert our [signup/onboarding] form to multi-step:
- Step 1: The easiest, most engaging question
- Step 2: The information we need to deliver value
- Step 3: Account details (email, password)
- Add progress indicator ("Step 2 of 3")
- Validate inline on blur with green checkmarks
- Use appropriate input types (email, tel, number) for mobile keyboards
```

---

## Behavioral Triggers

| Trigger | How to Use It |
|---------|--------------|
| **Loss aversion** | "Your free trial ends in 3 days" > "Upgrade now" |
| **Social proof** | "4,200 teams signed up this month" |
| **Anchoring** | Show the "before" (manual, slow) vs. "after" (with your product) |
| **Commitment/consistency** | Small yes → big yes. Free tool → signup → paid. |
| **Scarcity (use honestly)** | "3 spots left in this cohort" (only if true) |

**Tell AI:**
```
Add social proof and behavioral triggers to our [signup/pricing/landing] page:
- Add a live counter or recent activity: "[X] teams signed up this month"
- Add testimonial quotes near the CTA
- Add trust badges near payment forms (SSL, money-back guarantee)
- Frame the CTA as low-commitment: "Start free — no credit card required"
```

---

## A/B Testing (Simple Version)

You don't need complex testing infrastructure. Here's the bootstrapped founder approach:

### When to A/B Test

- You have at least 100 users/week going through the flow
- You have a specific hypothesis, not just "let's try something different"
- The change is significant enough to matter (button color doesn't matter; headline copy does)

### How to Run a Test

**Tell AI:**
```
Set up a simple A/B test:
- Create a feature flag that splits users 50/50
- Variant A: [current version]
- Variant B: [proposed change]
- Track [conversion event] for both variants
- Run until we have 100+ users per variant (or 2 weeks, whichever is longer)
- Show me the conversion rate for each variant
```

### Reading Results

- **>20% difference:** Likely real. Ship the winner.
- **5-20% difference:** Might be real. Run longer or test with more users.
- **<5% difference:** Probably noise. Either change doesn't matter or your test needs more volume.

**Rule:** Don't peek at results daily and stop early. Set a duration and stick to it.

---

## What to Measure

| Metric | What It Tells You |
|--------|------------------|
| Signup rate (visitor → account) | Is your landing page compelling? |
| Activation rate (account → key action) | Is your onboarding working? |
| Trial-to-paid conversion | Is your product delivering enough value? |
| Time to value | How fast do users reach "aha"? |
| Expansion revenue triggers | What behavior precedes upgrades? |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Optimizing low-traffic pages | Focus on your highest-traffic funnel step |
| A/B testing button colors | Test headlines, CTAs, and page structure instead |
| Adding more fields "for data" | Every field costs conversions. Defer to later. |
| Ignoring mobile | 50%+ of traffic is mobile. Test there first. |
| Complex testing tools at small scale | Feature flags are enough until 1,000+ users/week |
