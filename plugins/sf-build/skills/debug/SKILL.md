---
name: debug
description: "Use this skill when features break, users report errors, deployments fail, or tests don't pass. Guides systematic debugging: reproducing bugs, gathering diagnostic info, reading error messages, and working with AI tools to fix issues efficiently."
---

# Debug

## The golden rule

**NO GUESSING. GATHER INFO FIRST.**

Bad: Something broke → try random fix → doesn't work → try another → still broken after 5 attempts.

Good: Something broke → reproduce it → gather diagnostic info → diagnose root cause → fix it (usually first try).

**Diagnosis before fixes.**

---

## Debugging by tool

How you debug depends on which tool you're using.

### Claude Code (you have direct access)

Claude Code can gather its own diagnostics. Before asking the founder for screenshots or logs, do this automatically:

```
Auto-debug steps (do these yourself):
1. Check git history: git log --oneline -10 and git diff HEAD~3
2. Search for the error: Grep for error text across the codebase
3. Read the failing file: Read the file + surrounding context
4. Run the app/tests: Bash to run dev server, test suite, or reproduce
5. Check logs: Read server logs, build output, or error logs
6. Check environment: Verify .env.example vs actual config
```

Only ask the founder for information you can't get yourself: what they saw in the browser, what they clicked, screenshots of visual bugs.

### Lovable / Replit (founder pastes into chat)

The founder needs to gather info manually and paste it. Use the "Tell AI:" prompts in [DEBUG-PROMPTS.md](DEBUG-PROMPTS.md) — they're structured templates that ensure complete context.

### Production bugs (check monitoring first)

Before debugging production issues, check monitoring and error tracking:

```
1. Error tracker (Sentry, LogRocket): exact error + stack trace + user context
2. Server logs: filter by timestamp of report
3. Hosting dashboard: any deployment or outage at that time?
4. Database: any failed migrations or connection issues?
```

See /monitor skill for setting up monitoring. See /deploy skill for rollback procedures.

---

## Workflow

```
Debug process:
- [ ] Reproduce bug consistently
- [ ] Gather diagnostic info (auto in Claude Code, manual elsewhere)
- [ ] Check what changed recently
- [ ] Diagnose root cause before proposing fixes
- [ ] Fix the root cause
- [ ] Test fix works
- [ ] Verify didn't break anything else
- [ ] Ask: how do we prevent this?
```

---

## Reproducing bugs

Before fixing, reproduce it:

```
Can you reproduce it?
- [ ] Exact steps to trigger bug
- [ ] Happens every time or intermittently?
- [ ] Specific browser/device?
- [ ] Specific data or user?

If can't reproduce:
- Ask user for exact steps or screen recording
- Try different browser/device/account
- Try with different data
- Clear cache and retry
- Check if timing-dependent
```

**Tell AI:**
```
Bug: [description]

Steps to reproduce:
1. [Step]
2. [Step]
3. [Bug happens]

Happens: [Always / Sometimes / Once]
Browser: [Chrome 120 on Mac]
Screenshot: [attach]
```

---

## Capturing error info

### Browser console

1. Right-click page → Inspect → Console tab
2. Look for red errors
3. Screenshot the full error including stack trace

**Tell AI:**
```
Console error: [paste full error message]
When it happens: [what you were doing]
```

### Network tab

1. DevTools → Network tab → reproduce bug
2. Look for failed requests (red, 4xx, 5xx)
3. Click failed request → check Response tab

**Tell AI:**
```
API call failing:
URL: /api/endpoint
Method: [GET/POST]
Status: [status code]
Response: [paste error response]
This happens when: [action]
```

### Visual bugs

Screenshot what you expected vs what actually shows. Include device and browser.

---

## Common bug types

### "Nothing happens when I click"
Check: console errors? Network request failing? Element actually clickable (not covered by another element)?

### "Page won't load"
Check: network errors? JavaScript errors? Infinite redirect? Missing environment variable?

### "Wrong data showing"
Check: API returning wrong data (network tab)? Caching issue? State not updating? Wrong user context?

### "Form doesn't submit"
Check: validation errors visible? Console errors? Network request firing at all?

### "Works in dev, broken in production"
Check: environment variables set? Different database? Build step stripping something? CORS configured for production domain?

### "Works in Chrome, broken in Safari"
Check: CSS/JS compatibility? Safari-specific defaults? Date parsing differences?

---

## Escalation discipline

### After 1 failed fix

Reassess. Did we misdiagnose? Is there more info we should gather?

```
Fix didn't work. Here's what happened after applying it: [new info].
Are we fixing the right thing?
```

### After 2 failed fixes

**Stop trying fixes.** The diagnosis is probably wrong.

```
2 fixes failed.
Fix 1: [tried] → [result]
Fix 2: [tried] → [result]

Are we fixing the wrong thing? Should we rethink the approach entirely?
```

### After 3 failed fixes

Don't try a 4th. Change strategy:
1. Rebuild the feature with a simpler approach
2. Get a human developer to look at it (see /hiring)
3. Ship a workaround and fix properly later

---

## Digging deeper: find the real root cause

Most debugging failures happen because you stop at the first plausible cause instead of the actual root cause. Use the "keep asking why" technique:

```
Problem: Server crashed
  Why? → Out of memory
  Why? → Memory leak in the auth service          ← Most people stop here and "add more RAM"
  Why? → Database connections not being released
  Why? → Error handler doesn't close connections
  Why? → No cleanup in the finally block           ← THIS is the fix
```

**How to tell you've found the real root cause:**
- It's something you can actually change (code, config, process)
- Fixing it would prevent the problem from recurring
- Asking "why?" again doesn't lead anywhere actionable

**Common mistake: stopping at "the AI broke it."** That's blame, not a cause. Ask instead: what process would have caught this? Missing test? Missing validation? No code review?

### When a bug has multiple causes

Sometimes a bug needs two things to go wrong at the same time. When the obvious cause doesn't fully explain the problem, look for a second branch:

```
Problem: Deployment failed
  Why? → Database migration timed out
    Branch A: Why was the migration slow?
      → Table lock from a long-running query → Missing index
    Branch B: Why is the timeout so short?
      → Using default timeout → No deployment-specific config
```

Both branches need fixing, or the bug will come back under slightly different conditions.

### Validate your diagnosis

Before implementing a fix, trace it backwards: "If I fix X, does that prevent Y, which prevents Z, which prevents the original problem?" If the chain breaks, you found the wrong root cause.

---

## Intermittent bugs

"Works sometimes, breaks sometimes" — likely a race condition, caching issue, or external API flakiness.

**Tell AI:**
```
Bug is intermittent.
Works: [X] out of 10 times
Fails: [Y] out of 10 times

Pattern: Fails more when [condition]. Never fails when [condition].

Add logging to capture state when it fails.
```

---

## Edge case testing

When a fix works for the main case, also test:

- **Empty states**: no data, empty lists, missing fields
- **Volume**: 1 item, 100 items, 10,000 items
- **Timing**: slow connection (3G throttle in DevTools), rapid double-clicks, expired sessions, multiple tabs
- **Boundaries**: very long text, special characters, zero values, negative numbers

---

## Bugs in production

**Priority 1: Can users work around it?**
- Yes → fix in next deployment
- No → emergency fix needed

**Emergency fix:**
```
Production bug blocking users.
Bug: [description]
Impact: [how many users affected]

Need the simplest fix that unblocks users. Can improve later.
```

---

## Multiple bugs at once

Symptoms that look like one bug might be several, or several symptoms might share one root cause.

```
List all symptoms:
1. [Symptom]
2. [Symptom]
3. [Symptom]

Are these separate bugs or one root cause?
```

**Fix in priority order:** blocking (can't use app) → critical (main features broken) → major → minor. Don't fix minor bugs while critical ones are unfixed.

---

## Adding debug logging

When a bug is hard to diagnose, add strategic logging:

```
Add logging at:
- Function entry with input values
- Before/after API calls with request/response
- State changes with before/after values
- Error handlers with full context
- Decision points (which branch was taken)

Format: [TIMESTAMP] [LEVEL] [CONTEXT] Message
Example: [2025-01-13 10:30:45] [ERROR] [UserAuth] Login failed for user@example.com - Reason: Invalid password - Attempts: 3
```

Remove or reduce logging after the bug is fixed.

---

## Prevention

After every fix, think at three levels:

1. **Immediate fix** — you already did this (the bug is gone)
2. **Preventive measure** — what stops this from ever happening again? (validation, test, type check)
3. **Detection mechanism** — if prevention fails, how do you catch it early? (monitoring alert, error tracking)

```
Bug is fixed. Now:
- What validation or test would prevent this from recurring?
- What monitoring or alert would catch it early if it does recur? (see /monitor)
- Is this a pattern? Could the same type of bug exist elsewhere in the codebase?
```

---

## When to get help

**Consider hiring a developer when:**
- Stuck after following this entire process
- Critical production bug you can't figure out
- Same bug keeps coming back after fixing
- Bug in a complex third-party integration
- Security issue or data corruption risk

For most bugs, this process with AI tools is sufficient.

---

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Trying fixes without info | Gather diagnostic info first |
| "It doesn't work" (vague) | Be specific: what exactly doesn't work? |
| Not reproducing first | Find consistent steps to trigger the bug |
| Asking AI for random fixes | Diagnose root cause first |
| Ignoring console/network errors | Always check both tabs |
| Not testing after fix | Verify fix works AND didn't break other things |
| Fixing minor bugs while critical ones exist | Prioritize by user impact |
| Accepting first plausible cause | Keep asking "why?" until you reach something you can actually fix |
| "The AI broke it" (blame, not diagnosis) | Ask: what process would have caught this? |
