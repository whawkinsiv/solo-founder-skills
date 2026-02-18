---
name: design
description: "Use this skill when the user needs to create a design system, establish UI patterns, improve visual hierarchy, refine interactions, or ensure visual consistency across their SaaS app. Covers design system management (CREATE/MODIFY/WORK WITHIN modes), screen-by-screen UI guidance, component selection, and spacing rules."
---

# Design

Manage your app's design system through `instructions/design-system.md` - the single source of truth for all UX/UI work.

## Choose Your Mode

**CREATE** → No design system yet, or extracting from existing code
**MODIFY** → Have a design system, need to update it
**WORK WITHIN** → Have a design system, building features that follow it

---

## CREATE Mode

Generate a new `instructions/design-system.md` from one of these entry points:

### From URL (Reference App)

Analyze a live app and extract its design patterns.

**Tell AI:**
```
Analyze the design system at [URL].
Identify: colors, typography, spacing, component patterns.
Match to recognized framework (shadcn, Material UI, Radix, etc.).
Generate instructions/design-system.md based on this analysis.
```

**Good reference apps:**
- linear.app (minimal, fast, keyboard-focused)
- stripe.com/dashboard (data-heavy, clear hierarchy)
- notion.so (flexible, calm)
- vercel.com (modern, technical)

### From Code (Extract & Audit)

Paste existing source code to extract and document current patterns.

**Tell AI:**
```
Analyze this code and extract the design system:
[paste relevant components, styles, or config files]

Document: colors, typography, spacing, component specs.
Identify inconsistencies (e.g., multiple button heights, conflicting colors).
Generate instructions/design-system.md with recommendations to standardize.
```

**What to paste:**
- Tailwind config or CSS variables
- Button/Input/Card components
- Theme or design token files
- 2-3 representative page components

### From Screenshot

Upload an image as a visual reference.

**Tell AI:**
```
Analyze this screenshot and extract the design system.
Identify: colors, typography, spacing, component patterns.
Match to closest recognized framework.
Generate instructions/design-system.md based on this analysis.
```

**What to screenshot:**
- Dashboard or main app view
- A form or data entry screen
- Navigation (sidebar or topnav)

### From Scratch

Start fresh with guided decisions.

**Tell AI:**
```
Help me create a design system for [app type].
I want it to feel like [reference: minimal/playful/professional/technical].
Primary brand color: [color or "help me choose"].
Generate instructions/design-system.md with sensible defaults.
```

See [LAWSOFUX.md](LAWSOFUX.md) for why certain patterns work better.

---

## MODIFY Mode

Update an existing `instructions/design-system.md`:

### Update Values

Change colors, fonts, or spacing.

**Tell AI:**
```
Update instructions/design-system.md:
- Change primary color from [old] to [new]
- Update font from [old] to [new]
Ensure all related values are updated (hover states, etc.).
```

### Add Patterns

Add new component types not yet documented.

**Tell AI:**
```
Add a [pricing table / data table / modal] pattern to instructions/design-system.md.
Follow existing design system values (colors, spacing, typography).
Reference: [URL or description of what you want]
```

See [COMPONENTS.md](COMPONENTS.md) for common SaaS component patterns.

### Audit & Reconcile

Compare current code to design system, resolve drift.

**Tell AI:**
```
Audit this code against instructions/design-system.md:
[paste code]

Option A: List deviations so I can fix the code
Option B: Update design-system.md to reflect what code actually does
```

**Always identifies:**
- Inconsistent values (3 different grays, 2 button heights)
- Undocumented patterns (components not in design system)
- Unused specs (documented but not implemented)

### Migrate Framework

Transition from one component library to another.

**Tell AI:**
```
Migrate instructions/design-system.md from [Material UI] to [shadcn].
Keep existing colors, typography, and spacing.
Update component specs to match new framework patterns.
```

---

## WORK WITHIN Mode

Reference existing `instructions/design-system.md` when building:

### Build Feature

Follow the system when implementing new UI.

**Tell AI:**
```
Build [feature description].
Follow instructions/design-system.md for all design decisions.
Use the documented colors, typography, spacing, and component patterns.
```

### Review Compliance

Check AI-built code against the system.

**Tell AI:**
```
Review this code for design system compliance:
[paste code]

Check against instructions/design-system.md.
Flag any deviations from documented patterns.
```

### Answer Questions

Quick design decisions.

**Tell AI:**
```
Based on instructions/design-system.md:
- What color should [element] be?
- What spacing between [A] and [B]?
- Which button variant for [action]?
```

---

## Design-System.md Structure

When CREATE mode generates the file, it follows this structure:

```markdown
# Design System

## Reference
- Primary reference: [app name/URL]
- Component library: [shadcn/Material UI/Radix/custom]
- Design philosophy: [minimal/playful/professional/technical]

## Colors

### Brand
- Primary: #XXXXXX
- Primary hover: #XXXXXX

### Gray Scale
- 50: #XXXXXX (backgrounds)
- 100-400: [values]
- 500: #XXXXXX (borders, secondary text)
- 600-800: [values]
- 900: #XXXXXX (primary text)

### Semantic
- Success: #XXXXXX
- Error: #XXXXXX
- Warning: #XXXXXX

## Typography

### Font
- Family: [Inter/SF Pro/etc.]
- Fallback: system-ui, sans-serif

### Scale
- H1: 32px / 1.2 line-height / semibold
- H2: 24px / 1.25 / semibold
- H3: 20px / 1.3 / medium
- Body: 16px / 1.5 / regular
- Small: 14px / 1.5 / regular
- Tiny: 12px / 1.4 / regular

## Spacing

- Base unit: 4px
- Scale: 4, 8, 12, 16, 24, 32, 48, 64
- Component padding: 16px
- Section spacing: 32px
- Card gap: 16px

## Components

### Buttons
| Variant | Background | Text | Height | Padding | Border Radius |
|---------|------------|------|--------|---------|---------------|
| Primary | primary | white | 40px | 16px 24px | 6px |
| Secondary | gray-100 | gray-900 | 40px | 16px 24px | 6px |
| Ghost | transparent | gray-600 | 40px | 16px 24px | 6px |
| Destructive | error | white | 40px | 16px 24px | 6px |

States: hover (darken 10%), active (darken 15%), disabled (opacity 50%)

### Inputs
- Height: 40px
- Border: 1px gray-300
- Border radius: 6px
- Padding: 12px
- Focus: primary border + ring
- Error: error border
- Disabled: gray-100 background

### Cards
- Background: white
- Border: 1px gray-200 OR shadow-sm
- Border radius: 8px
- Padding: 16px or 24px

## Patterns

### Navigation
- Style: [sidebar/topnav/both]
- Width: [if sidebar, e.g., 240px]
- Behavior: [collapsible/fixed/responsive]

### Forms
- Layout: single column, labels above
- Field spacing: 16px
- Button placement: right-aligned
- Validation: inline, on blur

### Tables
- Row height: 48px
- Actions: right side
- Hover: gray-50 background
- Pagination: bottom

## Inconsistencies Found
[If extracted from existing code, list what was found and standardized]
- Example: Found 3 button heights (36px, 40px, 44px) → standardized to 40px
```

---

## User Override

If you already have a `instructions/design-system.md` file, it takes precedence over any generated recommendations. The skill will work within your documented system.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Building UI without design system | CREATE mode first, then build |
| Inconsistent components | Use MODIFY → Audit & Reconcile |
| "It looks off but I can't say why" | Check compliance against design-system.md |
| Reinventing patterns | Reference [COMPONENTS.md](COMPONENTS.md) for proven SaaS patterns |
| Ignoring UX principles | Reference [LAWSOFUX.md](LAWSOFUX.md) for why patterns work |

---

## Success Looks Like

✅ Every project has `instructions/design-system.md`
✅ AI builds consistent UI without repeated instructions
✅ Design decisions are documented, not guessed
✅ Code audits catch drift before it compounds
✅ New team members/contractors have clear reference

---

## What You Decide vs. What AI Implements

| You Decide | Claude Code Implements |
|------------|----------------------|
| "This page's goal is getting users to create a project" | Visual hierarchy that makes the CTA dominant |
| "We need a settings page with tabs" | Tabbed layout with proper spacing and states |
| "The dashboard should show key metrics first" | Card layout with data visualization |
| "Forms should validate as users type" | Inline validation with clear error messages |

**Rule:** You define the goal of each screen. AI handles the pixels.

---

## Priority Order: What to Get Right First

### Tier 1: Gets You 80% of the Way

1. **One primary action per screen** — If you can't name it, the page is broken.
2. **Visual hierarchy** — Size, weight, and contrast guide the eye. Most important = biggest.
3. **Consistent spacing** — Use your component library's defaults. Don't manually tweak pixels.
4. **Design states** — Every screen needs: empty, loading, error, success, and overflow states.

### Tier 2: After Launch

5. **Mobile responsiveness** — Test core flows on mobile. 50%+ of traffic may be mobile.
6. **Micro-interactions** — Loading spinners, success checkmarks, smooth transitions.
7. **Keyboard navigation** — Tab through every form. Escape closes every modal.

---

## Screen-by-Screen Guidance

### Dashboard

**Tell AI:**
```
Design a SaaS dashboard that shows:
- 3-4 key metric cards at the top (e.g., MRR, active users, signups this week)
- A recent activity feed or table below
- A primary CTA: "Create [your main object]"
- Empty state for new users with onboarding guidance
Use [component library]. Mobile-responsive.
```

### Settings Page

**Tell AI:**
```
Create a settings page with tabs:
- Profile (name, email, avatar)
- Billing (current plan, usage, manage subscription link)
- Notifications (email preferences with toggles)
- [Team/API/other sections you need]
Each tab has its own save button. Show success toast on save.
```

### Data Tables

**Tell AI:**
```
Build a data table for [items — users, projects, invoices]:
- Columns: [list your columns]
- Sortable by [which columns]
- Search/filter bar above the table
- Row actions: edit, delete (with confirmation dialog)
- Pagination for 20+ items
- Empty state: "No [items] yet. Create your first one."
```

### Forms

**Tell AI:**
```
Create a [create/edit] form for [object]:
- Fields: [list fields with types — text, email, select, etc.]
- Validate on blur (not on every keystroke)
- Show inline errors below each field
- Submit button disabled until form is valid
- Show loading state on submit, success toast on completion
```

---

## Component Selection Guide

| Situation | Use This |
|-----------|----------|
| User needs to choose from 3-5 options | Radio buttons or segmented control |
| User needs to choose from 6+ options | Select dropdown |
| Yes/no toggle | Switch |
| Confirming a destructive action | Alert dialog ("Are you sure?") |
| Showing transient feedback | Toast notification (auto-dismiss) |
| Showing persistent info/warning | Alert banner (stays until dismissed) |
| Editing a record without leaving the page | Dialog or sheet (slide-out panel) |
| Navigating between views | Tabs (same page) or sidebar nav (different pages) |
| Showing user status | Badge (active, trial, overdue) |

---

## Visual Hierarchy Checklist

For every screen, verify:

- [ ] The primary action is the most visually prominent element
- [ ] Only ONE primary button per section (others are secondary or ghost)
- [ ] Headings use size + weight to create clear hierarchy (h1 > h2 > h3)
- [ ] Related items are grouped with consistent spacing
- [ ] Labels are above inputs (not placeholder-only)
- [ ] Color is not the only way to convey meaning (add icons or text)

---

## Common UI Mistakes

| Mistake | Fix |
|---------|-----|
| Two primary buttons side by side | One should be secondary (outlined). Only one primary per section. |
| No empty state | Every list/table needs a "nothing here yet" message with a CTA. |
| No loading state | Show skeleton loaders or spinners while data fetches. |
| Placeholder text as labels | Always use a visible label above the input. Placeholders disappear. |
| Too many things on one screen | Progressive disclosure: show the essentials, hide advanced options behind "Show more" or tabs. |
| Inconsistent alignment | Left-align text, right-align numbers. Don't center body text. |
| Ignoring mobile | Test your most important flow on a phone-sized screen. |
