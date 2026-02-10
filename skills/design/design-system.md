# Design System Reference

When you use a component library (shadcn/ui, Radix, etc.), your AI tool handles the implementation details. This reference helps you know what's available and how to ask for it.

---

## Choosing a Component Library

| Library | Best For | Works With |
|---------|----------|------------|
| **shadcn/ui** | Most SaaS apps. Clean, professional, customizable. | Next.js, React, Tailwind |
| **Radix UI** | Accessible primitives (shadcn is built on this) | React |
| **Headless UI** | Tailwind-first, fewer components | React, Vue |
| **Material UI** | Google-style design, large component set | React |

**Recommendation:** Start with **shadcn/ui**. It's the default choice for most AI coding tools and has the best coverage for SaaS patterns.

**Tell AI:**
```
Set up shadcn/ui in our project. Install the core components we'll need:
Button, Card, Dialog, Input, Label, Select, Table, Tabs, Toast, Badge, Form.
Use the default theme with [your brand color] as the primary color.
```

---

## Components You'll Actually Use

You don't need all 49+ components from day one. Here are the ones that cover 90% of SaaS UI needs:

### Must-Have (Install First)

| Component | Use For |
|-----------|---------|
| **Button** | Every action (primary, secondary, destructive, ghost, link variants) |
| **Card** | Content containers, dashboard widgets, settings sections |
| **Dialog** | Confirmations, create/edit forms, important actions |
| **Input + Label** | All form fields (always pair them) |
| **Select** | Dropdowns for choosing from a list |
| **Table** | Displaying data (users, invoices, projects) |
| **Toast** | Success/error notifications after actions |
| **Badge** | Status indicators (active, trial, overdue) |
| **Form** | Form validation and error handling |

### Add When Needed

| Component | Use For |
|-----------|---------|
| **Tabs** | Switching between views on the same page |
| **Sheet** | Slide-out panels for detail views |
| **Alert** | Important messages (warnings, errors, info) |
| **Dropdown Menu** | Action menus (settings, user menu, "more" menus) |
| **Skeleton** | Loading states while data fetches |
| **Progress** | Upload progress, onboarding completion |
| **Avatar** | User profile images |
| **Pagination** | Navigating through long lists |
| **Command** | Search/command palette (power user feature) |
| **Accordion** | FAQ sections, collapsible settings |

**Tell AI:**
```
Add [component name] from shadcn/ui to our project.
Use it on [page name] for [what it should do].
```

---

## Design Tokens: What to Decide

You don't need to set CSS variables yourself. Just decide these things and tell AI:

### Colors

| Decision | What to Tell AI |
|----------|----------------|
| Primary brand color | "Use #3B82F6 (blue) as our primary color" |
| Semantic colors | Use defaults: green=success, red=error, amber=warning, blue=info |
| Dark mode | "Add dark mode support" (or skip for now) |

### Typography

| Decision | What to Tell AI |
|----------|----------------|
| Font | "Use Inter" (safe default) or "Use the system font stack" |
| Headings | Handled automatically by the component library |

### Spacing and Radius

| Decision | What to Tell AI |
|----------|----------------|
| Rounded corners | "Use rounded corners" (default) or "Use sharp corners" |
| Spacing | Handled by the component library's defaults |

**Tell AI:**
```
Set up our design tokens:
- Primary color: [your hex color]
- Font: Inter (or system fonts)
- Border radius: default rounded (8px)
- Include dark mode support: [yes/no]
```

---

## Button Patterns

Buttons are the most used component. Know which variant to use:

| Variant | When to Use | Example |
|---------|-------------|---------|
| **Primary** (filled) | The main action on the page | "Create Project", "Save Changes" |
| **Secondary** (outlined) | Alternative actions | "Cancel", "Export" |
| **Destructive** (red) | Dangerous/irreversible actions | "Delete Account" |
| **Ghost** (no border) | Subtle actions, toolbars | Settings icon, close button |
| **Link** (text only) | Navigation-like actions | "Learn more", "View all" |

**Rule:** Only one primary button per section. If two actions compete, one should be secondary.

---

## Common Patterns to Ask For

**Tell AI:**
```
Build a [pattern] using shadcn/ui components:

Dashboard layout:
- Sidebar navigation with collapsible sections
- Top bar with user avatar and dropdown menu
- Main content area with card-based widgets

Settings page:
- Tabbed layout (Profile, Billing, Notifications, Team)
- Form inputs with validation and save button per section

Data table:
- Sortable columns, search/filter bar, pagination
- Row actions via dropdown menu (edit, delete)
- Empty state with CTA when no data exists

Modal form:
- Dialog with form inputs, validation, and submit/cancel buttons
- Close on success with toast notification
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Installing all 49 components upfront | Install only what you need. Add more as you build. |
| Customizing component internals | Use variants and props first. Only customize if the built-in options don't work. |
| Mixing component libraries | Pick one library and stick with it. Mixing creates inconsistency. |
| Skipping loading/error states | Every data-fetching component needs: loading (skeleton), error (alert), empty (CTA) states. |
| No dark mode consideration | Either support dark mode from day one or explicitly decide not to. Don't leave it half-done. |
