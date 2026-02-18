---
name: brand
description: "Use this skill when the user needs to create a brand identity, choose a color palette, design a logo, establish design tokens, or build visual consistency for their SaaS product. Covers color systems, typography, logo design, and brand recognition."
---

# Brand Identity & Visual Design

A brand is not a logo. It's the gut feeling people have about your product. This skill helps you make the decisions that define your brand — then hand them to Claude Code to implement everywhere.

## Core Principles

- Consistency is more important than creativity. A mediocre system applied consistently beats brilliant one-offs.
- Visual design should make the product feel inevitable — like it couldn't look any other way.
- Every SaaS product should feel: trustworthy, modern, and clear. Your differentiator comes on top of these.
- Design for recognition at every scale: favicon, app icon, social preview, full-screen dashboard.

---

## What You Decide vs. What AI Implements

| You Decide | Claude Code Implements |
|------------|----------------------|
| Primary brand color (emotional fit for your audience) | All tints, shades, hover/active states |
| Whether the tone is warm or cool | Full neutral scale (9-11 shades) |
| Heading font and body font | Typography scale, weights, line heights |
| Brand voice (casual vs. formal) | Consistent application across UI |
| Whether to support dark mode at launch | Dark mode color mapping |
| Icon style (rounded, squared, minimal) | Icon integration throughout app |

**Rule:** Make the creative decisions. Let AI handle the math, code, and consistency.

---

## Color System

You need three things:

### 1. Primary Color (You Pick This)

Your brand's signature. Used for buttons, links, and key accents.

**How to choose:**
- What emotion should your product evoke? (Blue = trust, Green = growth, Purple = premium, Orange = energy)
- Look at competitors — pick something that stands out from them
- Test it: does it look good as a button on a white background?

**Tell AI:**
```
My brand's primary color is [your hex code or color name].
Generate a full color system:
- Primary scale (50-900 tints)
- Neutral scale (warm/cool gray, 50-900)
- Semantic colors (success green, warning amber, error red, info blue)
- Surface colors (background, card, elevated, overlay)
Apply this as CSS custom properties and/or Tailwind config.
```

### 2. Neutral Scale (AI Generates This)

9-11 shades from near-white to near-black. This does 80% of the work in your UI (text, backgrounds, borders). AI generates this from your warm/cool preference.

### 3. Semantic Colors (AI Generates This)

Success (green), Warning (amber), Error (red), Info (blue). AI picks these to not clash with your primary color.

---

## Typography

**Two decisions to make:**

1. **Heading font:** Pick one with personality but legibility. Good defaults for SaaS: Inter, Plus Jakarta Sans, Outfit, Geist.
2. **Body font:** Prioritize readability at 14-16px. Often the same as headings.

**Tell AI:**
```
My heading font is [font name] and body font is [font name].
Set up a typography system:
- Scale: 0.75rem to 3rem
- Weights: Regular (400) for body, Medium (500) for emphasis, Semibold (600) for headings
- Line heights optimized for readability
- Apply across all headings, body text, and UI elements.
```

**Skip for now:** Monospace font selection. Only matters if your product shows code or data tables — Claude Code will pick a sensible default.

---

## Logo

Most solo founders should NOT design their own logo. Instead:

**Minimum viable logo:**
1. Choose a clean sans-serif font
2. Type your product name
3. Pick your primary brand color

**Tell AI:**
```
Create a simple text-based logo for [product name]:
- Font: [your heading font] in Semibold
- Color: [your primary color]
- Create versions: full wordmark, icon-only (first letter or abbreviation), favicon (16x16)
- Export as SVG for web
```

**Requirements for any logo:**
- Works at 16x16 (favicon), 32x32, and full size
- Horizontal lockup (icon + wordmark) for headers
- Icon-only version for compact spaces
- Works on light and dark backgrounds
- SVG format for web (not PNG)

**When to invest in a real logo:** After you've validated your product and have paying customers. Budget $200-500 for a freelance designer on Fiverr or 99designs. Don't spend $5,000 pre-launch.

---

## Icons

One decision: pick an icon library and stick with it.

| Style | Library | Best For |
|-------|---------|----------|
| Rounded/friendly | Lucide | Consumer SaaS, creative tools |
| Clean/professional | Heroicons | Business SaaS, dashboards |
| Versatile/detailed | Phosphor | Products needing many icon variants |

**Tell AI:**
```
Use [Lucide/Heroicons/Phosphor] icons throughout the app.
Never mix icon libraries. Keep icons at consistent sizes (16px inline, 20px buttons, 24px navigation).
```

---

## Brand Voice Attributes

Define 3-4 positions on these spectrums. These feed into copywriting and UI text decisions:

- Casual ←————→ Formal
- Playful ←————→ Serious
- Technical ←————→ Approachable
- Bold ←————→ Understated

**Example:** A project management tool for freelancers might be: Casual, Slightly Playful, Approachable, Bold.

**Tell AI:**
```
Our brand voice is [casual/formal], [playful/serious], [approachable/technical], and [bold/understated].
Apply this tone to all UI copy, error messages, and empty states.
```

---

## Social Preview / OG Image

Every page needs an Open Graph image for social sharing.

- Size: 1200x630px
- Template: Brand color background + page title in heading font + product logo in corner

**Tell AI:**
```
Create a reusable OG image template:
- Background: our primary color (or gradient)
- Title text: white, our heading font, centered
- Logo: small, bottom-right corner
- Generate dynamically for blog posts using page title.
```

---

## Dark Mode (Decide Later)

For your MVP, ship light mode only. Dark mode is a nice-to-have that doubles your design surface area.

**When to add dark mode:**
- Users are requesting it
- Your product is used for long sessions (dashboards, writing tools, dev tools)
- You're past MVP and have bandwidth

**When you're ready, Tell AI:**
```
Add dark mode support:
- Background: dark gray (#111), not pure black
- Cards: slightly lighter than background (#1a1a1a)
- Text: off-white (#e5e5e5 body, #fafafa headings), not pure white
- Adjust primary color if needed for contrast
- Use CSS custom properties so themes switch cleanly
- Add a toggle in the header/settings
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Spending weeks on branding before validating | Pick a color, font, and name. Ship. Rebrand after PMF |
| Mixing icon libraries | Pick one, use it everywhere |
| Pure black backgrounds in dark mode | Use #111 or #0a0a0a, not #000 |
| Inconsistent color usage | Define system once, reference everywhere |
| Designing a logo before having customers | Use text-based logo until post-validation |
| Overthinking typography | Inter or your heading font for everything. Done |

---

## Output Format

When creating or reviewing brand identity:

1. **Decisions:** What primary color, fonts, icon library, and voice attributes were chosen
2. **System:** Color scale, type scale, and spacing as CSS properties or Tailwind config
3. **Application:** Show how system applies across 2-3 contexts (button, card, page header)
4. **Assets:** Logo versions, OG image template, favicon
