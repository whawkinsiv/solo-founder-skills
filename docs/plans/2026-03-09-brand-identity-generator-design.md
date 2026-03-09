# Brand Identity Generator — Design Document

## Problem

Our existing `brand/SKILL.md` is educational content with no action or output. Founders read guidance about branding decisions but still have nothing concrete to use. Meanwhile, AI tools (Claude Code, Codex, Cursor) fill design gaps with generic AI slop — gratuitous gradients, random shadows, inconsistent states, stock-photo energy.

We need a skill that produces a comprehensive, project-level brand identity document that leaves no room for AI improvisation.

## Solution

### What We're Building

1. **`brand-identity-generator/SKILL.md`** — A new skill in this plugin. Replaces `brand/SKILL.md`. Walks founders through creating their brand identity via guided discovery. Has a clear action and output.

2. **`BRAND-IDENTITY.md`** — The output. A standalone file dropped into the user's project root. Not a skill. Referenced by any AI tool working in the codebase.

### What We're Deleting

- `skills/brand/SKILL.md` — Absorbed into the generator. Educational-only content with no action doesn't belong as a skill.

## Generator Skill Design

### Discovery Process

Two paths, auto-detected:

**Default path (non-designers):**
1. Ask: "What are you building and who is it for?"
2. Based on the answer, recommend a complete brand identity with plain-English reasoning, citing reference brands
3. User reacts ("love it" / "I want it warmer" / "I hate green")
4. Skill adjusts and re-proposes
5. Generate `BRAND-IDENTITY.md`

**Expert path (designers):**
- Detect when user provides specific design tokens (hex codes, font names, radius values)
- Skip discovery, generate output, fill gaps with smart defaults

### Reference Brand Library

24 brands across 7 categories, baked into the skill:

| Category | Brands |
|----------|--------|
| Minimal/Precise | Stripe, Linear, Vercel, Superhuman |
| Warm/Approachable | Notion, Basecamp, Mailchimp, Canva |
| Collaborative/Social | Slack, Figma, Loom, Discord |
| Trust/Authority | Plaid, Gusto, Mercury, Wise |
| Calm/Wellness | Calm, Headspace, Apple Health |
| Bold/Consumer | Spotify, Duolingo, Robinhood |
| Data/Dashboard | Datadog, Mixpanel, Airtable |

Each reference includes: plain-English description of feel, target audience, and internal design patterns (colors, radius, spacing, typography, shadow usage) that Claude uses to generate recommendations.

### Enforced Best Practices

Injected into every output, non-negotiable:

- **Accessibility:** WCAG 2.1 AA contrast, focus indicators, 44px touch targets, color not sole indicator, visible form labels, logical heading hierarchy
- **Responsive:** Mobile-first breakpoints, fluid typography, no horizontal scroll, touch-friendly targets
- **Performance:** Max 2 font families, system fallbacks, font-display: swap
- **Typography readability:** 45-75 char line length, 16px minimum body, proper line heights

### Quality Gate

Before outputting, verify:
- All 12 sections populated
- All contrast ratios pass WCAG AA
- No gaps that invite AI improvisation
- All component state variants specified
- Anti-patterns list included

## Output Structure (`BRAND-IDENTITY.md`)

12 sections:

1. **Brand Context** — What the product is, who it's for, what feeling it evokes
2. **Colors** — Primary + state variants, secondary accents, full neutral scale (50-950), semantic colors with bg/border/text variants, surface colors, dark mode mapping (or explicit opt-out)
3. **Typography** — Fonts + fallbacks, full type scale (size, weight, line-height, letter-spacing), max line width, min body size, font loading strategy
4. **Spacing & Layout** — Base unit, full scale, component padding, section spacing, grid/container max-widths, breakpoints, mobile-first responsive rules
5. **Shape & Elevation** — Corner radius scale, shadow scale with exact values, when to use shadow vs border vs background change, border widths
6. **Iconography** — Library, sizes (inline/button/nav/decorative), stroke weight, color inheritance rules
7. **Animation & Motion** — Default duration/easing, what animates, what does NOT animate, prefers-reduced-motion support
8. **Component Specs** — Buttons, inputs, cards, badges, toasts, modals, tables, navigation. All states: default, hover, active, focus, disabled, loading, error. Exact values, not relative adjustments.
9. **Anti-Patterns** — Explicit "do not do this" list. No gratuitous gradients, no text shadows, no stock photos, no AI hero images, no decorative borders, no mixed icon libraries, etc.
10. **Accessibility (Enforced)** — WCAG 2.1 AA contrast, focus indicators, touch targets, color not sole indicator, visible labels, heading hierarchy, skip nav
11. **Responsive Design (Enforced)** — Mobile-first breakpoints, fluid type (clamp values), no horizontal scroll, touch targets, navigation mobile transform
12. **Application Examples** — Concrete CSS/Tailwind for: button row, card, form with validation, page header, data table row, empty state, error state, modal

## Relationship to Existing Skills

- **Replaces** `brand/SKILL.md` — absorbs useful content (logo guidance, common mistakes, what-you-decide-vs-AI)
- **Upstream of** `design/SKILL.md` — brand identity informs the component-level design system
- **No changes** to `design/SKILL.md` or any other existing skill

## Key Design Principle

The skill does the heavy lifting, not the user. Users speak human, the skill translates to design. Users react to proposals instead of generating ideas. Every gap in the output is an invitation for AI slop — leave no gaps.
