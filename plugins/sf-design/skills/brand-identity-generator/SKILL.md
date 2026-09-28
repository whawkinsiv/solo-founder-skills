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

Based on their answer, select the 1-2 closest reference brands from [references/brand-library.md](references/brand-library.md). Use the "Best for" field to match.

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

25 brands across 7 categories live in [references/brand-library.md](references/brand-library.md).
Read it during discovery. Use each brand's "Feel" line to talk to the user, and its
"Design DNA" line to derive real values.

---

## Output Template

The structure for the generated `BRAND-IDENTITY.md` is
[assets/brand-identity-template.md](assets/brand-identity-template.md). Copy it to the
project root as `BRAND-IDENTITY.md`, then replace every bracketed field with a real value.

Fill every field. No optional sections, no "TBD," no placeholders. Every gap you leave is
a gap an AI tool fills with a generic default, which is the exact failure this skill exists
to prevent. Section 12 of the template asks for eight worked component examples; every
value in them must come from a section above it, with nothing invented.

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
- When you have budget for a designer (\$500-2000 range)
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

- **beautify** — How to apply these tokens beautifully (visual hierarchy, whitespace, composition)
- **ui-patterns** — Component implementation and page layouts using these tokens
- **motion-polish** — Animation timing and micro-interactions that match the brand personality
- **design-review** — Quality gate to audit whether the UI correctly implements this identity
