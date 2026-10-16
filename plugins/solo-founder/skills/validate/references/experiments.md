# Validation Experiments

Ways to test demand without building the product. Each one has a target metric and a pass bar — set both before you run it, never after.

## Choosing the experiment

| The gap in your evidence | Run this |
|---|---|
| Don't know if the problem is real | Problem research + 10 conversations |
| Don't know if anyone wants *your* solution | Landing page test |
| Don't know which feature they want | Fake door test |
| Don't know if they'll pay | Pre-sale test |
| Don't know what they'd pay | Pre-sale at two price points |
| They paid — now, what must the product actually do? | Manual delivery test |

---

## Level 1 — Problem research

Before validating a solution, validate that the problem exists and hurts enough to pay for.

| Source | What to look for |
|---|---|
| Reddit, forums, communities | People complaining about the problem repeatedly |
| Google Trends | Search volume for problem-related terms |
| Competitor reviews (G2, Capterra) | 1–3 star reviews mentioning unmet needs |
| Twitter/X | People publicly frustrated with current solutions |
| Your own experience | You've felt this pain yourself — strongest starting signal, weakest standalone evidence |

**Pass bar:** three independent sources showing people actively looking for a solution, plus evidence of what they currently pay or work around.

---

## Level 2 — Landing page test

Create a page describing the product. Drive traffic. Measure signups.

The page needs: the problem stated in the customer's words, the solution in one sentence, a single CTA ("Join the waitlist" / "Get early access"), an email capture, and optionally 1–2 qualifying questions (role, company size).

**Target:** 100 visitors minimum. Fewer than 100 and the rate is noise.

| Signup rate | Read |
|---|---|
| < 5% | Weak interest. Rethink positioning or audience before rethinking the product. |
| 5–15% | Moderate. Worth one more experiment, not worth building yet. |
| 15%+ | Strong. Move to a pre-sale or the manual delivery test. |

A low rate on a well-targeted audience is information about the offer. A low rate on cold untargeted traffic is information about the traffic. Know which one you ran.

---

## Level 3 — Fake door test

Add a button or link for a feature that doesn't exist. Measure clicks.

```
1. Add a CTA for the feature: "Try [Feature Name]"
2. On click, show: "This feature is coming soon! Sign up to be first to know."
3. Collect email.
4. Measure click rate against page views.
```

Best used inside an existing product with real traffic. On a cold landing page it measures curiosity, not demand.

**Ethics:** always tell the truth on the other side of the click. "Coming soon, want to be notified" is fine. A fake checkout that takes card details is not.

---

## Level 4 — Pre-sale test

Offer the product at a discount before it exists. If people pay, that is the strongest signal available.

```
"[Product] launches in [timeframe]. Get 50% off as a founding member.
$X/month (normally $Y/month). Cancel anytime."
```

**Pass bar:** 10+ strangers pay. Friends and family don't count. Zero payments after 100 qualified visitors is a no-go, not a pricing problem.

Take real money, and refund it immediately if you decide not to build. Taking money you never intend to honor is fraud, not validation.

---

## Level 5 — Manual delivery test

Deliver the result the product promises, by hand, to paying customers. Use email, a form, a spreadsheet, and your own time. Write no code.

A pre-sale proves people will pay for a promise. This test proves they will pay for the result, and it shows exactly what the product must do. The founder learns every step by doing the work.

1. Write the promise in one sentence: what the customer has before, and what they have after.
2. Find 3 people with the problem. Start with people you know, then communities you belong to.
3. Charge them. A low price is fine. Free tells you nothing about payment.
4. Deliver the result by hand. For each customer, write down every step, the tool you used, and the time it took.
5. Repeat until 10 customers have paid.

**Pass bar:** 10 paying customers who are not friends or family, and your steps did not change for the last 3.

**What to keep:** the written steps. They are the first draft of the spec. The first build automates the step that takes the most time. Do not automate a step that still changes from customer to customer.

**When this test does not fit:** some products cannot be delivered by hand, such as real-time collaboration or anything that needs many users at once. Use a pre-sale instead. The goal stays at 10 paying customers.

---

## Timeline and budget

```
Week 1: Problem research + 5 customer conversations
Week 2: 5 more conversations + landing page live
Week 3: Drive traffic to landing page (100+ visitors)
Week 4: Analyze results, make the go/no-go call

Total cost: $0–200
Total time: 10–15 hours
```

Set the week-4 deadline before starting. Validation without a deadline becomes a way of avoiding the decision rather than making it.
