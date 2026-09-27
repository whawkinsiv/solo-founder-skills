---
name: pricing
description: "Use this skill when the user needs to set pricing, design pricing tiers, choose value metrics, build a pricing page, or test price changes. Also use when the user mentions 'how much should I charge,' 'freemium vs free trial,' 'pricing page,' or 'monetization.' Covers pricing psychology, tier design, anchoring, self-selection mechanisms, and monetization strategy for SaaS."
---

# Pricing & Monetization

Price is a signal. Too low says "toy." Too high says "enterprise." Your price tells customers who this product is for. This skill helps you choose what to charge, how to structure tiers, and how to build a pricing page that converts.

## Core Principles

- Pricing is a psychology problem, not a math problem.
- Align price with the value metric — the unit of value your customer receives.
- Three tiers is the default for a reason: anchoring, self-selection, and upgrade paths.
- The best pricing is simple to understand and hard to outgrow.
- Most SaaS companies underprice by 2-3x. Revisit pricing every 6 months.

---

## Workflow

```
Pricing Setup:
- [ ] Choose your value metric
- [ ] Design tier structure (Free → Pro → Business)
- [ ] Set price points
- [ ] Build the pricing page
- [ ] Plan expansion revenue mechanics
```

---

## Step 1: Choose Your Value Metric

The value metric is what you charge for. It should be:

1. **Easy to understand:** The customer can predict their bill.
2. **Aligned with value:** As they get more value, they pay more.
3. **Scalable:** It grows with their usage naturally.

| SaaS Type | Good Value Metric |
|-----------|------------------|
| Collaboration tools | Per seat/user |
| Developer tools | API calls, compute time, builds |
| Marketing tools | Contacts, emails sent, campaigns |
| Analytics | Events tracked, data points, queries |
| Storage/infra | GB stored, bandwidth |

**Bad value metrics:** Features-only gating (bloated top tiers), flat pricing (no expansion revenue), complex formulas nobody can predict.

**Tell AI:**
```
Help me choose a value metric for my SaaS:
- Product: [what it does]
- Users: [who uses it and how]
- Core value: [what outcome users get]
- Current model: [if any — flat rate, per user, etc.]

Recommend a value metric that's easy for users to understand, scales with the value
they receive, and creates natural expansion revenue. Show 2-3 options with tradeoffs.
```

---

## Step 2: Design Tier Structure

**Free / Starter:**
- Purpose: Acquisition. Get users in the door.
- Include: Core value prop, limited quantity (not crippled features).
- Limit: 1 user, 3 projects, 1,000 events, etc.
- Avoid: Time-limited free tiers for bottom-up SaaS. Use quantity limits.

**Pro / Team:**
- Purpose: Conversion. This is your primary revenue tier.
- Include: Everything in Free + collaboration + higher limits + integrations.
- Price: $10-30/user/month for SMB, $30-80 for mid-market.
- This tier should feel like an obvious upgrade when they hit Free limits.

**Business / Scale:**
- Purpose: Expansion. Capture more value from power users.
- Include: Everything in Pro + advanced features (SSO, audit logs, API access, priority support).
- Price: 2-3x the Pro tier.

**Enterprise (optional for now):**
- Purpose: Large deals. Custom pricing = "Contact us."
- Gate: SSO, SAML, SCIM, advanced security, SLA.

**Tell AI:**
```
Design pricing tiers for my SaaS:
- Product: [what it does]
- Value metric: [what you're charging for — users, projects, events, etc.]
- Target customer: [SMB, mid-market, enterprise]
- Competitors charge: [list 2-3 competitor prices if known]

Create 3 tiers with:
- Tier name, price, and what's included
- Clear differentiation between tiers (not just "more of the same")
- A reason to upgrade at each level (hit a limit, need a feature)
- The specific limits for the free tier
```

---

## Step 3: Set Price Points

### Psychological Pricing Tactics

- **Anchoring:** Display the most expensive plan prominently to make mid-tier feel reasonable.
- **Decoy effect:** Make the middle tier clearly the best value relative to the others.
- **Charm pricing:** $29 vs $30 — the effect is real, especially for SMB.
- **Per-day framing:** "Less than $1/day" for higher-priced plans.
- **Loss aversion:** On trial expiry, emphasize what they'll lose, not what they'll gain.

### Freemium vs. Free Trial

**Choose Freemium when:**
- Your product has viral/network effects (users invite others)
- The free tier drives organic growth or word-of-mouth
- Your marginal cost per free user is very low
- You're selling bottom-up (PLG)

**Choose Free Trial when:**
- The product's value requires setup/investment to experience
- You sell to decision-makers who evaluate then buy
- You can't afford to support large numbers of free users

**Reverse Trial (best of both):**
Give FULL access for 14 days, then downgrade to free tier. Users experience the premium, feel loss aversion, convert at higher rates.

---

## Industry Pricing Anchors

If you're building for your own profession, you already know what your peers pay for tools. Use this knowledge.

**Tell AI:**
```
Help me set pricing for my SaaS. Context about my industry:
- My target users are [profession/role]
- They currently pay for these tools: [list tools and rough prices]
- Their typical budget for software: [$ range per month, or "they expense it"]
- Buying decision made by: [individual practitioner / office manager / firm partner]
- Price sensitivity: [very price-sensitive / moderate / "if it works, cost doesn't matter"]

Based on these industry anchors, what price range makes sense?
Position my product relative to what they already pay.
```

**Key insight:** Your peers' existing software spending sets the anchor, not your costs. If every dentist already pays $300/month for practice management software, a $49/month add-on feels trivial. If your audience pays $0/month for tools, $29/month feels like a big ask.

---

## Step 4: Build the Pricing Page

**Tell AI:**
```
Build a pricing page for our SaaS:
- Tiers: [paste your tier structure from Step 2]
- Default to annual billing (show monthly as toggle)
- Show savings: "Save 20% with annual billing"
- Highlight the recommended plan with a "Most Popular" badge
- Feature comparison table below the tier cards
- FAQ section answering: "Can I cancel anytime?", "What happens to my data?",
  "Is there a setup fee?", "Can I switch plans?"
- Add social proof near the CTA: "[X] teams already use [Product]"
- Add a "Not sure?" CTA linking to a contact form or quiz

Use the design patterns from our existing pages. Make it responsive.
```

---

## Step 5: Plan Expansion Revenue

Don't just set it and forget it. Design mechanics that grow revenue as users grow.

- **Usage-based overages:** Charge for going over limits rather than hard-blocking.
- **Seat expansion:** Make it easy to add seats with self-serve billing.
- **Feature upsells:** Surface premium features in-context ("Upgrade to use custom fields").
- **Upsell timing:** Trigger when users hit 80% of a limit, not 100%.

**Tell AI:**
```
Add upgrade prompts to our product:
- When users hit 80% of their [resource] limit, show a gentle banner:
  "You're using 8 of 10 [resources]. Upgrade for unlimited."
- When users try a gated feature, show a modal explaining the feature
  and which plan includes it
- On the dashboard, show a usage meter: "X of Y [resource] used"
- Make the upgrade flow self-serve (no "contact sales" for Pro tier)
```

---

## Testing Price Changes

If you already have customers and want to adjust pricing:

- **Grandfather existing customers** at the old price (at least for 6-12 months)
- **Test on new signups only** — never change pricing mid-contract without notice
- **A/B test the page, not the price** — test how you present pricing, not different prices for the same plan
- **Announce increases 30+ days in advance** with clear reasoning

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Pricing based on costs, not value | Price based on what the customer saves or earns, not what it costs you |
| Only one paid tier | Three tiers enable anchoring and self-selection |
| Free tier is too generous | Free should create desire to upgrade, not satisfy forever |
| No annual discount | Annual billing improves cash flow and reduces churn |
| Hiding pricing ("Contact us" at $20/mo) | Show prices for SMB plans. Only hide enterprise/custom |
| Never revisiting pricing | Review every 6 months. You're probably underpricing. |

---

## Related Skills

- **conversion** — Optimize the pricing page for higher conversion
- **payments** — Implement Stripe, subscriptions, and billing
- **landing-page** — Build the full marketing site around pricing
- **analytics** — Track pricing page views, plan selection, and upgrade triggers
