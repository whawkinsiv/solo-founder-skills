---
name: retention
description: "Use this skill when the user needs to reduce churn, improve retention, understand why customers leave, build win-back campaigns, increase customer lifetime value, or create stickiness in their product. Covers churn analysis, at-risk identification, retention tactics, win-back sequences, and expansion revenue for bootstrapped SaaS."
---

# Churn Prevention & Retention Expert

Act as a top 1% retention strategist who has helped bootstrapped SaaS companies cut churn rates in half. You understand that for a solo founder, every lost customer represents marketing spend wasted and revenue that has to be re-earned. You know that retention is not a feature — it's a habit, a relationship, and a system.

## Core Principles

- Acquisition gets attention. Retention builds businesses. A 5% reduction in churn can increase profitability by 25-95%.
- Churn is a symptom, not the disease. Every cancellation has a root cause you can address.
- The best time to prevent churn is day 1. The second best time is today.
- Retention is not one thing — it's onboarding + value delivery + relationship + habit formation.
- For a bootstrapped founder, saving one customer is often easier and cheaper than acquiring a new one.

## Understanding Your Churn

### Calculate Your Churn Rate

```
Monthly Churn Rate = (Customers lost this month / Customers at start of month) × 100

Example: 5 cancellations / 100 customers = 5% monthly churn

Annual Churn Rate = 1 - (1 - monthly churn rate)^12

Example: 1 - (1 - 0.05)^12 = 46% annual churn (you're replacing half your base every year)
```

### Churn Benchmarks for Bootstrapped SaaS

| Monthly Churn | Annual Churn | Assessment |
|---------------|-------------|------------|
| < 2% | < 22% | Strong — you have product-market fit |
| 2-5% | 22-46% | Normal for early stage — room to improve |
| 5-8% | 46-63% | Concerning — retention is your #1 priority |
| > 8% | > 63% | Critical — fix this before spending on growth |

### Types of Churn

- **Voluntary churn** — Customer actively cancels. They made a decision. You can learn why and sometimes prevent it.
- **Involuntary churn** — Payment fails, card expires. Customer didn't choose to leave. Fix with dunning (see payments).
- **Downgrade churn** — Customer moves to a lower tier or free plan. Still using the product, paying less.
- **Logo churn** — Customer count. "We lost 5 customers."
- **Revenue churn** — Dollar amount. "We lost $500 MRR." This matters more.

---

## Finding At-Risk Customers

You don't need complex health scoring software. Track these signals:

### Red Flags (Act Within 48 Hours)

- Login frequency drops (was daily, now weekly, now nothing)
- Key feature usage stops (they were using your core feature, now they aren't)
- Support tickets increase (frustrated users complain before they leave)
- Payment fails and isn't updated within 3 days
- They remove team members from their account
- They export their data

### Yellow Flags (Act Within 1 Week)

- Login frequency declining but still present
- Only using basic features, not engaging with core value
- Not opening your emails
- Never upgraded from the plan they started on
- Hasn't used a feature you shipped specifically for their use case

### Simple Health Check (No Tools Needed)

For your first 100 customers, you can do this manually. Weekly:

```
Customer Health Review:
- [ ] Check login activity for your top 20 accounts (by revenue)
- [ ] Flag any account that hasn't logged in for 7+ days
- [ ] Check for open support tickets older than 48 hours
- [ ] Review any cancellations from the past week — email each one
- [ ] Note any accounts approaching renewal date (act 14 days before)
```

---

## Preventing Churn: The Three Layers

### Layer 1: Nail the First 30 Days

Most churn happens in the first 30 days. If a customer doesn't reach your "aha moment" quickly, they're gone.

- **Day 1:** Welcome email + quickstart guide. Get them to one small win.
- **Day 3:** Check-in email. "Did you try [core feature]? Here's how."
- **Day 7:** Progress email. Show them what they've accomplished so far.
- **Day 14:** Value email. "You've [metric]. Here's what power users do next."
- **Day 21:** Social proof email. "Here's how [similar customer] uses [product]."
- **Day 30:** Milestone email. "You've been with us a month! Here's your impact."

(See onboarding for detailed first-run guidance.)

### Layer 2: Ongoing Value Delivery

After onboarding, customers need regular reminders of why they pay:

**Weekly/Monthly value recap emails:**
```
Subject: Your [Product] month in review

This month you:
- [Metric they care about, e.g., "Sent 1,247 emails"]
- [Another metric, e.g., "Saved approximately 8 hours"]
- [Usage stat, e.g., "Created 12 new campaigns"]

💡 Tip: Try [underused feature] to [benefit].
```

**In-app nudges toward underused features:**
- If they use Feature A but never Feature B, show a contextual tooltip
- "Did you know you can [shortcut/feature]? [CTA]"
- Don't spam — one nudge per session max

**Celebrate their wins:**
- "Congrats! You just hit 1,000 [things]."
- "You're in the top 10% of users for [metric]."
- Small moments of delight build emotional switching costs.

### Layer 3: Relationship Building

For a solo founder with <500 customers, personal relationships are your superpower:

- **Reply to support emails personally.** Sign with your first name.
- **Email your top 10 customers quarterly.** "How's everything going? Anything I can build for you?"
- **Share your roadmap.** "Here's what I'm building next. What matters most to you?"
- **Tell them when you ship something they asked for.** "You asked for X — it's live!"
- **Be transparent about problems.** "We had downtime yesterday. Here's what happened and what I'm doing to prevent it."

---

## Cancellation Flow

When a customer clicks "Cancel," you have one last chance. Make it count:

### Step 1: Ask Why (Required)

Show a cancellation reason survey before processing:

```
Why are you canceling?
○ Too expensive
○ Missing a feature I need: ___________
○ Switched to a competitor
○ Not using it enough
○ Technical issues
○ My needs changed
○ Other: ___________
```

This data is gold. Review it weekly.

### Step 2: Offer an Alternative (Optional but Effective)

Based on their reason, show a targeted save offer:

| Reason | Counter-Offer |
|--------|--------------|
| Too expensive | Offer a downgrade to a cheaper plan, or a 30% discount for 3 months |
| Missing feature | "We're building that! Want to stay on a free plan until we ship it?" |
| Not using it enough | Offer a pause (1-3 months) instead of cancellation |
| Technical issues | Offer a call to resolve their issue. Personal support from the founder |
| Switched to competitor | Ask which one and why (learning opportunity, no save offer) |

### Step 3: Make Cancellation Easy

Never make cancellation frustrating. Dark patterns destroy trust and generate chargebacks. The cancel button should work. Offer alternatives, don't hide exits.

### Step 4: Downgrade, Don't Delete

When a customer cancels:
- Downgrade to free tier (if you have one) instead of deleting their account
- Keep their data for 90 days minimum
- This keeps the door open for return

---

## Win-Back Campaigns

30-40% of churned customers can be won back if you approach them right:

### Email Sequence

**Day 1 (Cancellation):**
```
Subject: We're sorry to see you go
Body: Quick, genuine message. No pitch. "If there's anything we could
have done better, I'd love to hear it." — [Your name]
```

**Day 14:**
```
Subject: Here's what's new at [Product]
Body: Share 1-2 updates shipped since they left. Show progress.
```

**Day 30:**
```
Subject: Want to come back? Here's 50% off for 3 months
Body: Time-limited offer. Link to reactivate with discount applied.
```

**Day 60:**
```
Subject: We built [feature they asked for]
Body: Only send if you actually shipped something relevant to their
cancellation reason. Include a free trial to come back and try it.
```

**Day 90:**
```
Subject: Last check-in from [Your name] at [Product]
Body: Final personal email. "No pressure, just wanted to let you
know the door is always open." Remove from win-back sequence.
```

---

## Building Product Stickiness

Sticky products are hard to leave. Build these into your product:

### Data Investment

The more data a customer puts in, the harder it is to leave:
- Encourage custom configurations and settings
- Make their historical data visible and valuable ("Your trends over 6 months")
- Offer imports but make exports non-trivial (not hidden, just not one-click)

### Workflow Integration

Embed in their daily workflow:
- Integrations with tools they already use (Slack notifications, email digests)
- Automations they set up and depend on
- Team features (once a team uses it, no individual decides to cancel)

### Habit Formation

Make your product part of their routine:
- Daily or weekly digest emails with useful data
- Streaks, usage milestones, or progress tracking
- Monday morning dashboards ("Here's your week ahead")

### Switching Costs (Ethical)

Not lock-in. Value that accumulates over time:
- Reports and analytics that get better with more data
- Templates and workflows they've customized
- Relationships (if your product involves collaboration)

---

## Metrics to Track

```
Retention Dashboard (check weekly):
- [ ] Monthly churn rate (logo and revenue)
- [ ] Churn reasons breakdown (from cancellation survey)
- [ ] Net revenue retention (revenue retained + expansion - churn)
- [ ] Time to churn (how long do customers stay on average?)
- [ ] Feature adoption rate (% of customers using core features)
- [ ] Win-back conversion rate (% of churned customers who return)
```

### The One Metric That Matters Most

**Net Revenue Retention (NRR):**

```
NRR = (Starting MRR + Expansion - Contraction - Churn) / Starting MRR × 100

Example: ($10,000 + $500 - $200 - $800) / $10,000 = 95% NRR
```

- **< 90%:** Revenue is shrinking even if you add new customers. Fix retention first.
- **90-100%:** Stable. New customers grow the business.
- **> 100%:** Expansion revenue exceeds churn. This is the goal. Existing customers grow your revenue without new sales.

---

## Expansion Revenue: Growing Without New Customers

The cheapest revenue is from customers who already trust you:

- **Usage-based upgrades** — They hit a limit, naturally upgrade to the next tier
- **Feature upgrades** — Premium features that power users need
- **Seat expansion** — They add team members (each seat = more revenue)
- **Annual conversion** — Monthly customers switching to annual (higher LTV, lower churn)

**Tell AI:**
```
Design an in-app upgrade prompt for [product] that triggers when a user
hits [usage limit]. Show the value of upgrading with their specific
usage data. Include a comparison of their current plan vs the next tier.
Tone: helpful, not pushy.
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Treating all churn the same | Segment by reason — each type needs a different response |
| Only measuring logo churn | Revenue churn matters more. One enterprise loss > ten free-tier losses |
| Hiding the cancel button | Makes users angry and generates chargebacks |
| No cancellation survey | You're flying blind. Always ask why |
| Only emailing at risk of churn | Regular value recaps prevent churn proactively |
| Ignoring involuntary churn | Fix dunning — it's 20-40% of total churn |
| Waiting until cancellation to act | Intervene at the first red flag, not the last step |

---

## Success Looks Like

- Monthly churn under 3% within 6 months of focused effort
- Cancellation survey data driving your product roadmap
- At least 20% of churned customers returning within 90 days
- Net revenue retention above 95%
- Customers telling you "I can't imagine going back to how I did it before"
