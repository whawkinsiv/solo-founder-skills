# Audit Checklist

Two versions: a rapid scan for quick assessments and a comprehensive audit for thorough reviews.

---

## 60-Second Visual Scan

A fast pass to identify the biggest issues. If everything here checks out, the design is in reasonable shape.

- [ ] One clear focal point identifiable within two seconds
- [ ] Primary CTA is the most visually prominent interactive element on the page
- [ ] At most one primary (filled) button per viewport section
- [ ] Heading sizes create at least three distinct visual levels
- [ ] Spacing feels consistent — no sections noticeably more cramped or loose than others
- [ ] Space between groups is visibly larger than space within groups
- [ ] Accent color appears sparingly — not on more than 10-15% of the page
- [ ] Body text line length does not exceed roughly 65 characters
- [ ] No elements appear to float disconnected from surrounding content
- [ ] Empty or loading states exist (navigate to one and check)
- [ ] Page looks intentional, not randomly assembled — elements feel like they belong together

If three or more items fail, start with hierarchy (P0) fixes before addressing anything else.

---

## Comprehensive Audit

Work through each category in order. Mark items as they pass. Any failed item is a finding to address at the priority level of its category.

### Hierarchy (P0)

- [ ] Single clear focal point per page section — no competing elements of equal visual weight
- [ ] Primary action button is largest, highest contrast, and most saturated
- [ ] Secondary actions are visually subordinate (outlined, ghost, or text-only)
- [ ] Page title is noticeably larger than section headings
- [ ] Section headings are noticeably larger than body text
- [ ] Decorative elements (icons, illustrations, backgrounds) do not compete with functional content
- [ ] Navigation is visually quieter than the main page content
- [ ] The user's eye follows a clear path from top to primary action

### Spacing (P1)

- [ ] A consistent spacing scale is used throughout (values from a defined set, not arbitrary)
- [ ] Space between groups is 2-3x the space within groups
- [ ] All content aligns to the same implicit grid — no off-by-a-few-pixels misalignment
- [ ] Page padding is the same on left and right sides
- [ ] Vertical spacing between similar elements is equal (e.g., all cards have the same gap)
- [ ] Section spacing is consistent — all major sections have the same top/bottom padding
- [ ] No elements feel "crammed" against edges or other elements

### Color (P2)

- [ ] 60-30-10 ratio: dominant neutral, secondary tone, accent color
- [ ] Accent color is used only for interactive or high-priority elements
- [ ] No purely decorative color — every colored element communicates meaning
- [ ] Status colors are consistent (same green/red/yellow/blue everywhere)
- [ ] Text has sufficient contrast against its background (4.5:1 for body, 3:1 for large text)
- [ ] Dark or colored backgrounds are used intentionally, not for visual variety
- [ ] No more than one accent color (or two with clear distinct purposes)

### Typography (P3)

- [ ] At least two distinct size steps between heading levels (not incremental 1-2px jumps)
- [ ] No more than three font weights in use across the page
- [ ] Body text line length stays under 65 characters
- [ ] Heading line height is tight (1.1-1.2) and body line height is open (1.5-1.6)
- [ ] No more than two typefaces on the page
- [ ] Text alignment is consistent — body text is left-aligned, not center-aligned in blocks
- [ ] Uppercase text (if any) has slight letter-spacing applied

### Components (P4)

- [ ] Button styles are consistent — same border radius, padding, and font size for the same variant
- [ ] Card treatment is uniform — same shadow, border radius, and internal padding throughout
- [ ] Form fields share the same height, border style, and padding
- [ ] Repeated elements (list items, grid cards, table rows) have identical internal spacing
- [ ] Icon style is consistent — all from the same set, same stroke width, same sizing
- [ ] Hover and active states are consistent across similar interactive elements
- [ ] Badge, tag, and label styles are uniform throughout

### States (P5)

- [ ] Loading states use skeletons or spinners — not blank screens
- [ ] Empty states include an explanation and a CTA to take the next action
- [ ] Error states are specific and actionable, not generic "Something went wrong"
- [ ] Long text truncates gracefully with ellipsis rather than breaking layout
- [ ] Lists handle zero, one, few, and many items without layout shifts
- [ ] Form validation shows inline errors adjacent to the relevant field
- [ ] Disabled elements look visually distinct from enabled ones (reduced opacity or muted color)

### Responsive (P6)

- [ ] Layout adapts at all standard breakpoints (640, 768, 1024, 1280px)
- [ ] No horizontal overflow at any viewport width
- [ ] Touch targets are at least 44x44px on mobile
- [ ] Navigation adapts for mobile (hamburger menu, bottom nav, or simplified layout)
- [ ] Tables scroll horizontally or reflow to a stacked/card layout on small screens
- [ ] Body font size is at least 16px on mobile (prevents iOS auto-zoom on input focus)
- [ ] Modal and overlay content is usable on mobile (not cut off, scrollable if needed)

### Accessibility (P6)

- [ ] All images have meaningful alt text (or empty alt for decorative images)
- [ ] Color is not the only indicator of state (e.g., errors also have icons or text, not just red)
- [ ] Focus states are visible on all interactive elements
- [ ] Interactive elements are reachable and operable via keyboard
- [ ] Form inputs have associated labels (not just placeholder text)
- [ ] Heading levels are sequential (no jumping from h1 to h4)

### Motion (P7)

- [ ] Transitions are present on state changes (hover, open/close, show/hide)
- [ ] Transition duration is subtle: 150-300ms with ease-out timing
- [ ] No jarring instant appear/disappear — elements fade or slide
- [ ] Frequently used interactions do not have slow or attention-grabbing animation
- [ ] Hover states exist on all interactive elements
- [ ] Focus indicators transition smoothly rather than snapping on/off
