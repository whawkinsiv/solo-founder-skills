---
name: growth-plg
description: "Use this skill when the user needs to design a product-led growth strategy, build viral loops, improve activation metrics, or reduce churn. Covers PLG funnels, activation metrics, viral mechanics, retention strategies, and growth systems."
---

# Growth & Product-Led Growth

In PLG, the product is your best salesperson. This skill helps you design growth into your product — with concrete tactics and prompts you can hand to Claude Code.

## Core Principles

- Growth is a system, not a hack. Build loops, not one-time campaigns.
- Activation is the most important metric. A user who never experiences value is already lost.
- Virality is engineered, not accidental. Design sharing into the product.
- Retention is the foundation. Growing on top of a leaky bucket is a losing game.
- For a solo founder: pick ONE growth lever, make it work, then add the next.

---

## The PLG Funnel

Acquisition → Activation → Retention → Revenue → Referral

**The most common mistake:** Founders focus on Acquisition first. Focus on Activation and Retention first — there's no point driving signups into a leaky bucket.

---

## Activation (Start Here)

### Define Your Aha Moment

The specific action where users first experience core value:

| Product Type | Example Aha Moment |
|-------------|-------------------|
| Project management | Created first project + added a task |
| Email tool | Sent first campaign |
| Analytics | Saw first dashboard with real data |
| Design tool | Exported first design |
| Scheduling | Booked first meeting through the tool |

**Your aha moment:** [Action that makes users say "I get it, this is useful"]

### Drive Users to Aha Fast

Every screen between signup and the aha moment is a drop-off risk.

**Tell AI:**
```
Design the onboarding flow to get users to [your aha moment] in under 3 minutes:
1. After signup, skip the "check your email" screen — go directly to the product
2. Show a setup wizard (3-5 steps max) that collects only what's needed to deliver value
3. Pre-populate with sample data or templates so the product looks useful immediately
4. Add a progress checklist: "Complete your setup: ☑ Create [X] ☐ [Next step] ☐ [Final step]"
5. Show an empty state with a clear CTA on every empty page ("Create your first [X]")
```

### Activation Emails

**Tell AI:**
```
Create an activation email sequence triggered by signup:

Email 1 (immediate): Welcome + direct link to start [aha action]. No fluff.
Email 2 (Day 1, if not activated): "Here's how [similar user] got started in 2 minutes" + link
Email 3 (Day 3, if not activated): "Need help? Here are 3 templates to get started" + link
Email 4 (Day 5, if not activated): "What's holding you back?" — reply to this email for help
Email 5 (Day 7, if not activated): Last chance: "Your account is ready. Here's what you're missing."

Stop sequence as soon as user completes [aha action].
```

---

## Acquisition Strategies

Pick ONE that matches your product. Don't spread across all of them.

| Strategy | Best For | Effort | Time to Results |
|----------|----------|--------|-----------------|
| Free tool / calculator | Products that solve measurable problems | Medium | 1-3 months |
| Template gallery | Products with customizable outputs | Medium | 2-4 months |
| Content-as-product | Products in information-heavy spaces | High | 3-6 months |
| Community-driven | Products with passionate niche users | High | 3-6 months |
| Integrations | Products that connect to other tools | Medium | 1-2 months per integration |
| Freemium | Products where free use drives word-of-mouth | Low | Immediate (but slow growth) |

**Tell AI:**
```
Build a [free tool / template gallery / calculator] that:
- Solves a specific problem our ICP has (related to our product)
- Requires no signup to use
- Shows a teaser of our full product's value
- Includes a CTA: "Want more? [Product name] does this automatically."
- Is SEO-optimized so it attracts organic traffic
```

---

## Viral Loop Design

A viral loop has 4 parts: User gets value → Has reason to share → New user sees value → Converts → Loop repeats.

### Viral Mechanics for SaaS

| Mechanic | How It Works | Example |
|----------|-------------|---------|
| Collaboration invites | Product requires multiple users | "Invite your team to edit this" |
| Shared outputs | User creates something shareable | Reports, links, dashboards with "Made with [Product]" |
| Referral rewards | Incentivized invitations | "Give $20, get $20" |
| Public pages | User content is SEO-indexable | Public profiles, portfolios, pages |
| Embeds | Widget on user's site links back | Badges, chat widgets, forms |

**Tell AI:**
```
Add a sharing/invite mechanic to our product:
- After a user completes [key action], prompt: "Share this with your team" or "Invite a collaborator"
- Make shared links show a preview of the output (not just a signup page)
- Add "Made with [Product]" branding on shared/public outputs with a link to our homepage
- Track invite sends, invite accepts, and invite-to-signup conversion
```

---

## Retention Mechanics

### Build Habit Loops

| Component | What It Is | Example |
|-----------|-----------|---------|
| Trigger | What brings them back | Email digest, notification, calendar event |
| Action | What they do in the product | Check dashboard, respond to comment, update status |
| Reward | Value they get | New insight, progress indicator, completed task |
| Investment | What makes leaving harder | More data, more connections, more history |

**Tell AI:**
```
Build retention mechanics into the product:
1. Weekly email digest: summarize what happened this week + one insight or action item
2. Activity notifications: "[Name] commented on your [item]" — not time-based ("It's been 3 days")
3. Progress indicators: Show users their cumulative value ("You've saved 14 hours this month")
4. Data investment: The more they use it, the more valuable their data becomes (history, reports, trends)
```

### Feature Drips

Don't show everything on day 1. Reveal features as users are ready:

**Tell AI:**
```
Implement progressive feature disclosure:
- Week 1: Show only core features (the ones needed for the aha moment)
- Week 2: Surface advanced feature with a tooltip: "Now that you've [done X], try [advanced feature]"
- Week 3+: Unlock remaining features with brief explanations
- Gate premium features with a gentle upgrade prompt at the moment of need
```

---

## Metrics to Track

Set these up in your analytics tool (see analytics-instrumentation skill):

| Stage | Key Metric | How to Calculate |
|-------|-----------|-----------------|
| Acquisition | Signup rate | Visitors → Signups |
| Activation | Activation rate | Signups → Completed aha moment |
| Activation | Time to aha | Average hours/days from signup to key action |
| Retention | D1/D7/D30 | % of users returning on day 1, 7, 30 |
| Revenue | Free-to-paid | Free users → Paying users |
| Referral | Viral coefficient | Invites sent × invite conversion rate |

**Tell AI:**
```
Set up growth tracking:
- Track signup events with source attribution (organic, paid, referral, direct)
- Track [aha moment action] completion with timestamp
- Calculate time-to-activate for each user
- Build a daily dashboard showing: signups, activations, D7 retention, free-to-paid conversion
- Alert me if activation rate drops below [X]% or D7 retention drops below [Y]%
```

---

## Growth Experiments

When you want to improve a metric:

1. **Hypothesis:** "If we [change], then [metric] will [improve] because [reason]."
2. **Metric:** What specifically will you measure?
3. **Duration:** Run for 1-2 weeks minimum, or until 100+ users have been through the flow.
4. **Decide:** Did the metric improve? Ship it or revert.
5. **Document:** Write down what you learned, even (especially) from failures.

**Tell AI:**
```
Set up a simple A/B test:
- Variant A (control): [current experience]
- Variant B (test): [proposed change]
- Success metric: [metric to improve]
- Split traffic 50/50
- Show me results after [100 users / 2 weeks]
Use a simple feature flag, not a complex testing framework.
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Focusing on acquisition before activation | Fix activation first — no point driving users into a broken onboarding |
| Building viral features nobody uses | Viral loops must be part of the core workflow, not a sidebar feature |
| Measuring vanity metrics (signups) | Track activation rate and retention, not just signups |
| Trying all channels at once | Pick ONE, make it work, then add another |
| Complex A/B testing infrastructure | Use simple feature flags. You don't need Optimizely at 100 users |
