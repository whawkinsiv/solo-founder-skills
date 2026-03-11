# Onboarding Design

Onboarding has one job: get users to the aha moment as fast as possible. Everything else is noise. The best onboarding feels like using the product, not learning the product — interactive beats passive, doing beats reading.

## Aha Moment Definition

Before designing onboarding, identify the single experience that makes a user say "I need this." Use this framework:

1. **Look at retained users:** What action did 80%+ of them take in their first week?
2. **Look at churned users:** What action did they NOT take?
3. **The gap** between these two groups is the activation metric. Onboarding exists to close this gap.

Examples of aha moments:
- **Project management tool:** Created a project and added a task
- **Analytics platform:** Saw their first dashboard with real data
- **Communication tool:** Sent and received a message from a teammate
- **Design tool:** Created and shared their first design

If the product is pre-launch and there is no retention data, identify the aha moment by asking: "What is the smallest demonstration of the product's core value?" Design onboarding to reach that moment in the fewest possible steps.

## Onboarding Patterns

Choose the pattern based on product characteristics. Multiple patterns can be combined.

### 1. Setup Wizard

**Best for:** Products that require configuration before they are useful (workspace setup, data connection, role selection).

Implementation:
- 3-5 steps maximum. Each step asks ONE question or performs ONE action.
- Show a progress indicator: "Step 2 of 4"
- Always allow "Skip" on each step — but track skip rates. High skip rate on a step means the step is not earning its place.
- The final step must land on a populated, useful state — never a blank dashboard.

Typical flow:
1. "What will you use [Product] for?" — role/use-case selection
2. "Set up your workspace" — name, invite link generation
3. "Connect your data" — integration or import
4. "Here's your first [core object]" — pre-populated with their data

### 2. Checklist

**Best for:** Products with multiple activation criteria that users complete at their own pace.

Implementation:
- Persistent, visible checklist (sidebar widget or top banner). 4-6 items maximum.
- Pre-check the first item (account creation) to give momentum.
- Each item is a direct link to the action — not a description of what to do.
- Show progress: "3 of 5 complete"
- Celebrate completion (confetti animation, congratulations message).
- Dismiss after completion but keep accessible from settings or help menu.

Example:
- [x] Create your account
- [ ] Create your first project
- [ ] Invite a teammate
- [ ] Connect a data source
- [ ] Create your first report

### 3. Interactive Walkthrough

**Best for:** Complex products where users need guided context on the actual UI, not a separate tutorial.

Implementation:
- Step-by-step guidance overlaid on the real product UI.
- Highlight the element to interact with, dim everything else.
- Show a tooltip: what to do + why it matters (one sentence each).
- The user takes the actual action — not a simulation or demo mode.
- Allow re-triggering from a help menu for users who dismissed it early.

### 4. Templates and Sample Data

**Best for:** Products where empty state anxiety prevents action (dashboards, project tools, content platforms).

Implementation:
- Pre-populate the workspace with realistic sample data on first login.
- Offer "Start from template" alongside "Start from scratch" — template first, scratch second.
- Tailor templates to the use case selected during setup.
- Label sample data clearly: "Sample project — delete anytime."

### 5. Progressive Disclosure

**Best for:** Feature-rich products where showing everything on day one overwhelms users.

Implementation:
- Hide advanced features initially. Reveal based on usage triggers.
- Trigger format: "You've created 5 projects — did you know you can use folders to organize them?"
- Delivery: tooltips, banners, or in-app notification cards.
- Track which features are surfaced and their adoption rate after surfacing.

## Personalization

Ask ONE question early to branch the experience. Keep it to a single selection screen.

**By role:**
- "I'm setting this up for myself" → solo onboarding, skip team features
- "I'm setting this up for my team" → workspace setup, invite flow, permissions overview
- "I'm evaluating tools for my company" → show ROI content, comparison features, import from competitor

**By use case:**
- Present 3-4 use cases that match the product's core segments
- Customize: templates offered, checklist items shown, example data populated, and feature emphasis

The personalization question should be the first or second step. Do not ask multiple branching questions — one is enough.

## Anti-Patterns

Avoid these patterns that consistently degrade activation rates:

- **Click-through tours** that users dismiss without reading. Users click "Next" reflexively.
- **Mandatory tutorials** that block product access. Let users skip and discover.
- **"Watch this video"** as the primary onboarding. Video is passive. Users need to do, not watch.
- **Tooltip overload** that highlights every feature on the page simultaneously. Highlight one thing at a time.
- **Static onboarding** that does not adapt to what the user has already completed. If they created a project on their own, do not ask them to create one.
- **No skip or exit option.** Users must always be able to dismiss onboarding entirely.
- **Ending on empty.** Onboarding must leave the user looking at something useful — data, a template, a sample — never a blank screen.

## Success Metrics

Track these to evaluate onboarding effectiveness:

| Metric | What it measures | Target |
|--------|-----------------|--------|
| **Setup completion rate** | % who finish the wizard or checklist | > 70% |
| **Activation rate** | % who reach the aha moment | > 40% for self-serve SaaS |
| **Time to activate** | Duration from signup to aha moment | Minimize — measure median, not average |
| **Step drop-off** | Which step loses the most users | Identify and redesign the worst step |
| **D7 retention by activation** | Day-7 return rate for activated vs. non-activated users | Validates the aha moment hypothesis. If no difference, redefine the aha moment. |
