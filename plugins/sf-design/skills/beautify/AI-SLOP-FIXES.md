# AI Slop Fixes

Specific antipatterns that appear in AI-generated UI and how to fix them. When auditing or improving a user's app, check for each of these patterns and apply the fix directly.

---

### Too Many Borders

**Symptom:** Every element — cards, inputs, sections, containers, headers, footers — has a visible `border`. The page looks like a wireframe or a spreadsheet.

**Why AI does this:** Borders are the safest way to create visual separation. AI defaults to explicit containment because it never has to "see" the result and judge whether separation is already achieved through spacing or background contrast.

**Fix:** Remove borders from cards and use `shadow-sm` or background contrast (`bg-white` on `bg-gray-50`) instead. Keep borders only on inputs, tables, and explicit dividers. A card on a gray background needs no border at all — the background contrast creates the boundary.

```
Before: border border-gray-200 rounded-lg p-4 (on every card, on a white background)
After:  bg-white rounded-lg p-6 shadow-sm (on a bg-gray-50 page)
  or:   bg-white rounded-lg p-6 (on a bg-gray-100 page — no shadow needed)
```

---

### Overuse of Cards

**Symptom:** Every piece of content is wrapped in a card container — single stats, labels, individual form fields, paragraphs of text. Cards nested inside cards.

**Why AI does this:** Cards are the default "container" pattern. AI wraps content in cards as a structural reflex, especially for dashboard layouts and data display.

**Fix:** Cards are for grouping related content that could plausibly be rearranged or compared. A single metric doesn't need a card — it needs a heading and a value. A form doesn't need each field in a card. Remove card wrappers from: individual stats (use a grid with shared background), form sections (use spacing and headings), single paragraphs, and any content that's already inside a card.

```
Before: 4 stat cards, each with border + shadow + padding, each containing one number
After:  One stats row with grid-cols-4, shared background, dividers between items
  or:   Simple flex row with gap-8, each stat is just a label + value, no container
```

---

### Everything the Same Size

**Symptom:** Page title, section headings, card titles, and body text are all within 2-4px of each other. Nothing jumps out. The page reads as a wall of text.

**Why AI does this:** AI generates structurally correct HTML (h1, h2, h3, p) but applies timid size differences. It avoids dramatic sizing because extreme differences feel "risky."

**Fix:** Force dramatic size contrast. Page title should be at least 2x the body text size. Apply this rule: if two adjacent heading levels don't look obviously different at arm's length, the difference isn't big enough. Use `text-3xl font-bold` for page titles, `text-lg font-semibold` for section heads, `text-sm` for body. Skip intermediate sizes.

---

### Rainbow Soup

**Symptom:** Multiple saturated colors on one screen — blue buttons, green badges, orange alerts, purple tags, red notifications, teal links. Every element has its own color.

**Why AI does this:** AI assigns semantically "appropriate" colors to each element independently without considering the aggregate effect. Green for success, blue for primary, orange for warning — individually reasonable, collectively chaotic.

**Fix:** Enforce the 60-30-10 rule. The fix is usually: make most things gray. Tags and badges that don't indicate status should be `bg-gray-100 text-gray-700`, not colored. Links should match the primary color, not be a separate blue. Limit the entire page to: one brand accent, one success green, one error red, and gray for everything else. Remove any color that doesn't answer the question "what status or action does this color communicate?"

```
Before: Blue button, green badge, orange tag, purple category, teal link
After:  Blue button, gray badge, gray tag, gray category, blue link
  (add color ONLY to badges that indicate live status: green=active, red=failed)
```

---

### Generic Spacing

**Symptom:** Everything is spaced with `gap-4` or `p-4`. Cards, sections, form fields, page margins — all use the same spacing value. The page feels monotonous and flat.

**Why AI does this:** Uniform spacing is safe. AI picks one comfortable value and applies it everywhere because varying spacing requires understanding visual grouping.

**Fix:** Apply the 2-3x rule. Space within groups should be smaller than space between groups. Within a card: `gap-2` to `gap-3`. Between cards: `gap-6`. Between sections: `py-12` to `py-16`. Page top padding: `pt-8`. This creates rhythm — the spacing itself communicates structure.

```
Before: Everything gap-4 p-4 space-y-4
After:  Card internal gap-3, between cards gap-6, between sections py-16, page px-8
```

---

### Centered Everything

**Symptom:** Body text, form fields, card content, descriptions, and lists are all `text-center`. The page looks like a presentation slide, not an application.

**Why AI does this:** Center alignment feels "designed" and "balanced." AI defaults to center because it works for marketing hero sections, and it overapplies the pattern.

**Fix:** Left-align everything except: hero headlines, empty state messages, and confirmation dialogs. Forms should always be left-aligned. Card content should be left-aligned. Data and descriptions should be left-aligned. Numbers in tables should be right-aligned. Apply `text-left` as the default and explicitly justify center-alignment for the rare cases where it belongs.

---

### Cluttered Headers

**Symptom:** The page header contains the logo, navigation, search bar, notification bell, user avatar, dropdown menu, breadcrumbs, and a CTA button — all fighting for attention in a 64px strip.

**Why AI does this:** AI includes every standard header element it's been trained on. Each element is individually reasonable, but combined they create visual overload.

**Fix:** Headers should contain at most: logo/name (left), primary nav (center or left), and 2-3 utility items (right). Move breadcrumbs below the header into the content area. Move search into the main content area or behind a toggle. Reduce icon sizes to 18-20px. Use `text-gray-500` for utility icons, not `text-gray-900`. The header's job is navigation, not information display.

```
Before: Logo | Nav | Search bar | Bell | Messages | Help | Avatar | CTA | Breadcrumbs
After:  Logo | Nav (3-5 items) | Search icon | Bell | Avatar
  (breadcrumbs go below header, search opens on click, help moves to a menu)
```

---

### Identical Page Layouts

**Symptom:** Every page is a carbon copy — same header, same single-column layout, same card grid, same spacing. The settings page looks like the dashboard which looks like the user list.

**Why AI does this:** It reuses the last successful layout. Once a page works, every subsequent page gets the same structure because deviation requires understanding what each page uniquely needs.

**Fix:** Match layout to purpose. Dashboards use multi-column grids with metric cards. Detail pages use a wide content area with a narrow sidebar for metadata. Settings pages use a left nav with a content panel. Form pages use single-column centered layout at `max-w-lg`. The layout communicates what type of page you're on before reading a single word.

---

### Overly Rounded Corners

**Symptom:** Buttons are pills (`rounded-full`). Cards have `rounded-2xl` or `rounded-3xl`. Inputs match. Everything looks like a children's app or a medical device UI.

**Why AI does this:** High border-radius feels "modern" and "friendly." AI overindexes on roundness because it's a visible design choice that seems intentional.

**Fix:** For most SaaS apps, `rounded-md` (6px) to `rounded-lg` (8px) is correct for cards, buttons, and inputs. Reserve `rounded-full` exclusively for avatars, small status indicators, and pill-shaped tags. Match radius to element size — small elements (badges) can be rounder, large elements (cards, modals) should be less round. A good test: if the radius is visible as an obvious curve rather than a subtle softening, it's probably too much.

```
Before: rounded-full on buttons, rounded-3xl on cards, rounded-2xl on inputs
After:  rounded-md on buttons, rounded-lg on cards, rounded-md on inputs
```

---

### Gratuitous Shadows

**Symptom:** Every card, button, input, badge, and container has a shadow. The page looks like a pile of floating Post-it notes.

**Why AI does this:** Shadows create perceived depth and "polish." AI adds them to make elements feel finished, but when everything is elevated, nothing is.

**Fix:** Shadows should indicate interactive elevation — elements that float above the page (dropdowns, modals, tooltips, popovers). Static content cards on a `bg-gray-50` background don't need shadows — background contrast is sufficient. Remove shadows from: cards that aren't hoverable, badges, static containers, and inputs (use border instead). Keep shadows on: dropdowns, modals, floating toolbars, and hover states on clickable cards.

---

### Placeholder-Quality Images and Icons

**Symptom:** Hero sections with unsplash stock photos. Feature sections with generic outline icons that don't match the app's style. Illustrations that look like they came from a different product.

**Why AI does this:** AI fills image placeholders with the most generic appropriate content. It selects icons individually without considering whether the set is visually cohesive.

**Fix:** Remove decorative images entirely rather than using stock photos — whitespace is better than a generic image. For icons, use a single icon library (Lucide, Heroicons, or Phosphor) at consistent sizes and stroke widths. Never mix libraries. For empty states and illustrations, use simple abstract shapes or the product's own UI elements as illustrations rather than stock illustrations. If the product doesn't have custom illustrations, a well-styled text block is better than a generic SVG illustration.

---

### Inconsistent Alignment Between Sections

**Symptom:** The hero section has content at `max-w-4xl`, the features section stretches full-width, the pricing cards use `max-w-6xl`, and the footer uses `max-w-5xl`. Each section starts at a different horizontal position.

**Why AI does this:** Each section is generated as an independent unit. AI optimizes each section for its own content without maintaining a shared alignment grid across the page.

**Fix:** Define one `max-w` container and use it for every section's content. The background can be full-width, but the content within must align to the same grid. Typically `max-w-6xl mx-auto px-6` for the outer container, with inner content using grid or flex for narrower columns where needed. Every section's left edge of content should align with every other section's left edge.

```
Before: Section 1 max-w-4xl, Section 2 max-w-full, Section 3 max-w-5xl
After:  All sections use max-w-6xl mx-auto px-6, inner content varies width as needed
```
