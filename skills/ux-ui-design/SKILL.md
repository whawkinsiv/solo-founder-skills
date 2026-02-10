---
name: ux-ui-design
description: "Use this skill when the user needs to improve their app's UI, fix visual hierarchy, refine interactions, or apply design best practices. Covers visual hierarchy, interaction patterns, design systems, mobile-first design, spacing, and usability."
---

# UX/UI Design

Good UI doesn't require a design degree. It requires knowing what matters, what to skip, and what to tell AI. This skill gives you the decisions and the prompts.

## What You Decide vs. What AI Implements

| You Decide | Claude Code Implements |
|------------|----------------------|
| "This page's goal is getting users to create a project" | Visual hierarchy that makes the CTA dominant |
| "We need a settings page with tabs" | Tabbed layout with proper spacing and states |
| "The dashboard should show key metrics first" | Card layout with data visualization |
| "Forms should validate as users type" | Inline validation with clear error messages |

**Rule:** You define the goal of each screen. AI handles the pixels.

---

## Priority Order: What to Get Right First

### Tier 1: Gets You 80% of the Way

1. **One primary action per screen** — If you can't name it, the page is broken.
2. **Visual hierarchy** — Size, weight, and contrast guide the eye. Most important = biggest.
3. **Consistent spacing** — Use your component library's defaults. Don't manually tweak pixels.
4. **Design states** — Every screen needs: empty, loading, error, success, and overflow states.

### Tier 2: After Launch

5. **Mobile responsiveness** — Test core flows on mobile. 50%+ of traffic may be mobile.
6. **Micro-interactions** — Loading spinners, success checkmarks, smooth transitions.
7. **Keyboard navigation** — Tab through every form. Escape closes every modal.

---

## Screen-by-Screen Guidance

### Dashboard

**Tell AI:**
```
Design a SaaS dashboard that shows:
- 3-4 key metric cards at the top (e.g., MRR, active users, signups this week)
- A recent activity feed or table below
- A primary CTA: "Create [your main object]"
- Empty state for new users with onboarding guidance
Use [component library]. Mobile-responsive.
```

### Settings Page

**Tell AI:**
```
Create a settings page with tabs:
- Profile (name, email, avatar)
- Billing (current plan, usage, manage subscription link)
- Notifications (email preferences with toggles)
- [Team/API/other sections you need]
Each tab has its own save button. Show success toast on save.
```

### Data Tables

**Tell AI:**
```
Build a data table for [items — users, projects, invoices]:
- Columns: [list your columns]
- Sortable by [which columns]
- Search/filter bar above the table
- Row actions: edit, delete (with confirmation dialog)
- Pagination for 20+ items
- Empty state: "No [items] yet. Create your first one."
```

### Forms

**Tell AI:**
```
Create a [create/edit] form for [object]:
- Fields: [list fields with types — text, email, select, etc.]
- Validate on blur (not on every keystroke)
- Show inline errors below each field
- Submit button disabled until form is valid
- Show loading state on submit, success toast on completion
```

---

## Component Selection Guide

When you're not sure what UI element to use:

| Situation | Use This |
|-----------|----------|
| User needs to choose from 3-5 options | Radio buttons or segmented control |
| User needs to choose from 6+ options | Select dropdown |
| Yes/no toggle | Switch |
| Confirming a destructive action | Alert dialog ("Are you sure?") |
| Showing transient feedback | Toast notification (auto-dismiss) |
| Showing persistent info/warning | Alert banner (stays until dismissed) |
| Editing a record without leaving the page | Dialog or sheet (slide-out panel) |
| Navigating between views | Tabs (same page) or sidebar nav (different pages) |
| Showing user status | Badge (active, trial, overdue) |

---

## Visual Hierarchy Checklist

For every screen, verify:

- [ ] The primary action is the most visually prominent element
- [ ] Only ONE primary button per section (others are secondary or ghost)
- [ ] Headings use size + weight to create clear hierarchy (h1 > h2 > h3)
- [ ] Related items are grouped with consistent spacing
- [ ] Labels are above inputs (not placeholder-only)
- [ ] Color is not the only way to convey meaning (add icons or text)

**Tell AI:**
```
Review the visual hierarchy of [page/component]:
- What is the primary action? Make it the most prominent element.
- Are there competing CTAs? Demote secondary ones to outline/ghost buttons.
- Is the heading hierarchy logical (h1 → h2 → h3, no skipping)?
- Is there enough whitespace between sections?
```

---

## Spacing and Layout Rules

You don't need to memorize pixel values. Just follow these principles:

| Principle | What It Means |
|-----------|--------------|
| **Section spacing > element spacing** | Space between "Profile" and "Billing" sections should be larger than space between form fields |
| **Group related items** | Fields that belong together should be closer together |
| **Consistent padding** | Cards, containers, and modals should all use the same internal padding |
| **Generous touch targets** | Buttons and clickable areas: minimum 44x44px |

**Tell AI:**
```
Fix the spacing on [page/component]:
- Add more space between major sections
- Tighten spacing between related form fields
- Ensure consistent padding inside all cards
- Make sure all buttons are at least 44px tall
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Two primary buttons side by side | One should be secondary (outlined). Only one primary per section. |
| No empty state | Every list/table needs a "nothing here yet" message with a CTA. |
| No loading state | Show skeleton loaders or spinners while data fetches. |
| Placeholder text as labels | Always use a visible label above the input. Placeholders disappear. |
| Too many things on one screen | Progressive disclosure: show the essentials, hide advanced options behind "Show more" or tabs. |
| Inconsistent alignment | Left-align text, right-align numbers. Don't center body text. |
| Ignoring mobile | Test your most important flow on a phone-sized screen. |
