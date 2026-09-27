# Component Reference

Use this reference when selecting and implementing UI components. Specs assume shadcn/ui + Tailwind CSS unless noted otherwise.

---

### Buttons

**When to use:** Every user-initiated action. The most important component to get right — inconsistent buttons undermine the entire interface.

**Variants:**
- **Primary** (`default`): Solid background, high contrast. One per visible section — the main action.
- **Secondary** (`secondary`): Muted background. Supporting actions: "Cancel", "Back", "Save Draft".
- **Destructive** (`destructive`): Red background. Delete, remove, revoke actions. Always require confirmation for irreversible operations.
- **Ghost** (`ghost`): No background, shows on hover. Toolbar actions, icon buttons, compact UIs.
- **Outline** (`outline`): Border only. Alternative to secondary when you need visual distinction.
- **Link** (`link`): Looks like a text link. Inline actions within text or for navigation-like actions.

**Key specs:**
- Default height: `h-10` (40px). Small: `h-9` (36px). Large: `h-11` (44px). Icon-only: `h-10 w-10`.
- Min width for text buttons: 80px. Don't let buttons be narrower than their label needs.
- Border radius: `rounded-md` (6px) — matches shadcn/ui defaults.
- Disabled state: `opacity-50 pointer-events-none`. Never hide buttons to indicate disabled — show them disabled with a tooltip explaining why.

**Placement rules:**
- Primary action goes rightmost in a button group. Destructive actions go leftmost, separated by a spacer.
- Form submit buttons: right-aligned. "Cancel" to the left of "Submit".
- Sticky bottom bar for long forms: `fixed bottom-0` with `border-t bg-background p-4`.
- Icon + label is better than icon alone for primary actions. Icon-only is fine for well-known actions (edit pencil, delete trash, close X) in toolbars.

**Loading state:** Replace label with spinner + "Loading..." or action-specific text ("Saving..."). Keep button width stable — don't let it resize when text changes. Use `disabled` during loading.

---

### Forms

**When to use:** Any data collection — settings, onboarding, creation flows, filters.

**Layout:**
- Single column for most forms. Two-column only when fields are logically paired (first name / last name, city / state).
- Label above input, not beside it. Label font: `text-sm font-medium`. Color: `text-foreground`.
- Optional field indicator: "(optional)" text after label. Don't mark required fields with asterisks — mark optional ones instead since most fields are required.
- Field spacing: `space-y-4` between fields. `space-y-6` between field groups.
- Group related fields with a section heading: `text-lg font-semibold` with `space-y-4` below.
- Max form width: `max-w-lg` (512px) for single-column forms. Inputs shouldn't stretch wider than ~500px.

**Validation display:**
- Inline validation below the field: `text-sm text-destructive mt-1`.
- Validate on blur for individual fields. Validate on submit for cross-field rules.
- Show error state on the input: `border-destructive focus-visible:ring-destructive`.
- Summary error banner at form top for server-side errors: `bg-destructive/10 border border-destructive/20 rounded-md p-4`.
- Success feedback: toast notification on save, or inline success message. Don't navigate away without confirmation the action succeeded.

**Multi-step forms:**
- Show step indicator: numbered steps with labels, current step highlighted.
- Persist data between steps — never lose input on back navigation.
- Validate each step before allowing progression.
- Show summary/review step before final submission for important flows (checkout, onboarding).

---

### Inputs

**When to use:** Individual form controls for specific data types.

**Text input:**
- Height: `h-10` (40px). Font: `text-sm`. Padding: `px-3`.
- Placeholder text: describe format or example, not the label. "jane@example.com" not "Enter your email".
- Prefix/suffix support: icon or text inside the input (search magnifier, currency symbol). Use `relative` positioning with `pl-10` for icon offset.

**Select:**
- Same height as text inputs (40px). Use shadcn/ui `Select` for custom styling, native `<select>` only for very simple cases.
- For 5+ options or searchable lists: use a `Combobox` (searchable select). Provide type-ahead filtering.
- Multi-select: use `Combobox` with pills/tags showing selected items.

**Checkbox:**
- Size: `h-4 w-4` (16px). Label to the right with `ml-2`.
- Group spacing: `space-y-2` between checkbox items.
- Use checkboxes for multi-select from a short list (2-7 items). Beyond 7, use a multi-select combobox.

**Toggle/Switch:**
- Use for binary on/off settings where the effect is immediate (no form submit needed).
- Label to the left, toggle to the right. Description text below the label in `text-sm text-muted-foreground`.
- Size: `h-6 w-11` default. Never use toggles inside forms that have a submit button — use checkboxes instead.

**Textarea:**
- Min height: `h-20` (80px). Allow vertical resize: `resize-y`.
- Show character count for limited fields: `text-xs text-muted-foreground` aligned right below the textarea.
- For rich text: integrate a lightweight editor (Tiptap) rather than building custom formatting controls.

---

### Cards

**When to use:** Grouping related content into a distinct visual unit.

**Metric cards (dashboard KPIs):**
- Fixed height per row for visual consistency. Typical: 120-140px.
- Structure: label (`text-sm text-muted-foreground`) top, value (`text-2xl font-bold`) center, trend/change indicator bottom.
- Grid: `grid grid-cols-2 lg:grid-cols-4 gap-4`.
- Trend indicator: green up arrow / red down arrow with percentage. Use `text-emerald-600` and `text-red-600`.

**Content cards (list items, feed entries):**
- Padding: `p-4` or `p-6`. Border: `border rounded-lg`.
- Structure: title, metadata line (date, author, status badge), truncated description, action links.
- Hover state if clickable: `hover:bg-muted/50 cursor-pointer transition-colors`.

**Interactive cards (selectable options, plan selection):**
- Selected state: `border-primary ring-2 ring-primary/20`.
- Unselected: `border hover:border-primary/50 cursor-pointer`.
- Radio-card pattern: wrap in a group, one selectable at a time.

---

### Tables (Data Tables)

**When to use:** Displaying structured data with multiple attributes per item. 5+ items with 3+ columns.

**Key specs:**
- Row height: 48-52px. Header: `text-sm font-medium text-muted-foreground`. Cells: `text-sm`.
- Horizontal padding: `px-4` per cell. First and last cells get `px-6`.
- Striped rows optional: `even:bg-muted/50`. Hover: `hover:bg-muted`.
- Border: bottom border on rows `border-b`. No vertical cell borders.
- Column alignment: text left, numbers right, status/badges center, actions right.

**Sorting:** Clickable column headers with sort direction indicator (chevron up/down). Active sort column gets `font-semibold`. Default sort on the most useful column (usually date, descending).

**Filtering:** Filter bar above the table. Search input + dropdown filters. Show active filter count: "3 filters applied" with clear-all option.

**Pagination:** Below the table. Show: "Showing 1-10 of 148 results". Page size selector: 10, 25, 50. Previous/Next buttons + page numbers for large sets.

**Row actions:** Right-most column. For 1-2 actions: inline icon buttons. For 3+: kebab menu (three dots) opening a dropdown. Always include the most common action as the first dropdown item.

**Empty state:** Replace the entire table body with a centered empty state message. Don't show column headers with "No results" in a single cell.

**Mobile:** Transform to card layout. Each card shows the 3-4 most important fields. Tap to expand or navigate to detail view. Provide a way to access the full table view if needed.

---

### Modals / Dialogs

**When to use:** Focused tasks that require attention before proceeding. Don't use for information that could be inline.

**Standard dialog:**
- Max width: `sm:max-w-lg` (512px). For forms with more content: `sm:max-w-xl` or `sm:max-w-2xl`.
- Structure: title, optional description, content, footer with actions.
- Footer buttons right-aligned: secondary action left, primary action right.
- Close: X button top-right, click outside to close, Escape key. Prevent close-on-outside-click for forms with unsaved changes.

**Confirmation dialog:**
- Use for destructive actions. Short and direct.
- Title: "Delete project?" not "Are you sure you want to delete this project?"
- Description: state the consequence. "This will permanently delete the project and all its data."
- Buttons: "Cancel" (secondary) and "Delete" (destructive). Match the button label to the action.

**Form dialog:**
- Same as standard with a form inside. Disable submit until valid. Show validation inline within the modal.
- If the form is longer than the viewport: use a sheet/slide-out instead of a modal.

**Rules:**
- Never stack modals. If a modal needs to trigger another action, use inline content or close the first modal.
- On mobile (<640px), modals become full-screen sheets sliding up from bottom.
- Always trap focus within the modal. Return focus to the trigger element on close.

---

### Navigation

**Sidebar navigation:**
- Width: 240-280px. Collapsible to icon-only: 64px.
- Structure: logo/brand top, primary nav items, spacer/divider, secondary items (settings, help), user menu bottom.
- Active state: `bg-muted font-medium`. Hover: `hover:bg-muted/50`.
- Icon + label for each item. Icons: 20px (`h-5 w-5`). Gap between icon and label: `gap-3`.
- Nested sections: collapsible groups with chevron indicator. Indent children by `pl-8`.
- On `lg` breakpoint and above: always visible. Below: overlay with backdrop, triggered by hamburger button.

**Top navigation:**
- Height: 56-64px. `border-b` bottom border.
- Left: logo + primary nav links. Right: search, notifications, user avatar menu.
- Use for apps with 4-6 top-level sections max. Beyond that, use sidebar.

**Breadcrumbs:**
- Use on detail pages and nested views. Show full path from section root.
- Separator: `/` or chevron. Truncate middle items with `...` if path exceeds 4 levels.
- Current page (last item): not a link, `text-foreground`. Previous items: `text-muted-foreground hover:text-foreground`.

**Tabs:**
- Use for switching views within a page without navigation. Content stays on the same page.
- Bottom border style: active tab has `border-b-2 border-primary`. Inactive: `text-muted-foreground hover:text-foreground`.
- Don't use more than 6-7 tabs. If more needed, use a select dropdown or sidebar sub-nav.

**Command palette (Cmd+K):**
- Implement for power users in apps with many sections/actions. Use `cmdk` library.
- Search across: pages, recent items, actions, settings. Group results by category.
- Not needed for MVP unless the app has 15+ distinct pages.

---

### Toast / Notifications

**When to use:** Feedback after user actions. Non-blocking confirmations.

**Positioning:** Top-right corner of viewport. Stack multiple toasts vertically with `gap-2`. Use `sonner` or shadcn/ui toast.

**Auto-dismiss timing:**
- Success toasts: 3-4 seconds.
- Error toasts: persist until dismissed (user needs time to read and act).
- Info toasts: 5 seconds.

**Variants:**
- Success: checkmark icon, green accent.
- Error: X icon, red accent. Include retry action if applicable.
- Info: info icon, blue accent.
- Warning: alert triangle, yellow accent.

**Specs:** Max width: 356px. Padding: `p-4`. Border radius: `rounded-lg`. Shadow: `shadow-lg`.

**Rules:** Don't use toasts for validation errors (those go inline on the form). Don't use toasts for information the user hasn't requested — that's a notification badge or banner.

---

### Badges

**When to use:** Status indicators, counts, labels, tags.

**Status badges:** Small pills showing state. `Active` (green), `Pending` (yellow), `Inactive` (gray), `Error` (red).
- Height: `h-5` or `h-6`. Font: `text-xs font-medium`. Padding: `px-2`.
- Use dot indicator before text for status: colored circle (`h-1.5 w-1.5 rounded-full`) + label.

**Count badges:** Notification counts on nav items or icons.
- Small: `h-5 w-5 text-xs` for single/double digit. Position: `absolute -top-1 -right-1`.
- Show "99+" for counts over 99.

**Label badges:** Categorization tags. Used in tables, cards, filters.
- Outline variant for low emphasis. Filled variant for high emphasis.
- Removable tags: add X button inside the badge.

---

### Dropdowns

**Action menus:** Triggered by a button (kebab menu, "More" button). Contains action items with optional icons, dividers between groups, and destructive items at the bottom separated by a divider.

**Selection menus:** Triggered by a button showing current selection. Contains selectable items with checkmarks. Use `DropdownMenuCheckboxItem` or `DropdownMenuRadioGroup` from shadcn/ui.

**Specs:** Min width: 160px. Max width: 320px. Item height: 36px. Padding: `px-2 py-1.5`. Keyboard navigation: arrow keys, Enter to select, Escape to close.

---

### Sheets / Slide-outs

**When to use:** Instead of modals when content is long or when the user needs to reference the page behind it. Detail views, long forms, multi-step processes.

- Slide in from the right on desktop. Width: `sm:max-w-md` (448px) or `sm:max-w-lg` (512px).
- On mobile: full-screen, slide up from bottom.
- Include close button and optional back navigation for multi-step.
- Backdrop: semi-transparent overlay on the page behind.

---

### Skeleton Loaders

**When to use:** While async content is loading. Replace each content block with a skeleton that matches its dimensions.

**Implementation:**
- Use `bg-muted animate-pulse rounded-md` blocks.
- Text lines: height `h-4`, varying widths (100%, 80%, 60%) to look natural.
- Avatars: `rounded-full` with matching size.
- Cards: full card outline with skeleton blocks inside.
- Tables: full row outlines with cell-width-matched blocks. Render 5-8 skeleton rows.
- Images: exact aspect ratio container with skeleton fill.

**Rules:** Never mix skeleton loaders with real content in the same container. Load the entire section or show the entire skeleton. Remove skeletons all at once, not one by one (avoids layout shifts).
