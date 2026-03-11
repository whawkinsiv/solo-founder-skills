---
name: ui-patterns
description: "Use this skill when the user needs to build a dashboard, settings page, data table, or any page layout. Also use when choosing component libraries, implementing responsive design, dark mode, or handling UI states (loading, empty, error). Covers component selection, page composition, and responsive implementation."
---

# UI Patterns

This skill covers how to build pages and compose components for SaaS applications. It provides the structural decisions — which components to use, how to lay out pages, and how to handle every UI state. For visual styling (colors, typography, spacing systems), see the aesthetics skill. For user flow design, see ux-design. For accessibility requirements (semantic HTML, keyboard nav, ARIA), see ux-design/ACCESSIBILITY.md.

## Component Library Selection

**Default: shadcn/ui + Tailwind CSS.** This is the correct choice for 90% of founder-built SaaS apps. shadcn/ui provides copy-paste components built on Radix primitives — you own the code, can customize freely, and avoid dependency lock-in.

Decision framework:

| Situation | Choice | Why |
|---|---|---|
| Public-facing SaaS product | shadcn/ui + Tailwind | Full design control, great defaults, accessible |
| Internal admin tool / back-office | Ant Design or MUI | Dense data display, built-in table/form patterns, faster to ship |
| Need one specific primitive (tooltip, dialog) | Radix directly | Skip the styling layer, use just the behavior |
| Existing MUI/Chakra codebase | Stay with current lib | Migration cost rarely worth it mid-project |
| React Native / mobile app | React Native Paper or Tamagui | Web component libs don't apply |

When using shadcn/ui: install components individually (`npx shadcn-ui@latest add button`), don't install everything upfront. Configure the `components.json` path aliases to match the project structure.

## Page Composition Principles

Every SaaS page follows a predictable anatomy. Structure pages using these content zones:

**Page header** — Title, description, primary action button (top-right). Breadcrumbs above the title if nested. Height: 64-80px.

**Primary content** — The main purpose of the page. Takes 60-70% of width on desktop. This is the "spine" — the vertical column the user's eye follows.

**Secondary content** — Supporting information, filters, related items. Sidebar or below primary content. Takes 30-40% width or full-width below on mobile.

**Actions area** — Sticky bottom bar for forms, floating action button, or inline with content. Never hide primary actions in menus.

The page spine principle: every page has one dominant vertical column. On a dashboard, it's the metrics-to-activity flow. On a settings page, it's the form sections. On a list page, it's the table. Identify the spine and give it visual priority — other content supports it.

Standard page container: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`. For content-heavy pages (docs, settings forms): `max-w-3xl`. For full-bleed layouts (dashboards): no max-width, use the sidebar to constrain.

## The State Matrix

Every data-driven component must handle five states. Missing any one of these creates a broken experience. When building any component that displays dynamic data, implement all five:

### Loading State
Use skeleton loaders that match the shape of the real content. Never use spinners for inline content — spinners are only for full-page loads or button actions.

- Tables: render 5-8 skeleton rows with column-width-matched blocks
- Cards: render the card shell with pulsing placeholder blocks
- Lists: render 3-5 skeleton items
- Use `animate-pulse` with `bg-muted` blocks. Match heights and widths to actual content.

### Empty State
The most neglected state. Every empty state needs: an icon or illustration, a headline explaining what will appear here, a description of how to populate it, and a primary CTA button.

```
No projects yet → "Create your first project" button
No search results → "Try different keywords" suggestion
No notifications → "You're all caught up" message (no CTA needed)
```

Empty states are onboarding moments. Use them to teach users what to do next.

### Error State
Display what went wrong in plain language and provide a retry action. Never show raw error codes or stack traces.

- Inline errors: red text below the failed component + retry button
- Full-page errors: centered message with retry and "go back" options
- Network errors: "Connection lost. Retrying..." with auto-retry logic
- Always preserve user input on form errors — never clear fields

### Success State
The normal content display. This is what most developers build first (and sometimes only). Ensure it handles variable content lengths — long titles, missing optional fields, various image aspect ratios.

### Overflow State
What happens when there's too much data:

- Tables: paginate at 10-25 rows, show total count, provide page size selector
- Lists: infinite scroll or "Load more" button. Show count: "Showing 20 of 148"
- Text: truncate with ellipsis and "Show more" expand option. Use `line-clamp-2` or `line-clamp-3`
- Tags/badges: show first 3 + "+N more" pill

## Responsive Strategy

Use mobile-first with Tailwind's breakpoint system. Default styles target mobile, then layer on complexity:

| Breakpoint | Width | Target |
|---|---|---|
| default | 0-639px | Mobile phones |
| `sm` | 640px+ | Large phones, small tablets |
| `md` | 768px+ | Tablets |
| `lg` | 1024px+ | Small laptops, landscape tablets |
| `xl` | 1280px+ | Desktops |
| `2xl` | 1536px+ | Large monitors |

**What changes at each breakpoint:**

- **Mobile (default):** Single column. Bottom navigation. Cards stack vertically. Tables become card lists. Sidebar hidden behind hamburger. Modals go full-screen. Horizontal padding: 16px.
- **sm:** Minor adjustments. Two-column grids where appropriate. Slightly more padding.
- **md:** Sidebar can appear as collapsible overlay. Tables can show with horizontal scroll. Two or three column grids. Padding: 24px.
- **lg:** Full sidebar visible. Tables display normally. Multi-column layouts activate. Dashboard grids expand. Padding: 32px.
- **xl+:** Max-width containers center content. Extra whitespace on sides. Optional: wider sidebar, more columns.

**Key responsive patterns:**

| Desktop Pattern | Mobile Adaptation |
|---|---|
| Sidebar navigation | Bottom tab bar (5 items max) or hamburger menu |
| Data table | Stacked cards with key fields visible |
| Multi-column grid | Single column, stacked |
| Side-by-side panels | Tabbed or stacked sections |
| Hover tooltips | Tap-to-reveal or always-visible labels |
| Right-click context menu | Long-press menu or action row with icons |
| Modal dialog | Full-screen sheet sliding up from bottom |

For the sidebar-to-bottom-nav pattern: don't just hide the sidebar. Build a dedicated `BottomNav` component with 4-5 icon+label items. The items should map to the top-level sidebar sections, not be a 1:1 copy.

## Dark Mode

**When to implement:** If building an MVP for validation, skip dark mode. If building a product users will spend hours in (dashboards, dev tools, writing apps), implement from day 1. Adding dark mode later requires touching every component — it's significantly cheaper to build it in from the start.

**Implementation approach:**

1. Define all colors as CSS custom properties in `:root` and `.dark`
2. Use Tailwind's `dark:` prefix for overrides
3. If using shadcn/ui, this is already set up — just configure the theme in `globals.css`
4. Toggle with a class on `<html>` element: `document.documentElement.classList.toggle('dark')`
5. Respect system preference with `prefers-color-scheme` media query, but let users override
6. Persist preference in `localStorage`

**What changes beyond swapping background/text colors:**

- Shadows: reduce opacity significantly or remove entirely. Dark surfaces don't cast visible shadows — use subtle borders or lighter surface colors to create elevation instead.
- Borders: increase visibility. Use `border-border` (which maps to a lighter value in dark mode) rather than hardcoded colors.
- Images and illustrations: reduce brightness slightly (`brightness-90`). Avoid pure-white images on dark backgrounds.
- Status colors: adjust saturation down and lightness up. A red that works on white won't work on dark gray — it needs to be softer.
- Hover states: use `hover:bg-muted` rather than hardcoded opacity changes. Light mode hovers darken, dark mode hovers lighten.
- Focus rings: ensure visibility on dark backgrounds. Default blue rings work; custom colored rings may not.

## Common Mistakes

| Mistake | What to do instead |
|---|---|
| Building a custom component library from scratch | Use shadcn/ui. Customize after shipping. |
| Only implementing the success state | Build all five states (loading, empty, error, success, overflow) for every data component |
| Using spinners everywhere | Skeleton loaders for inline content, spinners only for page-level or button loading |
| Fixed layouts that don't respond to screen size | Mobile-first responsive with Tailwind breakpoints, test at 375px width |
| Hiding critical actions in dropdown menus | Primary actions get dedicated buttons, only secondary/tertiary go in menus |
| Pixel-perfect custom breakpoints | Use Tailwind's standard breakpoints — they cover real devices |
| Dark mode as an afterthought | Decide at project start: implement now or explicitly defer. Don't half-implement. |
| Tables on mobile with horizontal scroll only | Transform tables into card layouts on mobile, showing key data points |
| Modals on top of modals | One modal at a time. Use sheets/slide-outs for secondary actions from a modal. |
| Inconsistent spacing between sections | Pick a page section gap and stick with it: `space-y-8` for page sections, `space-y-4` within sections |
