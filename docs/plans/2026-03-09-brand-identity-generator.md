# Brand Identity Generator — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create a skill that walks founders through generating a comprehensive `BRAND-IDENTITY.md` file for their project, replacing the existing action-less `brand/SKILL.md`.

**Architecture:** Single skill file (`skills/brand-identity-generator/SKILL.md`) that contains the discovery process, 24-brand reference library, enforced web design best practices, and the full 12-section output template. The old `skills/brand/` directory is deleted.

**Tech Stack:** Markdown skill files (no code dependencies)

---

### Task 1: Delete the old brand skill

**Files:**
- Delete: `skills/brand/SKILL.md`

**Step 1: Delete the file**

```bash
rm skills/brand/SKILL.md
rmdir skills/brand
```

**Step 2: Search for references to the old skill**

```bash
grep -r "brand/SKILL" skills/ --include="*.md"
grep -r "skills/brand" . --include="*.md"
```

If any cross-references exist, note them for Task 3.

**Step 3: Commit**

```bash
git add -A skills/brand/
git commit -m "chore: remove action-less brand skill (replaced by brand-identity-generator)"
```

---

### Task 2: Create the brand-identity-generator skill

**Files:**
- Create: `skills/brand-identity-generator/SKILL.md`

**Step 1: Create the directory**

```bash
mkdir -p skills/brand-identity-generator
```

**Step 2: Write the SKILL.md**

Create `skills/brand-identity-generator/SKILL.md` with the following content. This is the full skill — it's long because it must be comprehensive enough that the output leaves no gaps for AI to fill with slop.

The file must contain these sections in order:

#### Frontmatter

```yaml
---
name: brand-identity-generator
description: "Use this skill when the user needs to create a visual brand identity for their product. Generates a comprehensive BRAND-IDENTITY.md file for the project root. Covers colors, typography, spacing, components, accessibility, and responsive design — with no gaps for AI to fill with generic defaults."
---
```

#### Section: Overview

- One-sentence purpose: generates a `BRAND-IDENTITY.md` file for the user's project
- Two modes: guided discovery (default) and expert shortcut
- The output is a project-level reference file, not a skill

#### Section: Discovery Process

Instructions for Claude on how to guide the user. Must include:

**Default path:**
1. Ask ONE question: "What are you building and who is it for?"
2. Based on the answer, select the closest reference brand(s) from the library
3. Propose a COMPLETE brand identity in plain English. Example tone: "Your users are developers who'll have this open all day. Products that succeed in this space — like Linear and GitHub — use calm, minimal aesthetics because your users stare at this 8 hours a day. Here's what I'd recommend for you and why..."
4. Present the recommendation as a human-readable summary (NOT the full 12-section spec — that comes after approval)
5. User reacts: "love it" / "warmer" / "I hate green" / "more like Notion"
6. Adjust and re-propose until user approves
7. Generate the full `BRAND-IDENTITY.md`

**Expert path:**
- Detect when user provides specific design tokens (hex codes, font names, radius values, etc.)
- Acknowledge what they've specified, fill gaps with smart defaults informed by their choices
- Skip discovery, go straight to generating output
- Still apply all enforced best practices (accessibility, responsive, etc.)

Key instruction: "The user should never need to use design vocabulary. They react to your proposals. You do the heavy lifting."

#### Section: Reference Brand Library

24 brands organized by category. For each brand, include:
- **Category** (for internal organization)
- **Feel** (plain-English, 5-10 words — this IS shown to user)
- **Best for** (audience/product type)
- **Design DNA** (the actual patterns — for Claude's internal use when generating):
  - Color temperature (warm/cool/neutral)
  - Spacing density (spacious/moderate/dense)
  - Corner radius tendency (sharp/moderate/rounded/pill)
  - Shadow usage (none/subtle/moderate/prominent)
  - Typography character (geometric/humanist/monospace-accented)
  - Visual weight (light/medium/heavy)
  - Contrast approach (high/moderate/low)

Full brand list:

**Minimal/Precise:**
- Stripe — Precise, confident, no wasted space. Best for: financial tools, APIs, B2B platforms. DNA: cool, moderate density, moderate radius, subtle shadows, geometric type, medium weight, high contrast.
- Linear — Fast, quiet, stays out of your way. Best for: dev tools, productivity, power users. DNA: cool, moderate density, moderate radius, minimal shadows, geometric type, light weight, high contrast.
- Vercel — Bold, dark, futuristic. Best for: technical platforms, developer tools. DNA: cool, moderate density, sharp radius, no shadows, geometric type, heavy weight, high contrast.
- Superhuman — Luxurious, dense, keyboard-driven. Best for: premium productivity, speed-focused tools. DNA: cool, dense, moderate radius, subtle shadows, geometric type, medium weight, high contrast.

**Warm/Approachable:**
- Notion — Warm, inviting, like a blank notebook. Best for: creative tools, knowledge work, flexible platforms. DNA: warm, spacious, moderate radius, subtle shadows, humanist type, light weight, moderate contrast.
- Basecamp — Honest, unpretentious, handmade feel. Best for: small business tools, opinionated products. DNA: warm, spacious, rounded radius, no shadows, humanist type, medium weight, moderate contrast.
- Mailchimp — Quirky, fun, doesn't take itself too seriously. Best for: small business marketing, email tools. DNA: warm, spacious, rounded radius, subtle shadows, humanist type, medium weight, moderate contrast.
- Canva — Bright, encouraging, "you can do this." Best for: creative tools for non-designers, consumer. DNA: warm, moderate density, rounded radius, subtle shadows, geometric type, medium weight, high contrast.

**Collaborative/Social:**
- Slack — Friendly, colorful, energetic. Best for: team communication, collaboration tools. DNA: warm, moderate density, rounded radius, subtle shadows, humanist type, medium weight, high contrast.
- Figma — Playful, creative, multiplayer. Best for: design collaboration, creative tools. DNA: neutral, moderate density, rounded radius, subtle shadows, geometric type, medium weight, high contrast.
- Loom — Personal, casual, lightweight. Best for: async video, internal communications. DNA: warm, spacious, rounded radius, moderate shadows, humanist type, light weight, moderate contrast.
- Discord — Bold, youthful, expressive. Best for: community platforms, gaming-adjacent tools. DNA: cool, moderate density, rounded radius, moderate shadows, geometric type, heavy weight, high contrast.

**Trust/Authority:**
- Plaid — Trustworthy, institutional, safe. Best for: fintech infrastructure, banking APIs. DNA: cool, moderate density, moderate radius, no shadows, geometric type, medium weight, high contrast.
- Gusto — Approachable authority, grown-up but not stuffy. Best for: HR/payroll, small business operations. DNA: warm, spacious, rounded radius, subtle shadows, humanist type, medium weight, moderate contrast.
- Mercury — Sleek, premium, quietly confident. Best for: business banking, B2B finance. DNA: cool, spacious, moderate radius, subtle shadows, geometric type, light weight, high contrast.
- Wise — Transparent, clean, no-nonsense. Best for: international finance, consumer fintech. DNA: cool, spacious, moderate radius, no shadows, geometric type, light weight, high contrast.

**Calm/Wellness:**
- Calm — Soft, spacious, like a deep breath. Best for: meditation, wellness, low-stress apps. DNA: warm, spacious, rounded radius, no shadows, humanist type, light weight, low contrast.
- Headspace — Warm, illustrated, gentle. Best for: mental health, consumer wellness. DNA: warm, spacious, pill radius, no shadows, geometric type, medium weight, low contrast.
- Apple Health — Clinical but friendly, data-forward. Best for: health/fitness tracking, consumer health. DNA: neutral, moderate density, rounded radius, no shadows, geometric type, light weight, moderate contrast.

**Bold/Consumer:**
- Spotify — Dark, vibrant, high-energy. Best for: entertainment, media, consumer apps. DNA: cool, moderate density, pill radius, no shadows, geometric type, heavy weight, high contrast.
- Duolingo — Playful, cartoonish, addictive. Best for: education, gamified products. DNA: warm, spacious, rounded radius, moderate shadows, geometric type, heavy weight, high contrast.
- Robinhood — Simple, green, "investing is easy." Best for: consumer fintech, simple trading. DNA: neutral, spacious, moderate radius, no shadows, geometric type, light weight, moderate contrast.

**Data/Dashboard:**
- Datadog — Dense, dark, information-rich. Best for: monitoring, infrastructure, DevOps. DNA: cool, dense, sharp radius, no shadows, monospace-accented type, medium weight, moderate contrast.
- Mixpanel — Clean data viz, chart-forward. Best for: analytics, product teams. DNA: cool, moderate density, moderate radius, subtle shadows, geometric type, light weight, moderate contrast.
- Airtable — Colorful, organized, approachable complexity. Best for: structured data, spreadsheet-plus tools. DNA: warm, moderate density, rounded radius, subtle shadows, geometric type, medium weight, high contrast.

#### Section: Output Template

The full 12-section `BRAND-IDENTITY.md` template. This is the structure Claude fills in based on discovery. Every field must be specified — no optional sections, no "TBD."

**Section 1 — Brand Context:**
```markdown
## Brand Context
- **Product:** [What this product is]
- **Audience:** [Who uses it and in what context]
- **Feel:** [Plain-English description of intended feeling]
- **Reference:** [1-2 reference brands and what to take from each]
```

**Section 2 — Colors:**
Must include:
- Primary color + hover, active, disabled variants (exact hex)
- Secondary accent + same variants
- Full neutral scale: 50, 100, 150, 200, 300, 400, 500, 600, 700, 800, 900, 950 with one-line usage note per shade
- Semantic colors: success, warning, error, info — each with: text, background, border hex values
- Surface colors: page background, card background, elevated surface, overlay backdrop
- Dark mode: either full mapping OR explicit statement "Dark mode is not supported. Do not generate dark mode variants."

**Section 3 — Typography:**
Must include:
- Heading font + system fallback stack
- Body font + system fallback stack
- Monospace font (if applicable) + fallback
- Full type scale: display, h1, h2, h3, h4, body-lg, body, body-sm, caption, overline — each with: font-size (rem + px), font-weight, line-height, letter-spacing
- Max line width: value in `ch` units
- Minimum body font size: 16px (enforced)
- Font loading: `font-display: swap`, preload strategy

**Section 4 — Spacing & Layout:**
Must include:
- Base unit (e.g., 4px)
- Full spacing scale: 0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24 (mapped to px)
- Component internal padding: buttons, inputs, cards, modals
- Section spacing: between page sections
- Container max-widths per breakpoint
- Breakpoints: sm, md, lg, xl with exact px values
- Grid: column count, gutter width

**Section 5 — Shape & Elevation:**
Must include:
- Corner radius scale: none (0), sm, default, md, lg, xl, full (9999px) with px values
- Where each radius is used (buttons=default, cards=md, pills=full, etc.)
- Shadow scale: none, xs, sm, md, lg, xl with exact CSS values
- When to use shadow vs border vs background color change
- Border: default width (1px), colors for default/strong/subtle

**Section 6 — Iconography:**
Must include:
- Icon library name (Lucide, Heroicons, Phosphor, etc.)
- Sizes: inline (16px), button (18px), navigation (20px), feature/decorative (24px)
- Stroke weight (e.g., 1.5px for Lucide)
- Color rules: when icons inherit text color, when they use muted color, when they use accent
- "Never mix icon libraries"

**Section 7 — Animation & Motion:**
Must include:
- Default transition: duration (e.g., 150ms), easing (e.g., ease-out)
- What animates: button/link hover, focus rings, modal open/close, dropdown open/close, page transitions (if any)
- What does NOT animate: layout shifts, color scheme changes, font changes, scroll position
- Reduced motion: `@media (prefers-reduced-motion: reduce)` — remove all non-essential animation
- "No decorative animations (bouncing, pulsing, floating) unless explicitly specified below"

**Section 8 — Component Specs:**
For EACH of: Button, Input, Card, Badge, Toast/Notification, Modal/Dialog, Table, Navigation — specify ALL of these states with exact values:
- Default state
- Hover state
- Active/pressed state
- Focus state (ring color, width, offset)
- Disabled state (opacity or specific colors)
- Loading state (how it looks)
- Error state (where applicable)

Example format for one component:
```markdown
### Button
| Property | Primary | Secondary | Ghost | Destructive |
|----------|---------|-----------|-------|-------------|
| Background | #XXXXXX | #XXXXXX | transparent | #XXXXXX |
| Text | #XXXXXX | #XXXXXX | #XXXXXX | #XXXXXX |
| Border | none | 1px #XXXXXX | none | none |
| Height | 40px | 40px | 40px | 40px |
| Padding | 12px 20px | 12px 20px | 12px 20px | 12px 20px |
| Radius | [from scale] | [from scale] | [from scale] | [from scale] |
| **Hover** | bg #XXXXXX | bg #XXXXXX | bg #XXXXXX | bg #XXXXXX |
| **Active** | bg #XXXXXX | bg #XXXXXX | bg #XXXXXX | bg #XXXXXX |
| **Focus** | ring 2px #XXXXXX offset 2px | ... | ... | ... |
| **Disabled** | opacity 0.5, no pointer | ... | ... | ... |
| **Loading** | spinner replaces text, same bg | ... | ... | ... |
```

**Section 9 — Anti-Patterns:**
Must include at minimum:
- No gratuitous gradients (unless explicitly specified in Colors section)
- No drop shadows on text
- No stock photography or generic illustrations
- No AI-generated hero/feature images unless explicitly directed
- No decorative borders or dividers that don't serve visual hierarchy
- Never mix icon libraries
- No color as sole indicator of meaning
- No placeholder-only form labels (always visible labels)
- No pure black (#000) backgrounds — use darkest neutral
- No pure white (#fff) text on dark backgrounds — use lightest neutral
- No more than 2 font families
- No font sizes below 12px (14px minimum for body text, 12px only for captions/labels)
- No horizontal scrolling at any viewport width
- [Brand-specific anti-patterns derived from discovery]

**Section 10 — Accessibility (Enforced):**
Must include:
- WCAG 2.1 AA minimum: 4.5:1 for normal text, 3:1 for large text (18px+ bold or 24px+)
- Focus indicators: visible on ALL interactive elements, minimum 2px, sufficient contrast
- Touch/click targets: minimum 44x44px
- Color: never the sole indicator of meaning (always pair with icon, text, or pattern)
- Form labels: always visible, positioned above input, associated with `for`/`id`
- Heading hierarchy: no skipping levels (h1 → h2 → h3, never h1 → h3)
- Skip navigation: include skip-to-main-content link
- Alt text: required on all meaningful images, empty `alt=""` on decorative images
- Contrast ratios for every color pairing in the Colors section must be listed

**Section 11 — Responsive Design (Enforced):**
Must include:
- Mobile-first: base styles are mobile, larger breakpoints add complexity
- Breakpoints: exact values (e.g., sm: 640px, md: 768px, lg: 1024px, xl: 1280px)
- Fluid typography: `clamp()` values for key type sizes (h1, h2, body at minimum)
- No horizontal scroll at any breakpoint
- Touch targets: 44px minimum on mobile
- Navigation: how it transforms (e.g., sidebar → hamburger, topnav → bottom nav)
- Images: `max-width: 100%`, responsive loading with `srcset` where applicable
- Container: max-width with auto margins, padding on mobile

**Section 12 — Application Examples:**
Concrete CSS custom properties + Tailwind class examples for:
- A primary button + secondary button side by side
- A card with heading, body text, and action
- A form with label, input, helper text, and error state
- A page header with logo, navigation, and CTA
- A data table row with status badge and action menu
- An empty state with icon, message, and CTA
- An error state (inline and full-page)
- A modal with header, body, and action buttons

Each example should use the actual values from the preceding sections — not generic placeholders.

#### Section: Absorbed Content from Old Brand Skill

Include useful guidance absorbed from the deleted `brand/SKILL.md`:

**Logo guidance:**
- Most solo founders should NOT design their own logo
- Minimum viable logo: clean sans-serif font + product name + brand color
- Create versions: full wordmark, icon-only (first letter), favicon (16x16)
- Export as SVG
- When to invest in a real logo: after validation with paying customers

**What you decide vs. what AI implements:**
| You Decide | AI Implements |
|------------|---------------|
| Primary brand color | All tints, shades, state variants |
| What your product is and who it's for | Visual personality derived from audience |
| "I like the feel of [reference brand]" | Concrete design tokens that create that feel |
| Whether to support dark mode | Full dark mode color mapping |

**Common mistakes:**
| Mistake | Fix |
|---------|-----|
| Spending weeks on branding pre-validation | Generate a BRAND-IDENTITY.md in 10 minutes. Revisit after PMF |
| Describing what you want in design jargon | Just say what you're building and who for. React to proposals |
| Leaving gaps in the brand spec | Every gap = AI fills with generic slop. Be comprehensive |
| Inconsistent application | Reference BRAND-IDENTITY.md from project root. One source of truth |
| Designing a logo before having customers | Use text-based logo until post-validation |

#### Section: Quality Gate

Before generating the final `BRAND-IDENTITY.md`, Claude must verify:
- [ ] All 12 sections are fully populated — no "TBD," no empty fields
- [ ] Every color pairing used in component specs passes WCAG 2.1 AA contrast (4.5:1 normal text, 3:1 large text)
- [ ] All component states are specified (no missing hover/focus/disabled)
- [ ] Anti-patterns list includes at least 10 items plus brand-specific ones
- [ ] Fluid typography clamp() values are mathematically correct
- [ ] Spacing scale is internally consistent
- [ ] Application examples use actual values from preceding sections (no placeholders)
- [ ] Font loading strategy is specified
- [ ] Dark mode is either fully mapped or explicitly opted out
- [ ] All accessibility requirements are present and specific

**Step 3: Commit**

```bash
git add skills/brand-identity-generator/SKILL.md
git commit -m "feat: add brand-identity-generator skill with guided discovery and comprehensive output template"
```

---

### Task 3: Fix cross-references

**Files:**
- Potentially modify: any files that reference `skills/brand` or `brand/SKILL.md`

**Step 1: Search for references**

```bash
grep -r "brand/SKILL" . --include="*.md"
grep -r "skills/brand" . --include="*.md"
grep -r "brand skill" . --include="*.md" -i
```

**Step 2: Update any references found**

Replace references to the old `brand` skill with `brand-identity-generator`. Update any descriptions that mention the old skill's educational purpose to reflect the new skill's generator purpose.

**Step 3: Update plugin description if needed**

Check `.claude-plugin/plugin.json` — the description mentions "45 skills." The count stays the same (deleted one, added one), so no change needed unless the skill name appears.

**Step 4: Commit**

```bash
git add -A
git commit -m "chore: update cross-references from brand to brand-identity-generator"
```

---

### Task 4: Verify the skill works in the plugin structure

**Step 1: Verify skill discovery**

```bash
ls -la skills/brand-identity-generator/SKILL.md
```

Confirm file exists and has correct frontmatter.

**Step 2: Verify frontmatter format**

Read the first 5 lines of the file. Confirm:
- Line 1: `---`
- Line 2: `name: brand-identity-generator`
- Line 3: `description:` with quoted string
- Line 4: `---`

**Step 3: Verify no orphaned files**

```bash
ls skills/brand/ 2>/dev/null && echo "ERROR: old brand dir still exists" || echo "OK: old brand dir removed"
```

**Step 4: Commit (if any fixes needed)**

```bash
git add -A
git commit -m "fix: ensure brand-identity-generator skill structure matches plugin conventions"
```

---

## Execution Notes

- Task 2 is the bulk of the work — writing the full SKILL.md file. The content is fully specified in this plan.
- The SKILL.md will be long (likely 400-600 lines) because comprehensiveness prevents AI slop. This is intentional.
- The reference brand library data (Design DNA) is internal to the skill — Claude uses it to inform recommendations but doesn't dump the raw table on users.
- All web design best practices in sections 10-11 of the output template are non-negotiable and get included in every generated `BRAND-IDENTITY.md` regardless of brand choices.
