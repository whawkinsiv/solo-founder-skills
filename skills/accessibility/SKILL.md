---
name: accessibility
description: "Use this skill when the user needs to make their app accessible, comply with WCAG guidelines, implement ARIA patterns, support screen readers, or ensure keyboard navigation works. Covers WCAG 2.2, semantic HTML, assistive technology testing, and inclusive design."
---

# Accessibility (a11y)

Accessibility is not optional — it's a quality attribute like performance or security. The good news: if you build with correct HTML from the start, you get 80% of accessibility for free. This skill tells you what to prioritize and what to hand to Claude Code.

## What You Decide vs. What AI Implements

| You Decide | Claude Code Implements |
|------------|----------------------|
| "Our app must be keyboard-navigable" | Proper focus management, tab order, keyboard handlers |
| "All images need descriptions" | Alt text on every image |
| "Forms must have clear error messages" | Linked labels, aria-describedby, validation messages |
| "We support screen readers" | Semantic HTML, ARIA roles, live regions |

**Rule:** You set the standard. Claude Code does the implementation. Your job is to test it.

---

## Priority Order (What Gives You the Most Value)

Don't try to achieve WCAG AAA compliance on day one. Start with the highest-impact wins:

### Tier 1: Start Here (Covers 80% of Issues)

1. **Semantic HTML** — The foundation of all accessibility
2. **Keyboard navigation** — Every interactive element works without a mouse
3. **Color contrast** — Text is readable against its background
4. **Form labels** — Every input has a visible, linked label
5. **Image alt text** — Every meaningful image has a description

### Tier 2: Add Next (After Launch)

6. **Focus management** — Modals trap focus, focus returns on close
7. **Error messages** — Connected to inputs, announced by screen readers
8. **Skip navigation** — Link to skip to main content
9. **Reduced motion** — Respect user's motion preferences

### Tier 3: Polish (After Product-Market Fit)

10. **Full ARIA patterns** — Custom components (tabs, menus, date pickers)
11. **Screen reader testing** — Test full flows with VoiceOver/NVDA
12. **Color blindness** — Don't rely on color alone to convey information

---

## Tier 1: Implementation

### Semantic HTML

**Tell AI:**
```
Audit and fix HTML semantics across the app:
- Use <button> for actions, <a> for navigation (never the reverse)
- Use <nav>, <main>, <aside>, <header>, <footer>, <article>, <section> for page structure
- Use <h1>-<h6> in order (no skipped levels, never used just for styling)
- Use <label> linked to every form input
- Use <ul>/<ol> for lists
- Use <table> with proper <th> headers for tabular data
- Use <dialog> for modals
```

### Keyboard Navigation

**Tell AI:**
```
Ensure full keyboard accessibility:
- Every interactive element (button, link, input, select) must be reachable with Tab
- Every interactive element must be activatable with Enter or Space
- Tab order must follow visual reading order
- Focus states must be clearly visible (not just outline: none)
- Modals must trap focus inside and return focus to the trigger on close
- Add a "Skip to main content" link as the first focusable element
```

### Color Contrast

| Element | Minimum Contrast Ratio |
|---------|----------------------|
| Body text | 4.5:1 against background |
| Large text (18px+ or 14px+ bold) | 3:1 |
| UI components (borders, icons) | 3:1 |

**Tell AI:**
```
Check and fix color contrast across the app:
- Verify all text meets WCAG AA contrast ratios (4.5:1 for body, 3:1 for large text)
- Verify UI elements (borders, icons, focus rings) meet 3:1 contrast
- Don't rely on color alone — add icons, patterns, or text labels alongside color indicators
- Test with the browser's built-in contrast checker
```

### Form Labels and Alt Text

**Tell AI:**
```
Fix form accessibility:
- Every input must have a visible <label> linked via for="id" attribute
- Placeholder text is NOT a label (it disappears on focus)
- Required fields: add visual indicator AND aria-required="true"
- Add autocomplete attributes for personal data: autocomplete="email", "name", etc.

Fix image accessibility:
- Every meaningful image needs descriptive alt text (max 125 chars)
- Decorative images need alt="" (empty alt, not missing alt)
- Charts and diagrams need a text description nearby or via aria-describedby
```

---

## Tier 2: After Launch

### Focus Management and Error Messages

**Tell AI:**
```
Improve focus management and error handling:
- When a modal opens, move focus to the first interactive element inside
- When a modal closes, return focus to the button that opened it
- Trap focus inside modals (Tab shouldn't escape to the background)
- Connect error messages to inputs via aria-describedby
- When a form has errors, add aria-invalid="true" to invalid fields
- Announce dynamic content changes with aria-live="polite" (status messages) or aria-live="assertive" (errors)
```

### Reduced Motion

**Tell AI:**
```
Respect user motion preferences:
- Add a CSS media query: @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
- Disable autoplay on videos and carousels when reduced motion is preferred
- Keep transitions under 200ms or remove them for reduced-motion users
```

---

## Testing Checklist

Run through these checks before each release:

### Quick Test (5 minutes)

- [ ] Put your mouse away. Navigate the entire signup → core action flow with keyboard only.
- [ ] Can you reach every button, link, and input with Tab?
- [ ] Can you see where focus is on every element?
- [ ] Can you activate every button with Enter or Space?
- [ ] Can you escape every modal with Escape?

### Automated Test

**Tell AI:**
```
Run an accessibility audit:
- Run axe-core or Lighthouse accessibility audit on our main pages
- Report all violations grouped by severity (critical, serious, moderate, minor)
- Fix all critical and serious violations
- Add accessibility checks to our CI pipeline so new issues are caught automatically
```

### Deeper Test (When Ready)

- [ ] Test with VoiceOver (Mac: Cmd+F5) or NVDA (Windows, free)
- [ ] Test at 200% browser zoom — no content loss or horizontal scrolling
- [ ] Test with a color blindness simulator browser extension
- [ ] Verify all videos have captions

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Adding `outline: none` to make focus "look clean" | Never remove focus indicators. Style them instead. |
| Using `<div>` for everything | Use semantic HTML elements. Buttons are `<button>`, not `<div onclick>`. |
| Placeholder as label | Always use a visible `<label>`. Placeholders are hints, not labels. |
| Ignoring keyboard users | Test without a mouse. If you can't complete the flow, keyboard users can't either. |
| Bolting on ARIA to fix bad HTML | Fix the HTML first. ARIA is a repair tool, not a substitute. |
| Waiting until "later" to care | Build semantic HTML from day one. It's free and prevents 80% of issues. |
