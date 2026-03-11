# Accessibility (a11y)

Accessibility is a quality attribute like performance or security. Building with correct HTML from the start provides 80% of accessibility for free. Retrofitting is expensive. This guide is organized in priority tiers — implement Tier 1 from day one, add Tiers 2 and 3 as the product matures.

## Tier 1: Build From Day One

These five items cover 80% of accessibility issues. Implement them in every component from the start.

### Semantic HTML

Use the correct HTML element for every purpose:

- `<button>` for actions, `<a>` for navigation — never the reverse, never `<div onclick>`
- `<nav>`, `<main>`, `<aside>`, `<header>`, `<footer>`, `<article>`, `<section>` for page structure
- `<h1>`-`<h6>` in order — no skipped levels, never used purely for styling
- `<label>` linked to every form input via `for="id"` attribute
- `<ul>`/`<ol>` for lists of items
- `<table>` with `<th>` headers for tabular data — never for layout
- `<dialog>` for modals

Semantic HTML provides screen reader navigation, keyboard behavior, and correct ARIA roles automatically. Fix HTML before adding ARIA attributes — ARIA is a repair tool, not a substitute for correct elements.

### Keyboard Navigation

Every interaction must work without a mouse:

- All interactive elements (`<button>`, `<a>`, `<input>`, `<select>`) must be reachable with Tab
- All interactive elements must be activatable with Enter or Space
- Tab order must follow visual reading order (use DOM order, not `tabindex` hacks)
- Focus states must be clearly visible — never apply `outline: none` without a visible replacement. Style focus rings with a high-contrast outline (e.g., `outline: 2px solid #005fcc; outline-offset: 2px`)
- Escape must close modals, dropdowns, and popovers

### Color Contrast

Minimum contrast ratios (WCAG AA):

| Element | Ratio |
|---------|-------|
| Body text (under 18px) | 4.5:1 against background |
| Large text (18px+ or 14px+ bold) | 3:1 |
| UI components (borders, icons, focus rings) | 3:1 |

Never rely on color alone to convey information. Status indicators, form validation, and charts must use icons, patterns, or text labels in addition to color.

### Form Labels

- Every input must have a visible `<label>` linked via `for="id"`. Placeholder text is not a label — it disappears on focus.
- Required fields: add a visual indicator (asterisk or "required" text) AND `aria-required="true"`
- Add `autocomplete` attributes for personal data fields: `autocomplete="email"`, `autocomplete="name"`, `autocomplete="tel"`, etc.
- Group related fields with `<fieldset>` and `<legend>` (e.g., billing address fields).

### Image Alt Text

- Every meaningful image: descriptive `alt` text, max 125 characters. Describe the content and function, not the appearance.
- Decorative images: `alt=""` (empty alt attribute, not a missing alt attribute)
- Charts and diagrams: provide a text summary nearby or via `aria-describedby` linking to a description element
- Icons used as buttons: the `<button>` must have an accessible label via `aria-label` or visually hidden text

## Tier 2: Add After Launch

These items add significant value but require more implementation effort. Prioritize them once core flows are stable.

### Focus Management

- When a modal opens, move focus to the first interactive element inside it
- When a modal closes, return focus to the element that triggered it
- Trap focus inside modals — Tab must not escape to background content. Implement with a focus trap utility.
- When content is dynamically added (new list item, inline edit), move focus to the new content or confirm action with a status message
- After a page-level action (delete item from list, form submission), move focus to a logical location — not the top of the page

### Error Message Accessibility

- Connect error messages to their input via `aria-describedby` pointing to the error element's ID
- Add `aria-invalid="true"` to fields with validation errors
- Announce dynamic status changes with `aria-live="polite"` for status messages (save confirmation, progress updates)
- Announce urgent errors with `aria-live="assertive"` (form submission failure, session expiry)
- Error summary at the top of a form should be a list of links, each linking to the invalid field

### Skip Navigation

Add a "Skip to main content" link as the first focusable element on every page. It should be visually hidden until focused:

```css
.skip-link {
  position: absolute;
  left: -9999px;
  top: auto;
}
.skip-link:focus {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 9999;
  padding: 1rem;
  background: white;
  color: black;
}
```

### Reduced Motion

Respect the user's OS-level motion preference:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

- Disable autoplay on videos and carousels when reduced motion is preferred
- Keep essential transitions (opacity fades) but remove motion (slides, bounces, zooms)

## Tier 3: Polish

Implement after achieving product-market fit, or when targeting enterprise/government customers with compliance requirements.

### Full ARIA Patterns

For custom interactive components that have no native HTML equivalent, implement complete ARIA patterns:

- **Tabs:** `role="tablist"`, `role="tab"`, `role="tabpanel"`, `aria-selected`, arrow key navigation between tabs
- **Menus:** `role="menu"`, `role="menuitem"`, arrow key navigation, typeahead selection
- **Combobox/Autocomplete:** `role="combobox"`, `aria-expanded`, `aria-activedescendant`, announced option count
- **Date pickers:** keyboard-navigable calendar grid, arrow keys for date navigation, announced month/year changes
- **Drag and drop:** provide keyboard alternative (move up/down buttons or reorder via menu)

Reference the WAI-ARIA Authoring Practices for the full specification of each pattern.

### Screen Reader Testing

Test complete user flows with a screen reader — not just individual components:

- **macOS:** VoiceOver (Cmd+F5). Test in Safari (best VoiceOver support).
- **Windows:** NVDA (free) or JAWS. Test in Chrome or Firefox.
- Verify: page title announced on navigation, headings provide document outline, form labels read correctly, dynamic content changes announced, error states communicated.

### Color Blindness

- Test with a color blindness simulator extension (e.g., Colorblindly, Sim Daltonism)
- Verify that no information is conveyed by color alone — all color-coded elements must have a secondary indicator
- Common failure: red/green for success/error without icons or text

## Testing Checklist

### Quick Test (5 minutes, every PR)

- [ ] Navigate the primary user flow (signup through core action) using only the keyboard
- [ ] Verify every interactive element is reachable with Tab
- [ ] Verify focus is visible on every element
- [ ] Verify every button activates with Enter or Space
- [ ] Verify Escape closes every modal and dropdown
- [ ] Verify no images are missing alt attributes

### Automated Test (CI pipeline)

Run axe-core or Lighthouse accessibility audit on all primary pages. Integrate into CI so new violations block the build. Fix all critical and serious violations before merging. Track moderate violations as technical debt.

### Deeper Test (quarterly or pre-major-release)

- [ ] Full flow test with VoiceOver or NVDA
- [ ] Browser zoom to 200% — verify no content loss or horizontal scrolling
- [ ] Color blindness simulation — verify no color-only information
- [ ] Verify all video content has captions

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| `outline: none` to make focus "look clean" | Style focus indicators instead of removing them |
| `<div>` with click handlers for everything | Use `<button>` for actions, `<a>` for navigation |
| Placeholder text as the only label | Always use a visible `<label>` element |
| Ignoring keyboard users entirely | Test every flow without a mouse |
| Adding ARIA to fix bad HTML structure | Fix the HTML first — correct elements provide accessibility automatically |
| Deferring all accessibility to "later" | Build Tier 1 from day one — it is free when done from the start |
| Missing `lang` attribute on `<html>` | Always set `<html lang="en">` (or appropriate language code) |
| Auto-playing video or animation | Respect `prefers-reduced-motion` and never autoplay with sound |
