# Page Layouts

Layout templates for common SaaS pages. Each includes structure, key decisions, and common mistakes. All layouts assume a sidebar navigation context — adjust for top-nav by replacing the sidebar column with a full-width top bar.

---

### Dashboard

**Structure:**
```
┌──────────────────────────────────────────────┐
│  Page Header: "Dashboard"         [Actions ▾]│
├──────────────────────────────────────────────┤
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐        │
│  │Metric│ │Metric│ │Metric│ │Metric│        │
│  └──────┘ └──────┘ └──────┘ └──────┘        │
├──────────────────────────────────────────────┤
│  ┌─────────────────────┐ ┌────────────────┐  │
│  │                     │ │                │  │
│  │   Primary Chart /   │ │  Quick Actions │  │
│  │   Activity Feed     │ │  / Recent List │  │
│  │                     │ │                │  │
│  └─────────────────────┘ └────────────────┘  │
└──────────────────────────────────────────────┘
```

**Grid:** `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6`. Metrics row: `grid grid-cols-2 lg:grid-cols-4 gap-4`. Content area: `grid grid-cols-1 lg:grid-cols-3 gap-6` with primary content spanning `lg:col-span-2`.

**Key decisions:**
- Which 3-4 metrics to surface (pick the ones the user checks daily, not every metric available)
- Whether the primary content is a chart, activity feed, or recent items list
- What quick actions go in the secondary panel (create new, recent drafts, pinned items)
- Time range selector: default to last 7 or 30 days

**Common mistakes:**
- Cramming every metric onto the dashboard. Limit to 4-6 KPI cards max.
- No loading state for metrics — each card needs its own skeleton.
- Charts without axis labels or context for what the numbers mean.
- Dashboard that's just a list of links to other pages — it should surface data, not navigation.

---

### List / Table Page

**Structure:**
```
┌──────────────────────────────────────────────┐
│  Page Header: "Projects"      [+ New Project]│
├──────────────────────────────────────────────┤
│  [Search........]  [Status ▾] [Type ▾] [⋯]  │
├──────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────┐│
│  │ Name        │ Status  │ Date    │ Actions││
│  ├─────────────┼─────────┼─────────┼────────┤│
│  │ Project A   │ Active  │ Mar 1   │  ⋯    ││
│  │ Project B   │ Draft   │ Feb 28  │  ⋯    ││
│  │ Project C   │ Active  │ Feb 25  │  ⋯    ││
│  └──────────────────────────────────────────┘│
├──────────────────────────────────────────────┤
│  Showing 1-10 of 48       [< 1 2 3 4 5  >]  │
└──────────────────────────────────────────────┘
```

**Grid:** `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-4`. Filter bar: `flex flex-wrap items-center gap-3`. Table: full width within container.

**Key decisions:**
- Default sort column and direction (usually created date, descending)
- Which columns to show by default (5-7 max, hide less important ones behind column toggle)
- Whether rows are clickable (navigate to detail) or have inline actions only
- Bulk actions: checkbox column + sticky action bar on selection
- Search scope: which fields does the search input cover

**Common mistakes:**
- No empty state when filters produce zero results (show "No results match your filters" with clear-filters CTA)
- Pagination resets when applying a filter — keep the user on page 1 when filters change
- Missing the primary create action in the page header
- Table not sortable on any column — at minimum support sorting on the primary identifier and date

---

### Detail Page

**Structure:**
```
┌──────────────────────────────────────────────┐
│  ← Back to Projects                          │
├──────────────────────────────────────────────┤
│  Project Name                                │
│  Status badge  ·  Created Mar 1  ·  Owner    │
│                          [Edit] [Delete] [⋯] │
├──────────────────────────────────────────────┤
│  ┌─────────────────────┐ ┌────────────────┐  │
│  │                     │ │  Metadata       │  │
│  │  Primary Content    │ │  Created: ...   │  │
│  │  (description,      │ │  Updated: ...   │  │
│  │   content sections, │ │  Owner: ...     │  │
│  │   nested items)     │ │  Tags: ...      │  │
│  │                     │ │                │  │
│  └─────────────────────┘ └────────────────┘  │
└──────────────────────────────────────────────┘
```

**Grid:** `max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6`. Two-column layout: `grid grid-cols-1 lg:grid-cols-3 gap-8` with primary `lg:col-span-2`. On mobile, metadata section moves below primary content.

**Key decisions:**
- Whether metadata lives in a right sidebar or in a top header area
- Tab navigation for sub-sections (overview, activity, settings) vs single scrollable page
- Inline editing vs dedicated edit mode/page
- Related items: show inline list or link to filtered list page

**Common mistakes:**
- No breadcrumb or back link — user can't navigate up
- Action buttons (edit, delete) buried in a menu instead of visible in the header
- Detail page that's just a form — separate read view from edit view
- Long pages with no content anchoring — use sticky header or section tabs for pages with 5+ sections

---

### Settings Page

**Structure:**
```
┌──────────────────────────────────────────────┐
│  Settings                                    │
├────────────┬─────────────────────────────────┤
│            │                                 │
│  General   │  General Settings               │
│  Profile   │  ─────────────────              │
│  Team      │                                 │
│  Billing   │  [Form section 1]               │
│  Security  │                                 │
│  API       │  [Form section 2]               │
│  Danger    │                                 │
│            │  [Form section 3]               │
│            │                                 │
│            │            [Save Changes]       │
└────────────┴─────────────────────────────────┘
```

**Grid:** Full width, no max-width on outer container. Sidebar: `w-48 lg:w-56` with `space-y-1` for nav items. Content: `max-w-2xl space-y-8`. On mobile: sidebar becomes horizontal scrolling tabs at top or a select dropdown.

**Key decisions:**
- Whether each settings tab auto-saves or has a "Save" button (auto-save for toggles, save button for forms)
- Danger zone section at the bottom of the appropriate tab: red-bordered area with delete account, transfer ownership, etc.
- Whether team/billing/API get their own top-level pages or stay as settings tabs

**Common mistakes:**
- All settings on one endless scrolling page — split into logical tabs
- No confirmation when navigating away with unsaved changes
- Danger zone actions too easy to trigger — require typing confirmation for destructive actions
- Settings that take effect immediately but look like they need a save button (or vice versa)

---

### Billing Page

**Structure:**
```
┌──────────────────────────────────────────────┐
│  Billing                                     │
├──────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────┐│
│  │ Current Plan: Pro           [Change Plan]││
│  │ $49/mo · Renews Apr 10                   ││
│  └──────────────────────────────────────────┘│
├──────────────────────────────────────────────┤
│  Usage This Period                           │
│  ┌──────┐ ┌──────┐ ┌──────┐                 │
│  │ API  │ │Users │ │Store │                 │
│  │23/100│ │ 4/10 │ │2/5GB │                 │
│  └──────┘ └──────┘ └──────┘                 │
├──────────────────────────────────────────────┤
│  Payment Method                              │
│  Visa ****4242  Exp 12/27       [Update]     │
├──────────────────────────────────────────────┤
│  Invoice History                             │
│  Mar 1  │ Pro Plan  │ $49.00  │ [Download]   │
│  Feb 1  │ Pro Plan  │ $49.00  │ [Download]   │
└──────────────────────────────────────────────┘
```

**Grid:** `max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8`. Each section is a card with `p-6 border rounded-lg`. Usage meters: `grid grid-cols-2 sm:grid-cols-3 gap-4`.

**Key decisions:**
- Whether plan change is inline or opens a dedicated plan comparison page
- Usage display: progress bars vs numeric (progress bars for visual impact, use both)
- Invoice download format (PDF, accessible from within the app)
- Proration display when mid-cycle plan changes occur

**Common mistakes:**
- No visual warning when approaching usage limits — show yellow at 80%, red at 95%
- Can't download invoices — always provide downloadable PDFs
- Plan comparison not showing what the user currently has highlighted
- Cancellation flow that's a single button — provide offboarding flow with reason collection and save offers

---

### Auth Pages (Login, Signup, Forgot Password)

**Structure:**
```
┌──────────────────────────────────────────────┐
│                                              │
│              ┌────────────────┐              │
│              │     Logo       │              │
│              │                │              │
│              │  Welcome back  │              │
│              │                │              │
│              │  [Email     ]  │              │
│              │  [Password  ]  │              │
│              │                │              │
│              │  [Sign In    ] │              │
│              │                │              │
│              │  ── or ──      │              │
│              │  [Google]      │              │
│              │                │              │
│              │  Don't have    │              │
│              │  an account?   │              │
│              └────────────────┘              │
│                                              │
└──────────────────────────────────────────────┘
```

**Grid:** Full screen height: `min-h-screen flex items-center justify-center`. Card: `w-full max-w-sm p-8`. For split layouts (marketing + form): `grid grid-cols-1 lg:grid-cols-2` with full viewport height — left side is marketing content / hero image, right side is the form.

**Key decisions:**
- Social auth providers: Google is nearly universal. Add GitHub for dev tools, Apple for consumer apps.
- Split layout (marketing left, form right) vs centered card — split is better for conversion, centered is simpler to build
- Magic link vs password-based auth — magic link is easier to implement (no password reset flow)
- Whether signup requires email confirmation before access

**Common mistakes:**
- No password visibility toggle — always include the eye icon
- Forgot password link not visible — place it below the password field, right-aligned
- Social auth buttons styled inconsistently with each other
- Error messages that reveal whether an email exists in the system ("Invalid email or password" is correct, "No account found" leaks information)
- Sign up form asking for too many fields — email and password only, collect profile info after

---

### Empty / Zero-Data State

**Structure:**
```
┌──────────────────────────────────────────────┐
│  Page Header: "Projects"      [+ New Project]│
├──────────────────────────────────────────────┤
│                                              │
│                                              │
│              [  Illustration  ]              │
│                                              │
│            No projects yet                   │
│                                              │
│      Create your first project to get        │
│      started organizing your work.           │
│                                              │
│           [+ Create Project]                 │
│                                              │
│                                              │
└──────────────────────────────────────────────┘
```

**Grid:** Center the empty state content: `flex flex-col items-center justify-center py-16 text-center max-w-md mx-auto`. Icon/illustration: `h-12 w-12 text-muted-foreground mb-4`. Headline: `text-lg font-semibold`. Description: `text-sm text-muted-foreground mt-1 mb-6`. CTA button: primary variant.

**Key decisions:**
- Whether to use an illustration, icon, or emoji for the visual element (icon is safest — illustrations require design work)
- CTA should match the primary page action (same as the header button)
- For filtered-empty states: "No results match your filters" + "Clear filters" button (different from zero-data)

**Common mistakes:**
- Generic "No data" text with no guidance on what to do next
- Missing the CTA button — the empty state should reduce friction, not just acknowledge emptiness
- Same empty state for "no data yet" and "no search results" — these need different messages
- Empty state that looks broken rather than intentional — add enough visual design to make it feel considered

---

### Landing Page

**Structure:**
```
┌──────────────────────────────────────────────┐
│  Logo            Features  Pricing   [Login] │
├──────────────────────────────────────────────┤
│                                              │
│        Headline (value proposition)          │
│        Subheadline (one sentence)            │
│        [Primary CTA]   [Secondary CTA]       │
│        Hero image / screenshot               │
│                                              │
├──────────────────────────────────────────────┤
│  Social proof: logos, testimonial, stat      │
├──────────────────────────────────────────────┤
│  Feature 1    │  Feature 2    │  Feature 3   │
│  icon + text  │  icon + text  │  icon + text │
├──────────────────────────────────────────────┤
│  Detailed feature section (alternating       │
│  image left/right with text)                 │
├──────────────────────────────────────────────┤
│  Testimonials (2-3 quotes with photos)       │
├──────────────────────────────────────────────┤
│  Pricing table (plans side by side)          │
├──────────────────────────────────────────────┤
│  FAQ (accordion)                             │
├──────────────────────────────────────────────┤
│  Final CTA section (repeat primary CTA)      │
├──────────────────────────────────────────────┤
│  Footer (links, legal, social)               │
└──────────────────────────────────────────────┘
```

**Grid:** Full width, no sidebar. Each section: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24`. Hero: `text-center` or `grid grid-cols-1 lg:grid-cols-2`. Features grid: `grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8`. Section spacing: `py-16 sm:py-24` alternating with optional `bg-muted/50` backgrounds.

**Key decisions:**
- Hero layout: centered text with screenshot below, or split (text left, image right)
- Number of pricing tiers: 2-3 is optimal. Highlight the recommended plan.
- Social proof type: customer logos (B2B), testimonials (B2C), usage stats ("10,000+ users")
- Whether to include a live demo or video

**Common mistakes:**
- Headline describes the product instead of the outcome ("AI-powered project management" vs "Ship projects 2x faster")
- No CTA above the fold — primary CTA must be visible without scrolling
- Feature sections that are walls of text — use icons, visuals, and short descriptions
- Footer links to every possible page — keep it focused: product, company, legal, social

---

### Blog / Content Page

**Structure:**
```
┌──────────────────────────────────────────────┐
│  Nav                              [Login]    │
├──────────────────────────────────────────────┤
│                                              │
│  Category badge                              │
│  Article Title (h1)                          │
│  Author · Date · Read time                   │
│                                              │
│  ┌──────────────────────────────────────┐    │
│  │          Featured Image             │    │
│  └──────────────────────────────────────┘    │
│                                              │
│  Article body content                        │
│  with headings, paragraphs,                  │
│  images, and code blocks                     │
│                                              │
│  ─────────────────────────                   │
│  Author bio                                  │
│  Related articles (3 cards)                  │
│                                              │
└──────────────────────────────────────────────┘
```

**Grid:** Content column: `max-w-prose mx-auto px-4 sm:px-6` (65ch width — optimal reading width). If adding a table of contents sidebar: `grid grid-cols-1 lg:grid-cols-[1fr_250px] max-w-5xl mx-auto gap-8` with sticky ToC.

**Key decisions:**
- Table of contents: yes for articles with 4+ headings, sticky sidebar on desktop, hidden or collapsible on mobile
- Related articles: manual selection or auto-generated by tag/category
- Whether to include reading progress bar at top
- Comments section: usually not worth building — link to Twitter/social discussion instead

**Common mistakes:**
- Content column too wide — text lines beyond 75 characters are hard to read
- No heading hierarchy — jumping from h1 to h4
- Images without proper aspect ratio containers causing layout shift
- Missing meta tags (og:title, og:description, og:image) for social sharing
