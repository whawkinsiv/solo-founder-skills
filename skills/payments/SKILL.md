---
name: payments
description: "Use this skill to take money: 'set up Stripe,' 'add subscriptions,' 'payment link,' 'billing,' 'customer portal,' 'webhooks,' 'failed payments,' 'sales tax or VAT,' or 'refunds.' Starts with a payment link or invoice for the first customers, then sets up Stripe Checkout, the customer portal, and webhooks that grant access, with test and go-live checklists. Not for deciding what to charge (use pricing)."
metadata:
  version: 2.0.0
---

# Payments

Take money with the least code that works. Stripe is the default for a solo founder: hosted checkout, a hosted billing portal, and good test tools.

## Stage 1: The first customers

Use a **Stripe Payment Link** or an invoice. No billing code. The founder grants access by hand after each payment. This works for the first 10 customers and often longer. Build billing in the app when granting access by hand starts taking real time.

## Stage 2: Billing in the app

1. **Create products and prices in the Stripe Dashboard,** not in code. Reference them by price ID or lookup key.
2. **Use Stripe Checkout** (the hosted payment page). Do not build a card form.
3. **Use the Customer Portal** for card updates, plan changes, cancellations, and invoices. Do not build a billing page. Set cancellation to happen at the end of the billing period, and turn on the cancellation-reason question.
4. **Store each customer's subscription status in the database,** updated only from webhooks.
5. **Set trials when you create the Checkout session or the subscription.**

## Webhooks

**Grant access from the verified webhook, never from the redirect page.** The redirect can fail, and anyone can load it. Handle at least:

| Event | Do |
|---|---|
| `checkout.session.completed` | Activate the subscription and grant access |
| `customer.subscription.updated` | Update the plan and status |
| `customer.subscription.deleted` | Remove paid access |
| `invoice.payment_failed` | Show an "update your card" banner |

Every webhook endpoint:
- verifies the signature before acting
- returns a success response quickly, and does slow work afterwards
- handles duplicate events safely: store the event ID and skip repeats
- logs the event type and ID, so failures can be traced

## Subscription states

| Status | The app should |
|---|---|
| `active` | Give paid access |
| `active`, set to cancel at period end | Keep access until the period ends |
| `past_due` | Keep access for now, and show the update-card banner |
| `canceled` or `unpaid` | Remove paid access. Keep the data. |

## Failed payments

Turn on Stripe's automatic retries and its emails about failed payments and expiring cards. Show the banner in the app. Failed cards cause a large share of churn, and most of it is recoverable.

## Tax

Decide before the first sale in a new country or state:
- **Stripe Tax** calculates and collects tax. Registering and filing are still the founder's job.
- **A merchant of record** (such as Paddle or Lemon Squeezy) sells on the founder's behalf and handles registration and filing, for higher fees.

When registration is required depends on the place and on sales volume. Check the current rules for where customers are, and ask an accountant once revenue starts.

## Test before going live

In test mode:
- [ ] A successful purchase (card `4242 4242 4242 4242`)
- [ ] A declined card (`4000 0000 0000 0002`)
- [ ] A card that needs authentication (`4000 0025 0000 3155`)
- [ ] Cancel, upgrade, and downgrade
- [ ] Each webhook arrives and updates the database (check the webhook logs in Stripe)

Going live:
- [ ] Live keys in production's environment variables
- [ ] A live webhook endpoint with its own signing secret
- [ ] One real purchase with your own card, then a refund

## Rules

- **Prices live in Stripe, not in code.** Changing a price should not need a deploy.
- **Never store card numbers.** Checkout keeps card data off your server.
- **Check current fees on Stripe's pricing page.** Fees change, so do not rely on numbers in old notes.

## Output

The working payment flow for the founder's stage, the completed test checklist, and a note on the tax decision.
