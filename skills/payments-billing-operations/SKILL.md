---
name: payments-billing-operations
description: "Use this skill when the user needs to set up Stripe, implement subscriptions, handle billing, configure payment plans, manage failed payments, deal with refunds, set up tax collection, or troubleshoot payment issues. Covers Stripe configuration, subscription lifecycle, dunning, tax compliance, and billing operations for bootstrapped SaaS."
---

# Payments & Billing Operations Expert

Act as a top 1% billing operations specialist who has configured Stripe for 200+ bootstrapped SaaS products. You understand that for a solo founder, payments are 20% code and 80% configuration, business decisions, and edge cases that nobody warns you about. You've seen every billing mistake a founder can make — double charges, tax audits, failed payment spirals, and accidental free-forever plans.

## Core Principles

- Stripe is the right choice for 95% of bootstrapped SaaS. Do not overthink this decision.
- Test mode exists for a reason. Never touch live mode until you've tested every flow end-to-end.
- Billing is the one place you cannot "move fast and break things." A billing bug loses trust permanently.
- Automate everything. Manual invoicing does not scale and you will forget.
- Tax compliance is not optional. Set it up from day one or pay for it later.

## Stripe Setup Checklist

```
Stripe Configuration:
- [ ] Create Stripe account and verify identity
- [ ] Enable test mode (toggle in top-right of dashboard)
- [ ] Set up products and prices in Stripe dashboard (not just in code)
- [ ] Configure customer portal (Settings → Billing → Customer portal)
- [ ] Enable Stripe Tax (Settings → Tax)
- [ ] Set up webhook endpoint in your app
- [ ] Add Stripe publishable key and secret key to environment variables
- [ ] Test complete purchase flow in test mode with test card 4242424242424242
- [ ] Test failed payment with decline card 4000000000000002
- [ ] Test subscription cancellation flow
- [ ] Test upgrade/downgrade flow
- [ ] Switch to live mode and re-add live API keys
- [ ] Make one real purchase with your own card to verify
- [ ] Set up Stripe email receipts (Settings → Emails)
```

**Tell AI:**
```
Set up Stripe subscription billing for my SaaS. I need:
- Monthly and annual pricing tiers: [list your tiers and prices]
- Checkout flow using Stripe Checkout (hosted payment page)
- Customer portal for managing subscriptions
- Webhook handler for subscription events
- Environment variables for Stripe keys
Use [your framework/stack].
```

---

## Products & Prices: Dashboard vs Code

**Always create products and prices in the Stripe Dashboard first.** Then reference them by price ID in your code.

Why: Dashboard-created prices are the source of truth. If you create prices only in code, they're hard to find, modify, or debug.

### Setting Up Your Plans

In Stripe Dashboard → Products:

1. **Create one Product per tier** (e.g., "Starter", "Pro", "Business")
2. **Add two Prices per product** — monthly and annual
3. **Copy the Price IDs** (starts with `price_`) into your app config
4. **Use lookup keys** for cleaner code (e.g., `starter_monthly`, `pro_annual`)

### Pricing Tips

- Set annual pricing at 2 months free (annual = monthly × 10)
- Always show monthly price with annual savings highlighted
- Use Stripe's built-in trial period (set on the Price object, not in code)
- Don't create "free" prices in Stripe — handle free tier in your app logic

---

## Subscription Lifecycle

Every subscription state a founder needs to handle:

```
Customer signs up
    → Checkout session created
    → Payment succeeds
    → Subscription status: "active"
    → Grant access to paid features

Customer's card fails on renewal
    → Subscription status: "past_due"
    → Stripe retries (Smart Retries: 3 attempts over ~3 weeks)
    → Show "update payment method" banner in app
    → If all retries fail → status: "unpaid" or "canceled"

Customer cancels
    → Subscription status: "active" until period end
    → Access continues until billing period ends
    → Status becomes "canceled" at period end
    → Downgrade to free tier

Customer upgrades
    → Prorate remaining time on current plan
    → Charge difference immediately
    → New plan active immediately

Customer downgrades
    → Schedule change for end of current billing period
    → Continue current plan access until period end
    → New (lower) plan starts at next renewal
```

---

## Essential Webhooks

Your app MUST handle these Stripe webhook events:

| Event | What Happened | Your App Should |
|-------|--------------|-----------------|
| `checkout.session.completed` | Customer finished checkout | Activate subscription, grant access |
| `customer.subscription.updated` | Plan changed, renewed, or status changed | Update user's plan in your database |
| `customer.subscription.deleted` | Subscription fully canceled | Revoke paid access, move to free tier |
| `invoice.payment_succeeded` | Recurring payment went through | Update billing status, send receipt |
| `invoice.payment_failed` | Recurring payment failed | Show "update payment" banner, send email |

**Tell AI:**
```
Create a Stripe webhook handler for my [framework] app. Handle these events:
- checkout.session.completed (activate subscription)
- customer.subscription.updated (sync plan changes)
- customer.subscription.deleted (revoke access)
- invoice.payment_failed (flag account, show banner)
Verify webhook signatures. Store subscription status in [database].
```

### Webhook Security

- **Always verify webhook signatures.** Stripe signs every webhook with your endpoint secret.
- Use the `stripe.webhooks.constructEvent()` method, never parse the raw body yourself.
- Return 200 immediately, process async if needed. Stripe retries on timeout.

---

## Customer Portal

Stripe's hosted Customer Portal lets users manage their own subscriptions without you building anything. Enable it.

**Settings → Billing → Customer portal:**

```
Customer Portal Configuration:
- [ ] Allow customers to update payment method: ON
- [ ] Allow customers to cancel subscription: ON
- [ ] Allow customers to switch plans: ON (if you have multiple tiers)
- [ ] Show invoices and receipts: ON
- [ ] Cancellation reason collection: ON (gives you churn data)
- [ ] Set cancellation policy: "At end of billing period" (not immediate)
```

**Tell AI:**
```
Add a "Manage Billing" button to my app's settings page that redirects
to a Stripe Customer Portal session. Use [framework].
```

---

## Handling Failed Payments (Dunning)

Failed payments are inevitable. ~5-10% of recurring charges fail each month.

### Stripe's Smart Retries

Enable Smart Retries in Settings → Billing → Automatic collection. Stripe will:
- Retry the charge up to 3 times over ~3 weeks
- Use machine learning to pick optimal retry times
- This alone recovers 30-40% of failed payments

### Your Dunning Sequence

On top of Smart Retries, send your own emails:

1. **Day 0 (payment fails):** "Your payment didn't go through. Update your card to keep access." Link to Customer Portal.
2. **Day 3:** "Reminder: your account is at risk. Update payment method."
3. **Day 7:** "Last chance before your account is downgraded." Add urgency.
4. **Day 14:** If not resolved, downgrade to free tier. Send "We miss you" email with reactivation link.

**Tell AI:**
```
Create an email sequence for failed subscription payments:
- Email 1: Day 0, friendly notification with update-payment link
- Email 2: Day 3, reminder with urgency
- Email 3: Day 7, final warning
- Email 4: Day 14, account downgraded, reactivation offer
Tone: helpful, not threatening. Include [product name].
```

---

## Tax Collection

You are legally required to collect sales tax / VAT in most jurisdictions. Do not skip this.

### Stripe Tax (Recommended)

Enable Stripe Tax and let Stripe handle it:

1. **Settings → Tax → Enable Stripe Tax**
2. Set your business address (this determines your "tax origin")
3. Stripe automatically calculates and collects the right tax based on customer location
4. Stripe files reports you can use for tax remittance

**Cost:** 0.5% per transaction on top of Stripe's standard fees. Worth it.

### Tax Registration

You need to register for tax collection in jurisdictions where you have "nexus" (obligation):
- **US:** Your home state + states where you exceed economic thresholds (~$100K in sales)
- **EU:** If selling to EU customers, you need VAT registration (or use Stripe Tax + Merchant of Record)
- **Start with your home state/country.** Expand registration as revenue grows.

### Alternative: Merchant of Record

If tax terrifies you, use a Merchant of Record service (Paddle, Lemon Squeezy). They handle all tax collection, remittance, and compliance. You get a single payout. Trade-off: higher fees (~5-10% vs Stripe's ~3%) and less control.

---

## Common Pricing Implementation Patterns

### Free Trial → Paid

```
Flow: Sign up → 14-day trial (no card required) → Trial ending email
→ Enter card → Subscription starts

Stripe setup:
- Don't create a subscription during trial
- Track trial expiry in your database
- Create Checkout Session when trial ends
- Send reminder emails at day 10, day 13, day 14
```

### Freemium → Paid Upgrade

```
Flow: Sign up → Free forever plan → Hit usage limit → Upgrade prompt
→ Checkout → Subscription starts

Stripe setup:
- No Stripe involvement for free users
- Create Checkout Session only when upgrading
- Store plan type in your database, not in Stripe
```

### Card-Required Trial

```
Flow: Sign up → Enter card → 14-day trial → Auto-convert to paid

Stripe setup:
- Create subscription with trial_period_days: 14
- Card is captured but not charged
- Auto-charges on day 15
- Send email on day 12 warning about upcoming charge
```

---

## Testing Checklist

Test every flow in Stripe test mode before going live:

```
Payment Testing:
- [ ] Successful subscription purchase (card: 4242424242424242)
- [ ] Failed payment (card: 4000000000000002)
- [ ] 3D Secure authentication (card: 4000002500003155)
- [ ] Subscription cancellation and access revocation
- [ ] Plan upgrade (check proration)
- [ ] Plan downgrade (check scheduling)
- [ ] Customer Portal access
- [ ] Webhook delivery (check Stripe Dashboard → Webhooks → logs)
- [ ] Failed webhook retry behavior
- [ ] Trial expiration and conversion to paid
- [ ] Refund processing
```

---

## Going Live Checklist

```
Go-Live:
- [ ] Switch Stripe dashboard from test to live mode
- [ ] Replace test API keys with live API keys in production env
- [ ] Update webhook endpoint URL to production URL
- [ ] Update webhook signing secret to live mode secret
- [ ] Verify Stripe Tax is enabled in live mode
- [ ] Make a real $1 purchase with your own card
- [ ] Verify webhook received in Stripe Dashboard logs
- [ ] Refund your test purchase
- [ ] Remove any test customers/subscriptions from live mode
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Hardcoding prices in your app | Use Stripe Price IDs from the dashboard |
| Skipping webhook signature verification | Always verify — it prevents spoofed events |
| Not handling `past_due` status | Show a banner, send dunning emails |
| Granting access based on Checkout success only | Use webhooks — Checkout redirects can fail |
| Forgetting to test with decline cards | Test every failure path, not just happy path |
| Ignoring tax collection | Set up Stripe Tax or use a Merchant of Record |
| Building your own customer portal | Use Stripe's hosted Customer Portal |
| Not testing in test mode first | Always test the full lifecycle before going live |

---

## Stripe Fees Reference

- **Standard:** 2.9% + $0.30 per transaction (US cards)
- **International:** +1.5% for non-US cards
- **Stripe Tax:** +0.5% per transaction
- **Disputes (chargebacks):** $15 per dispute
- **No monthly fees.** No setup fees. No minimum.

---

## Success Looks Like

- Customers can sign up, pay, upgrade, downgrade, and cancel without you touching anything
- Failed payments recover automatically through Smart Retries + your dunning emails
- Tax is collected correctly from day one
- You get a Slack/email notification for every new subscription (celebration!) and every cancellation (learning opportunity)
- You can see MRR, churn, and revenue in Stripe Dashboard without any custom analytics
