---
name: retention
description: "Use this skill to keep the customers the founder already has: 'customers are leaving,' 'reduce churn,' 'onboarding,' 'welcome emails,' 'people sign up but don't use it,' 'collect feedback,' 'feature requests,' 'customer support,' 'help docs,' or 'someone cancelled.' Gets new customers to their first result, sets up a weekly check-in, simple support, a feedback loop, and an honest cancellation flow, all by hand first. Not for finding new customers (use first-customers)."
metadata:
  version: 1.0.0
---

# Retention

Before 100 customers, keeping customers is personal work, not automation. Talk to every customer, fix what they hit, and tell them when you did.

## Step 1: Get every new customer to the first result

1. **Define the first result:** the first action where the customer gets what they paid for. Examples: the first invoice sent, the first report seen with their own data.
2. **Before about 20 customers,** onboard each one yourself: a short call, or a written walkthrough sent the day they pay. Watch where they get stuck.
3. **After that,** add a short welcome email series that stops as soon as the customer reaches the first result:
   - right away: one action to take, and nothing else
   - day 1 and day 3, if not done yet: how to get there in 2 minutes
   - day 7: a personal note from the founder: "Reply to this. I read every one."
4. In the product, an empty screen shows the next step (see **beautify**).

## Step 2: Talk to customers

- **Under 50 customers, talk to every one.** No survey tools needed.
- Ask: "What were you trying to do? What almost stopped you? What would you miss if this disappeared?"
- Customers describe solutions. Find the problem underneath:
  - "Add a calendar view" may mean "I need to see things by date."
  - "Build an API" may mean "I want to connect this to my other tools."
- **Close the loop.** When you ship something a customer asked for, tell them by name. Nothing builds loyalty faster.
- Build what 3 or more paying customers need. One loud request is an anecdote (see **focus**).

## Step 3: Weekly check (about 15 minutes)

- Who has not used the product in 7 days? Send each one a personal note.
- Which support threads are older than 48 hours?
- Which payments failed? (The founder can see this in their payment dashboard.)
- Who cancelled this week? Email each one personally and ask why.

## Step 4: Simple support

- One support address that reaches the founder (see **email**). Reply personally, signed with a first name.
- A help page that answers the 5–10 most common questions is enough before 100 customers.
- Keep short reply templates and adapt each one:
  - **Investigating:** "I can see the issue and I'm looking into it. I'll update you by [time]."
  - **Bug confirmed:** "You're right, that's a bug on my end. I'll email you when the fix is live."
  - **Not now:** "I can see how [feature] would help with [their goal]. Right now I'm focused on [priority]. Here's a workaround: …"
- **Once a month:** tag every question. For the top 5, decide whether the fix belongs in the product, the help page, or the first-use steps.

## Step 5: Cancellation

1. Ask why, with one question and a few options: too expensive, missing a feature, not using it enough, switched to something else, technical problems.
2. Offer one alternative that matches the reason: a cheaper plan, a pause, or a call with the founder. Only one.
3. **Make cancelling easy.** A hidden cancel button causes chargebacks and angry reviews.
4. Keep the customer's data for at least 90 days. Exporting it is easy.
5. Write back only when you ship the thing they left over.

## Rules

- **Do it by hand before you automate it.** Automate a step only after you have done it by hand enough to know what works.
- **At small numbers, read the reasons, not the rate.** Three cancellations out of 20 customers is a story to understand, not a statistic.
- **No dark patterns.** No hidden cancel button, no guilt-trip copy, no hard exports.

## Output

```
First result:     <the action, and how each new customer reaches it>
Weekly check:     <who to contact this week, and why>
Feedback themes:  <problems heard 3+ times>
Support:          <top questions, and the fix for each>
Cancellations:    <reasons this month, and the response to each>
```
