# Testing Scenarios

Common scenarios to test for SaaS applications.

---

## Authentication Scenarios

### Signup Flow
```
Happy Path:
1. Enter valid email and password
2. Click "Sign Up"
3. See "Check your email" message
4. Click link in email
5. Redirected to dashboard

Edge Cases:
- Email already registered: "Email already in use"
- Weak password: "Password must be 8+ characters"
- Invalid email format: "Enter valid email"
- Email link expired: "Link expired. Request new one"
- Email link already used: "Already confirmed. Log in"
```

### Login Flow
```
Happy Path:
1. Enter correct email and password
2. Click "Log In"
3. Redirected to dashboard

Edge Cases:
- Wrong password: "Invalid email or password"
- Account doesn't exist: "Invalid email or password"
- Too many attempts: "Too many attempts. Try again in 15 minutes"
- Session expired: Redirect to login with message
```

### Password Reset
```
Happy Path:
1. Click "Forgot Password"
2. Enter email
3. Click link in email
4. Enter new password
5. See "Password updated" message
6. Can log in with new password

Edge Cases:
- Email not found: "If email exists, we sent a link"
- Reset link expired: "Link expired. Request new one"
- Passwords don't match: "Passwords must match"
- Weak new password: "Password requirements not met"
```

---

## Form Scenarios

### Contact Form
```
Happy Path:
1. Fill in name, email, message
2. Click "Send"
3. See "Message sent!" confirmation
4. Form clears

Edge Cases:
- Missing required field: "This field is required"
- Invalid email: "Enter valid email address"
- Message too short: "Message must be at least 10 characters"
- Submit while loading: Button disabled, show spinner
- Network error: "Could not send. Try again"
```

### Profile Update
```
Happy Path:
1. Change name
2. Upload new photo
3. Click "Save"
4. See "Profile updated!" message
5. Changes reflected immediately

Edge Cases:
- No changes made: "No changes to save"
- Image too large: "Image must be under 5MB"
- Invalid image type: "Only JPG and PNG allowed"
- Name too long: "Max 50 characters"
- Save during upload: Wait for upload, then save
```

---

## Data Display Scenarios

### List/Table View
```
Happy Path:
1. Load page
2. See list of items
3. Click item to view details
4. Navigate between pages

Edge Cases:
- No items: "No items yet. Create your first one!"
- Loading: Show skeleton/spinner
- Error loading: "Could not load. Try refreshing"
- Very long list: Paginate (50 items/page)
- Search with no results: "No matches found"
```

### Dashboard
```
Happy Path:
1. Load dashboard
2. See metrics update
3. Charts render correctly
4. Data is current

Edge Cases:
- No data yet: "Getting started? Here's what to do"
- Data still loading: Show skeleton cards
- API fails: Show cached data + "Using cached data"
- Very large numbers: Format (1.2M not 1200000)
- Negative values: Handle gracefully (red color, parentheses)
```

---

## Payment Scenarios

### Checkout
```
Happy Path:
1. Select plan
2. Enter card details (Stripe)
3. Click "Subscribe"
4. See success message
5. Receive email receipt
6. Access pro features

Edge Cases:
- Card declined: "Payment failed. Try different card"
- Missing card details: "Enter card information"
- Invalid card: "Invalid card number"
- Expired card: "Card is expired"
- Network timeout: "Payment processing. Check email for confirmation"
```

### Subscription Management
```
Happy Path:
1. View current plan
2. Change to different plan
3. Confirm change
4. See updated features
5. Receive confirmation email

Edge Cases:
- Downgrade with data loss: "Downgrading will remove X. Continue?"
- Cancel subscription: "Cancel subscription? Access until [date]"
- Reactivate cancelled: "Reactivate subscription?"
- Payment method failed: "Update payment method to continue"
```

---

## File Upload Scenarios

### Single File Upload
```
Happy Path:
1. Click "Upload"
2. Select file
3. See progress bar
4. File uploads successfully
5. See uploaded file

Edge Cases:
- File too large: "Max 5MB"
- Wrong file type: "Only PDF and images allowed"
- Network error during upload: "Upload failed. Try again"
- File with same name exists: "File already exists. Replace?"
- Cancel during upload: Stop upload, remove partial
```

### Multiple Files
```
Happy Path:
1. Select multiple files
2. See all files listed
3. Upload starts automatically
4. Progress shown for each
5. All succeed

Edge Cases:
- Some files invalid: "3 files uploaded, 2 failed"
- Mixed success/failure: Show status per file
- Very slow connection: Show time remaining estimate
- Upload folder: "Folders not supported"
```

---

## Search Scenarios

### Basic Search
```
Happy Path:
1. Enter search term
2. Results appear instantly
3. Click result to view
4. Highlight matching text

Edge Cases:
- No results: "No matches for 'term'. Try different keywords"
- Search while typing: Debounce (wait 300ms)
- Special characters: Handle gracefully
- Very long search term: Truncate, still search
- Empty search: Show all items or recent
```

### Advanced Search
```
Happy Path:
1. Enter search with filters
2. Results match all criteria
3. Clear filters individually
4. Results update

Edge Cases:
- Conflicting filters: "No items match all filters"
- Invalid date range: "End date must be after start date"
- Too many results: "500+ results. Narrow your search"
- Filters with no results: "0 results. Try removing filters"
```

---

## Navigation Scenarios

### Multi-Step Form
```
Happy Path:
1. Complete step 1
2. Click "Next"
3. Complete step 2
4. Click "Next"
5. Review and submit
6. See confirmation

Edge Cases:
- Click "Next" without completing: "Complete required fields"
- Click "Back": Previous data preserved
- Refresh page mid-flow: Resume where left off
- Abandon and return: Resume or start over?
- Invalid step: Jump directly to step 3 in URL
```

### Tabs
```
Happy Path:
1. Click tab
2. Content switches
3. Tab stays active on refresh
4. Deep link to tab works

Edge Cases:
- Unsaved changes: "You have unsaved changes. Leave?"
- Loading new tab: Show loading state
- Tab with error: Show error, don't break all tabs
- Too many tabs: Horizontal scroll or dropdown
```

---

## Real-Time Scenarios

### Live Updates
```
Happy Path:
1. Data changes on server
2. UI updates automatically
3. Smooth transition, no flicker
4. User sees latest data

Edge Cases:
- User editing during update: Don't overwrite
- Conflict (2 users edit): Show conflict resolution
- Connection lost: Show "Offline" banner
- Reconnect: Sync changes, show what happened
```

### Notifications
```
Happy Path:
1. Event occurs
2. Notification appears
3. Click to view details
4. Mark as read

Edge Cases:
- Many notifications: Group similar ones
- Notification while typing: Don't interrupt
- Old notifications: Auto-mark read after 7 days
- Disabled notifications: Store, show in app only
```

---

## Error Recovery Scenarios

### Network Failure
```
Test:
1. Start action
2. Disable network (DevTools)
3. Action fails
4. Re-enable network
5. Retry action

Expected:
- Clear error message
- Easy retry (button or auto-retry)
- Don't lose user's data
- Recover gracefully when back online
```

### Session Expiry
```
Test:
1. Log in
2. Wait 30 minutes (or change system time)
3. Try to perform action
4. Session expired

Expected:
- Redirect to login
- Show "Session expired. Please log in"
- After re-login, return to where they were
- Don't lose unsaved data if possible
```

---

## Mobile-Specific Scenarios

### Portrait/Landscape
```
Test:
1. Open app in portrait
2. Rotate to landscape
3. Rotate back to portrait

Expected:
- Layout adapts smoothly
- No content cut off
- Maintain scroll position
- Inputs don't lose focus
```

### Touch Interactions
```
Test:
1. Tap buttons (not click)
2. Swipe to scroll
3. Pinch to zoom (if allowed)
4. Long press (if used)

Expected:
- Tap targets 44x44px minimum
- No hover states (they stick)
- Smooth scrolling
- No accidental taps
```

---

## Accessibility Scenarios

### Keyboard Navigation
```
Test:
1. Use only Tab key
2. Navigate through forms
3. Submit with Enter
4. Escape closes modals

Expected:
- All interactive elements reachable
- Visible focus indicator
- Logical tab order
- Shortcuts work
```

### Screen Reader
```
Test (with VoiceOver/NVDA):
1. Navigate page with screen reader
2. Forms are labeled
3. Buttons are described
4. Images have alt text

Expected:
- Content makes sense
- No "button button button"
- Form errors announced
- Skip links available
```

---

## Quick Scenario Checklist

**Before every deploy:**
```
- [ ] Sign up and log in
- [ ] Complete main user flow
- [ ] Submit a form (valid and invalid)
- [ ] Upload a file
- [ ] Search for something
- [ ] View list/table
- [ ] Edit something and save
- [ ] Delete something
- [ ] Check mobile layout
- [ ] Try in Safari
```