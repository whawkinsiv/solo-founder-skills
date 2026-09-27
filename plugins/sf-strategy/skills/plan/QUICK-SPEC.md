# Quick Feature Spec Template

Use this for single features, iterations, or additions to existing products (10-15 minutes).

## Complete Template

```markdown
# [Feature Name]

## What Users Will Do
[2-3 sentences describing user actions and outcomes]

## What It Looks Like
[Reference app OR screenshot OR detailed description]

## How It Behaves

### Happy Path
1. [Step]
2. [Step]
3. [Step]

### Edge Cases
- **[Scenario]:** [Response shown to user]
- **[Scenario]:** [Response shown to user]
- **[Scenario]:** [Response shown to user]

## Out of Scope
- [Thing you're NOT building]
- [Feature to add later]

## Done When
- [ ] Happy path works end-to-end
- [ ] Edge cases handled
- [ ] Matches design reference
- [ ] Works on mobile
```

---

## Example 1: User Authentication

```markdown
# User Authentication

## What Users Will Do
Users sign up with email/password, receive confirmation email, and log in to see 
their dashboard. They can reset forgotten passwords via email link.

## What It Looks Like
Login form like Linear - minimal, centered card with email/password fields and 
one blue button. Forgot password link below button.

## How It Behaves

### Happy Path
1. User clicks "Sign Up"
2. Enters email + password
3. Sees "Check your email" message
4. Clicks confirmation link in email
5. Lands on dashboard with "Get Started" prompt

### Edge Cases
- **Email exists:** "That email is registered. Try logging in?"
- **Weak password:** "Password needs 8+ characters with one number"
- **Link expired:** "This link expired. Request a new one?"
- **Wrong credentials:** "Email or password incorrect"

## Out of Scope
- Social login (add in v2)
- Two-factor authentication
- Password strength meter

## Done When
- [ ] Happy path works end-to-end
- [ ] All edge cases handled
- [ ] Matches Linear-style design
- [ ] Works on mobile
```

---

## Example 2: Payment Upgrade Flow

```markdown
# Payment Upgrade Flow

## What Users Will Do
Users can upgrade from free to paid ($29/month) by entering credit card info. They 
get email receipt and see 'Pro' badge in dashboard. They can cancel anytime and 
revert to free tier.

## What It Looks Like
Centered card 500px wide. Header "Upgrade to Pro", feature list with checkmarks, 
Stripe payment form, total shown as "$29/month", blue "Start Pro Plan" button.

## How It Behaves

### Happy Path
1. User clicks "Upgrade" in dashboard
2. Sees feature comparison and pricing
3. Enters credit card via Stripe
4. Sees "Success! Welcome to Pro" message
5. Dashboard shows Pro badge
6. Receives email receipt

### Edge Cases
- **Card declined:** "Payment failed. Please try another card."
- **Already Pro:** Redirect to billing page with "You're already Pro"
- **Payment processing:** Show spinner, "Processing payment..."
- **Cancel flow:** "Cancel Pro? You'll lose [features]. Keep Pro / Cancel Plan"

## Out of Scope
- Annual billing discount
- Team/multi-user plans
- Proration for mid-month cancellations

## Done When
- [ ] Happy path works end-to-end
- [ ] Card decline handled gracefully
- [ ] Email receipt sent
- [ ] Cancel flow works
- [ ] Works on mobile
```

---

## Example 3: Export Data Feature

```markdown
# Export Data Feature

## What Users Will Do
Users can export their data as CSV or JSON file. Export includes all records with 
timestamps. Large exports (1000+ records) get emailed as download link instead of 
immediate download.

## What It Looks Like
Export button in Settings page. Clicking shows modal: "Export Format: CSV / JSON" 
radio buttons, "Include archived items" checkbox, blue "Export" button.

## How It Behaves

### Happy Path
1. User clicks "Export Data" in Settings
2. Selects format (CSV or JSON)
3. Clicks "Export"
4. Small dataset (<1000 records): File downloads immediately
5. Large dataset (1000+ records): "Check your email for download link"

### Edge Cases
- **No data:** "You don't have any data to export yet"
- **In progress:** "Previous export still processing. Try again in 2 minutes."
- **Email failed:** Show download link directly in UI as backup

## Out of Scope
- Filtered exports (specific date ranges)
- Scheduled/recurring exports
- Export to Google Sheets/Excel directly

## Done When
- [ ] Both CSV and JSON export work
- [ ] Email delivery works for large exports
- [ ] No data case handled
- [ ] Works on mobile
```

---

## Tips for Writing Quick Specs

**What Users Will Do section:**
- Focus on outcomes, not implementation
- 2-3 sentences max
- Answer: "What can users accomplish with this?"

**What It Looks Like section:**
- Reference existing apps when possible (faster than describing)
- If describing: specific measurements (400px wide), fonts (Inter 24px), colors (blue button)
- Screenshots work better than words

**Happy Path section:**
- 3-5 steps only
- Start with user action, end with visible outcome
- Use active voice: "User clicks" not "Button is clicked"

**Edge Cases section:**
- Focus on what USER SEES, not technical errors
- 2-4 most common failure scenarios
- Format: **[What went wrong]:** "[User-friendly message]"

**Out of Scope section:**
- Critical for preventing scope creep
- List tempting features you're explicitly NOT building
- Helps AI stay focused on core functionality
