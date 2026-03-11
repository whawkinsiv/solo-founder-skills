---
name: brand-identity-generator
description: "Use this skill when the user needs to create a visual brand identity for their product. Generates a comprehensive BRAND-IDENTITY.md file for the project root. Covers colors, typography, spacing, components, accessibility, and responsive design — with no gaps for AI to fill with generic defaults."
---

# Brand Identity Generator

Generate a complete `BRAND-IDENTITY.md` file for the user's project root — a single reference document that specifies every visual decision so AI tools never guess.

**Two modes:**
- **Guided discovery** (default) — Ask one question, propose a full identity, refine from reactions. The user never needs design vocabulary.
- **Expert shortcut** — Detect when the user already provides specific design tokens (hex codes, font names, spacing values). Acknowledge what they've specified, fill gaps with smart defaults, skip discovery.

The output is a project-level reference file, not a skill. Once generated, any AI tool (Claude Code, Lovable, Cursor, Replit) can read `BRAND-IDENTITY.md` and build consistent UI without repeated instructions.

> Logo guidance, decision frameworks, and common branding mistakes are included at the end.

---

## Discovery Process

**Core principle: The user should never need to use design vocabulary. They react to your proposals. You do the heavy lifting.**

### Default Path (Guided Discovery)

**Step 1 — Ask ONE question:**

> "What are you building and who is it for?"

That's it. One question. Do not ask about colors, fonts, or design preferences.

**Step 2 — Select reference brands:**

Based on their answer, select the 1-2 closest reference brands from the Reference Brand Library below. Use the "Best for" field to match.

**Step 3 — Propose a complete identity in plain English:**

Write a human-readable recommendation. Talk about feeling, not specs. Example tone:

> "Your users are developers who'll have this open all day. Products that succeed in this space — like Linear and GitHub — use calm, minimal aesthetics because your users stare at this 8 hours a day. I'd go with a dark-compatible palette built around a single cool accent, tight spacing so information density is high, and geometric type that feels fast. Here's what I'd recommend and why..."

Then present a summary covering:
- Overall feel in plain words
- Which reference brands you're drawing from and why
- Color direction (warm/cool, light/dark, accent character)
- Typography character (not font names — "clean and precise" vs "warm and readable")
- Density and spacing feel
- Component personality (sharp and fast vs soft and friendly)

Do NOT present the full 12-section spec yet. Keep it conversational.

**Step 4 — User reacts:**

They might say things like:
- "Love it"
- "Warmer"
- "I hate green"
- "More like Notion"
- "Can we make it feel more premium?"
- "Less corporate"

Adjust and re-propose. This loop usually takes 1-3 rounds.

**Step 5 — Generate the full BRAND-IDENTITY.md:**

Once the user approves, generate the complete output using the Output Template below. Write it to the project root as `BRAND-IDENTITY.md`.

### Expert Path

Detect when the user provides specific design tokens — hex codes, font names, radius values, spacing scales. Signs of an expert:
- They paste CSS custom properties or Tailwind config
- They name specific fonts ("Inter for headings, Source Sans for body")
- They provide hex codes
- They reference specific component libraries

When detected:
1. Acknowledge exactly what they've specified
2. Fill every gap with smart defaults that complement their choices
3. Skip the discovery conversation
4. Generate the full BRAND-IDENTITY.md
5. Still apply ALL enforced best practices (accessibility, responsive, etc.)

---

## Reference Brand Library

25 brands across 7 categories. Use the "Feel" to describe brands to users. Use the "Design DNA" internally to derive specific values.

### Minimal / Precise

**Stripe**
- Feel: Precise, confident, no wasted space
- Best for: Financial tools, APIs, B2B platforms
- Design DNA: Cool temperature | Moderate spacing | Moderate radius | Subtle shadows | Geometric type | Medium weight | High contrast

**Linear**
- Feel: Fast, quiet, stays out of your way
- Best for: Dev tools, productivity apps, task management
- Design DNA: Cool temperature | Moderate spacing | Moderate radius | Minimal shadows | Geometric type | Light weight | High contrast

**Vercel**
- Feel: Bold, dark, futuristic
- Best for: Technical platforms, dev tools, infrastructure
- Design DNA: Cool temperature | Moderate spacing | Sharp radius | No shadows | Geometric type | Heavy weight | High contrast

**Superhuman**
- Feel: Luxurious, dense, keyboard-driven
- Best for: Premium productivity, power-user tools
- Design DNA: Cool temperature | Dense spacing | Moderate radius | Subtle shadows | Geometric type | Medium weight | High contrast

### Warm / Approachable

**Notion**
- Feel: Warm, inviting, like a blank notebook
- Best for: Creative tools, knowledge work, wikis
- Design DNA: Warm temperature | Spacious spacing | Moderate radius | Subtle shadows | Humanist type | Light weight | Moderate contrast

**Basecamp**
- Feel: Honest, unpretentious, handmade feel
- Best for: Small business tools, project management
- Design DNA: Warm temperature | Spacious spacing | Rounded radius | No shadows | Humanist type | Medium weight | Moderate contrast

**Mailchimp**
- Feel: Quirky, fun, doesn't take itself too seriously
- Best for: Small business marketing, email tools
- Design DNA: Warm temperature | Spacious spacing | Rounded radius | Subtle shadows | Humanist type | Medium weight | Moderate contrast

**Canva**
- Feel: Bright, encouraging, "you can do this"
- Best for: Creative tools for non-designers, visual editors
- Design DNA: Warm temperature | Moderate spacing | Rounded radius | Subtle shadows | Geometric type | Medium weight | High contrast

### Collaborative / Social

**Slack**
- Feel: Friendly, colorful, energetic
- Best for: Team communication, workplace tools
- Design DNA: Warm temperature | Moderate spacing | Rounded radius | Subtle shadows | Humanist type | Medium weight | High contrast

**Figma**
- Feel: Playful, creative, multiplayer
- Best for: Design collaboration, real-time editing
- Design DNA: Neutral temperature | Moderate spacing | Rounded radius | Subtle shadows | Geometric type | Medium weight | High contrast

**Loom**
- Feel: Personal, casual, lightweight
- Best for: Async video, screen recording, communication
- Design DNA: Warm temperature | Spacious spacing | Rounded radius | Moderate shadows | Humanist type | Light weight | Moderate contrast

**Discord**
- Feel: Bold, youthful, expressive
- Best for: Community platforms, social features, gaming
- Design DNA: Cool temperature | Moderate spacing | Rounded radius | Moderate shadows | Geometric type | Heavy weight | High contrast

### Trust / Authority

**Plaid**
- Feel: Trustworthy, institutional, safe
- Best for: Fintech infrastructure, banking integrations
- Design DNA: Cool temperature | Moderate spacing | Moderate radius | No shadows | Geometric type | Medium weight | High contrast

**Gusto**
- Feel: Approachable authority, grown-up but not stuffy
- Best for: HR, payroll, compliance tools
- Design DNA: Warm temperature | Spacious spacing | Rounded radius | Subtle shadows | Humanist type | Medium weight | Moderate contrast

**Mercury**
- Feel: Sleek, premium, quietly confident
- Best for: Business banking, financial dashboards
- Design DNA: Cool temperature | Spacious spacing | Moderate radius | Subtle shadows | Geometric type | Light weight | High contrast

**Wise**
- Feel: Transparent, clean, no-nonsense
- Best for: International finance, money transfer, transparent pricing
- Design DNA: Cool temperature | Spacious spacing | Moderate radius | No shadows | Geometric type | Light weight | High contrast

### Calm / Wellness

**Calm**
- Feel: Soft, spacious, like a deep breath
- Best for: Meditation, wellness, self-care
- Design DNA: Warm temperature | Spacious spacing | Rounded radius | No shadows | Humanist type | Light weight | Low contrast

**Headspace**
- Feel: Warm, illustrated, gentle
- Best for: Mental health, habit tracking, guided experiences
- Design DNA: Warm temperature | Spacious spacing | Pill radius | No shadows | Geometric type | Medium weight | Low contrast

**Apple Health**
- Feel: Clinical but friendly, data-forward
- Best for: Health, fitness tracking, medical
- Design DNA: Neutral temperature | Moderate spacing | Rounded radius | No shadows | Geometric type | Light weight | Moderate contrast

### Bold / Consumer

**Spotify**
- Feel: Dark, vibrant, high-energy
- Best for: Entertainment, media, content platforms
- Design DNA: Cool temperature | Moderate spacing | Pill radius | No shadows | Geometric type | Heavy weight | High contrast

**Duolingo**
- Feel: Playful, cartoonish, addictive
- Best for: Education, gamified experiences, learning
- Design DNA: Warm temperature | Spacious spacing | Rounded radius | Moderate shadows | Geometric type | Heavy weight | High contrast

**Robinhood**
- Feel: Simple, green, "investing is easy"
- Best for: Consumer fintech, simplified complex tools
- Design DNA: Neutral temperature | Spacious spacing | Moderate radius | No shadows | Geometric type | Light weight | Moderate contrast

### Data / Dashboard

**Datadog**
- Feel: Dense, dark, information-rich
- Best for: Monitoring, infrastructure, observability
- Design DNA: Cool temperature | Dense spacing | Sharp radius | No shadows | Monospace-accented type | Medium weight | Moderate contrast

**Mixpanel**
- Feel: Clean data viz, chart-forward
- Best for: Analytics, reporting, metrics dashboards
- Design DNA: Cool temperature | Moderate spacing | Moderate radius | Subtle shadows | Geometric type | Light weight | Moderate contrast

**Airtable**
- Feel: Colorful, organized, approachable complexity
- Best for: Structured data, spreadsheet-like tools, databases
- Design DNA: Warm temperature | Moderate spacing | Rounded radius | Subtle shadows | Geometric type | Medium weight | High contrast

---

## Output Template

This is the exact structure for the generated `BRAND-IDENTITY.md`. Every field must be filled — no optional sections, no "TBD," no placeholders. Every gap is an invitation for AI to fill with generic defaults. Leave no gaps.

````markdown
# Brand Identity — [Product Name]

> Generated by brand-identity-generator. This file is the single source of truth for all visual decisions.
> Every AI tool building UI for this project should read this file first.

---

## 1. Brand Context

- **Product:** [What it is — one sentence]
- **Audience:** [Who uses it, in what context, how often, on what devices]
- **Feel:** [Plain-English feeling — 1-2 sentences]
- **Reference brands:** [1-2 brands] — [what to take from each, specifically]

---

## 2. Colors

### Primary
| State | Hex | Usage |
|-------|-----|-------|
| Default | #XXXXXX | Primary buttons, links, active indicators |
| Hover | #XXXXXX | Darkened/lightened on hover |
| Active | #XXXXXX | While being pressed |
| Disabled | #XXXXXX | Disabled primary elements (pair with opacity 0.5) |

### Secondary Accent
| State | Hex | Usage |
|-------|-----|-------|
| Default | #XXXXXX | Secondary buttons, accent elements |
| Hover | #XXXXXX | Hover state |
| Active | #XXXXXX | Active/pressed state |
| Disabled | #XXXXXX | Disabled state |

### Neutral Scale
| Shade | Hex | Usage |
|-------|-----|-------|
| 50 | #XXXXXX | Page backgrounds, subtle fills |
| 100 | #XXXXXX | Card backgrounds, hover states on white |
| 150 | #XXXXXX | Dividers on light backgrounds |
| 200 | #XXXXXX | Input borders, secondary dividers |
| 300 | #XXXXXX | Disabled text, placeholder text |
| 400 | #XXXXXX | Icon default color, helper text |
| 500 | #XXXXXX | Secondary text, labels |
| 600 | #XXXXXX | Body text on light backgrounds |
| 700 | #XXXXXX | Strong text, emphasis |
| 800 | #XXXXXX | Headings |
| 900 | #XXXXXX | Primary text, highest contrast |
| 950 | #XXXXXX | Near-black, use sparingly |

### Semantic Colors
| Role | Text | Background | Border |
|------|------|------------|--------|
| Success | #XXXXXX | #XXXXXX | #XXXXXX |
| Warning | #XXXXXX | #XXXXXX | #XXXXXX |
| Error | #XXXXXX | #XXXXXX | #XXXXXX |
| Info | #XXXXXX | #XXXXXX | #XXXXXX |

### Surface Colors
| Surface | Hex | Usage |
|---------|-----|-------|
| Page background | #XXXXXX | `<body>` background |
| Card background | #XXXXXX | Card, panel, popover backgrounds |
| Elevated surface | #XXXXXX | Dropdowns, tooltips, floating elements |
| Overlay backdrop | rgba(X,X,X,0.X) | Behind modals and drawers |

### Dark Mode

[Either provide a full mapping for dark mode:]

| Light token | Dark equivalent |
|-------------|-----------------|
| Page background #XXXXXX | #XXXXXX |
| Card background #XXXXXX | #XXXXXX |
| Primary text #XXXXXX | #XXXXXX |
| Secondary text #XXXXXX | #XXXXXX |
| Border #XXXXXX | #XXXXXX |
| Primary #XXXXXX | #XXXXXX (adjust for dark bg contrast) |
[...complete mapping for every token above]

[Or explicitly opt out:]

> Dark mode not supported. Do not generate dark mode variants.

---

## 3. Typography

### Font Stack
- **Headings:** [Font Name], [fallback stack]
- **Body:** [Font Name], [fallback stack]
- **Monospace:** [Font Name], [fallback stack] *(if applicable — omit if no code/data display)*

### Type Scale
| Role | Size (rem / px) | Weight | Line Height | Letter Spacing |
|------|-----------------|--------|-------------|----------------|
| Display | X.Xrem / XXpx | XXX | 1.1 | -0.02em |
| H1 | X.Xrem / XXpx | XXX | 1.2 | -0.01em |
| H2 | X.Xrem / XXpx | XXX | 1.25 | -0.005em |
| H3 | X.Xrem / XXpx | XXX | 1.3 | 0 |
| H4 | X.Xrem / XXpx | XXX | 1.35 | 0 |
| Body Large | X.Xrem / XXpx | XXX | 1.6 | 0 |
| Body | 1rem / 16px | 400 | 1.5 | 0 |
| Body Small | X.Xrem / XXpx | XXX | 1.5 | 0 |
| Caption | X.Xrem / XXpx | XXX | 1.4 | 0.01em |
| Overline | X.Xrem / XXpx | XXX | 1.4 | 0.05em |

### Typography Rules
- **Max line width:** 65ch for body text, 45ch for narrow columns
- **Min body size:** 16px — never go smaller for body text
- **Font loading:** Use `font-display: swap` and `<link rel="preload">` for custom fonts

---

## 4. Spacing & Layout

### Base Unit
- Base: Xpx

### Spacing Scale

All values are multiples of the base unit.

| Token | Value | Common Use |
|-------|-------|------------|
| space-0 | 0px | No spacing |
| space-1 | Xpx | Tight inline spacing, icon-to-text gap |
| space-2 | Xpx | Input padding (vertical), badge padding |
| space-3 | Xpx | Button padding (vertical), list item gap |
| space-4 | Xpx | Card padding (internal), form field gap |
| space-5 | Xpx | Group separation, field-to-field gap |
| space-6 | Xpx | Section padding, card spacing |
| space-8 | Xpx | Large section breaks |
| space-10 | Xpx | Page-level vertical rhythm |
| space-12 | Xpx | Major content separations |
| space-16 | Xpx | Hero sections, page-level spacing |
| space-20 | Xpx | Full-page section gaps |
| space-24 | Xpx | Maximum spacing (hero to content) |

### Component Padding
| Component | Padding |
|-----------|---------|
| Button (sm) | Xpx Xpx |
| Button (md) | Xpx Xpx |
| Button (lg) | Xpx Xpx |
| Input | Xpx Xpx |
| Card | Xpx |
| Modal | Xpx |
| Section spacing | Xpx (between major page sections) |

### Breakpoints
| Name | Min Width | Columns | Gutter |
|------|-----------|---------|--------|
| sm | XXXpx | X | Xpx |
| md | XXXpx | X | Xpx |
| lg | XXXpx | XX | Xpx |
| xl | XXXXpx | XX | Xpx |

### Container
| Breakpoint | Max Width |
|------------|-----------|
| sm | 100% (padding Xpx) |
| md | XXXpx |
| lg | XXXXpx |
| xl | XXXXpx |

---

## 5. Shape & Elevation

### Corner Radius Scale
| Token | Value | Usage |
|-------|-------|-------|
| radius-none | 0px | Tables, full-bleed elements |
| radius-sm | Xpx | Badges, chips, small elements |
| radius-default | Xpx | Buttons, inputs |
| radius-md | Xpx | Cards, dropdowns |
| radius-lg | Xpx | Modals, large panels |
| radius-xl | Xpx | Feature cards, hero sections |
| radius-full | 9999px | Avatars, pill buttons, indicators |

### Shadow Scale
| Token | CSS Value | Usage |
|-------|-----------|-------|
| shadow-none | none | Flat elements, bordered cards |
| shadow-xs | 0 1px 2px rgba(X,X,X,0.XX) | Subtle lift, input focus |
| shadow-sm | 0 1px 3px rgba(X,X,X,0.XX), 0 1px 2px rgba(X,X,X,0.XX) | Cards, buttons |
| shadow-md | 0 4px 6px rgba(X,X,X,0.XX), 0 2px 4px rgba(X,X,X,0.XX) | Dropdowns, popovers |
| shadow-lg | 0 10px 15px rgba(X,X,X,0.XX), 0 4px 6px rgba(X,X,X,0.XX) | Modals, drawers |
| shadow-xl | 0 20px 25px rgba(X,X,X,0.XX), 0 8px 10px rgba(X,X,X,0.XX) | Floating panels |

### Elevation Rules
- Use **shadow** for floating elements (dropdowns, modals, tooltips)
- Use **border** for inline elements (cards, inputs, dividers)
- Use **background change** for state changes (hover, selected)
- Never combine shadow + heavy border on the same element

### Borders
| Token | Value |
|-------|-------|
| border-thin | 1px solid [neutral-200 hex] |
| border-default | 1px solid [neutral-300 hex] |
| border-heavy | 2px solid [neutral-400 hex] |

---

## 6. Iconography

- **Library:** [Icon library name — e.g., Lucide, Heroicons, Phosphor]
- **Style:** [Outline / Solid / Duotone] — use ONE style consistently

### Icon Sizes
| Context | Size | Notes |
|---------|------|-------|
| Inline (with text) | 16px | Aligns with body text |
| Button icon | 18px | Pairs with button text |
| Navigation | 20px | Sidebar and nav items |
| Decorative / empty state | 24px | Standalone icons, illustrations |

### Icon Rules
- Stroke weight: [X.X]px
- Color: inherits text color by default. Use `currentColor`.
- Never mix icon libraries. Pick one and use it everywhere.
- Icons in buttons go left of text. Icons in nav go left of label.

---

## 7. Animation & Motion

### Default Transition
- Duration: [XXX]ms
- Easing: [easing function — e.g., cubic-bezier(0.4, 0, 0.2, 1)]

### What Animates
- Button hover/active state changes
- Dropdown open/close
- Modal enter/exit
- Toast slide-in and fade-out
- Focus ring appearance
- Color and background-color transitions
- Accordion expand/collapse

### What Does NOT Animate
- Page layouts or grid shifts
- Font size or weight changes
- Border-radius changes
- Box-shadow changes (except focus ring)
- Scroll position (use native smooth scroll)

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

- Always support `prefers-reduced-motion`
- No decorative animations unless explicitly specified in this document

---

## 8. Component Specs (Summary)

This section specifies the brand-level token values for key components. For detailed component behavior, patterns, and implementation guidance, see the **ui-patterns** skill.

### Key Component Tokens

Specify values for these components using the brand tokens from sections above:

| Component | Key Properties to Specify |
|-----------|--------------------------|
| Button (primary, secondary, ghost, destructive) | Background, text color, border, height, padding, radius, font weight, hover/active/focus/disabled states |
| Input | Background, border, text/placeholder colors, height, padding, radius, focus ring, error state |
| Card | Background, border, shadow, radius, padding, hover state (if clickable) |
| Badge (default, success, warning, error, info) | Background, text color, padding, radius, font size/weight |
| Toast (success, error, warning, info) | Background, text color, icon, border-left, shadow, auto-dismiss duration |
| Modal | Backdrop color, background, radius, shadow, padding, max-width, animation |
| Table | Header style, row height/border/hover, cell padding, sort indicators |
| Navigation | Style (sidebar/topnav), background, dimensions, item states, mobile behavior |

**State coverage requirements:**
- **Interactive** (Button, Input, Nav items): default, hover, active, focus, disabled, loading, error
- **Container** (Card, Modal): default, hover (if clickable), selected, disabled, loading (skeleton)
- **Status** (Badge, Toast): variant-based — not interactive-state-based
- **Data** (Table): row default, hover, selected, header, empty state, loading (skeleton)

---

## 9. Anti-Patterns

These are explicitly banned. Any AI tool reading this file should treat these as hard rules.

1. **No gratuitous gradients** — Solid colors only unless explicitly specified above
2. **No text shadows** — Never apply shadow to text elements
3. **No stock photography** — Use icons, illustrations, or user-generated content instead
4. **No AI-generated hero images** — They look generic and undermine trust
5. **No decorative borders** — Borders serve structure (separation, containment), not decoration
6. **Never mix icon libraries** — Use [specified library] exclusively
7. **No color as sole indicator** — Always pair color with text, icon, or pattern (accessibility requirement)
8. **No placeholder-only labels** — Every input needs a visible label above it; placeholders are supplemental
9. **No pure black (#000000) backgrounds** — Use [neutral-950 hex] instead
10. **No pure white (#FFFFFF) on dark backgrounds** — Use [neutral-50 hex] for softer contrast
11. **No more than 2 font families** — Heading + body (+ mono if needed for code)
12. **No font sizes below 12px** — Caption and overline can go to 12px but never smaller
13. **No horizontal scrolling** — Content must fit viewport width at every breakpoint
14. [Brand-specific anti-pattern based on chosen reference — e.g., "No rounded corners over Xpx" for a Stripe-like brand, or "No dark mode" for a Calm-like brand]
15. [Brand-specific anti-pattern]
16. [Brand-specific anti-pattern]

---

## 10. Accessibility (Enforced)

These are not suggestions. They are requirements. Every component and page must comply.

### Color Contrast (WCAG 2.1 AA)
- Normal text (< 24px / < 18.66px bold): **4.5:1** minimum contrast ratio
- Large text (>= 24px / >= 18.66px bold): **3:1** minimum contrast ratio
- UI components and graphical objects: **3:1** minimum

### Contrast Ratios for This Brand
| Pairing | Foreground | Background | Ratio | Pass? |
|---------|------------|------------|-------|-------|
| Body text on page bg | #XXXXXX | #XXXXXX | XX:1 | AA |
| Body text on card bg | #XXXXXX | #XXXXXX | XX:1 | AA |
| Primary button text on primary bg | #XXXXXX | #XXXXXX | XX:1 | AA |
| Secondary text on page bg | #XXXXXX | #XXXXXX | XX:1 | AA |
| Placeholder on input bg | #XXXXXX | #XXXXXX | XX:1 | AA |
| Link text on page bg | #XXXXXX | #XXXXXX | XX:1 | AA |
| Error text on error bg | #XXXXXX | #XXXXXX | XX:1 | AA |
| Success text on success bg | #XXXXXX | #XXXXXX | XX:1 | AA |

### Interactive Elements
- **Focus indicators** on ALL interactive elements (buttons, links, inputs, selects, checkboxes)
- Focus ring: 2px solid [primary hex], 2px offset — visible on both light and dark backgrounds
- **Touch targets:** minimum 44x44px on all interactive elements
- **Color not sole indicator:** Never use color alone to communicate state. Pair with icon, text, or pattern.

### Forms
- **Visible labels** above every input (not placeholder-only)
- **Error messages** appear below the field with icon + text (not color alone)
- **Required fields** marked with text "(required)" — not asterisk only
- **Autocomplete** attributes on all standard fields (name, email, address, etc.)

### Structure
- **Heading hierarchy:** h1 > h2 > h3 > h4 — never skip levels
- **Skip navigation link** as first focusable element on every page
- **Landmark roles:** main, nav, footer, aside — used correctly
- **Alt text:** All meaningful images have descriptive alt text. Decorative images use `alt=""`
- **Language attribute:** `<html lang="en">` (or appropriate language)

---

## 11. Responsive Design (Enforced)

### Approach
- **Mobile-first:** Base styles are mobile. Layer up with min-width media queries.

### Breakpoints
| Name | Value | Target |
|------|-------|--------|
| sm | XXXpx | Large phones, landscape |
| md | XXXpx | Tablets |
| lg | XXXpx | Laptops, small desktops |
| xl | XXXXpx | Large desktops |

### Fluid Typography
Use `clamp()` for responsive type sizing:
```css
--font-display: clamp(X.Xrem, Xvw + Xrem, X.Xrem);
--font-h1: clamp(X.Xrem, Xvw + Xrem, X.Xrem);
--font-h2: clamp(X.Xrem, Xvw + Xrem, X.Xrem);
--font-h3: clamp(X.Xrem, Xvw + Xrem, X.Xrem);
--font-body-lg: clamp(X.Xrem, Xvw + Xrem, X.Xrem);
```

### Mobile Requirements
- No horizontal scroll at any viewport width
- Touch targets: 44px minimum on mobile
- Input font size: 16px minimum (prevents iOS zoom)
- Thumb-friendly zones for primary actions

### Navigation Transformation
- **Desktop (>= [lg breakpoint]):** [sidebar/topnav as specified in component specs]
- **Tablet ([md] to [lg]):** [collapsed sidebar / topnav with overflow menu]
- **Mobile (< [md]):** [hamburger menu / bottom tab bar / drawer nav]

### Images
- `max-width: 100%` on all images
- Use `srcset` and `sizes` for responsive images
- Provide WebP with fallback
- Lazy load below-the-fold images: `loading="lazy"`

### Container
- Max width: [xl container max-width]
- Auto side margins for centering
- Horizontal padding: [space-4] on mobile, [space-6] on desktop
````

---

## 12. Application Examples

These examples use actual values from the sections above — not placeholders. They show how the system comes together in real components.

For each example, provide both CSS custom properties AND Tailwind utility classes.

### Example format (follow this pattern for all 8):

**Primary + secondary button side by side:**
```css
/* CSS Custom Properties */
.btn-primary {
  background-color: var(--color-primary);        /* #XXXXXX from Section 2 */
  color: var(--color-primary-text);               /* #XXXXXX from Section 8 Button table */
  padding: var(--space-3) var(--space-5);          /* Xpx Xpx from Section 4 */
  border-radius: var(--radius-default);            /* Xpx from Section 5 */
  font-weight: var(--font-weight-button);          /* XXX from Section 8 */
  font-size: var(--font-body);                     /* 1rem from Section 3 */
  height: Xpx;                                     /* from Section 8 */
  transition: background-color var(--transition-duration) var(--transition-easing);
}
.btn-primary:hover { background-color: #XXXXXX; }  /* from Section 8 Hover row */
.btn-primary:focus-visible {
  outline: 2px solid #XXXXXX;                      /* from Section 8 Focus row */
  outline-offset: 2px;
}
```
```html
<!-- Tailwind -->
<div class="flex gap-[Xpx]">
  <button class="bg-[#XXXXXX] text-[#XXXXXX] px-[Xpx] py-[Xpx] rounded-[Xpx] font-[XXX] h-[Xpx] hover:bg-[#XXXXXX] focus-visible:outline-2 focus-visible:outline-[#XXXXXX] focus-visible:outline-offset-2">
    Primary Action
  </button>
  <button class="bg-[#XXXXXX] text-[#XXXXXX] border border-[#XXXXXX] px-[Xpx] py-[Xpx] rounded-[Xpx] font-[XXX] h-[Xpx] hover:bg-[#XXXXXX]">
    Secondary Action
  </button>
</div>
```

### Required examples (follow the format above for each):

1. **Primary + secondary button side by side** — button variants with correct spacing
2. **Card with heading, body text, and action button** — card, typography, and button integration
3. **Form with label, input, helper text, and error state** — form field in both valid and error states
4. **Page header with logo area, navigation, and CTA button** — nav and layout integration
5. **Data table row with status badge and action buttons** — table, badge, and button together
6. **Empty state with icon, message, and CTA** — empty state pattern with correct spacing
7. **Error state (inline field error + full-page error)** — both error display variants
8. **Modal with header, body content, and action buttons** — modal with correct padding and button placement

Every value in these examples must come from a specific section above. No invented values.

---

## Logo Guidance

### MVP Logo
- Use text-only for MVP. Your product name in your heading font at display weight is a logo.
- Create a simple favicon: first letter of your product on your primary color background.
- Use an SVG for crispness at all sizes.

### Versions Needed
| Version | Where It Goes | Notes |
|---------|---------------|-------|
| Full logo (text) | Header, login page | Your product name in heading font |
| Icon only | Favicon, mobile app icon | Single letter or simple mark |
| Dark background variant | Dark nav, footer | Ensure contrast |
| Light background variant | Light pages, emails | Default version |

### When to Invest in a Real Logo
- After product-market fit (not before)
- When you're embarrassed showing the text logo to potential customers
- When you have budget for a designer ($500-2000 range)
- Never let logo design block your launch

---

## What You Decide vs. What AI Implements

| You Decide | AI Implements |
|------------|---------------|
| "I want it to feel like Linear" | Complete color, type, and spacing system |
| "Warmer, more approachable" | Adjusts temperature, radius, type to humanist |
| "I hate that green" | Swaps green for next-best semantic color |
| "Can the buttons be softer?" | Increases radius, reduces weight, adjusts shadow |
| "I need dark mode" | Full dark mode token mapping |
| "This is for enterprise" | Trust-oriented palette, geometric type, high contrast |

**Rule:** You describe the destination. AI drives.

---

## Common Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Skipping brand identity, letting AI choose | Every page looks different, AI fills gaps with random defaults | Generate BRAND-IDENTITY.md first |
| Specifying colors but not states | Hover, active, disabled states get invented randomly | This template specifies every state |
| "Just make it look modern" | AI defaults to generic SaaS — indistinguishable from templates | Pick reference brands instead |
| Choosing colors you personally like | Your brand might clash with accessibility or audience expectations | React to proposals based on your audience, not personal taste |
| Skipping dark mode decision | Some AI tools generate dark mode anyway, others don't | Explicitly opt in or out |
| No anti-patterns list | AI adds gradients, shadows, and decorations "to make it pop" | Anti-patterns section bans the usual suspects |

---

## Quality Gate

Before writing the final `BRAND-IDENTITY.md`, verify every item:

- [ ] All 12 sections fully populated — no "TBD," no placeholders, no empty cells
- [ ] Every color pairing listed in Section 10 passes WCAG 2.1 AA (4.5:1 for normal text, 3:1 for large text)
- [ ] All component states specified (default, hover, active, focus, disabled, loading, error as applicable)
- [ ] Anti-patterns list has 16+ items including at least 3 brand-specific entries
- [ ] Fluid typography `clamp()` values produce correct sizes at 320px and 1440px viewport widths
- [ ] Spacing scale is internally consistent (based on base unit, no arbitrary jumps)
- [ ] Application examples in Section 12 use actual hex values, spacing, and font specs — not placeholders
- [ ] Font loading strategy specified (`font-display: swap`, preload)
- [ ] Dark mode either fully mapped (every token) or explicitly opted out with the exact phrase "Dark mode not supported. Do not generate dark mode variants."
- [ ] All accessibility requirements from Section 10 are present and filled in
- [ ] Contrast ratio table has at least 8 pairings calculated
- [ ] Touch targets specified as 44px minimum in both Section 10 and Section 11
- [ ] Breakpoint values are consistent between Section 4 and Section 11
- [ ] Icon library specified and "never mix" rule included
- [ ] Reduced motion CSS included in Section 7

---

## Related Skills

Once the brand identity is generated, these skills use the tokens to build the actual UI:

- **aesthetics** — How to apply these tokens beautifully (visual hierarchy, whitespace, composition)
- **ui-patterns** — Component implementation and page layouts using these tokens
- **motion-polish** — Animation timing and micro-interactions that match the brand personality
- **design-review** — Quality gate to audit whether the UI correctly implements this identity
