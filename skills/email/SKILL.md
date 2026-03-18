---
name: email
description: "Use this skill when the user needs to create email sequences, design onboarding drips, write welcome emails, set up behavioral triggers, or improve email engagement. Also use when the user mentions 'drip campaign,' 'welcome email,' 'trial expiry email,' 'email automation,' or 'lifecycle emails.' Covers lifecycle email programs, subject line formulas, and drip campaign design."
---

# Email & Lifecycle Marketing

Email is the highest-ROI channel in SaaS — when done right. This skill helps you design email sequences that drive activation, retention, and revenue with specific copy you can paste into your email tool.

## Core Principles

- Every email must answer: "Why should I care about this right now?"
- Behavioral triggers > time-based drips. React to what users DO, not how long they've been around.
- One email, one goal, one CTA. Multiple CTAs = no CTA.
- Subject lines determine whether your email is read. Body copy determines whether it's acted on.
- Unsubscribes are better than spam complaints. Make it easy to leave.

---

## Workflow

```
Email Sequence Setup:
- [ ] Choose which sequence you need (welcome, trial expiry, re-engagement, etc.)
- [ ] Write each email (subject, preview text, body, CTA)
- [ ] Define triggers and timing
- [ ] Set up in your email tool
- [ ] Test: send to yourself on mobile
- [ ] Track opens, clicks, and conversions
```

---

## Choosing an Email Tool

| Stage | Tool | Why | Cost |
|-------|------|-----|------|
| Pre-revenue | **Resend** or **Loops** | Modern, developer-friendly, good free tier | Free tier |
| 0-$5K MRR | **Customer.io** or **Loops** | Behavioral triggers, event-based sequences | $0-150/mo |
| $5K+ MRR | **Customer.io** or **Intercom** | Advanced segmentation, in-app + email | $150+/mo |

For most bootstrapped founders: **Loops** (simple, modern) or **Resend** (if you want to code your own templates). Graduate to Customer.io when you need complex behavioral triggers.

---

## Welcome Sequence (Most Important)

Triggered on signup. Goal: get users to their aha moment.

**Tell AI:**
```
Write a 5-email welcome sequence for our SaaS:
- Product: [what it does]
- Aha moment: [the first action where users experience value]
- Signup flow: [what happens after signup — onboarding wizard, empty dashboard, etc.]

Email 1 (send immediately): Welcome + single CTA to start [aha action]. No fluff.
  Subject line under 50 chars. Body under 100 words.

Email 2 (Day 1, if user hasn't activated): Quick win tip — how to get value in 2 minutes.
  Include a specific "here's how" with a link directly to the action.

Email 3 (Day 3, if user hasn't activated): Social proof — brief story of how
  someone like them got results. End with CTA to try it.

Email 4 (Day 5, if user hasn't activated): Address the #1 objection or confusion
  that prevents activation.

Email 5 (Day 7, if user hasn't activated): Personal check-in from founder.
  "Reply to this email — I read every one."

Stop the sequence as soon as the user completes [aha action].
For each email: subject line, preview text, body, CTA button text.
```

---

## Trial Expiry Sequence

Triggered 3 days before trial ends. Goal: convert to paid.

**Tell AI:**
```
Write a 4-email trial expiry sequence:
- Product: [what it does]
- Trial length: [14 days / 30 days]
- What they lose on expiry: [specific features or data access]

Email 1 (Day -3): Remind what they'll lose + easy upgrade CTA.
  Mention specific features they've used during trial.

Email 2 (Day -1): Urgency + "here's everything you've built" —
  show them what's at stake.

Email 3 (Day 0): "Your trial ended." What happens next — is their data safe?
  Clear, calm, not pushy.

Email 4 (Day +3): "We saved your data." Final offer — extended trial
  or discount for annual plan.

For each: subject line, preview text, body, CTA. Keep subject lines under 50 chars.
```

---

## Re-engagement Sequence

Triggered after 14+ days inactive. Goal: bring them back.

**Tell AI:**
```
Write a 3-email re-engagement sequence:
- Product: [what it does]
- Trigger: user hasn't logged in for 14+ days

Email 1 (Day 14): "Here's what's new" — 2-3 improvements since they left + CTA.
  Subject: not "We miss you" (too generic). Something specific about what changed.

Email 2 (Day 21): Value reminder — "Here's what [similar user] accomplished this week."
  Show what they're missing out on.

Email 3 (Day 30): Direct ask — "Is [Product] still useful to you?"
  If not, offer to help. If they're done, let them go gracefully.

For each: subject line, preview text, body, CTA.
```

---

## Subject Line Formulas

- **Curiosity:** "The one thing most [role]s get wrong about [topic]"
- **Specificity:** "3 ways to [outcome] in [Product]"
- **Personal:** "Quick question about your [project name]" (use merge tags)
- **Urgency (honest):** "Your trial ends tomorrow"
- **Value:** "Save 2 hours this week with [feature]"

### Rules

- Under 50 characters for mobile preview
- No ALL CAPS. No excessive punctuation.
- Personalization increases opens 20-30%
- Preview text is the second subject line — don't waste it
- A/B test subject lines on every send if volume allows

---

## Transactional Emails

Receipts, password resets, invitations, notifications:

- Send instantly. Users expect these within seconds.
- Clear subject: "Your receipt from [Product]" or "Reset your password"
- Minimal design. These are utility, not marketing.
- Include a plain-text version.
- Don't sneak marketing into transactional emails — legal risk and trust erosion.

---

## Technical Setup

Before sending anything:

```
- [ ] SPF, DKIM, and DMARC configured (deliverability non-negotiable)
- [ ] Sending from a subdomain (e.g., mail.yourproduct.com) to protect main domain reputation
- [ ] List hygiene: remove hard bounces immediately, soft bounces after 3 fails
- [ ] Plain text fallback for every HTML email
- [ ] Mobile-responsive templates (60%+ of emails opened on mobile)
- [ ] Preference center (let users choose email types, not just unsubscribe from all)
- [ ] Track: opens, clicks, unsubscribes, spam complaints, conversions
```

**Tell AI:**
```
Set up email infrastructure for our app:
- Configure SPF, DKIM, and DMARC for [our domain]
- Set up a sending subdomain: mail.[domain].com
- Create mobile-responsive email templates for:
  1. Transactional (receipt, password reset, invite)
  2. Marketing (sequence emails, announcements)
- Add unsubscribe link and email preference center
- Verify deliverability with a test send
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Time-based drips only ("Day 3, Day 5") | Use behavioral triggers: "hasn't completed X" |
| Multiple CTAs in one email | One email, one goal, one button |
| "We miss you" as a subject line | Be specific: "3 new features since you left" |
| No plain-text version | Always include one. Some clients strip HTML. |
| Sending from noreply@ | Use a real address. Let people reply. |
| No tracking | Track opens, clicks, and conversions per email |
| Marketing in transactional emails | Keep them separate. Trust > short-term engagement. |

---

## Related Skills

- **growth** — Activation strategies that email sequences support
- **conversion** — Optimize the full signup-to-paid funnel
- **analytics** — Track email-driven conversions and attribution
- **copywriting** — Write stronger subject lines and email body copy
