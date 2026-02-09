# Laws of UX Reference

Collection of UX principles from https://lawsofux.com/ adapted for SaaS founders building with AI tools.

---

## Jakob's Law

**Users spend most of their time on other sites. They expect your site to work the same way.**

### What This Means
Users transfer expectations from familiar products to yours. If they've used Stripe, Notion, or Linear, they expect similar patterns.

### How to Apply
- Copy navigation patterns from popular apps
- Don't reinvent form layouts, login flows, or settings pages
- When changing patterns, allow users to preview before committing

### Examples
**Login forms:** Email field, password field, "Forgot password?" link - every login looks the same for a reason

**Dashboard navigation:** Logo top-left, search top-right, user profile top-right corner

**Settings pages:** Tabs on left side, content on right - same pattern as Slack, Linear, Notion

### Tell AI Tools
"Make the login form look like Linear - minimal, centered, email/password/button"

---

## Hick's Law

**The time to make a decision increases with the number and complexity of choices.**

### What This Means
More options = longer decisions = user paralysis. Every extra choice adds cognitive load.

### How to Apply
- Limit navigation to 5-7 top-level items
- Show 3-5 pricing tiers, not 8
- Hide advanced features until user is ready
- Use progressive disclosure

### Examples
**Bad:** 12 buttons on a page  
**Good:** 1 primary action, 2-3 secondary actions

**Bad:** Settings page with 50 options visible  
**Good:** Settings grouped into 5-7 categories

### Tell AI Tools
"Show only 3 pricing tiers: Free, Pro, Enterprise. Hide advanced features in a collapsible section."

---

## Fitts's Law

**The time to click a target depends on its size and distance from the cursor.**

### What This Means
Bigger, closer targets are faster to click. Small buttons far from the cursor slow users down.

### How to Apply
- Make primary buttons large (at least 44x44px)
- Place important actions near where users look/click
- Put related actions close together
- On mobile: buttons should be easy to tap with thumb

### Examples
**Primary action button:** Large, centered, high contrast  
**Secondary actions:** Smaller, less prominent

**Mobile navigation:** Bottom bar (easy to reach with thumb)  
**Delete button:** Smaller, far from common actions

### Tell AI Tools
"Make the 'Start Trial' button 200px wide and center it below the pricing. Make 'Learn More' links smaller and gray."

---

## Miller's Law

**The average person can keep 7 (±2) items in working memory.**

### What This Means
People struggle when presented with more than 7 items at once. Chunk information into groups of 5-7.

### How to Apply
- Navigation: 5-7 top-level items maximum
- Forms: Group fields into sections of 5-7
- Lists: Show 7-10 items per page
- Phone numbers: Already chunked (555-1234, not 5551234)

### Examples
**Navigation:** Dashboard, Projects, Team, Settings, Billing (5 items, not 15)

**Forms:** Break long forms into steps with 5-7 fields each

**Pricing table:** Show 3-5 tiers, not 10

### Tell AI Tools
"Group the form into 3 sections: Personal Info (5 fields), Company Info (4 fields), Preferences (3 fields)"

---

## Aesthetic-Usability Effect

**Users perceive aesthetically pleasing design as more usable.**

### What This Means
Beautiful interfaces feel easier to use, even when functionality is identical. Polish matters.

### How to Apply
- Use consistent spacing and alignment
- Choose a professional font (Inter, SF Pro)
- Limit colors to 2-3 (brand color + grays)
- Add subtle shadows and borders
- Ensure visual hierarchy (headings, body text, captions)

### Examples
**Good spacing:** Consistent padding (16px, 24px, 32px)  
**Color palette:** One primary color + 3 shades of gray  
**Typography:** 2-3 font sizes with clear hierarchy

### Tell AI Tools
"Use Inter font throughout. Primary buttons use #0070F3 blue. All cards have subtle shadow (0 1px 3px rgba(0,0,0,0.1))"

---

## Peak-End Rule

**Users judge an experience by its peak moment and final moment.**

### What This Means
First and last impressions matter most. The middle is less memorable.

### How to Apply
- Nail the onboarding (first impression)
- Make signup/checkout smooth (peak moment)
- End with success message (final impression)
- Make errors less painful with helpful messages

### Examples
**Onboarding:** Welcoming, clear next steps  
**Success message:** Celebrate completing signup  
**Error handling:** Friendly, helpful, not technical jargon

### Tell AI Tools
"After user signs up, show a success message with confetti animation and clear 'Get Started' button"

---

## Law of Proximity

**Objects near each other are perceived as related.**

### What This Means
Grouping related items together makes interfaces easier to scan and understand.

### How to Apply
- Group related form fields together
- Put action buttons near the content they affect
- Use whitespace to separate unrelated sections
- Keep labels close to their inputs

### Examples
**Form layout:** Group "First Name" and "Last Name" close together, separate from "Email"

**Card design:** Keep title, description, and action button grouped with minimal space between them

**Navigation:** Group related menu items together

### Tell AI Tools
"Group billing info fields together with 8px spacing between them. Add 32px spacing before the next section"

---

## Cognitive Load

**The amount of mental effort needed to use an interface.**

### What This Means
Every element on screen requires mental processing. Reduce load by removing unnecessary elements.

### How to Apply
- Show only essential information
- Use progressive disclosure (basic → advanced)
- Provide clear defaults
- Use familiar patterns
- Minimize jargon

### Examples
**Dashboard:** Show 4-6 key metrics, hide details until clicked

**Settings:** Show common options first, hide advanced in collapsible section

**Forms:** Use smart defaults, show only required fields

### Tell AI Tools
"Show only 4 metrics on the main dashboard. Put detailed analytics in a separate 'Reports' section users can navigate to"

---

## Serial Position Effect

**Users best remember the first and last items in a list.**

### What This Means
Items in the middle get forgotten. Put important things at the start or end.

### How to Apply
- Put key features at top or bottom of pricing table
- Most important navigation items go first
- Critical info in first or last paragraph
- Put primary action last in a flow

### Examples
**Pricing table:** Best features at top, most popular feature at bottom

**Navigation:** Most used items first (Dashboard, Projects) or last (Settings, Logout)

**Multi-step form:** Most important question first or last

### Tell AI Tools
"In the pricing table, put the most important feature ('Unlimited projects') at the top of the feature list"

---

## Tesler's Law (Law of Conservation of Complexity)

**For any system, there is a certain amount of complexity that cannot be reduced.**

### What This Means
You can't eliminate complexity, only move it. Either users deal with it or the system does.

### How to Apply
- Make the system handle complexity when possible
- Provide smart defaults
- Hide complexity behind "Advanced" sections
- Guide users through complex tasks step-by-step

### Examples
**Bad:** Make users configure 50 settings  
**Good:** Set smart defaults, let users change if needed

**Bad:** Show all database options to non-technical users  
**Good:** Provide preset configurations (Small/Medium/Large)

### Tell AI Tools
"Provide 3 preset configurations: Starter, Growth, Enterprise. Put custom configuration in an 'Advanced' section"

---

## Choice Overload (Paradox of Choice)

**Too many options makes decisions harder and less satisfying.**

### What This Means
More choices seems better but leads to decision paralysis and regret.

### How to Apply
- Offer 3-5 options maximum per decision
- Provide clear recommendation
- Use default selections
- Allow customization after initial simple choice

### Examples
**Pricing:** 3 tiers (Free, Pro, Enterprise) not 7

**Onboarding:** Ask 3-4 key questions, not 20

**Feature flags:** Show most popular features, hide edge cases

### Tell AI Tools
"Show 3 pricing plans with 'Most Popular' badge on the middle tier. Put enterprise features in a separate 'Contact Sales' option"

---

## Von Restorff Effect (Isolation Effect)

**When multiple similar items are present, the one that differs is most likely to be remembered.**

### What This Means
Make important things stand out by making them different.

### How to Apply
- Highlight primary action with distinct color
- Mark "Most Popular" plan differently
- Use icons or badges to draw attention
- Make important notifications visually distinct

### Examples
**Buttons:** Blue primary button among gray secondary buttons

**Pricing:** "Most Popular" plan has colored border and badge

**Forms:** Required fields marked with red asterisk

### Tell AI Tools
"Make the 'Start Trial' button blue and prominent. All other buttons should be gray and smaller"

---

## Applying Multiple Laws Together

Most interfaces benefit from combining several laws:

**Login Page Example:**
- Jakob's Law: Email/password layout everyone knows
- Fitts's Law: Large "Sign In" button
- Aesthetic-Usability: Clean, centered design with good spacing
- Cognitive Load: Only email and password visible, "Forgot password?" subtle

**Dashboard Example:**
- Miller's Law: Show 6 key metrics maximum
- Law of Proximity: Group related metrics together
- Aesthetic-Usability: Consistent card design with shadows
- Serial Position: Most important metric top-left, second most important top-right

**Tell AI:**
"Create a dashboard with 6 metric cards following the Linear design pattern - clean, minimal, good spacing between cards"

---

## Quick Reference: Most Important Laws for SaaS

1. **Jakob's Law** - Copy what works, don't reinvent patterns
2. **Hick's Law** - Limit choices to 3-5 options
3. **Fitts's Law** - Make important buttons big and close
4. **Miller's Law** - Show 5-7 items maximum
5. **Aesthetic-Usability** - Polish makes things feel more usable

Apply these 5 laws to every design decision and you'll have 80% of good UX covered.
