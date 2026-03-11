---
name: design-review
description: "Use this skill when the user wants a design audit, asks what to fix, wants to compare against reference apps, asks if something is good enough to ship, or wants to elevate AI-generated UI to production quality. The quality gate for visual design."
---

# Design Review

The quality gate for visual design. This skill is for evaluating and systematically improving existing UI — not generating new designs. Use it to audit pages, identify what to fix first, and elevate AI-generated output to production quality.

For design principles and system creation, reference the **design** skill. For specific AI-generated UI antipatterns (gradient overuse, excessive rounded corners, decorative emptiness), reference the **aesthetics** skill's AI slop fixes.

---

## Audit Methodology

Systematically evaluate any page or screen using this process:

### 1. Five-Second First Impression

Squint at the page (or blur your eyes) and note what your eye lands on first. If it is not the primary action or primary content, visual hierarchy is broken — that becomes P0.

Ask:
- What is the single most important thing the user should do on this page?
- Is that thing the most visually prominent element?
- Can you identify the page's purpose within two seconds?

### 2. Systematic Page Walkthrough

Work top-to-bottom, left-to-right through the page. For each section:
- Identify its purpose (navigation, content, action, status)
- Check whether it competes with the primary focal point
- Note specific issues with exact locations ("the secondary button in the hero section is the same weight as the primary CTA"), not vague complaints ("buttons feel off")

### 3. Categorize by Priority

Every issue gets a priority level. This ordering is critical — fixing P0 issues often resolves multiple downstream problems automatically.

### 4. Fix in Order

Apply fixes one priority category at a time. Reassess after each category before moving to the next.

---

## Priority Framework

What to fix first for maximum visual impact.

### P0: Visual Hierarchy

If the eye does not know where to go, nothing else matters. This is the single highest-leverage fix.

Check:
- One clear focal point per page/section — not two competing elements
- Primary CTA is the most visually prominent interactive element (largest, highest contrast, most saturated)
- Secondary actions are visually subordinate (outlined, ghost, or text-only buttons)
- Heading sizes create clear levels — page title is noticeably larger than section headings, which are noticeably larger than body text
- Decorative elements do not compete with functional elements
- Navigation is visually quieter than page content

### P1: Spacing and Alignment

The fastest way to make something look "designed" rather than "generated." Inconsistent spacing is the number-one tell of AI-generated UI.

Check:
- Consistent spacing scale used throughout (e.g., 4/8/12/16/24/32/48px — not arbitrary values)
- Space between groups is 2-3x the space within groups (Gestalt proximity)
- All content aligns to the same grid — no elements offset by a few pixels
- Page padding is consistent on all sides
- Vertical rhythm is maintained — equal spacing between similar elements
- No "floating" elements that feel disconnected from their context

### P2: Color Usage

Check:
- 60-30-10 ratio observed — dominant neutral (60%), secondary tone (30%), accent color (10%)
- Accent color used sparingly and only for interactive or high-priority elements
- No decorative color — every colored element communicates meaning (action, status, category)
- Status colors are consistent throughout (same green for success everywhere, same red for errors)
- Sufficient contrast between text and background (4.5:1 minimum for body text)
- Dark sections or colored backgrounds used intentionally, not for visual variety

### P3: Typography

Check:
- Clear size hierarchy with at least two distinct steps between levels (e.g., 14/18/24/32, not 14/15/16/17)
- Maximum three font weights in use (e.g., regular, medium, bold)
- Body text line length stays under 65 characters (measure with the alphabet test: if you can fit more than 2.5 alphabets on one line, it is too wide)
- Line height is proportional — tighter on headings (1.1-1.2), more open on body text (1.5-1.6)
- Appropriate letter-spacing: slight tracking on uppercase/small text, default or tighter on large headings
- No more than two typefaces total

### P4: Component Consistency

Check:
- Same button styles used for the same purpose everywhere (not rounded on one page, square on another)
- Same card treatment throughout — same border radius, shadow depth, padding
- Same form field styling across all forms
- Same spacing within repeated elements (all cards have the same internal padding)
- Icon style is consistent (all outlined, all filled, or all a matching set — not mixed)
- Same hover/active states on similar interactive elements

### P5: States and Edge Cases

Check:
- Loading states exist and use skeletons or appropriate spinners (not blank screens)
- Empty states include context and a CTA ("No projects yet. Create your first project.")
- Error states are specific and actionable ("Could not save — check your connection and try again"), not generic ("Something went wrong")
- Long text content handles overflow gracefully (truncation with ellipsis, not layout breaking)
- Lists handle zero, one, and many items without layout shifts
- Form validation shows inline errors near the relevant field

### P6: Responsiveness

Check:
- Layout adapts at standard breakpoints (640/768/1024/1280px)
- Nothing overflows horizontally at any viewport width
- Touch targets are at least 44x44px on mobile
- Navigation transforms appropriately for mobile (hamburger, bottom nav, or simplified)
- Tables either scroll horizontally or reflow to cards on mobile
- Font sizes remain readable on small screens (minimum 16px body on mobile to prevent iOS zoom)

### P7: Motion and Polish

Check:
- Transitions are present but subtle (150-300ms, ease-out)
- No jarring state changes — elements fade, slide, or scale rather than appearing/disappearing instantly
- Hover states exist on all interactive elements (buttons, links, cards, toggles)
- Focus states are visible for keyboard navigation
- No animation on elements that the user interacts with frequently (avoid animation fatigue)
- Page transitions feel cohesive — similar pages transition similarly

---

## Before/After Methodology

When improving a page, follow this process to avoid making things worse:

1. **Document current state** — describe or screenshot exactly what exists now
2. **Apply fixes in priority order** — start with P0, complete it fully, then reassess
3. **One category at a time** — do not mix hierarchy fixes with spacing fixes in the same pass. Changing hierarchy often shifts what needs spacing adjustment.
4. **Reassess after each category** — P0 fixes frequently resolve P1 and P2 issues downstream. Check whether the next priority still needs work before changing anything.
5. **Preserve what works** — if a section already looks good, do not touch it. Audit is about targeted improvement, not wholesale redesign.

---

## Cross-Page Consistency Check

After auditing individual pages, navigate the full app and verify consistency across pages:

- **Header**: same height, same style, same content on every page
- **Page padding and max-width**: identical on all content pages
- **Heading hierarchy**: same sizes and weights used for the same heading levels
- **Card and component styles**: same border radius, shadows, and padding everywhere they appear
- **Button variants**: same primary, secondary, and ghost styles throughout
- **Color usage**: accent color means the same thing on every page
- **Empty/loading states**: same patterns used app-wide, not different approaches per page
- **Footer**: same treatment on all pages (or intentionally absent on app screens vs. marketing pages)

If cross-page inconsistencies exist, establish the correct pattern from the best-executed page and propagate it to the rest.

---

## When to Stop

Design review has diminishing returns. Use these thresholds:

**MVP / Early Product (P0-P3 addressed)**
The design looks intentional. Hierarchy is clear, spacing is consistent, colors are purposeful, and typography has structure. This is good enough to put in front of users and start collecting feedback. Ship it.

**Pre-Marketing (P4-P5 addressed)**
Components are consistent and edge cases are handled. The app does not break visually in unexpected states. This is the bar for a public launch, landing page traffic, or any context where first impressions matter at scale.

**Growth Stage (P6-P7 addressed)**
Responsive polish and motion refinement. Do this when the product has traction and retention data supports investing in fit and finish. Not before.

**The goal is "intentionally designed," not "award-winning."** A clean, consistent UI that communicates hierarchy and guides the user is better than a visually ambitious design with broken fundamentals. Stop when the design no longer distracts from the product.

See `AUDIT-CHECKLIST.md` for a structured checklist version of this framework — use the 60-second scan for quick assessments and the comprehensive audit for thorough reviews.
