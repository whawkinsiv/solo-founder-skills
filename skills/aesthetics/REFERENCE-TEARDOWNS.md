# Reference Teardowns

What makes premium apps look premium. Not surface-level observations ("Stripe uses purple") — specific techniques that can be transferred to any app.

---

### Stripe (Dashboard)

**Category:** Financial data, API management, payments

**Key aesthetic moves:**

- **Extreme typographic hierarchy on data.** Revenue numbers are displayed at `text-4xl font-semibold` while their labels are `text-xs font-medium text-gray-500 uppercase tracking-wider`. The ratio between data and label is roughly 4:1 in visual weight. This makes numbers scannable from across a room — you absorb the data before you read the label.

- **Restrained color on a neutral canvas.** The dashboard is 95% white and gray. Color appears only for: the brand purple (CTAs and active nav), semantic status (green for succeeded, red for failed, yellow for pending), and charts. No colored section backgrounds, no colored card headers, no decorative color. This makes the colors that DO appear extremely meaningful.

- **Information density without clutter.** Tables show 8-10 columns with `text-sm`, tight row padding (`py-3`), and no row borders — only a subtle `hover:bg-gray-50`. The density is high but readable because typography does the separation work, not borders. Column headers are `text-xs text-gray-500 uppercase tracking-wide` — a completely different visual register from cell content, so headers never compete with data.

- **Progressive disclosure through surface levels.** The main view shows summary cards. Clicking into a card reveals a detail view with its own hierarchy. Each level uses whitespace and typography scale to indicate depth — drill-down pages have slightly less page padding and denser layouts than the overview, subtly signaling "you're one level deeper."

**What to steal:** Use dramatically different typographic treatments for data vs. labels (4:1 size ratio, different weights, different colors). Make the data the hero, make the label quiet. Apply this to any dashboard metric, stat card, or summary view.

---

### Linear

**Category:** Project management, issue tracking

**Key aesthetic moves:**

- **Monochrome with surgical accent color.** The dark interface is built from 3-4 shades of dark gray (`#1a1a1a` to `#2a2a2a` to `#3a3a3a`). The only color comes from status indicators (purple, yellow, green, red dots — each 8px) and the currently active item's highlight. This extreme restraint makes every colored pixel meaningful. When you see purple, it means "in progress" — not decoration.

- **Speed as aesthetic.** Animations are 100-150ms (most apps use 200-300ms). Transitions use ease-out curves that start fast. Keyboard shortcuts are shown inline next to menu items in `text-xs text-gray-500 font-mono`. The visual language communicates "this tool is fast" through timing, not through marketing copy about speed.

- **Flat hierarchy with hover-reveal.** List items show only the essential info (title, status dot, assignee avatar) at rest. Actions (priority selector, label picker, due date) appear on hover. This keeps the default view clean and scannable while maintaining full functionality. The hover state uses a subtle `bg-gray-800/50` to indicate interactivity without disrupting the visual flow.

- **Typographic minimalism.** One font (Inter), two weights (400 and 500), three sizes. Issue titles are `text-sm font-medium`, descriptions are `text-sm font-normal text-gray-400`, metadata is `text-xs text-gray-500`. The hierarchy is created entirely through color value (white vs. gray-400 vs. gray-500) rather than size differences.

**What to steal:** Create hierarchy through color value (brightness) instead of size. Three levels of gray on the same font size creates a clean, dense interface that doesn't sacrifice scanability. This works exceptionally well for list-heavy interfaces.

---

### Vercel

**Category:** Deployment platform, developer tools

**Key aesthetic moves:**

- **Typographic confidence at scale.** Landing page headings use `text-6xl` to `text-8xl` with `font-bold tracking-tighter`. The letter-spacing is noticeably tight — `-0.04em` to `-0.05em` — which makes large text feel precise and engineered rather than generic. Body text is comparatively small (`text-base` or `text-sm`), creating a dramatic hierarchy. The heading IS the design — no supporting imagery needed.

- **Black and white as a power move.** The palette is essentially black (`#000`), white (`#fafafa`), and one accent (the triangle gradient for the logo). This isn't laziness — it's confidence. By removing all color decisions, every element is defined by typography, spacing, and composition alone. This forces the typography and layout to be excellent because there's nothing else to lean on.

- **Generous vertical rhythm.** Sections are separated by `py-24` to `py-32` — far more than most apps. Each section feels like a distinct "room" you scroll into. Within sections, content groups use `gap-6` to `gap-8`. The contrast between tight internal spacing and expansive section gaps creates a breathing rhythm that feels premium.

- **Geometric precision.** Elements snap to an obvious grid. Card corners are consistently `rounded-lg`. Code blocks use `rounded-md` with a monospace font at exactly the right size to feel native to the surrounding type. Nothing is decorative — every element earns its space.

**What to steal:** Use tight letter-spacing (`tracking-tight` or `tracking-tighter`) on large headings. It immediately elevates typography from default to intentional. Pair with generous section spacing (`py-20` to `py-32`) to create the "rooms" effect.

---

### Notion

**Category:** Knowledge management, documents, wikis

**Key aesthetic moves:**

- **Content-first by subtraction.** The UI chrome is nearly invisible. The sidebar is plain text with small icons — no backgrounds on nav items, no borders, minimal hover states (just a `bg-gray-100` rectangle). The toolbar appears only on hover or selection. This aggressively removes everything that isn't your content, making the content itself feel important.

- **Warm neutrals instead of cool grays.** Notion's grays have a slight warm tint — they lean toward `#37352f` instead of `#374151`. This makes the interface feel like paper rather than a screen. The background isn't `#ffffff` but a slightly warm off-white. The difference is subtle but cumulative: the entire app feels calm and approachable rather than clinical.

- **Spacious line-height and wide content.** Body text uses `line-height: 1.7` to `1.8` — significantly more than the typical `1.5`. Content blocks have generous vertical margins. The editing area is `max-w-3xl` centered, which keeps text readable without feeling cramped. This spaciousness is the core brand — it says "you have room to think here."

- **Type as UI.** Page titles, headings, toggles, callouts — almost every UI element is primarily a typographic choice rather than a component with borders and backgrounds. A "callout" is just an emoji + indented text with a light background. A "toggle" is a triangle icon + text. By building UI from typography rather than from boxes, the interface feels lightweight and flexible.

**What to steal:** Increase line-height to 1.7 for content-heavy apps. Switch from cool grays to warm grays (add a hint of brown/amber to your gray scale). These two changes make any content-focused app feel calmer and more readable.

---

### Mercury

**Category:** Business banking, financial dashboard

**Key aesthetic moves:**

- **Trust through restraint.** The color palette is almost entirely gray-blue neutrals (`#f8fafc`, `#e2e8f0`, `#64748b`) with money amounts in near-black. The only deliberate color is a muted green for positive values and muted red for negative. No bright blues, no gradients, no visual excitement. Financial apps earn trust by being boring — visual restraint communicates "we take your money seriously."

- **Premium whitespace ratios.** Account balance is displayed with `text-3xl font-light` (note: light weight, not bold — this is unusual and distinctive) with `mb-1` to a `text-sm text-gray-500` label below. The entire balance section sits in `py-8` of whitespace before the transaction list begins. The transaction list then uses tight spacing (`py-3` per row). This contrast — expansive space around the hero data, dense space for the detail — communicates "the balance is what matters, transactions are supporting detail."

- **Horizontal line as design element.** Sections are separated by a single `border-b border-gray-200` with generous margins above and below (`my-8`). No cards, no shadows, no background changes. Just a thin gray line and whitespace. This minimal separation technique feels more premium than cards because it implies the content is important enough to stand on its own without containment.

- **Type weight inversion.** Where most apps use bold for important numbers, Mercury uses `font-light` for the primary balance and `font-medium` for smaller amounts in the transaction list. This counterintuitive choice works because the large size already creates hierarchy — adding bold would be redundant. The light weight feels elegant and confident, like a luxury brand that doesn't need to shout.

**What to steal:** Try `font-light` on your largest, most important number. When an element is already the largest thing on screen, light weight adds elegance while bold adds nothing. Use thin horizontal rules (`border-b border-gray-200`) instead of cards to separate sections — it's the more confident choice.
