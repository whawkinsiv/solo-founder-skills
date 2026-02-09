# Breaking Things on Purpose

How to intentionally break your app to find bugs before users do.

---

## Why Break Things?

Users are creative at finding bugs. They:
- Click too fast
- Enter weird data
- Use your app in unexpected ways
- Have slow connections
- Use old browsers

**Better you find bugs than users.**

---

## The Chaos Monkey Approach

### 1. Click Everything Rapidly

```
Test: Click submit button 10 times fast
Good: Button disables after first click
Bad: Creates 10 duplicate submissions

Test: Click between tabs rapidly
Good: Tabs switch smoothly, no errors
Bad: UI breaks, data gets mixed up

Test: Navigate back/forward fast
Good: Pages load correctly
Bad: Page shows wrong data or errors
```

### 2. Enter Absurd Data

```
Test: Enter 10,000 characters in "name" field
Good: Truncates to 50 chars or shows error
Bad: Breaks layout or crashes

Test: Enter: <script>alert('xss')</script>
Good: Sanitizes input, stores as plain text
Bad: Alert appears (XSS vulnerability)

Test: Enter: '; DROP TABLE users;--
Good: Treated as plain text
Bad: Database error (SQL injection)
```

### 3. Do Things Out of Order

```
Test: Go directly to step 3 of 5 (URL hack)
Good: Redirects to step 1 or shows error
Bad: Breaks or skips validation

Test: Submit form before fields loaded
Good: Form disabled until ready
Bad: Submits partial/empty data

Test: Edit item you just deleted
Good: Shows "Item not found"
Bad: Crashes or shows stale data
```

### 4. Refresh at Wrong Times

```
Test: Refresh during form submission
Good: Shows confirmation or idempotent
Bad: Submits twice

Test: Refresh during file upload
Good: Upload cancels or resumes
Bad: Partial file saved or error

Test: Refresh after successful action
Good: Shows result, no re-execution
Bad: Action runs again
```

---

## Network Chaos

### Simulate Slow Connection

**Chrome DevTools:**
1. Open DevTools (F12)
2. Network tab
3. Dropdown: "Slow 3G"
4. Try your app

**What breaks:**
- Missing loading states
- Timeouts with no error message
- Double-submits (user clicks again)
- Broken layout (images don't load)

### Simulate Offline

**Chrome DevTools:**
1. Network tab
2. Check "Offline"
3. Try actions

**What breaks:**
- No offline message shown
- Actions fail silently
- Error messages unhelpful
- Can't recover when back online

### Interrupt Actions

```
Test: Start upload, disable network
Good: Shows error, allows retry
Bad: Hangs forever or crashes

Test: Submit form, go offline mid-request
Good: Shows "Connection lost, retrying..."
Bad: Form clears or shows success incorrectly
```

---

## Authentication Chaos

### Expired Sessions

```
Test: Log in, wait 30 min, try action
Good: Redirects to login with clear message
Bad: Shows generic error or crashes

Test: Open app in 2 tabs, logout in one
Good: Other tab detects logout
Bad: Other tab breaks on next action
```

### Permission Chaos

```
Test: Regular user tries /admin URL
Good: 403 error or redirect with message
Bad: Shows admin page or crashes

Test: Edit URL to view other user's data
Good: Permission denied
Bad: Shows other user's data (security issue!)
```

### Token Manipulation

```
Test: Clear auth token, try protected action
Good: Redirects to login
Bad: Shows error page or crashes

Test: Modify token in DevTools, make request
Good: Rejects invalid token
Bad: Accepts tampered token (security issue!)
```

---

## Data Chaos

### Empty States

```
Test: New account, view dashboard
Good: Clear empty state with action
Bad: Blank page or loading forever

Test: Delete all items, view list
Good: "No items" with "Create" button
Bad: Error or broken layout
```

### Volume Stress

```
Test: Create 1000 items, load list
Good: Paginates, loads quickly
Bad: Crashes or takes minutes

Test: Upload 100 files at once
Good: Handles or limits queue
Bad: Crashes or uploads fail
```

### Weird Characters

```
Test: Name with emoji: "John 🎉 Doe"
Good: Saves and displays correctly
Bad: Breaks display or saves incorrectly

Test: Bio with every special char: !@#$%^&*()
Good: Handles gracefully
Bad: Breaks layout or parsing
```

---

## Browser Chaos

### Different Browsers

```
Test in Safari (iOS):
- Dates formatted differently
- Flexbox behaves differently
- Some CSS might not work

Test in Firefox:
- Extensions might interfere
- Scrolling feels different
- Input behaviors vary
```

### Browser Settings

```
Test: Disable JavaScript
Good: Shows "Please enable JS" message
Bad: Blank page

Test: Disable cookies
Good: Still works or clear message
Bad: Infinite redirect or error

Test: Enable "Do Not Track"
Good: Respects privacy setting
Bad: Tracking breaks app
```

### Extensions

```
Test: Ad blocker active
Good: App works (maybe disable ads gracefully)
Bad: App breaks or loads forever

Test: Password manager active
Good: Plays nice with autofill
Bad: Double-fills fields or breaks
```

---

## Mobile Chaos

### Rotation

```
Test: Fill form, rotate device
Good: Form data preserved
Bad: Form clears

Test: Rotate during action
Good: Action continues
Bad: Action cancels or duplicates
```

### Keyboards

```
Test: Keyboard covers input
Good: Page scrolls to show input
Bad: Can't see what you're typing

Test: Autocorrect changes input
Good: Validation still works
Bad: Form rejects valid input
```

### Gestures

```
Test: Swipe vs scroll confusion
Good: Clear distinction
Bad: Accidental actions

Test: Pinch to zoom (if not intended)
Good: Disabled on form
Bad: Zooms and breaks layout
```

---

## Timing Attacks

### Race Conditions

```
Test: Submit form, immediately click elsewhere
Good: Form submission completes
Bad: Submission cancelled

Test: Open modal, immediately press Escape
Good: Modal closes gracefully
Bad: Modal stuck or errors

Test: Load data, immediately navigate away
Good: Request cancelled, no errors
Bad: Memory leak or errors
```

### Rapid Actions

```
Test: Type very fast in search
Good: Debounces, searches after pause
Bad: Makes 50 API calls

Test: Scroll up/down rapidly
Good: Smooth, no flicker
Bad: Jumpy or errors

Test: Click pagination rapidly
Good: Loads correctly
Bad: Wrong page or duplicate requests
```

---

## Copy/Paste Attacks

### Large Pastes

```
Test: Copy 10,000 words, paste in field
Good: Truncates or shows error
Bad: Freezes or crashes

Test: Paste HTML from website
Good: Strips HTML, keeps text
Bad: Renders HTML (security issue!)
```

### Weird Paste

```
Test: Paste image in text field
Good: Ignores or shows error
Bad: Crashes

Test: Paste formatted text
Good: Strips formatting
Bad: Breaks layout
```

---

## File Upload Chaos

### File Types

```
Test: Upload .exe file (expecting .pdf)
Good: Rejects with clear message
Bad: Accepts or crashes

Test: Rename virus.exe to virus.pdf
Good: Checks file content, not just name
Bad: Accepts malicious file
```

### File Sizes

```
Test: Upload 100MB file (limit 5MB)
Good: Rejects before uploading
Bad: Uploads then fails

Test: Upload 0-byte file
Good: Rejects with message
Bad: Saves broken file
```

---

## The Nuclear Option

### Ultimate Stress Test

```
Do all of these at once:
1. Slow 3G connection
2. Fill every field with maximum data
3. Double-click all buttons
4. Open 5 tabs doing different things
5. Go offline mid-action
6. Rotate device continuously
7. Paste 10,000 characters everywhere
8. Refresh randomly

If app survives: Very robust
If app breaks: You found bugs!
```

---

## Automated Breaking (Optional)

### Simple Script

```javascript
// Run in browser console
// Clicks "submit" button 100 times
for(let i=0; i<100; i++) {
  document.querySelector('button[type="submit"]').click();
}
```

### Monkey Testing Tools

- **Gremlins.js** - Random clicks and inputs
- **FuzzDB** - Malicious input strings
- **Chrome DevTools** - Throttling, offline mode

---

## What to Do When Things Break

**When you find a bug:**

1. **Document it:**
   - Exact steps to reproduce
   - Screenshot/video
   - Browser and device
   - Frequency

2. **Assess severity:**
   - Blocker: Can't use app at all
   - Critical: Main feature broken
   - Major: Important feature broken
   - Minor: Edge case, rare issue

3. **Give to AI to fix:**
```
Found bug: [paste documentation]
Severity: [level]
Please fix and verify it doesn't break anything else.
```

4. **Test the fix:**
   - Reproduce original bug (should be gone)
   - Test related features (no regression)
   - Try to break fix in new ways

---

## Breaking Things Checklist

**Before every deploy:**
```
- [ ] Clicked buttons rapidly
- [ ] Entered 1000+ characters in fields
- [ ] Tested with slow 3G
- [ ] Tested offline scenario
- [ ] Tried to access protected routes
- [ ] Submitted forms twice
- [ ] Refreshed during actions
- [ ] Tested on mobile device
- [ ] Rotated device during use
- [ ] Tried SQL/HTML injection
```

**If nothing broke:** Either very robust or need to try harder!
