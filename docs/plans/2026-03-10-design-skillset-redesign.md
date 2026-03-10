# Design Skillset Redesign

## Problem

The current design skills are fragmented and miss the most critical capability: making apps actually look good. The `design/` skill tries to cover systems, components, UX principles, and design thinking in one skill. There's no skill for visual polish — the thing that separates Stripe from a Bootstrap template. And there's no workflow for auditing/elevating AI-generated UI.

## Goal

A complete skillset for taking a web app from AI-generated slop to polished, unique, fully responsive, good-looking, and with frictionless UX/UI. Target quality: Stripe, Linear, Vercel.

## Architecture: 6 Skills

### 1. Brand Identity (KEEP — minor updates)

**Trigger:** "Create a brand," "choose colors," "set up design tokens"

**Scope:** Design token generation — colors, typography, spacing scale, radius, shadows, iconography. The raw materials.

**Changes:** Trim component specs section (moves to UI Patterns). Otherwise keep as-is — this skill is already excellent.

### 2. Aesthetics (NEW)

**Trigger:** "Make this look better," "this looks like a template," "how do I make it look like Stripe," "it looks off but I can't say why"

**Scope:**
- Visual hierarchy — size, weight, color, contrast to guide the eye
- Whitespace — when to add space, when density is appropriate, breathing room
- Composition — arranging elements on a page, visual balance, alignment grids
- Color application — how to use your palette (not pick it). 60-30-10 rule. When to use accent vs neutral.
- Typography in practice — pairing weights, when to go subtle, line lengths, optical alignment
- Visual consistency — ensuring the same "feel" across pages
- AI slop patterns — what AI tools get wrong visually and specific fixes (too many borders, inconsistent spacing, overuse of cards, everything the same size, no hierarchy)
- Reference teardowns — what specifically makes Stripe/Linear/Vercel look premium

**Not covered:** Token selection (Brand Identity), component APIs (UI Patterns), user flows (UX), animations (Motion & Polish)

### 3. UI Patterns (REWORK of current design skill)

**Trigger:** "Build a dashboard," "add a settings page," "create a data table," "make this responsive," "implement dark mode"

**Scope:**
- Component library selection and setup (shadcn, Radix, etc.)
- Page layout patterns — dashboard, list/detail, settings, profile, billing, empty/zero-data
- Data display — tables, cards, metrics/KPIs, charts, lists
- Forms — input patterns, validation, multi-step forms, inline editing
- Navigation components — sidebar, top nav, command palette, breadcrumbs, tabs, mobile nav
- Responsive implementation — breakpoints, what changes at each, mobile-first, touch targets
- States — loading/skeleton, empty, error, success, disabled, hover, focus, selected
- Dark mode — implementation strategy
- Common page compositions

**Not covered:** Whether it looks good (Aesthetics), flow between pages (UX), animations (Motion & Polish)

### 4. UX Design (NEW — absorbs navigation, onboarding, accessibility)

**Trigger:** "This flow feels clunky," "users are confused," "how should signup work," "plan the navigation," "make it accessible"

**Scope:**
- Information architecture — page hierarchy, URL structure, where things live, mental models
- User flows — task analysis, step reduction, friction identification
- Navigation design — patterns, wayfinding, sidebar vs tabs vs breadcrumbs
- Onboarding — aha moment, progressive disclosure, first-run, activation
- Interaction patterns — feedback, confirmation, undo vs confirm, inline vs modal
- Progressive disclosure — what to show when, reducing cognitive load
- Accessibility — semantic HTML, keyboard nav, screen readers, contrast, ARIA (tiered)
- Error handling UX — recovery paths
- Performance perception — optimistic updates, skeleton screens

**Not covered:** Visual styling (Aesthetics), component specs (UI Patterns), copy (copywriting skill)

### 5. Motion & Polish (NEW)

**Trigger:** "Add animations," "make transitions smooth," "it feels static," "add micro-interactions," "the final polish"

**Scope:**
- Transition patterns — what to animate, duration/easing, enter/exit
- Micro-interactions — button feedback, hover states, toggle animations
- Page transitions — route changes, content loading, list reordering
- Scroll interactions — sticky headers, scroll-triggered reveals
- Loading & progress — spinners, progress bars, skeleton shimmer, optimistic UI
- Feedback animations — success/error/warning, toast entrance
- Reduced motion — respecting prefers-reduced-motion
- CSS vs JS animation — when to use which, performance
- Restraint principle — what NOT to animate

**Not covered:** Static appearance (Aesthetics), component structure (UI Patterns)

### 6. Design Review (NEW)

**Trigger:** "Review the design," "audit the UI," "what should I fix," "is this good enough to ship"

**Scope:**
- Visual audit checklist — spacing, alignment, hierarchy, color, typography
- AI-generation antipattern detection and fixes
- Responsive audit — every breakpoint, common breakage
- Consistency check — same patterns across pages
- Accessibility audit — automated + manual, WCAG
- Performance audit — layout shift, paint times, images
- Priority framework — what to fix first for max impact
- Before/after methodology

**Not covered:** Doesn't generate designs from scratch (other skills). This is the quality gate.

## Skill Chaining

```
Brand Identity → defines tokens
     ↓
Aesthetics → how to apply tokens beautifully
UI Patterns → how to build components/pages
UX Design → how to structure flows/architecture
     ↓
Motion & Polish → the final 10%
     ↓
Design Review → quality gate before shipping
```

## Migration Plan

| Current Skill | Fate |
|---|---|
| `design/` | Split into Aesthetics + UI Patterns |
| `brand-identity-generator/` | Keep (minor trim) |
| `navigation/` | Absorb into UX Design |
| `onboarding/` | Absorb into UX Design |
| `accessibility/` | Absorb into UX Design |
| `ux-ui-design/` | Delete (replaced by this system) |
| `copywriting/` | Keep as-is (separate concern) |
| `landing-page/` | Keep as-is (separate concern) |
| `conversion/` | Keep as-is (separate concern) |

## Key Design Decisions

1. **Split UX from UI** — Claude loads only what's relevant to the task. "Make this look better" doesn't need flow analysis. "This flow is clunky" doesn't need spacing principles.
2. **Aesthetics as its own skill** — The biggest gap in the current system. The hardest thing to get right. Deserves dedicated, deep treatment.
3. **Design Review as quality gate** — No current skill addresses "evaluate and improve what exists." Critical for the AI-tool workflow where you start from generated output.
4. **Absorb navigation/onboarding/accessibility into UX** — These are all UX subdisciplines. Keeping them separate fragments the UX perspective.
5. **Motion & Polish separate** — This is a distinct phase of work ("make it feel premium") and a distinct set of knowledge (timing, easing, performance).
