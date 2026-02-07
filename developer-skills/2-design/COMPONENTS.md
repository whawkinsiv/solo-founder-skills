# SaaS Component Patterns

> **Note:** This file supplements `instructions/design-system.md`. Use it as reference when adding new component patterns to your design system via MODIFY mode, or when you need detailed specs for common SaaS components.

Practical component guidance for building clean, professional SaaS interfaces with AI tools.

---

## Component Libraries

### shadcn/ui (Recommended)

**Use for:** Modern SaaS applications, customer-facing products

**Why it's good:**
- Built with Radix UI (accessible by default)
- Works with Tailwind CSS
- Customizable without fighting the framework
- Used by: Linear, Vercel, Resend, Cal.com

**Tell AI:**
"Use shadcn/ui components throughout. Install button, card, and input components."

### Radix UI (Advanced)

**Use for:** When you need full design control with accessible foundations

**Why it's good:**
- Headless components (you control all styling)
- Maximum flexibility
- Perfect accessibility

**Tell AI:**
"Use Radix UI for the dropdown menu. Style it to match Linear's minimal aesthetic."

### Ant Design / Material UI

**Use for:** Internal tools, admin dashboards, B2B back-office apps

**Why they're good:**
- Complete component set out of the box
- Works well for data-heavy interfaces
- Quick to build with

**When NOT to use:**
- Consumer-facing products (looks generic)
- When brand identity matters
- Modern SaaS aesthetics

---

## Button Patterns

### Primary Button

**Visual:**
- Large (44px min height on mobile)
- High contrast color (brand blue)
- Rounded corners (6-8px)
- Subtle shadow

**Code hint for AI:**
```typescript
<Button variant="primary" size="lg">
  Start Free Trial
</Button>
```

**Tell AI:**
"Primary button should be blue (#0070F3), 44px tall, 16px padding left/right, rounded corners"

### Secondary Button

**Visual:**
- Same size as primary
- Gray/subtle color
- Less prominent

**Tell AI:**
"Secondary button gray (#6B7280), same size as primary but less prominent"

### Button States

**Must have:**
- Hover: Slightly darker
- Active/Pressed: Even darker
- Disabled: Grayed out, no pointer cursor
- Loading: Show spinner, disable interaction

**Tell AI:**
"Add hover, active, disabled, and loading states to all buttons"

### Button Placement

**Single action:** Center button below content  
**Multiple actions:** Primary right, secondary left  
**Forms:** Submit right, cancel/back left

---

## Form Patterns

### Standard Form Layout

**Structure:**
```
[Label]
[Input field - full width]
[Helper text / error message]
[12-16px spacing]
[Next label]
```

**Key rules:**
- Labels above fields, not beside
- One column layout (easier to scan)
- Required fields marked with * or (Required)
- Full-width inputs on mobile

**Tell AI:**
"Create a form with labels above each field, full-width inputs, and 16px spacing between fields"

### Inline Validation

**Show validation:**
- As user types (for format validation)
- On blur for complex validation
- Before submit attempt

**Visual cues:**
- Green checkmark for valid
- Red border + error message for invalid
- Gray neutral state by default

**Tell AI:**
"Add inline validation that shows green checkmark when email format is valid, red error message when invalid"

### Multi-Step Forms

**Pattern:**
1. Show progress indicator (steps)
2. 5-7 fields per step maximum
3. Allow going back without losing data
4. Clear "Next" and "Back" buttons

**Tell AI:**
"Create a 3-step form with progress indicator at top. Each step has 5 fields max. Show 'Next' and 'Back' buttons"

---

## Card Components

### Metric Card (Dashboard)

**Structure:**
```
[Card]
  [Label / Title]
  [Large Number]
  [Change indicator: ↑ 12% vs last month]
  [Optional sparkline chart]
```

**Visual:**
- Subtle shadow or border
- Consistent padding (16-24px)
- Grid layout (2x2 or 3x3)

**Examples:** Linear dashboard, Stripe dashboard, Vercel analytics

**Tell AI:**
"Create metric cards in a 2x2 grid. Each card shows label, large number, and percentage change with up/down arrow"

### Content Card

**Structure:**
```
[Card]
  [Title]
  [Description]
  [Optional image/icon]
  [Action button or link]
```

**Visual:**
- Clear visual hierarchy
- Consistent spacing
- Hover state (subtle lift or border change)

**Tell AI:**
"Create content cards with title, 2-line description, and 'Learn More' link. Cards should lift slightly on hover"

---

## Table / List Patterns

### Data Table

**Structure:**
- Header row with sortable columns
- Actions on right side of each row
- Bulk actions above table (when applicable)
- Pagination at bottom
- Filters/search at top

**Visual:**
- Alternating row colors or dividing lines
- Hover state on rows
- Clear column headers

**Examples:** Linear issues table, Stripe transactions, GitHub PRs

**Tell AI:**
"Create a data table with sortable columns, actions dropdown on right side of each row, and pagination at bottom"

### Empty States

**What to show when table is empty:**
- Icon or illustration
- Clear message explaining why it's empty
- Primary action to add first item
- Optional help text

**Tell AI:**
"When table is empty, show centered message 'No projects yet' with 'Create Project' button below"

---

## Navigation Patterns

### Top Navigation Bar

**Structure:**
```
[Logo] [Main nav items] ............. [Search] [User menu]
```

**Visual:**
- Fixed at top
- Subtle bottom border or shadow
- ~60px height

**Example:** Linear, Notion, Stripe

**Tell AI:**
"Create top nav bar with logo left, 5 nav items center, search and user menu right. Fixed position, 60px tall"

### Sidebar Navigation

**Structure:**
```
[Logo]
[Nav Item 1]
[Nav Item 2]
[Nav Item 3]
---
[Settings]
[Help]
[User Profile]
```

**Visual:**
- ~240px wide (collapsible to ~60px on mobile)
- Active state clearly marked
- Icons + text for top items
- User/settings at bottom

**Examples:** Notion, Linear, Slack

**Tell AI:**
"Create sidebar nav 240px wide, collapsible. Show icons with labels, highlight active item, put settings at bottom"

---

## Modal / Dialog Patterns

### Standard Modal

**Structure:**
```
[X close button - top right]
[Title]
[Content area]
[Action buttons - bottom right]
```

**Visual:**
- Centered overlay
- Darkened background (overlay)
- Max width 500-600px
- Rounded corners

**Behavior:**
- Close on X click
- Close on background click
- Close on ESC key
- Trap focus inside modal

**Tell AI:**
"Create modal centered on page, 500px wide, with dark overlay. X button top-right, action buttons bottom-right"

### Confirmation Dialog

**For destructive actions (delete, cancel subscription):**
```
[Warning icon]
"Are you sure you want to delete this project?"
"This action cannot be undone."
[Cancel - gray] [Delete - red]
```

**Tell AI:**
"Create confirmation dialog for delete action. Show warning icon, explain consequence, red 'Delete' button and gray 'Cancel' button"

---

## Input Components

### Text Input

**Visual:**
- Clear border (1px)
- Focus state (blue border + shadow)
- Disabled state (grayed out)
- Error state (red border)
- Success state (green border/checkmark)

**Sizes:**
- Default: 40px height
- Small: 32px height
- Large: 48px height

**Tell AI:**
"Text inputs should be 40px tall, 1px gray border, blue border on focus, red border when error"

### Dropdown / Select

**Visual:**
- Match text input styling
- Down arrow icon on right
- Clear selected value
- Scrollable list for many options

**Behavior:**
- Search/filter for 10+ options
- Keyboard navigation
- Clear indicator of selected item

**Tell AI:**
"Dropdown should match text input styling. Include search when more than 10 options. Show checkmark for selected item"

### Checkbox / Toggle

**Checkbox:** For multiple selections  
**Toggle/Switch:** For on/off settings

**Visual:**
- Clear checked/unchecked states
- Label to the right
- Accessible (44x44px clickable area minimum)

**Tell AI:**
"Use toggle switches for settings, checkboxes for multi-select lists. Minimum 44px clickable area"

---

## Loading States

### Skeleton Screens

**Use for:** Initial page load

**Pattern:**
- Gray rectangles where content will appear
- Subtle animation (pulse or shimmer)
- Matches layout of actual content

**Tell AI:**
"Show skeleton screen during data load - gray rectangles with pulse animation matching the final layout"

### Spinners

**Use for:** Button actions, small updates

**Pattern:**
- Small spinner on button
- Disable button during load
- Replace button text with "Loading..."

**Tell AI:**
"Show spinner on button when clicked, disable button, change text to 'Processing...'"

---

## Common Layouts

### Dashboard Layout

```
[Top Nav Bar]
[Sidebar] [Main Content Area]
          [Metric Cards - top]
          [Charts - middle]
          [Table - bottom]
```

**Examples:** Linear, Stripe, Vercel

### Settings Layout

```
[Top Nav]
[Left Sidebar] [Content Area]
[Setting tabs]  [Form fields]
               [Save/Cancel buttons]
```

**Examples:** GitHub, Linear, Notion

### Landing Page Layout

```
[Nav Bar]
[Hero Section]
[Features Grid]
[Social Proof]
[Pricing]
[CTA]
[Footer]
```

---

## Typography

### Font Recommendations

**Modern SaaS:** Inter, SF Pro, Geist  
**Technical/Code:** JetBrains Mono, Fira Code  
**Playful:** Circular, Avenir

**Tell AI:**
"Use Inter font throughout the app"

### Type Scale

**Headings:**
- H1: 32-36px
- H2: 24-28px
- H3: 20-24px

**Body:**
- Default: 16px
- Small: 14px
- Tiny: 12px

**Line height:**
- Headings: 1.2-1.3
- Body: 1.5-1.6

**Tell AI:**
"Use these font sizes: H1 32px, H2 24px, body 16px, captions 14px. Line height 1.5 for body text"

---

## Color Palette

### Minimal SaaS Palette

**Core:**
- Primary: One brand color (usually blue)
- Gray scale: 50, 100, 200, 300, 400, 500, 600, 700, 800, 900
- Semantic colors: Success green, Error red, Warning yellow

**Example:**
```
Primary: #0070F3 (blue)
Gray 50: #F9FAFB
Gray 900: #111827
Success: #10B981
Error: #EF4444
```

**Tell AI:**
"Use this color palette: Primary #0070F3, Gray scale from #F9FAFB to #111827, Success #10B981, Error #EF4444"

---

## Spacing System

### Consistent Scale

Use multiples of 4 or 8:
- 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px

**Common uses:**
- 4px: Tight spacing (icon + text)
- 8px: Between form fields
- 16px: Card padding
- 24px: Section spacing
- 32px: Between major sections

**Tell AI:**
"Use 8px spacing between form fields, 16px padding in cards, 32px spacing between sections"

---

## References

**Study these for inspiration:**
- Linear (linear.app) - minimal, fast, clean
- Stripe Dashboard - data-heavy done right
- Notion - flexible, calm
- Vercel - modern, technical
- Superhuman - speed-focused

**Component libraries:**
- shadcn/ui: ui.shadcn.com
- Radix UI: radix-ui.com
- Tailwind UI: tailwindui.com (paid)
