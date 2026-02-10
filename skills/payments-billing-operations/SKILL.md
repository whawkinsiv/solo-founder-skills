---
name: payments-billing-operations
description: "Use this skill when the user needs to set up Stripe, implement subscriptions, handle billing, configure payment plans, manage failed payments, deal with refunds, set up tax collection, or troubleshoot payment issues. Covers Stripe configuration, subscription lifecycle, dunning, tax compliance, and billing operations for bootstrapped SaaS."
---

# Payments & Billing Operations

Billing is 20% code and 80% configuration and business decisions. This skill helps you set up Stripe correctly, handle the edge cases, and avoid the mistakes that lose customer trust.

## Core Principles

- Stripe is the right choice for 95% of bootstrapped SaaS. Do not overthink this decision.
- Test mode exists for a reason. Never touch live mode until you've tested every flow.
- Billing is the one place you cannot "move fast and break things." A billing bug loses trust permanently.
- Automate everything. Manual invoicing doesn't scale and you will forget.
- Tax compliance is not optional. Set it up from day one.

---

## Stripe Setup Checklist

```
Stripe Configuration:
- [ ] Create Stripe account and verify identity
- [ ] Enable test mode (toggle in top-right of dashboard)
- [ ] Set up products and prices in Stripe Dashboard (not in code)
- [ ] Configure Customer Portal (Settings -> Billing -> Customer portal)
- [ ] Enable Stripe Tax (Settings -> Tax)
- [ ] Set up webhook endpoint in your app
- [ ] Add Stripe keys to environment variables
- [ ] Test complete purchase flow (test card: 4242424242424242)
- [ ] Test failed payment (decline card: 4000000000000002)
- [ ] Test subscription cancellation and upgrade/downgrade flows
- [ ] Switch to live mode, re-add live API keys
- [ ] Make one real purchase with your own card to verify
```

**Tell AI:**
```
Set up Stripe subscription billing for my SaaS:
- Monthly and annual pricing tiers: [list your tiers and prices]
- Checkout flow using Stripe Checkout (hosted payment page)
- Customer Portal for managing subscriptions
- Webhook handler for subscription events
- Environment variables for Stripe keys
Use [your framework/stack].
```

---

## Products & Prices: Dashboard First

**Always create products and prices in the Stripe Dashboard.** Then reference them by Price ID in your code.

### How to Set Up

1. Stripe Dashboard -> Products -> Create one Product per tier (e.g., "Starter", "Pro")
2. Add two Prices per product — monthly and annual
3. Copy the Price IDs (`price_...`) into your app config
4. Use lookup keys for cleaner code (e.g., `starter_monthly`, `pro_annual`)

### Pricing Tips

- Annual pricing = monthly x 10 (2 months free)
- Show monthly price with annual savings highlighted
- Use Stripe's built-in trial period (set on the Price, not in code)
- Don't create "free" prices — handle free tier in your app logic

---

## Subscription Lifecycle

Every state your app needs to handle:

| Event | Subscription Status | Your App Should |
|-------|-------------------|----------------|
| Payment succeeds after checkout | `active` | Grant paid features |
| Card fails on renewal | `past_due` | Show "update payment" banner |
| All retries fail | `unpaid` or `canceled` | Downgrade to free tier |
| Customer cancels | `active` (until period end) | Continue access until period ends, then downgrade |
| Customer upgrades | `active` (new plan) | Prorate and grant new plan immediately |
| Customer downgrades | `active` (current plan) | Schedule change for end of billing period |

---

## Essential Webhooks

Your app MUST handle these events:

| Event | What Happened | Your App Should |
|-------|--------------|-----------------|
| `checkout.session.completed` | Customer finished checkout | Activate subscription, grant access |
| `customer.subscription.updated` | Plan changed or status changed | Update user's plan in database |
| `customer.subscription.deleted` | Subscription fully canceled | Revoke paid access, move to free tier |
| `invoice.payment_failed` | Recurring payment failed | Show "update payment" banner, send email |

**Tell AI:**
```
Create a Stripe webhook handler for my [framework] app:
- Handle: checkout.session.completed, customer.subscription.updated,
  customer.subscription.deleted, invoice.payment_failed
- Verify webhook signatures using the endpoint secret
- Store subscription status in [database]
- Return 200 immediately (process async if needed)
```

**Webhook security:** Always verify signatures. Use `stripe.webhooks.constructEvent()`. Return 200 immediately — Stripe retries on timeout.

---

## Customer Portal

Stripe's hosted Customer Portal lets users manage subscriptions without you building anything.

**Configure in Settings -> Billing -> Customer portal:**
- Allow: update payment method, cancel subscription, switch plans, view invoices
- Enable cancellation reason collection (gives you churn data)
- Set cancellation policy to "at end of billing period" (not immediate)

**Tell AI:**
```
Add a "Manage Billing" button to my app's settings page.
It should create a Stripe Customer Portal session and redirect the user.
Use [framework].
```

---

## Failed Payments (Dunning)

~5-10% of recurring charges fail each month. Plan for it.

### Automatic Recovery

1. **Enable Smart Retries** (Settings -> Billing -> Automatic collection) — Stripe retries 3 times over ~3 weeks, recovers 30-40% of failures automatically
2. **Add your own email sequence** on top of Smart Retries:

**Tell AI:**
```
Create a dunning email sequence for failed payments:
- Day 0: "Your payment didn't go through. Update your card." + Customer Portal link
- Day 3: "Reminder: your account is at risk."
- Day 7: "Final warning before downgrade."
- Day 14: Account downgraded. "We miss you" + reactivation link.
Tone: helpful, not threatening.
```

---

## Tax Collection

You are legally required to collect sales tax / VAT in most jurisdictions.

### Option 1: Stripe Tax (Recommended)

1. Settings -> Tax -> Enable Stripe Tax
2. Set your business address
3. Stripe automatically calculates and collects tax by customer location
4. Cost: 0.5% per transaction. Worth it.

### Option 2: Merchant of Record

If tax terrifies you, use Paddle or Lemon Squeezy. They handle all tax collection and remittance. Trade-off: higher fees (~5-10% vs Stripe's ~3%) and less control.

### Tax Registration

- **Start with your home state/country.** Expand as revenue grows.
- US: Register in your home state + states where you exceed ~$100K in sales
- EU: Need VAT registration if selling to EU customers

---

## Pricing Implementation Patterns

| Pattern | How It Works | Stripe Setup |
|---------|-------------|-------------|
| **Free trial -> Paid** | 14-day trial, no card. Enter card to continue. | Track trial in your DB. Create Checkout Session when trial ends. |
| **Freemium -> Upgrade** | Free forever. Upgrade when hitting limits. | No Stripe for free users. Checkout Session on upgrade only. |
| **Card-required trial** | Enter card at signup. Auto-charges after 14 days. | Create subscription with `trial_period_days: 14`. |

---

## Testing Checklist

Test every flow in Stripe test mode before going live:

```
- [ ] Successful purchase (card: 4242424242424242)
- [ ] Failed payment (card: 4000000000000002)
- [ ] 3D Secure authentication (card: 4000002500003155)
- [ ] Subscription cancellation and access revocation
- [ ] Plan upgrade (check proration)
- [ ] Plan downgrade (check scheduling)
- [ ] Customer Portal access
- [ ] Webhook delivery (Stripe Dashboard -> Webhooks -> logs)
- [ ] Trial expiration and conversion to paid
```

## Going Live Checklist

```
- [ ] Switch to live mode in Stripe Dashboard
- [ ] Replace test API keys with live keys in production
- [ ] Update webhook endpoint URL and signing secret
- [ ] Verify Stripe Tax is enabled in live mode
- [ ] Make a real $1 purchase with your own card
- [ ] Verify webhook received in Stripe logs
- [ ] Refund your test purchase
```

---

## Stripe Fees

| Fee | Amount |
|-----|--------|
| Standard (US cards) | 2.9% + $0.30 per transaction |
| International cards | +1.5% |
| Stripe Tax | +0.5% per transaction |
| Chargebacks | $15 per dispute |
| Monthly/setup fees | None |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Hardcoding prices in your app | Use Stripe Price IDs from the Dashboard |
| Skipping webhook signature verification | Always verify — prevents spoofed events |
| Not handling `past_due` status | Show a banner, send dunning emails |
| Granting access based on Checkout redirect only | Use webhooks — redirects can fail silently |
| Forgetting to test decline cards | Test every failure path, not just happy path |
| Ignoring tax collection | Set up Stripe Tax or use a Merchant of Record |
| Building your own billing portal | Use Stripe's hosted Customer Portal |
