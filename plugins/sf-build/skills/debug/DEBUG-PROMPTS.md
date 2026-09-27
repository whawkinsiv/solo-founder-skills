# Debug prompts for Lovable, Replit, and Cursor

Copy-paste these templates when debugging in tools where you chat with AI rather than giving it direct file access. Fill in the brackets. Include screenshots when possible.

In Claude Code, most of this info can be gathered automatically — see the main skill file.

---

## General bug report

```
Bug: [Short description]

Steps to reproduce:
1. [Action]
2. [Action]
3. [Bug happens]

Expected: [What should happen]
Actual: [What happens]

Console error: [paste or screenshot]
Network error: [paste response]
Browser: [Chrome 120 on Mac]
Screenshot: [attach]

Recent changes: [Anything changed recently?]

Before proposing fixes, explain: What's the root cause? Why is it happening?
```

---

## Specific bug types

### Can't reproduce a user-reported bug

```
User reports: [bug description]

I can't reproduce it.

Tried:
- [Browsers tested]
- [Devices tested]
- [Steps tried]

What conditions might trigger this that I haven't tested?
```

### Performance bug

```
[Feature/Page] is very slow.
Takes: [X] seconds. Should take: [Y] seconds.
Action: [What's slow]
Device: [Type]
Network tab: [Any slow requests?]

What's causing the slowdown?
```

### Security-related bug

```
Potential security issue:
What happened: [Description]
Concern: [Why this might be security-related]
Evidence: [What you observed]

Is this a real security issue? How serious? What's the fix?
Prioritize security in your response.
```

### Regression (worked before, broke after a change)

```
This worked before, broke after recent change.
What broke: [Feature]
When it broke: [After which deploy/change]
Recent changes: [List]
Error: [If any]

Which change caused the regression? Fix without breaking the new feature.
```

### Database bug

```
Issue seems database-related:
Symptom: [What's happening]
Error: [Database error message]
When: [What action triggers it]
Database: [PostgreSQL/MySQL/Supabase/etc]

Is this a query problem or a data problem? Fix it safely.
```

### Third-party integration bug

```
Issue with [Stripe/SendGrid/Supabase/etc]:
What's not working: [Description]
Error from service: [Paste error]
Service dashboard shows: [What you see]

Is this our bug or theirs? Are we calling the API correctly?
```

### Mobile-only bug

```
Bug only on mobile:
Works on: Desktop Chrome, Desktop Safari
Fails on: [iPhone/Android] [Browser]
Behavior on mobile: [Description]
Error: [If available]

Fix for mobile without breaking desktop.
```

---

## Escalation prompts

### Fix didn't work

```
Tried fixing but issue persists.
Original bug: [Description]
Fix attempted: [What we changed]
Result: [Still broken? Different error?]
New console errors: [Any?]

Did we fix the wrong thing? Different root cause?
```

### Multiple failed fixes

```
Stuck after [2/3] fix attempts.
Original problem: [Description]
Fix 1: [Tried] → [Result]
Fix 2: [Tried] → [Result]

Are we approaching this wrong? Is there a simpler solution?
```

---

## Post-fix prompts

### Verify the fix

```
Bug is fixed (we think).
Original bug: [Description]
Fix applied: [What we changed]

Verify this fixes the root cause. Could this break anything else?
What edge cases should I test?
```

### Prevent similar bugs

```
Bug fixed and deployed.
Root cause: [Why it happened]
Fix: [How we fixed it]

How do we prevent similar bugs? What validation, tests, or monitoring should we add?
```

---

## Quick prompts

**Fast diagnosis:**
```
Quick debug: [one sentence]. Error: [paste]. When: [one sentence]. What's wrong?
```

**Severity check:**
```
Got this error: [paste]. How serious? Needs immediate fix? Impact on users?
```

**Better error messages:**
```
Error message says: "[current message]". This confuses users. Rewrite to be user-friendly and add helpful instructions.
```
