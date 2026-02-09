# Debug Prompts for AI

Effective prompts for debugging with AI tools.

---

## Initial Bug Report

```
Bug found: [Short description]

Steps to reproduce:
1. [Action]
2. [Action]
3. [Bug happens]

Expected: [What should happen]
Actual: [What happens]

Evidence:
- Console error: [paste or screenshot]
- Network error: [paste response]
- Screenshot: [attach]

Environment:
- Browser: [Chrome 120 on Mac]
- Device: [Desktop / iPhone 14]
- URL: [where it occurred]

Recent changes:
- [Anything changed recently?]

Before proposing fixes, please:
1. Explain what you think is wrong
2. Why it's happening
3. What needs to change
```

---

## Asking AI to Diagnose

```
[Paste bug report above]

Before fixing, help me understand:
- What's the root cause?
- Why is this happening?
- Is this the real problem or a symptom?
- Are there related issues?

Explain in plain English first.
```

---

## Reproduction Issues

```
Users report: [bug description]

But I can't reproduce it.

Tried:
- [Browsers tested]
- [Devices tested]
- [Steps tried]

Can you help identify:
- What conditions might trigger this?
- What should I test that I haven't?
- How to make it happen consistently?
```

---

## Intermittent Bugs

```
Bug happens sometimes, not always.

Frequency: Works [X] times, fails [Y] times out of 10

Pattern noticed:
- Fails more when: [condition]
- Never fails when: [condition]
- Sometimes happens after: [event]

Please:
1. Add detailed logging to capture when it fails
2. Log relevant state before/after
3. Help identify timing or condition that triggers it
```

---

## Console Error Diagnosis

```
Getting this error in console:
[Paste full error message and stack trace]

When: [What action triggers it]
Frequency: [Always / Sometimes]
Browser: [Which browser]

Questions:
- What does this error mean in plain English?
- What's the likely cause?
- How serious is it?
- How do we fix it?
```

---

## Network Error Diagnosis

```
API call failing:

Request:
- URL: /api/endpoint
- Method: POST
- Body: [paste request body]

Response:
- Status: 500
- Body: [paste error response]

When: [What triggers this call]
Context: [What user was doing]

Questions:
- What went wrong on the server?
- Is this a frontend or backend issue?
- How do we fix it?
```

---

## Visual Bug Diagnosis

```
Visual bug on [page/component]:

Expected: [Screenshot or description]
Actual: [Screenshot showing problem]

Occurs on:
- Device: [Desktop / iPhone 14]
- Browser: [Chrome / Safari]
- Screen size: [Specific size if known]

Doesn't occur on:
- [Where it works correctly]

Please:
1. Identify what's causing the layout issue
2. Propose CSS fix
3. Ensure fix works on all screen sizes
```

---

## "Nothing Happens" Bugs

```
Bug: Clicking [button/link] does nothing

Expected: [What should happen]
Actual: Nothing (no error, no action)

Checked:
- Console: [Any errors? Paste if yes]
- Network: [Any request made? Paste if yes]
- Button state: [Enabled/disabled]

The button appears clickable but nothing happens.
What could cause this?
```

---

## "Wrong Data" Bugs

```
Bug: Showing wrong data

Expected: [User A's data / Specific data]
Showing: [User B's data / Wrong data]

Context:
- User ID: [If relevant]
- Page: [Where showing wrong data]
- Data source: [API endpoint if known]

API Response (from Network tab):
[Paste response]

Questions:
- Is API returning wrong data?
- Is frontend displaying wrong data?
- Is there a caching issue?
```

---

## Fix Didn't Work

```
Tried fixing but issue persists.

Original bug: [Description]

Fix attempted:
[What we changed]

Result:
[What happened - still broken? Different error?]

New information:
- Console now shows: [Any new errors]
- Behavior changed to: [How it's different]

Questions:
- Did we fix the wrong thing?
- Is there a different root cause?
- Should we try different approach?
```

---

## Multiple Failed Fixes

```
Stuck on this bug after [2/3] fix attempts.

Original problem:
[Description]

Fix 1: [What we tried]
Result: [Didn't work / Made it worse]

Fix 2: [What we tried]
Result: [Still broken]

Questions:
- Are we approaching this wrong?
- Should we start over?
- Is there a simpler solution?
- What are we missing?
```

---

## Edge Case Investigation

```
Bug only happens in specific situation:

Works when:
- [Conditions where it works]

Fails when:
- [Conditions where it fails]

Specific trigger:
[Exact condition that causes failure]

This seems like an edge case.
How do we handle this scenario properly?
```

---

## Performance Bug

```
[Feature/Page] is very slow.

Observed performance:
- Takes: [X] seconds
- Should take: [Y] seconds

When measured:
- Action: [What's slow]
- Device: [Type]
- Network: [Fast / 3G]

What I checked:
- Network tab: [Any slow requests?]
- Console: [Any warnings?]
- Happens: [Always / Sometimes]

What's causing the slowdown?
```

---

## After User Report

```
User reported issue but can't reproduce.

User's report:
"[Exact words from user]"

User context:
- When: [Date/time]
- Where: [Page/feature]
- Device: [If known]
- Browser: [If known]

Monitoring shows:
- Errors at that time: [Check Sentry]
- Logs at that time: [Check logs]

Can you help interpret what happened?
```

---

## Security-Related Bug

```
Potential security issue:

What happened:
[Description of unexpected behavior]

Concern:
[Why this might be security issue]

Evidence:
- [What you observed]
- [Screenshots/logs]

Questions:
- Is this a real security issue?
- How serious?
- What's the proper fix?
- What else should we check?

Please prioritize security in your response.
```

---

## Regression Bug

```
This worked before, broke after recent change.

What broke:
[Feature/functionality]

When it broke:
[After which deploy/change]

Recent changes:
[List changes from that deploy]

Error:
[If any error, paste it]

Please:
1. Identify which change caused regression
2. How to fix without breaking new feature
3. How to prevent similar regressions
```

---

## Database-Related Bug

```
Issue seems database-related:

Symptom:
[What's happening]

Error (if any):
[Database error message]

When:
[What action triggers it]

Database context:
- Type: [PostgreSQL/MySQL/etc]
- Query: [If known]
- Data size: [How much data]

Questions:
- Is this a query problem?
- Is this a data problem?
- How do we fix it safely?
```

---

## Integration Bug

```
Issue with [Third-party service] integration:

Service: [Stripe/SendGrid/etc]
Issue: [What's not working]

Error from service:
[Paste error message/response]

Our code:
[Relevant code snippet if short]

Service dashboard shows:
[What you see in their dashboard]

Questions:
- Is this our bug or their bug?
- Are we calling API correctly?
- How do we fix this?
```

---

## Mobile-Specific Bug

```
Bug only on mobile:

Works on:
- Desktop Chrome
- Desktop Safari

Fails on:
- [iPhone/Android]
- [Browser]

Error:
[Mobile console error if available]

Behavior:
[Describe what happens on mobile]

Screenshots:
[Mobile screenshots]

How do we fix for mobile without breaking desktop?
```

---

## Testing Fix Request

```
Bug is fixed (we think).

Original bug: [Description]
Fix applied: [What we changed]

Before deploying, please:
1. Verify this fixes the root cause
2. Check if this could break anything else
3. Suggest how to test the fix
4. Identify any edge cases to test
```

---

## Prevention Analysis

```
Bug is fixed and deployed.

Original bug: [What happened]
Root cause: [Why it happened]
Fix: [How we fixed it]

Questions:
- How could we have prevented this?
- What validation should we add?
- What monitoring should we add?
- What tests should we write?

Help me prevent similar bugs in the future.
```

---

## Quick Debug Prompts

**Fast diagnosis:**
```
Quick debug needed:
- Bug: [One sentence]
- Error: [Paste error]
- When: [One sentence]

What's wrong and how to fix?
```

**Is this serious:**
```
Got this error: [Paste error]

Questions:
- How serious? (Critical/Important/Minor)
- Needs immediate fix?
- Impact on users?
```

**Better error messages:**
```
Error message says: "[Current message]"

This is confusing to users.

Please:
1. Change to user-friendly message
2. Add helpful instructions
3. Log technical details separately
```