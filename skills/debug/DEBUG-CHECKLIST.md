# Debug Checklist

Systematic steps for debugging any issue.

---

## Phase 1: Reproduce

### Make It Happen Consistently

```
Reproduction Steps:
1. What exact actions trigger the bug?
2. Does it happen every time?
3. Does it happen on all browsers?
4. Does it happen with all data?
5. Does it happen for all users?
```

### Document Steps

```
Bug Report:
Title: [Short description]
Steps:
1. [Action]
2. [Action]
3. [Bug occurs]

Expected: [What should happen]
Actual: [What actually happens]
Frequency: [Always / 80% / Rare]
```

### If Can't Reproduce

```
Try:
- Different browser (Chrome, Safari, Firefox)
- Different device (phone, desktop)
- Different account/user
- Different data/inputs
- Clear cache and try again

Still can't reproduce?
- Ask user for more details
- Screen recording from user
- Might be environmental (network, etc)
```

---

## Phase 2: Gather Evidence

### Check Console

```
1. Open DevTools (F12)
2. Click "Console" tab
3. Reproduce bug
4. Look for:
   - Red errors (critical)
   - Yellow warnings (important)
   - Failed network requests
```

**Screenshot and save:**
- Full error message
- Stack trace (if any)
- Context (what you were doing)

### Check Network

```
1. DevTools → Network tab
2. Reproduce bug
3. Look for:
   - Failed requests (red, 4xx, 5xx)
   - Slow requests (>1 second)
   - Missing requests (expected call didn't happen)
```

**For failed requests:**
- Click failed request
- Check "Response" tab
- Screenshot error response
- Note request URL and method

### Check What Changed

```
Review recent changes:
- Git commits today
- Features deployed recently
- Settings changed
- Dependencies updated

Ask: What's different from when it worked?
```

---

## Phase 3: Diagnose with AI

### Give Complete Context

```
Provide to AI:

Bug: [description]

Steps to reproduce:
1. [Step]
2. [Step]
3. [Bug happens]

Evidence:
- Console error: [paste]
- Network error: [paste]
- Screenshot: [attach]

Environment:
- Browser: [Chrome 120]
- Device: [MacBook Pro]
- URL: [where it happened]

Recent changes:
- [What changed recently]

Before proposing fixes:
1. What's the root cause?
2. Why is it happening?
3. What needs to change?
```

### Ask for Explanation First

```
Don't jump to fixes.

Ask AI:
- What's actually wrong?
- Why is this happening?
- Is this the real problem or symptom?

Understand before fixing.
```

---

## Phase 4: Fix and Verify

### AI Proposes Fix

```
After AI proposes fix:

Questions to ask:
- Will this fix the root cause?
- Could this break anything else?
- How do I test that it worked?

If unclear, ask AI to explain more.
```

### Test the Fix

```
Testing checklist:
- [ ] Reproduce original bug (should be gone)
- [ ] Test happy path (still works)
- [ ] Test related features (no regression)
- [ ] Check console (no new errors)
- [ ] Test in multiple browsers
- [ ] Test on mobile
```

### Verify No Regression

```
After fix, test:
- Feature that was broken (now works)
- Related features (still work)
- Unrelated features (quick check)

If anything broke:
"Fix worked but broke [X]. Need to adjust."
```

---

## Common Debug Patterns

### Pattern 1: It Worked, Now Broken

**Diagnosis:**
- What changed between working and broken?
- Deployment? Code change? Setting change?

**Action:**
```
Tell AI:
"Worked yesterday, broke today.
Changes made: [list changes]
Which could cause: [the bug]?"
```

### Pattern 2: Works Sometimes

**Diagnosis:**
- Timing issue?
- Race condition?
- Caching?
- External API flaky?

**Action:**
```
Tell AI:
"Intermittent bug.
Works: [X%] of time
Pattern: [when it fails more/less]
Need logging to capture failures."
```

### Pattern 3: Works in Dev, Broken in Production

**Diagnosis:**
- Environment differences?
- Missing env variables?
- Different data?
- Different traffic/load?

**Action:**
```
Tell AI:
"Works locally, fails in production.
Production error: [error]
Check environment config and deployment."
```

### Pattern 4: Works in Chrome, Broken in Safari

**Diagnosis:**
- Browser compatibility issue
- CSS/JS not supported
- Different default behaviors

**Action:**
```
Tell AI:
"Works in Chrome, broken in Safari.
Safari error: [error or description]
Fix browser compatibility."
```

---

## Debugging Edge Cases

### Empty State Bugs

```
Test with:
- No data at all
- Empty lists
- Missing fields

Common issues:
- "Cannot read property" errors
- Blank pages
- Broken layouts
```

### Data Volume Bugs

```
Test with:
- 1 item
- 100 items
- 10,000 items

Common issues:
- Slow performance
- Crashes
- UI breaks
```

### Timing Bugs

```
Test:
- Slow connection (3G)
- Fast actions (double-click)
- Let session expire
- Multiple tabs

Common issues:
- Race conditions
- Stale data
- Session issues
```

---

## Multi-Issue Debugging

### One Bug or Many?

**Symptoms that look like one bug might be:**
- Multiple small issues
- One root cause with many symptoms

**Approach:**
```
List all symptoms:
1. [Symptom]
2. [Symptom]
3. [Symptom]

Ask AI:
"Are these separate bugs or one root cause?"
```

### Priority Order

```
Fix in order:
1. Blocking bugs (can't use app)
2. Critical bugs (main features broken)
3. Major bugs (important features broken)
4. Minor bugs (edge cases)

Don't fix minor while critical unfixed.
```

---

## When Stuck

### After 1 Failed Fix

```
Reassess:
- Did we misdiagnose?
- Is there more info needed?
- Try different approach?

Tell AI:
"Fix didn't work. Here's what happened: [new info]"
```

### After 2 Failed Fixes

```
Stop trying fixes.

Tell AI:
"2 fixes failed. 
Fix 1: [tried] → [result]
Fix 2: [tried] → [result]

Are we fixing wrong thing?
Should we rethink approach?"
```

### After 3 Failed Fixes

```
Don't try 4th fix.

Options:
1. Start feature over with better approach
2. Get human developer help
3. Work around the bug temporarily

Tell AI:
"3 fixes failed. This approach isn't working.
Should we rebuild this differently?"
```

---

## Logging for Debugging

### Add Strategic Logs

```
Tell AI:
"Add logging to help debug:
- Log when [event] happens
- Log [variable] values
- Log API request/response
- Log errors with context"
```

### Useful Log Points

```
Log at:
- Function entry/exit
- Before/after API calls
- When changing state
- In error handlers
- At decision points
```

### Log Format

```
Good log:
[TIMESTAMP] [LEVEL] [CONTEXT] Message

Example:
[2025-01-13 10:30:45] [ERROR] [UserAuth] 
Login failed for user: user@example.com
Reason: Invalid password
Attempts: 3
```

---

## Documentation

### Bug Fix Log

```
Keep simple log:

Date: 2025-01-13
Bug: Form submission fails
Root cause: Missing validation
Fix: Added client-side validation
Tested: Chrome, Safari, mobile
Prevention: Add validation to all forms
```

### Known Issues

```
Track unfixed bugs:

Bug: Dashboard slow with 1000+ items
Workaround: Pagination added
Permanent fix: TODO - optimize query
Priority: Medium
```

---

## Prevention

### After Every Bug Fix

```
Ask:
- How could we have caught this earlier?
- What test would have found this?
- What validation would prevent this?

Tell AI:
"Bug fixed. How do we prevent similar bugs?"
```

### Common Prevention

```
Prevent by:
- Input validation
- Error boundaries
- Type checking
- Better error messages
- Loading states
- Edge case testing
```

---

## Quick Reference

**5-Minute Debug:**
```
1. Reproduce bug
2. Check console errors
3. Check network errors
4. Screenshot everything
5. Give to AI with context
```

**15-Minute Debug:**
```
1. Reproduce consistently
2. Gather all diagnostic info
3. Check what changed
4. AI diagnoses root cause
5. AI fixes
6. Test fix + verify no regression
```

**When to escalate:**
```
- After 2-3 failed fix attempts
- Critical production bug
- Can't reproduce at all
- Security issue
- Data corruption risk
```