# Design Skillset Redesign — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the fragmented design skills (design, navigation, onboarding, accessibility) with 6 focused skills: Brand Identity, Aesthetics, UI Patterns, UX Design, Motion & Polish, Design Review.

**Architecture:** Each skill is a directory under `skills/` containing `SKILL.md` (required) plus optional supporting files. Skills use YAML frontmatter with `name` and `description`. Content is written for Claude consumption — opinionated, specific, actionable. No "Tell AI:" prompts (those were for the old non-technical founder audience; these skills ARE the AI instructions).

**Tech Stack:** Markdown files with YAML frontmatter. No code dependencies.

**Conventions:**
- File names: ALL CAPS with hyphens (`SKILL.md`, `AI-SLOP-FIXES.md`)
- Frontmatter: `name` (kebab-case) and `description` (trigger-focused, starts with "Use this skill when...")
- Max 1 level of supporting files deep from SKILL.md
- Skills reference each other by name in parenthetical notes, not inline links
- Content assumes Claude's intelligence — focus on WHAT to do and WHEN, not explaining concepts

---

### Task 1: Create the Aesthetics Skill

This is the highest-value new skill — the biggest gap in the current system. Write it first so we can validate the quality bar.

**Files:**
- Create: `skills/aesthetics/SKILL.md`
- Create: `skills/aesthetics/AI-SLOP-FIXES.md`
- Create: `skills/aesthetics/REFERENCE-TEARDOWNS.md`

**Step 1: Write `skills/aesthetics/SKILL.md`**

The core skill file. Covers:
- Visual hierarchy (size, weight, color, contrast)
- Whitespace and breathing room (when to add, when density is correct)
- Composition and layout balance (alignment grids, visual weight distribution)
- Color application (60-30-10, accent usage, saturation management — NOT color selection)
- Typography in practice (weight pairing, optical alignment, line length — NOT font/scale selection)
- Visual consistency across pages
- The difference between "technically correct" and "beautiful"

Frontmatter:
```yaml
---
name: aesthetics
description: "Use this skill when the user wants to make their app look better, says it looks like a template, asks how to achieve Stripe/Linear quality, or says something looks off. Covers visual hierarchy, whitespace, composition, color application, and typography in practice."
---
```

Structure the content as:
1. Brief intro (2-3 sentences — what this skill is for)
2. Core principles (5-7 numbered items, each 1-2 sentences)
3. Visual Hierarchy section (the most important topic — how to guide the eye)
4. Whitespace section (when to add space, when density is right)
5. Color Application section (how to USE a palette, not choose one)
6. Typography in Practice section (weight pairing, sizing relationships)
7. Composition section (page-level balance, alignment, visual rhythm)
8. Consistency section (cross-page coherence checks)
9. Quick reference checklist (audit any screen in 60 seconds)

Each section should be 100-200 words max. Total SKILL.md target: ~1500 words. Dense, no filler.

**Step 2: Write `skills/aesthetics/AI-SLOP-FIXES.md`**

A pattern library of specific AI-generation antipatterns and their fixes. Structure as a table or repeated pattern:

```
### [Pattern Name]
**Symptom:** What it looks like
**Why AI does this:** Brief explanation
**Fix:** Specific instructions
**Before/After:** Described in words (CSS/Tailwind where helpful)
```

Cover these patterns (at minimum):
- Too many borders (everything has a border)
- Overuse of cards (flat content wrapped in unnecessary containers)
- Everything the same size (no hierarchy)
- Too much color / rainbow soup
- Generic spacing (everything 16px apart)
- Centered everything (when left-align is correct)
- Cluttered headers (too many elements competing)
- Identical page layouts (every page looks the same)
- Overly rounded corners
- Gratuitous shadows
- Placeholder-quality images and icons
- Inconsistent alignment between sections

Target: ~1500 words.

**Step 3: Write `skills/aesthetics/REFERENCE-TEARDOWNS.md`**

Analyze what makes 4-5 reference apps look premium. NOT "Stripe uses blue" — dig into the WHY.

Structure per reference:
```
### [App Name]
**Category:** [What type of app]
**Key aesthetic moves:**
- [Specific principle with specific example]
- [Specific principle with specific example]
- [Specific principle with specific example]
**What to steal:** [1-2 transferable lessons]
```

Apps to tear down:
- Stripe (dashboard) — data density with clarity
- Linear — dark mode minimalism, speed aesthetic
- Vercel — technical sophistication, typographic confidence
- Notion — calm, spacious, content-first
- Mercury — financial trust, clean premium

Target: ~1000 words.

**Step 4: Commit**

```bash
git add skills/aesthetics/
git commit -m "feat: add aesthetics skill — visual polish and quality principles"
```

---

### Task 2: Create the UI Patterns Skill

Rework the current `design/` skill content into a focused component/layout implementation guide.

**Files:**
- Create: `skills/ui-patterns/SKILL.md`
- Create: `skills/ui-patterns/COMPONENTS.md` (migrate + improve from `skills/design/COMPONENTS.md`)
- Create: `skills/ui-patterns/LAYOUTS.md`

**Step 1: Write `skills/ui-patterns/SKILL.md`**

Frontmatter:
```yaml
---
name: ui-patterns
description: "Use this skill when the user needs to build a dashboard, settings page, data table, or any page layout. Also use when choosing component libraries, implementing responsive design, dark mode, or handling UI states (loading, empty, error). Covers component selection, page composition, and responsive implementation."
---
```

Content structure:
1. Brief intro
2. Component library selection (keep shadcn recommendation, trim details)
3. Page composition principles (how to structure a page, content zones)
4. Responsive strategy (breakpoints, what changes at each, mobile-first)
5. UI States (loading/skeleton, empty, error, success — the full state matrix)
6. Dark mode implementation strategy
7. Common mistakes table

Migrate useful content from current `skills/design/SKILL.md` (the screen-by-screen guidance, component selection guide, visual hierarchy checklist). Drop the "Tell AI:" prompts — this IS the AI instructions now.

Target: ~1500 words.

**Step 2: Write `skills/ui-patterns/COMPONENTS.md`**

Migrate and improve from current `skills/design/COMPONENTS.md`. Remove "Tell AI:" prompts. Make it a reference Claude uses directly. Keep:
- Button patterns and variants
- Form patterns
- Card patterns
- Table patterns
- Modal/dialog patterns
- Input component specs
- Navigation component specs (sidebar, top nav, etc.)
- Loading state patterns

Add:
- Command palette pattern
- Toast/notification patterns
- Badge and status indicator patterns
- Dropdown menu patterns
- Sheet/slide-out panel patterns

Target: ~2000 words.

**Step 3: Write `skills/ui-patterns/LAYOUTS.md`**

Page-level layout templates for common SaaS pages. Structure each as:

```
### [Page Type]
**Structure:** ASCII layout diagram
**Key decisions:** What varies per implementation
**Common mistakes:** What goes wrong
```

Cover:
- Dashboard (metrics + activity + quick actions)
- List/table page (filters + data + pagination)
- Detail page (header + content sections + actions)
- Settings page (sidebar tabs + form sections)
- Billing page (plan info + usage + invoices)
- Profile page
- Empty/zero-data state (for any page type)
- Auth pages (login, signup, forgot password)
- Landing page (hero + features + social proof + pricing + CTA)
- Blog/content page

Target: ~1500 words.

**Step 4: Commit**

```bash
git add skills/ui-patterns/
git commit -m "feat: add ui-patterns skill — components, layouts, and responsive design"
```

---

### Task 3: Create the UX Design Skill

Absorb navigation, onboarding, and accessibility into a unified UX skill.

**Files:**
- Create: `skills/ux-design/SKILL.md`
- Create: `skills/ux-design/ONBOARDING.md`
- Create: `skills/ux-design/ACCESSIBILITY.md`

**Step 1: Write `skills/ux-design/SKILL.md`**

Frontmatter:
```yaml
---
name: ux-design
description: "Use this skill when flows feel clunky, users are confused, navigation needs planning, onboarding needs design, or accessibility needs implementation. Covers information architecture, user flows, interaction patterns, progressive disclosure, and error handling UX."
---
```

Content structure:
1. Brief intro
2. Information architecture (absorb best of navigation skill — page hierarchy, URL structure, mental models, grouping principles)
3. Navigation patterns (sidebar vs top nav vs tabs vs breadcrumbs — decision framework)
4. User flows (task analysis, step reduction, friction identification)
5. Interaction patterns (feedback, confirmation dialogs, undo vs confirm, inline vs modal editing)
6. Progressive disclosure (what to show when, levels of detail)
7. Error handling UX (recovery paths, error message patterns, graceful degradation)
8. Performance perception (optimistic updates, skeleton screens, perceived speed)

Absorb the best content from `skills/navigation/SKILL.md`. Drop redundant content that's covered better elsewhere.

Target: ~1800 words.

**Step 2: Write `skills/ux-design/ONBOARDING.md`**

Migrate from `skills/onboarding/SKILL.md`. Keep:
- Aha moment framework
- Onboarding pattern descriptions (wizard, checklist, walkthrough, templates, progressive disclosure)
- Personalization approach
- Anti-patterns
- Success metrics

Drop:
- "Tell AI:" prompts
- Onboarding email section (belongs in email skill)

Rewrite for Claude consumption (these are instructions for Claude, not instructions for a founder to give to Claude).

Target: ~1200 words.

**Step 3: Write `skills/ux-design/ACCESSIBILITY.md`**

Migrate from `skills/accessibility/SKILL.md`. Keep the tiered approach and all implementation details. This is already well-structured. Main changes:
- Remove "Tell AI:" prompts
- Rewrite as direct instructions for Claude
- Keep the testing checklist
- Keep the common mistakes table

Target: ~1200 words.

**Step 4: Commit**

```bash
git add skills/ux-design/
git commit -m "feat: add ux-design skill — IA, flows, onboarding, and accessibility"
```

---

### Task 4: Create the Motion & Polish Skill

**Files:**
- Create: `skills/motion-polish/SKILL.md`

**Step 1: Write `skills/motion-polish/SKILL.md`**

Frontmatter:
```yaml
---
name: motion-polish
description: "Use this skill when the user wants to add animations, make transitions smooth, add micro-interactions, or apply final polish. Covers transition patterns, micro-interactions, page transitions, loading animations, scroll interactions, and the restraint principle."
---
```

Content structure:
1. Brief intro + the restraint principle (most important: what NOT to animate)
2. Timing and easing fundamentals (duration guidelines, easing curves, when to use which)
3. Transition patterns (enter/exit, expand/collapse, fade, slide, scale)
4. Micro-interactions (button feedback, hover states, toggle animations, checkbox/radio, input focus)
5. Page transitions (route changes, content loading, list reordering)
6. Loading and progress (skeleton shimmer, spinners, progress bars, optimistic UI)
7. Scroll interactions (sticky headers, scroll-triggered reveals, parallax — with restraint warnings)
8. Feedback animations (success/error/warning states, toast entrance/exit, notification badges)
9. Reduced motion support (prefers-reduced-motion implementation, what to disable vs simplify)
10. CSS vs JS animation decision framework

This is a single-file skill — motion doesn't need supporting files.

Target: ~1500 words.

**Step 2: Commit**

```bash
git add skills/motion-polish/
git commit -m "feat: add motion-polish skill — animations, transitions, and micro-interactions"
```

---

### Task 5: Create the Design Review Skill

**Files:**
- Create: `skills/design-review/SKILL.md`
- Create: `skills/design-review/AUDIT-CHECKLIST.md`

**Step 1: Write `skills/design-review/SKILL.md`**

Frontmatter:
```yaml
---
name: design-review
description: "Use this skill when the user wants a design audit, asks what to fix, wants to compare against reference apps, asks if something is good enough to ship, or wants to elevate AI-generated UI to production quality. The quality gate for visual design."
---
```

Content structure:
1. Brief intro — this skill is the quality gate, not a design generator
2. Audit methodology (how to systematically evaluate a design)
3. Priority framework (what to fix first for maximum visual impact):
   - P0: Visual hierarchy (if the eye doesn't know where to go, nothing else matters)
   - P1: Spacing and alignment (the fastest way to make something look "designed")
   - P2: Color usage (too much, too little, inconsistent)
   - P3: Typography (size relationships, weight usage, line lengths)
   - P4: States and edge cases (empty, loading, error, overflow)
   - P5: Responsiveness (breakpoint behavior)
   - P6: Motion and polish (last priority)
4. Before/after methodology (how to systematically improve a page)
5. Cross-page consistency check (same patterns, same spacing, same components)
6. When to stop (diminishing returns, "good enough to ship" criteria)

Target: ~1200 words.

**Step 2: Write `skills/design-review/AUDIT-CHECKLIST.md`**

A structured checklist Claude can run against any page/component. Organized by category:

```
## Hierarchy
- [ ] Primary action is visually dominant
- [ ] Clear size/weight progression in headings
...

## Spacing
- [ ] Consistent spacing scale used throughout
- [ ] Adequate whitespace between sections
...

## Color
...

## Typography
...

## States
...

## Responsive
...

## Accessibility
...
```

Include a "60-second visual scan" quick version and a "comprehensive audit" full version.

Target: ~1000 words.

**Step 3: Commit**

```bash
git add skills/design-review/
git commit -m "feat: add design-review skill — visual audit and quality gate"
```

---

### Task 6: Update Brand Identity Skill

Minor changes to trim content that now lives in other skills.

**Files:**
- Modify: `skills/brand-identity-generator/SKILL.md`

**Step 1: Read the full brand-identity-generator SKILL.md**

Read the complete file to identify what to trim.

**Step 2: Trim component specs section**

The component specs section (Section 8 in the output template) now belongs in UI Patterns. Reduce it to a brief note: "For detailed component implementation, see the ui-patterns skill." Keep the token-level specs (colors, typography scale, spacing scale, radius, shadows) — those are brand decisions.

**Step 3: Add cross-references**

Add a brief "Related Skills" section at the bottom:
- aesthetics — how to apply these tokens beautifully
- ui-patterns — component implementation using these tokens
- motion-polish — animation timing that matches brand personality

**Step 4: Commit**

```bash
git add skills/brand-identity-generator/
git commit -m "refactor: trim brand-identity skill, add cross-references to new design skills"
```

---

### Task 7: Remove Old Skills

Delete the skills that have been absorbed into the new ones.

**Files:**
- Delete: `skills/design/` (entire directory — SKILL.md, COMPONENTS.md, DESIGN-SYSTEM.md, LAWSOFUX.md, DESIGN-THINKING.md)
- Delete: `skills/navigation/` (entire directory)
- Delete: `skills/onboarding/` (entire directory)
- Delete: `skills/accessibility/` (entire directory)

**Step 1: Delete old skill directories**

```bash
rm -rf skills/design/ skills/navigation/ skills/onboarding/ skills/accessibility/
```

**Step 2: Verify no broken references**

Search all remaining skills for references to the deleted skill names. Fix any cross-references to point to the new skills.

```bash
grep -r "skills/design\|skills/navigation\|skills/onboarding\|skills/accessibility" skills/ --include="*.md"
grep -r "design skill\|navigation skill\|onboarding skill\|accessibility skill" skills/ --include="*.md"
```

**Step 3: Commit**

```bash
git add -A
git commit -m "refactor: remove old design, navigation, onboarding, accessibility skills (absorbed into new design skillset)"
```

---

### Task 8: Update Plugin Manifest and Metadata

**Files:**
- Modify: `.claude-plugin/plugin.json`

**Step 1: Update skill count**

The description mentions "45 skills". Count the new total after adding 5 (aesthetics, ui-patterns, ux-design, motion-polish, design-review) and removing 4 (design, navigation, onboarding, accessibility). Net change: +1. Update to "46 skills".

**Step 2: Verify the plugin.json is correct**

Read the file, update the description with the new count.

**Step 3: Update CLAUDE.md**

Update the skill listing in the Structure section to reflect the new design skills:

Old (under Design & UX): design, brand, navigation, onboarding, accessibility
New (under Design & UX): brand-identity-generator, aesthetics, ui-patterns, ux-design, motion-polish, design-review

**Step 4: Commit**

```bash
git add .claude-plugin/plugin.json CLAUDE.md
git commit -m "chore: update plugin manifest and CLAUDE.md for design skillset redesign"
```

---

### Task 9: Quality Review

**Step 1: Read all new skills end-to-end**

Read every new file in order:
1. `skills/aesthetics/SKILL.md`
2. `skills/aesthetics/AI-SLOP-FIXES.md`
3. `skills/aesthetics/REFERENCE-TEARDOWNS.md`
4. `skills/ui-patterns/SKILL.md`
5. `skills/ui-patterns/COMPONENTS.md`
6. `skills/ui-patterns/LAYOUTS.md`
7. `skills/ux-design/SKILL.md`
8. `skills/ux-design/ONBOARDING.md`
9. `skills/ux-design/ACCESSIBILITY.md`
10. `skills/motion-polish/SKILL.md`
11. `skills/design-review/SKILL.md`
12. `skills/design-review/AUDIT-CHECKLIST.md`

**Step 2: Check for**

- Duplicate content across skills (same advice in two places)
- Gaps (topics promised in design doc but not covered)
- Tone consistency (all written as Claude instructions, not founder instructions)
- No "Tell AI:" prompts remaining
- Cross-references are correct (skill names match)
- Each skill is self-contained (doesn't require reading another skill to be useful)
- Total token budget is reasonable (no single skill is bloated)

**Step 3: Fix any issues found**

Edit files as needed.

**Step 4: Commit fixes**

```bash
git add skills/
git commit -m "fix: quality review fixes across design skillset"
```
