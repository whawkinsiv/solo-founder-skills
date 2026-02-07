# Edge Case Testing

Comprehensive list of edge cases to test.

---

## Input Edge Cases

### Text Fields

**Empty:**
- Required field left blank
- Optional field left blank
- Space-only input ("   ")

**Length:**
- Exactly at max limit (if 50 chars, enter 50)
- One over max limit (enter 51)
- Extremely long (10,000 characters)
- Single character

**Special characters:**
- Emoji: 🎉💀🔥
- Accents: café, naïve, Zürich
- Quotes: "test" 'test' `test`
- HTML: `<script>alert('xss')</script>`
- SQL: `'; DROP TABLE users;--`
- Newlines and tabs

**Case sensitivity:**
- ALL CAPS
- all lowercase
- MiXeD cAsE

---

## Number Fields

**Boundaries:**
- Zero
- Negative numbers
- Decimal numbers (if integers only)
- Very large numbers (999999999)
- Scientific notation (1e10)

**Invalid:**
- Letters in number field
- Special characters: $1,000
- Multiple decimals: 12.34.56

---

## Email Fields

**Valid formats:**
- simple@example.com
- name+tag@example.com
- name.with.dots@example.com

**Invalid formats:**
- No @ sign: plaintext
- No domain: user@
- No username: @domain.com
- Multiple @: user@@example.com
- Spaces: user @example.com

---

## Date/Time Fields

**Boundaries:**
- Past dates (when not allowed)
- Future dates (when not allowed)
- February 29 (leap year)
- Invalid dates: Feb 30, April 31

**Formats:**
- Different input formats
- Different display formats
- Timezone handling

---

## Dropdown/Select

**Edge cases:**
- Nothing selected (if required)
- First option selected
- Last option selected
- Very long option text (does it truncate?)

---

## Checkboxes

**Edge cases:**
- None selected (if at least one required)
- All selected
- Checking/unchecking rapidly

---

## File Upload

**File types:**
- Correct type (PDF, JPG)
- Wrong type (EXE, ZIP)
- No extension: file
- Multiple extensions: file.pdf.exe

**File sizes:**
- Empty file (0 bytes)
- Exactly at limit (5MB file, 5MB limit)
- Slightly over limit (5.1MB)
- Huge file (100MB+)

**File names:**
- Very long filename (200+ chars)
- Special characters: file!@#$.jpg
- Non-English: 文档.pdf
- Spaces: my file.pdf
- No extension

---

## List/Table Edge Cases

**Data volume:**
- Empty list (0 items)
- Single item
- Exactly one page (50 items)
- Multiple pages (500 items)
- Huge list (10,000+ items)

**Item content:**
- Very long title (breaks layout?)
- No title/description
- Special characters in data
- Mixed data types

---

## URL/Link Edge Cases

**Valid URLs:**
- https://example.com
- http://example.com (if allowed)
- www.example.com (missing protocol)
- example.com (missing protocol)

**Invalid URLs:**
- Not a URL: "banana"
- JavaScript: javascript:alert('xss')
- Internal IPs: http://192.168.1.1
- File protocol: file:///etc/passwd

---

## User Action Edge Cases

### Timing

**Too fast:**
- Double-click submit button
- Click back button immediately
- Type and submit before validation

**Too slow:**
- Fill form, wait 30 min, submit
- Start action, let session expire
- Open page, leave for hour, interact

### Multiple actions

**Concurrent:**
- Open same page in 2 tabs
- Edit in tab 1, save in tab 2
- Log out in one tab, act in another

**Repeated:**
- Click button 10 times fast
- Submit form 5 times
- Refresh page repeatedly

### Unexpected order

**Skip steps:**
- Navigate directly to step 3 of 5
- Access protected route while logged out
- Submit without filling required fields

**Go backwards:**
- Click back button after submit
- Use browser back (not app navigation)
- Edit after finalizing

---

## Network Edge Cases

**Connection:**
- Slow connection (3G)
- Disconnected mid-action
- Intermittent connection
- Very high latency (500ms+)

**Errors:**
- 500 Internal Server Error
- 404 Not Found
- 503 Service Unavailable
- Timeout (no response)

---

## Browser/Device Edge Cases

### Browser

**Storage:**
- Cookies disabled
- Local storage full
- Private/incognito mode

**Settings:**
- JavaScript disabled
- Ad blocker active
- Browser extensions interfering

### Device

**Screen sizes:**
- Very small (320px width)
- Very large (4K monitor)
- Non-standard aspect ratio

**Performance:**
- Old/slow device
- Low memory
- CPU throttled

---

## Data State Edge Cases

**New user:**
- First login (onboarding flow)
- No data created yet
- Empty dashboard

**Active user:**
- Normal amount of data
- Some incomplete actions
- Recent activity

**Power user:**
- Lots of data (1000+ items)
- Complex setup
- Heavy usage patterns

**Inactive user:**
- Account dormant for months
- Old data format
- Deprecated features used

---

## Authentication Edge Cases

**Session:**
- Session expired mid-action
- Multiple concurrent sessions
- Session hijacking attempts

**Permissions:**
- Try to access admin route as regular user
- View another user's data
- Edit data you don't own

**Token:**
- Expired token
- Invalid token
- Missing token
- Malformed token

---

## Payment Edge Cases

**Card validation:**
- Test card: 4242 4242 4242 4242
- Declined card: 4000 0000 0000 0002
- Insufficient funds: 4000 0000 0000 9995
- Expired card
- Invalid CVV

**Billing:**
- Upgrade mid-cycle
- Downgrade mid-cycle
- Cancel with refund
- Failed payment retry

---

## Search Edge Cases

**Query:**
- Empty search
- Single character: "a"
- Very long query (500 chars)
- Special characters: *?%
- SQL injection attempt

**Results:**
- No results
- One result
- Thousands of results
- Exact match
- Partial match

---

## Real-Time Edge Cases

**Updates:**
- Data changes while user viewing
- Conflict: two users edit same item
- Delete item user is viewing
- Update item user is editing

**Notifications:**
- Single notification
- 100 notifications at once
- Notification while user typing
- Old unread notifications

---

## Mobile-Specific Edge Cases

**Gestures:**
- Swipe vs scroll
- Long press
- Pinch to zoom (if allowed)
- Pull to refresh

**Orientation:**
- Start portrait, rotate to landscape
- Rotate while form open
- Rotate during action

**Keyboard:**
- Keyboard covers input
- Auto-correct changes input
- Keyboard shortcuts (if any)

---

## Quick Edge Case Test

**10-minute edge case test:**
```
1. Leave required field empty → error?
2. Enter 1000 characters in text field → truncate or error?
3. Double-click submit button → prevents double submit?
4. Enter HTML/SQL in text field → sanitized?
5. Upload 10MB file (over limit) → clear error?
6. Go offline, try action → handles gracefully?
7. Very long item name → layout breaks?
8. Open 2 tabs, log out in one → other tab handles?
9. Enter invalid email → validates?
10. Submit form, immediately refresh → doesn't resubmit?
```