---
name: beautify
description: "Use this skill to make an AI-built app look intentionally designed and behave well: 'make it look better,' 'it looks like a template,' 'something looks off,' 'make it look like Stripe or Linear,' 'review my design,' 'is the UI good enough to ship,' 'pick a look for my app,' or when building any new screen. Covers visual direction, hierarchy, spacing, color, type, the five UI states, error messages, accessibility basics, and a design review with a fix order. Not for marketing-page copy (use landing-page)."
metadata:
  version: 1.0.0
---

# Beautify

Make the app look intentionally designed instead of generated, and make every screen handle real data. Restraint is the main tool: fewer colors, fewer weights, fewer borders, fewer shadows.

Read `references/ai-slop-fixes.md` for the 12 patterns AI-generated interfaces fall into and how to fix each one. Examples there use Tailwind class names. Translate them to the project's own styling.

## Choose the mode

- **Direction:** a new app with no visual style yet. Do Step 1.
- **Build:** a new screen. Apply the rules in Steps 2–4 while you build.
- **Review:** existing screens. Do Step 5.

## Step 1: Set a direction (once)

Ask one question: "What are you building, and who is it for?" Do not ask about colors or fonts. The founder reacts to proposals. They should not need design words.

Propose a direction in plain words, based on 1–2 well-known products the users already trust. For example: "Your users have this open all day, so calm and dense, like Linear: one cool accent, tight spacing, clean type." Adjust after the founder reacts. One to three rounds is normal.

Then write a small set of decisions where the project keeps its conventions (CLAUDE.md, or a file the founder names):
- neutral colors, one accent color, and status colors (success, warning, error)
- one font family, with 2–3 weights
- one spacing scale (for example 4, 8, 12, 16, 24, 32, 48 px)
- one corner radius and one shadow, or none

A finished logo is not needed before the first customers. The product name in the heading font is the logo.

## Step 2: Visual rules

- **One focal point per screen.** The primary action is the largest, highest-contrast element. Other buttons are outline or text buttons.
- **Size steps must be obvious.** Headings 50–100% larger than body text. Two sizes 2px apart look like a mistake.
- **Space between groups is 2–3 times the space within a group.** Most AI layouts have too little space between sections.
- **Color carries information.** About 60% neutral, 30% secondary, 10% accent. Never use the full-strength accent color as a large background.
- **Two font weights** for most screens: semibold for headings and labels, regular for body text.
- **Body text no wider than about 65 characters.**
- **Left-align content.** Center only heroes, empty states, and confirmations.
- **Repeated items look identical.** If one pricing card needs emphasis, change one thing: a border or a badge.
- **Reuse before inventing.** A new screen uses the existing buttons, cards, and spacing.

## Step 3: Every data screen handles five states

1. **Loading:** placeholders shaped like the real content. Use spinners only inside buttons and for a full-page load.
2. **Empty:** say what will appear here and give one action to start. An empty screen is onboarding.
3. **Error:** say what happened, why, and how to fix it. Keep the user's input. Never show a stack trace.
4. **Success:** handles long names, missing optional fields, and odd image sizes.
5. **Overflow:** paginate long lists, truncate long text, and show counts.

## Step 4: Behavior and access

- Give feedback within 100ms of every click.
- Prefer **undo** for actions that can be reversed. Ask for confirmation only for irreversible actions, and name the consequence: "Delete 'Q4 Report'? This cannot be undone."
- Text contrast of at least 4.5:1. A visible keyboard focus. A label on every input. Touch targets of at least 44px. The whole flow works with the keyboard.
- Motion only to confirm an action or to keep the user oriented: 150–250ms, ease-out. Respect reduced-motion settings. Skip decorative animation before the product has customers.
- Check every screen at phone width. Mobile breakage matters from the first customer.

## Step 5: Review existing screens

Run the app and look at the screens. Take screenshots if you can. Name each issue by location ("the secondary button in the hero has the same weight as the main button"), not by feeling.

Fix in this order, one category at a time. Re-check after each category, because early fixes often solve later ones:

1. Hierarchy: is the eye drawn to the main action?
2. Spacing and alignment
3. Color
4. Typography
5. Consistency across screens: the same header, padding, buttons, and cards everywhere
6. The five states
7. Phone width
8. Motion and polish

**When to stop:** before 10 customers, stop after items 1–4 and 7. The goal is "intentionally designed," not "award-winning." Stop when the design no longer distracts from the product.

## Output

- Direction mode: the decisions written to the file the founder chose.
- Review mode: issues grouped by the order above, each with its location and fix. Then fix them, one category at a time.
