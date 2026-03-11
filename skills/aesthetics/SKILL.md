---
name: aesthetics
description: "Use this skill when the user wants to make their app look better, says it looks like a template, asks how to achieve Stripe/Linear quality, or says something looks off. Covers visual hierarchy, whitespace, composition, color application, and typography in practice."
---

# Aesthetics

Make web apps look intentionally designed rather than AI-generated. This skill covers the visual principles that separate premium-feeling apps (Stripe, Linear, Vercel) from generic template output. Apply these principles when building new UI or when the user says something "looks off" but can't articulate why.

Reference [AI-SLOP-FIXES.md](AI-SLOP-FIXES.md) for specific antipattern remediation. Reference [REFERENCE-TEARDOWNS.md](REFERENCE-TEARDOWNS.md) for concrete examples from production apps.

---

## Core Principles

1. **Restraint is the primary aesthetic.** Premium apps use fewer colors, fewer font weights, fewer borders, fewer shadows. When in doubt, remove rather than add.
2. **Every visual difference must communicate a difference in meaning.** If two elements look different, they should BE different. If they're the same type of thing, they must look identical.
3. **Hierarchy is not optional.** Every screen has exactly one primary focal point, 2-3 secondary elements, and everything else recedes. If everything is emphasized, nothing is.
4. **Whitespace is a design element, not empty space.** It creates grouping, hierarchy, and breathing room. Increasing whitespace almost always improves perceived quality.
5. **Color is information, not decoration.** Each color in the palette should have a job. If a color doesn't communicate status, action, or brand, remove it.
6. **Consistency compounds.** One slightly-off spacing value is invisible. Twenty slightly-off values make an app feel broken. Nail the system, not individual screens.
7. **The eye follows contrast.** The highest-contrast element on screen gets attention first. Use this deliberately — never accidentally.

---

## Visual Hierarchy

This is the single most impactful skill. A clear hierarchy makes any design feel professional; a muddled one makes even beautiful components feel amateurish.

### Tools for creating hierarchy (in order of impact):

**Size difference.** The primary element should be dramatically larger than secondary elements. Not 10% larger — 50-100% larger. A page heading at `text-3xl` with body at `text-sm` creates immediate hierarchy. A heading at `text-xl` with body at `text-lg` creates mush.

**Weight contrast.** Pair `font-bold` (700) headings with `font-normal` (400) body text. Never use `font-medium` (500) for both headings and body — the difference is invisible. Use at most 3 font weights per page: one for headings, one for body, one for de-emphasized text.

**Color contrast.** Primary content in `text-gray-900`, secondary in `text-gray-500`, tertiary in `text-gray-400`. Three levels is usually enough. Don't use `text-gray-700` and `text-gray-600` on the same page — the difference is imperceptible.

**Spatial hierarchy.** The most important element gets the most surrounding whitespace. A CTA button with `py-3 px-8` surrounded by `mt-8` commands more attention than one with `py-2 px-4` and `mt-4`.

### Common hierarchy failures:

- **Flat hierarchy:** Every text element is `text-base font-medium text-gray-700`. Fix: Pick ONE weight/size for body, make headings dramatically different.
- **Inverted hierarchy:** Navigation or header competes with page content. Fix: Nav should be quieter than content — use `text-sm font-normal text-gray-500` for nav items.
- **Competing CTAs:** Multiple buttons with equal visual weight. Fix: One `bg-primary text-white` button per section. Everything else is `text-gray-600 hover:text-gray-900` or a ghost/outline variant.

---

## Whitespace

### The core rule: space between groups > space within groups

If items inside a card are spaced with `gap-3` (12px), the gap between cards should be `gap-6` (24px) or more. If sections use `gap-6` internally, section gaps should be `py-16` or `py-20`. This ratio (2-3x) is the single most important spacing principle.

### Where to add whitespace:

- **Page margins.** `px-6` minimum on mobile, `px-8` to `px-12` on desktop. Cramped edges make everything feel cheap.
- **Above page headings.** `pt-8` to `pt-12` before the first heading. Content that starts immediately below the nav feels rushed.
- **Between sections.** `py-12` to `py-20` between major sections. This is almost always too small in AI-generated output.
- **Around CTAs.** Primary buttons need breathing room. `mt-6` to `mt-8` above a CTA gives it importance.
- **Inside cards.** `p-6` is the minimum for cards with content. `p-4` works for compact list items but feels cramped for standalone cards.

### Where density is correct:

- **Data tables.** Tight rows (`py-2` to `py-3`) with compact cells are fine — density is the point.
- **Navigation items.** `py-2 px-3` keeps nav compact and functional.
- **Form fields.** `gap-4` to `gap-5` between form fields is appropriate — too much space makes forms feel disconnected.
- **Inline elements.** Icon-to-text gap of `gap-1.5` to `gap-2`. Badge padding of `px-2 py-0.5`.

---

## Color Application

### The 60-30-10 rule

- **60% neutral.** Backgrounds, cards, body text. White/gray/off-white. This is the canvas.
- **30% secondary.** Borders, secondary text, dividers, subtle backgrounds. Gray-200 to gray-500 range.
- **10% accent.** Primary buttons, active states, links, key indicators. Your brand color.

Most AI-generated apps flip this ratio — too much accent color, not enough neutral space. If more than 10% of the visible pixels are your brand color, pull back.

### Saturation management

- **Interactive elements** (buttons, links, active tabs) use full-saturation brand color.
- **Backgrounds and containers** use desaturated, lightened variants: `bg-blue-50` not `bg-blue-500`.
- **Status colors** (success, error, warning) use medium saturation for backgrounds (`bg-green-50`, `bg-red-50`) with full saturation for text and icons (`text-green-700`, `text-red-700`).
- **Never use full-saturation color as a large background.** A `bg-blue-600` hero section screams template. Use `bg-white` or `bg-gray-50` with a blue accent element instead.

### When NOT to use color

- Section backgrounds — use whitespace or subtle borders to separate sections, not colored backgrounds.
- Every card having a colored accent — pick one or two cards to highlight, leave the rest neutral.
- Decorative color blocks with no information purpose.

---

## Typography in Practice

### Weight pairing

Use exactly two weights for most UI: `font-semibold` (600) for headings and labels, `font-normal` (400) for body and descriptions. Add `font-medium` (500) only if you genuinely need a third level (e.g., subheadings within a section). Never use `font-light` (300) — it's unreadable at small sizes on most screens.

### Size relationships

Maintain a clear step ratio between sizes. A practical scale:

| Role | Tailwind | Size |
|------|----------|------|
| Page title | `text-2xl` or `text-3xl` | 24-30px |
| Section heading | `text-xl` | 20px |
| Card title | `text-lg` or `text-base font-semibold` | 16-18px |
| Body | `text-sm` or `text-base` | 14-16px |
| Secondary/meta | `text-xs` or `text-sm` | 12-14px |

The key: adjacent levels in the hierarchy should be at least 2 Tailwind size steps apart. `text-base` heading with `text-sm` body works. `text-lg` heading with `text-base` body is too close.

### Line length

Body text should never exceed `max-w-prose` (~65ch). Text that stretches across a full-width container is the fastest way to look unprofessional. For headings, `max-w-2xl` keeps them from stretching too wide on large screens.

### Letter-spacing

- Large headings (`text-3xl` and up): add `tracking-tight` (-0.025em). Large text has too much natural spacing.
- Body text: leave default (no tracking class).
- All-caps labels or overlines: add `tracking-wide` or `tracking-wider`. Uppercase text without extra tracking looks cramped.

---

## Composition

### Alignment grids

Pick ONE alignment edge for content and stick to it across pages. Left-align is correct for 90% of SaaS UIs. Center-align only for: hero sections, empty states, and confirmation dialogs. Never center body text, form fields, or data.

### Visual rhythm

Repeating elements (cards, list items, table rows) must be identical in structure. Same padding, same text sizes, same spacing between elements within each item. Variation in repeating elements creates visual noise — the eye constantly readjusts instead of scanning smoothly.

### Page-level balance

- **F-pattern for content pages:** Primary content left, secondary content right. The eye naturally scans left-to-right, top-to-bottom.
- **Single-column for focused tasks:** Forms, checkout flows, onboarding steps. Max-width `max-w-lg` to `max-w-xl`, centered.
- **Sidebar + content for dashboards:** Fixed-width sidebar (`w-64`), fluid content area. Content area should have its own internal max-width for readability.

### Asymmetry that works

Not everything needs to be perfectly centered or symmetrical. A page with a large content area and a narrow sidebar is asymmetric but balanced because the content has visual weight. A card grid with 3 columns where the first card is double-width creates intentional asymmetry that draws the eye.

---

## Consistency

### Cross-page coherence

Every page in the app should share:
- Identical header/nav height and style
- Same page padding and max-width
- Same heading hierarchy (h1 = page title at same size everywhere)
- Same card style (if pages use cards)
- Same button variants (primary/secondary/ghost look identical on every page)

### Pattern reuse

When building a new page, explicitly reuse patterns from existing pages. Don't invent a new card style when one exists. Don't create a new button variant when primary/secondary/ghost covers the need. Every unique visual pattern adds cognitive load.

### The "same but different" problem

Lists of items (pricing plans, feature comparisons, team members) should use identical visual structure with only content changing. When one pricing card has an icon and another doesn't, or one has a colored background and others don't, it creates unintentional hierarchy. If you need to highlight one option, do it with a single differentiator: a border color, a "Popular" badge, or a slight size increase — not three differences at once.

---

## Auditing

For structured audit checklists (60-second scan and comprehensive), use the **design-review** skill. The principles in this skill inform what to look for; design-review provides the systematic checklist.
