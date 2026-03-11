---
name: motion-polish
description: "Use this skill when the user wants to add animations, make transitions smooth, add micro-interactions, or apply final polish. Covers transition patterns, micro-interactions, page transitions, loading animations, scroll interactions, and the restraint principle."
---

# Motion & Polish

Animation is the final 10% that makes a functional app feel premium. Apply motion to reinforce spatial relationships, confirm user actions, and smooth state changes. This skill covers what to animate, how to animate it, and — most importantly — what to leave alone.

## The Restraint Principle

What you don't animate matters more than what you do. If a user notices an animation, it's probably too much. Motion should feel like physics — objects have weight, momentum, and settle into place. It should never feel like a performance.

**Hard rules:**

- Never animate something just because you can. Every animation must serve a purpose: confirm an action, maintain spatial context, or guide attention.
- Never animate more than two things simultaneously. The eye can't track it.
- Never add animation during MVP. Ship the product, then polish.
- If removing an animation makes the UI worse, keep it. If removing it changes nothing, delete it.
- When in doubt, use opacity. Fading is the least distracting transition and works in nearly every context.

---

## Timing and Easing

### Duration Guidelines

| Interaction Type | Duration | Why |
|-----------------|----------|-----|
| Micro-interactions (hover, focus) | 100–150ms | Must feel instant. User expects immediate feedback. |
| Element transitions (expand, collapse) | 150–250ms | Enough to see the change, not enough to wait. |
| Page transitions | 200–300ms | Smooth the jarring content swap. |
| Complex sequences (staggered lists) | 200–400ms total | Individual items faster, total sequence under 400ms. |

**Hard ceiling: 500ms.** No UI animation should ever exceed this. Anything longer feels broken, not polished.

### Easing Functions

- **`ease-out`** — For entrances. Element arrives and decelerates into place. Most common easing in UI.
- **`ease-in`** — For exits. Element accelerates away. Use when something is leaving the screen.
- **`ease-in-out`** — For state changes where the element stays on screen (toggle slide, position shift).
- **Never use `linear`** for UI animations. Linear motion has no acceleration — it feels robotic and mechanical. Reserve it for infinite loops like spinners.

### Tailwind Defaults

```
transition-all duration-150 ease-out    /* micro-interactions */
transition-all duration-200 ease-out    /* element transitions */
transition-all duration-300 ease-in-out /* page/state transitions */
```

For custom easing, define `cubic-bezier` values in your Tailwind config. A good general-purpose curve: `cubic-bezier(0.4, 0, 0.2, 1)` (Material Design standard).

---

## Transition Patterns

### Fade

Use for content replacing content — tab changes, page loads, image swaps.

```css
/* CSS */
.fade-enter { opacity: 0; }
.fade-enter-active { opacity: 1; transition: opacity 200ms ease-out; }
.fade-exit-active { opacity: 0; transition: opacity 150ms ease-in; }
```

Tailwind: `transition-opacity duration-200 ease-out`

Fade is the safest default. When unsure which transition to use, fade.

### Slide

Use for panels, drawers, mobile menus, and side sheets. The direction must match the trigger — a left sidebar slides in from the left, a bottom sheet slides up from the bottom.

```css
/* Slide from right (for side panels) */
.panel { transform: translateX(100%); transition: transform 250ms ease-out; }
.panel.open { transform: translateX(0); }
```

Tailwind for a right panel: `translate-x-full` → `translate-x-0` with `transition-transform duration-250 ease-out`

### Scale

Use for modals, tooltips, popovers, and dropdown menus. Scale from 95% to 100% — not 0% to 100%. The subtle 5% scale change adds life without being dramatic.

```css
.modal { opacity: 0; transform: scale(0.95); transition: all 200ms ease-out; }
.modal.open { opacity: 1; transform: scale(1); }
```

Tailwind: `scale-95 opacity-0` → `scale-100 opacity-100` with `transition-all duration-200 ease-out`

Always combine scale with fade. Scale alone looks jarring.

### Expand / Collapse

Use for accordions, detail disclosures, and expandable sections. Animate `max-height` or `grid-template-rows` — not `height`, which requires knowing the exact pixel value.

```css
/* Modern approach using grid */
.collapsible { display: grid; grid-template-rows: 0fr; transition: grid-template-rows 250ms ease-in-out; }
.collapsible.open { grid-template-rows: 1fr; }
.collapsible > div { overflow: hidden; }
```

Tailwind: Use `grid` with `grid-rows-[0fr]` → `grid-rows-[1fr]` and `transition-all duration-250 ease-in-out`. The inner content needs `overflow-hidden`.

---

## Micro-Interactions

These are the small details that make an app feel alive. Each one takes minutes to implement and compounds into a premium feel.

### Button Feedback

Add a subtle scale on press. Not on hover — on active press.

```
active:scale-[0.98] transition-transform duration-100 ease-out
```

Never go below `scale-[0.95]` — it looks broken, not responsive.

### Hover States

Go beyond color change. Combine two properties for a richer feel:

```
hover:shadow-md hover:-translate-y-0.5 transition-all duration-150 ease-out  /* cards */
hover:bg-gray-100 transition-colors duration-100 ease-out                    /* list items */
```

For primary action buttons, darken the background. For cards, elevate with shadow. For list items, add a background.

### Toggle / Switch

The thumb should slide smoothly, and the track color should transition:

```
/* Track */
transition-colors duration-200 ease-in-out

/* Thumb */
transition-transform duration-200 ease-in-out
```

### Checkbox and Radio

Add a scale bounce on check. The checkmark appears at `scale-100` from `scale-0`:

```
transition-all duration-150 ease-out
```

Do not add rotation or complex keyframes to checkboxes. A simple scale entrance is enough.

### Input Focus

Expand the focus ring outward. Combine `ring` with a color transition on the border:

```
focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all duration-150 ease-out
```

For floating labels, translate the label up and scale it down simultaneously:

```
/* Label moves from inside input to above it */
peer-focus:-translate-y-6 peer-focus:scale-75 transition-all duration-200 ease-out
```

### Link Hover

Animate the underline rather than toggling it. Use a pseudo-element that scales from 0 to 100% width:

```css
a { text-decoration: none; position: relative; }
a::after { content: ''; position: absolute; bottom: 0; left: 0; width: 0; height: 1px;
  background: currentColor; transition: width 200ms ease-out; }
a:hover::after { width: 100%; }
```

---

## Page Transitions

### Staggered List Entrance

When a list of items loads, stagger their entrance so each item fades in 50ms after the previous one. Cap the total at 400ms — after 8 items, all remaining items appear together.

```css
.list-item { opacity: 0; transform: translateY(8px); animation: fadeUp 200ms ease-out forwards; }
.list-item:nth-child(1) { animation-delay: 0ms; }
.list-item:nth-child(2) { animation-delay: 50ms; }
.list-item:nth-child(3) { animation-delay: 100ms; }
/* ... cap at nth-child(8) with 350ms delay */

@keyframes fadeUp { to { opacity: 1; transform: translateY(0); } }
```

Keep the vertical offset small — 8px max. Larger offsets feel sluggish.

### Content Fade on Route Change

When navigating between pages, fade the outgoing content out (150ms) and the incoming content in (200ms). Do not slide pages left/right — that pattern is for mobile native apps, not web.

### Skeleton-to-Content Crossfade

When skeleton placeholders are replaced with real content, crossfade rather than swap. The skeleton fades out as real content fades in, overlapping briefly. Duration: 200ms.

### List Item Reorder

When items change position (sorting, filtering, drag-and-drop), animate the layout shift. Items should glide to their new position over 200ms with `ease-in-out`. In CSS, use `View Transitions API` or in React use `layoutId` (Framer Motion) or `<AnimatePresence>`.

Never let list items jump to new positions without animation — it's disorienting.

---

## Loading and Progress

### Skeleton Shimmer

Use content-shaped placeholder blocks with a shimmer animation. Match the skeleton shape to the real content layout — if the content is a card with a title and two lines of text, the skeleton should have a wide bar and two narrower bars.

```
animate-pulse bg-gray-200 rounded
```

`animate-pulse` is sufficient for most cases. Custom shimmer (a moving gradient) looks more polished but adds complexity — only bother for landing pages or first-impression screens.

### Spinners

Use spinners only in two places: inside buttons during form submission, and as a full-page loader during initial app load. Never use spinners for inline content — use skeletons instead.

Button spinner: replace the button text with a small spinner (16px) and disable the button. Keep the button the same width to prevent layout shift.

### Progress Bars

Use for file uploads, multi-step forms, and any process where you can report a percentage. Animate the width with `transition-all duration-300 ease-out`. Add a subtle stripe or pulse animation to indicate active progress vs. stalled.

### Optimistic UI

The fastest animation is no animation — show the result immediately. When a user toggles a setting, likes a post, or sends a message, update the UI instantly and sync to the server in the background. If the server request fails, revert the UI and show an error toast. This makes apps feel dramatically faster than waiting for a round-trip.

---

## Scroll Interactions

### Sticky Header Shadow

Add a shadow to the header when the user scrolls past 0. This provides a visual cue that there is content above.

```js
// Add shadow-sm when scrolled
window.addEventListener('scroll', () => {
  header.classList.toggle('shadow-sm', window.scrollY > 0);
});
```

Transition the shadow: `transition-shadow duration-200 ease-out`.

### Scroll-Triggered Fade-In

For landing pages, fade in sections as they enter the viewport. Use `IntersectionObserver` — not scroll event listeners. Trigger when 20% of the element is visible.

```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); }
  });
}, { threshold: 0.2 });
```

```css
.reveal { opacity: 0; transform: translateY(16px); transition: all 400ms ease-out; }
.reveal.visible { opacity: 1; transform: translateY(0); }
```

Use this on landing pages and marketing pages. Do not use scroll-triggered animations inside the app dashboard — it slows down task completion.

### Parallax

Almost never use in SaaS apps. Parallax is a marketing site technique that adds visual complexity without functional value. If you absolutely must use it, limit it to the hero section of your landing page and keep the offset subtle (20-30px max).

### Infinite Scroll vs. Pagination

Use pagination for data tables, search results, and anything users need to reference or return to. Use infinite scroll only for social feeds, activity logs, and chat — content that is consumed chronologically and rarely revisited.

---

## Feedback Animations

### Toast Notifications

Entrance: slide + fade from the edge. Standard position is top-right for desktop, top-center for mobile.

```css
.toast { transform: translateX(100%); opacity: 0; transition: all 300ms ease-out; }
.toast.visible { transform: translateX(0); opacity: 1; }
```

Exit: fade out after 4–5 seconds. Use `opacity` only for exit — no slide-out needed.

Include a slim progress bar at the bottom of the toast showing remaining display time. This gives users a sense of control without requiring action.

### Success State

Use a subtle green flash on the saved element, or a checkmark icon that scales in from 0. Keep it under 300ms. Do not use confetti, bouncing checkmarks, or elaborate celebrations for routine actions. Save celebratory animation for milestone events (first project created, first paying customer).

### Error Shake

A horizontal shake draws attention to the error without being aggressive:

```css
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-4px); }
  75% { transform: translateX(4px); }
}
.error-shake { animation: shake 200ms ease-in-out; }
```

Use this on form fields with validation errors or on a login form after failed authentication. Do not shake the entire page or large containers.

### Form Submission Flow

The full sequence for a submit button: idle → loading (spinner replaces text, button disabled) → success (checkmark, green, 1 second) → reset to idle. If error, show error shake on the button and display the error message.

```
/* Button states via Tailwind */
idle:        bg-blue-600 text-white
loading:     bg-blue-600 text-white opacity-75 cursor-not-allowed
success:     bg-green-600 text-white (hold 1s, then transition back)
error:       bg-red-600 text-white (hold 0.5s, then transition back)
```

---

## Reduced Motion

Always respect the user's motion preferences. This is an accessibility requirement, not an optional enhancement.

### CSS Implementation

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

### Tailwind Implementation

Prefix motion-dependent classes with `motion-safe:`:

```
motion-safe:transition-all motion-safe:duration-200 motion-safe:ease-out
motion-safe:animate-pulse
motion-safe:hover:-translate-y-0.5
```

### What to Keep Under Reduced Motion

- **Keep:** Opacity transitions (fade is non-vestibular and generally safe), color transitions, border/shadow changes.
- **Remove:** All transforms (translate, scale, rotate), all keyframe animations, scroll-linked movement, parallax, staggered entrances.
- **Remove delays:** If any animation remains, it should be instant.

---

## CSS vs. JS Animation

### Use CSS When

- Hover and focus states
- Simple enter/exit transitions (fade, slide, scale)
- Skeleton shimmer and spinner loops
- State changes (color, shadow, border)
- Anything triggered by a class toggle

CSS transitions and keyframes are hardware-accelerated, have zero bundle cost, and work without JavaScript loading.

### Use JS (Framer Motion / Motion) When

- Layout animations (elements moving to new positions in the DOM)
- Exit animations (CSS cannot animate an element being removed)
- Spring physics (natural-feeling bounce and settle)
- Gesture-driven animation (drag, pinch, swipe)
- Complex orchestrated sequences (timeline of multiple elements)
- Shared layout transitions (element morphing between two states)

### The Rule

If CSS can do it, use CSS. Framer Motion adds ~30KB to your bundle. That cost is justified for layout animations and exit transitions, but not for hover states and fades.

When using Framer Motion, import only what you need:

```js
import { motion, AnimatePresence } from 'framer-motion';
// NOT: import * as framer from 'framer-motion';
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Animating everything | Apply the restraint principle. Animate interactions, not decorations. |
| Duration too long | If you can perceive the animation as "slow," cut the duration in half. |
| Using `linear` easing | Use `ease-out` for entrances, `ease-in` for exits. |
| Animating `width`/`height` | Animate `transform` and `opacity` — they're GPU-accelerated. `width`/`height` cause layout recalculation. |
| Ignoring `prefers-reduced-motion` | Wrap all motion in `motion-safe:` or the media query. |
| Adding motion during MVP | Ship first. Polish after you have users who will feel the difference. |
| Spinners for inline content | Use skeleton loaders. Spinners are for buttons and full-page loads only. |
| Parallax in a SaaS dashboard | Parallax is for marketing sites. Inside the app, it just gets in the way. |
