---
name: ux-design
description: "Use this skill when flows feel clunky, users are confused, navigation needs planning, onboarding needs design, or accessibility needs implementation. Covers information architecture, user flows, interaction patterns, progressive disclosure, and error handling UX."
---

# UX Design — Flows, Structure & Interaction

Design how users move through the app, find what they need, and accomplish tasks with minimal friction. This skill covers the structural and behavioral layer of UX — information architecture, navigation, user flows, interaction patterns, and error handling. For visual design (colors, typography, layout), see the aesthetics and ui-patterns skills. For onboarding flows, see ONBOARDING.md. For accessibility implementation, see ACCESSIBILITY.md.

## Information Architecture

The goal of IA is that users never have to think about where to find something. Navigation should match the user's mental model, not the database schema or org chart.

### Core Principles

- **Flat > deep.** Every additional level of nesting loses users. Aim for max 2 levels of hierarchy in navigation.
- **Labels are architecture.** Vague labels cause wrong turns. If a label needs explanation, change the label.
- **Group by user task, not data type.** "Marketing Assets" beats "Images | Documents | Videos." Users think in workflows, not file formats.
- **5-9 items per group** (Miller's Law). More than 9 items in a nav section means it needs restructuring.
- **Most-used items first.** Alphabetical ordering is lazy architecture — prioritize by frequency of use.

### URL Structure

URLs must mirror the information architecture:

```
/dashboard
/projects
/projects/[id]
/projects/[id]/settings
/settings/profile
/settings/billing
```

Rules:
- Nouns, not verbs: `/projects` not `/manage-projects`
- Lowercase with hyphens: `/team-members` not `/teamMembers`
- Meaningful IDs when possible: `/projects/acme-q4` not `/projects/a1b2c3`
- Max 3 levels of depth in the URL path
- Filter state in query params (`?status=active&owner=me`) for shareability

### Page Content Hierarchy

Every page must answer four questions in visual priority order:

1. **Where am I?** — Page title + breadcrumbs
2. **What can I do here?** — Primary actions visible above the fold
3. **What are the sub-sections?** — Tabs, cards, or clearly labeled sections
4. **What's most important?** — Visual hierarchy (size, weight, position) makes this obvious without reading

### Page Types

- **Dashboard:** Overview metrics + quick actions + recent activity. Never just a list of links.
- **List page:** Filterable, sortable, searchable collection. Primary CTA to create new item. Show item count.
- **Detail page:** Single object with all its information. Actions in the page header. Related objects linked.
- **Settings page:** Grouped form fields. Save per-section, not one giant save button for the entire page.
- **Empty state:** Explains what this page will contain + single CTA to add the first item. Never show an empty table with column headers.

## Navigation Patterns

Choose the pattern based on product complexity and number of sections:

### Decision Framework

| Pattern | When to use | Item count |
|---------|------------|------------|
| **Top nav (horizontal)** | Sections are equally important, product is simple | 3-7 top-level items |
| **Sidebar (vertical)** | Complex product, long sessions, sections have subsections | 5-20 items with grouping |
| **Tabs** | Related views of the same object (Overview / Activity / Settings) | 2-6 tabs on a single entity |
| **Command palette** | Power users, large apps, cross-cutting actions | Any size — supplements primary nav |
| **Breadcrumbs** | Depth > 2 levels — always show path back to parent | On all pages except homepage |

### Sidebar Best Practices

Group items with visual section headers. Use collapsible sections for depth. Structure:

```
WORKSPACE
  Dashboard
  Projects
  Templates
SETTINGS
  Profile
  Billing
  Integrations
```

### Command Palette (Cmd+K)

Implement as a modal overlay triggered by Cmd+K / Ctrl+K. Include three types of results:
- **Navigation:** "Go to Settings," "Open Projects"
- **Actions:** "Create project," "Invite teammate"
- **Search:** "Find user John," "Search invoices"

### Search and Filtering

- Global search accessible from every page (header search bar)
- Filters visible, not hidden in menus — show count of applied filters
- Common filter dimensions: Status, Date range, Owner, Tags/Labels
- Support saved/preset filters for common queries
- Persist filter state in URL query params for shareability and bookmarking

## User Flows

### Task Analysis

When designing or improving a flow, map the current steps a user takes to accomplish their goal. Then reduce:

1. **List every step** the user takes from intent to completion (including navigation, clicks, form fields, confirmations).
2. **Identify friction points:** Where does the user pause, make decisions, wait, or get confused?
3. **Eliminate steps:** Every step must earn its place. Can two steps merge? Can a default eliminate a choice? Can a step be deferred to later?
4. **Target: 3-click rule for common tasks.** The most frequent user actions should require no more than 3 interactions from any starting point.

### Step Reduction Principles

- **Smart defaults** over blank forms — pre-fill everything inferable from context
- **Inline creation** over navigate-to-form — let users create items where they need them
- **Bulk operations** over one-at-a-time — if users do it to 10 items, let them do it to 10 at once
- **Remember choices** — if the user picked a filter or view last time, restore it
- **Combine related steps** — name + description on the same screen, not two separate screens

## Interaction Patterns

### Feedback — What Happens When You Click

Every user action must produce visible feedback within 100ms. If the operation takes longer:
- **< 1 second:** Show a spinner on the button or inline indicator
- **1-10 seconds:** Show a progress indicator or skeleton screen
- **> 10 seconds:** Show a progress bar with estimated time; allow background processing with notification on completion

### Confirmation vs. Undo

| Approach | When to use |
|----------|------------|
| **No confirmation** | Reversible actions with no data loss (archiving, toggling, moving) |
| **Undo toast** | Destructive but recoverable actions (deleting a list item, removing a team member). Show "Undo" for 5-8 seconds. |
| **Confirmation dialog** | Irreversible, high-stakes actions only (deleting an account, publishing to production, bulk delete). Require typing a confirmation string for the most dangerous actions. |

Default to undo over confirmation dialogs. Confirmation dialogs interrupt flow and users click "OK" without reading them.

### Inline vs. Modal Editing

- **Inline editing** for single-field changes (rename, status change, quick note). Click to edit, blur or Enter to save.
- **Modal/drawer** for multi-field edits that need context isolation (edit profile, configure integration).
- **Full page** for complex creation flows (multi-step wizard, document editor).

### Optimistic vs. Pessimistic Updates

- **Optimistic** (update UI immediately, sync in background): Use for low-risk operations where failure is rare — toggling, liking, reordering, editing text. Roll back on failure with an error toast.
- **Pessimistic** (wait for server, then update UI): Use for financial transactions, permission changes, external API calls, and anything where partial failure creates inconsistency.

## Progressive Disclosure

Reveal complexity gradually. Four levels:

| Level | What to show | Example |
|-------|-------------|---------|
| **Essential** | Always visible — the core data and primary actions | List view with key columns, main CTA |
| **On interaction** | Revealed by hover, click, or expand | Row hover actions, expandable details, tooltip info |
| **On demand** | Available through explicit navigation or settings | Advanced settings, raw data view, export options |
| **Discoverable** | For power users who seek it out | Keyboard shortcuts, API access, bulk actions, command palette |

### When Hiding Makes UX Worse

Do not hide behind progressive disclosure:
- **Error states** — always surface errors prominently
- **Destructive consequences** — always show what will be deleted/changed
- **Required information** — never put required fields in collapsed sections
- **Current state** — the user should always see what's active, selected, or in progress

## Error Handling UX

### Error Message Pattern

Every error message must answer three questions:

1. **WHAT happened** — "Your payment failed" (not "Error 402")
2. **WHY it happened** — "Your card was declined by your bank"
3. **HOW TO FIX it** — "Update your payment method or try a different card" [with a link to payment settings]

### Error State Design

- **Form validation:** Validate inline on blur, not on submit. Show the error adjacent to the field, not in a banner at the top. Use `aria-invalid` and `aria-describedby` to link error text to the field.
- **Empty results:** "No projects match your filters" with a CTA to clear filters — never a blank screen.
- **Failed loads:** Show the last known good state with a "Retry" option, or a friendly error state with clear next steps.
- **Partial failures:** If 8 of 10 items succeed, show success for the 8 and specific errors for the 2.

### Retry Patterns

- Auto-retry network failures with exponential backoff (1s, 2s, 4s) — max 3 attempts
- Show a manual "Retry" button after auto-retries are exhausted
- For background operations, queue retries silently and notify on persistent failure

### Graceful Degradation

When a feature or service is unavailable:
- Show the rest of the page normally — do not block the entire UI
- Display a contextual message where the failed component would appear
- Provide an alternative path if one exists ("Analytics are temporarily unavailable. View raw data instead.")

## Performance Perception

Perceived speed matters more than actual speed. Techniques by situation:

| Technique | When to use |
|-----------|------------|
| **Optimistic updates** | User actions on their own data (edits, toggles, creates). Update UI immediately. |
| **Skeleton screens** | Initial page loads and data fetching. Show the layout shape before content arrives. Better than spinners for content-heavy pages. |
| **Progress indicators** | File uploads, data imports, long computations. Show percentage or steps completed. |
| **Lazy loading** | Below-the-fold content, images, secondary data. Load what's visible first. |
| **Prefetching** | Links the user is likely to click next (visible nav items, "next" in a pagination). Fetch data on hover or viewport entry. |

### Rules

- Never show a blank white screen. Always show structure (skeleton) or previous state.
- Animate transitions between states (loading → loaded) to avoid jarring layout shifts.
- If an operation completes in < 200ms, do not show a loading indicator — it creates a flash that feels slower.
- Prioritize above-the-fold content. The user does not need everything loaded before they can start reading or interacting.
