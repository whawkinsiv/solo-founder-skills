---
name: copywriting
description: "Use this skill when the user needs to write headlines, CTAs, button text, error messages, onboarding copy, or any UI text. Also use when the user says 'write copy for,' 'what should this say,' 'help me with the wording,' or is building any page or component that needs text. Covers headline formulas, microcopy best practices, benefit-driven copy, and SaaS writing style."
---

# Copywriting & Microcopy

Words are interface elements. They reduce confusion, build trust, and drive action. This skill helps you write copy for every surface of your product — from headlines to error messages.

> **If `ABOUT-ME.md` and/or `MY-ICP.md` exist in the project root**, read them before writing. Use ABOUT-ME.md for voice and tone — write like the founder. Use MY-ICP.md for message framing — speak to the customer's pain in their language. When both exist: the founder's voice delivers the customer's message.

## Core Principles

- Clarity over cleverness. The user should never have to re-read a line.
- Write like a smart friend, not a corporation. Warm, direct, confident.
- Every word must earn its place. Cut ruthlessly.
- Benefits before features. "Save 4 hours a week" beats "Automated reporting."
- The best microcopy is invisible — it prevents the question before it's asked.
- Use the user's language, not your internal jargon.
- Specificity builds credibility. "Join 12,847 teams" beats "Join thousands."

---

## Workflow

```
- [ ] Identify what you're writing (headline, CTA, error, empty state, etc.)
- [ ] Define the ONE job this copy has (inform, persuade, reassure, guide)
- [ ] Write a draft using the patterns below
- [ ] Review against the voice checklist
- [ ] Test: read it aloud. If it sounds stiff, rewrite.
```

---

## Headlines

Formulas that work:

- **[Desired outcome] without [pain point]:** "Ship faster without breaking things"
- **[Action verb] your [noun]:** "Automate your workflows"
- **The [noun] for [specific audience]:** "The CRM for founders who hate CRMs"
- **[Specific result] in [timeframe]:** "Launch your landing page in 10 minutes"
- **Stop [pain]. Start [gain]:** "Stop chasing invoices. Start getting paid."

**Tell AI:**
```
Write 5 headline options for our [page type]:
- Product: [what it does]
- Audience: [who it's for]
- Main benefit: [what they get]
- Use these formulas: outcome without pain, specific result in timeframe, the X for Y
- Make each under 10 words
- Show the strongest option first with reasoning
```

---

## Button & CTA Copy

- Use first person: "Start my free trial" not "Start your free trial"
- Be specific: "Create dashboard" not "Submit" or "Continue"
- Reinforce value: "Get my report" not "Download"
- Reduce anxiety: Add reassurance below CTAs ("No credit card required", "Cancel anytime", "Free for up to 3 projects")
- Destructive actions: Name the consequence. "Delete project" not "Delete". Confirmation: "This will permanently delete 'Acme Dashboard' and all its data."

**Tell AI:**
```
Write CTA copy for our [signup / pricing / feature] page:
- Primary action: [what the user does]
- Current CTA text: [what it says now]
- Anxiety reducers needed: [credit card concern, commitment concern, etc.]
- Give me 3 options: safe, bold, and playful
- Include the helper text that goes below the button
```

---

## Error Messages

The most underrated copy in any product.

- Say WHAT happened in plain language.
- Say WHY it happened if it helps.
- Say HOW TO FIX IT — always.
- Never blame the user.

| Bad | Good |
|-----|------|
| "Invalid input" | "That email address doesn't look right — check for typos." |
| "Error 403" | "You don't have access to this page. Ask your team admin for permission." |
| "Something went wrong" | "We couldn't save your changes. Check your connection and try again." |

**Tell AI:**
```
Write error messages for these scenarios in our app:
1. [Form validation failure — what field, what's wrong]
2. [API/network error — what the user was trying to do]
3. [Permission error — what they tried to access]
4. [Not found — what they were looking for]

For each: plain language, no blame, include how to fix it.
Follow this pattern: What happened + Why (if helpful) + How to fix it.
```

---

## Empty States

Never leave a blank screen. Empty states are onboarding opportunities.

Structure: [Illustration or icon] + [What this area is for] + [Single CTA to get started]

Example: "No projects yet. Projects help you organize your work into focused streams. [Create your first project]"

**Tell AI:**
```
Write empty state copy for these screens:
1. [Screen name — what it shows when populated]
2. [Screen name — what it shows when populated]
3. [Screen name — what it shows when populated]

For each: one sentence explaining what this area is for + one CTA button text.
Keep it encouraging, not sad. The user just got here — show them the path forward.
```

---

## Onboarding Copy

- Welcome screen: Reinforce the value prop, not "Welcome to AppName."
  - GOOD: "Let's get your first dashboard live in under 5 minutes."
- Progress indicators: "Step 2 of 4 — Connect your data source"
- Skip options: Always let users skip. "I'll do this later" not just "Skip."
- Tooltips: One idea per tooltip. Under 15 words.

**Tell AI:**
```
Write onboarding copy for our setup wizard:
- Product: [what it does]
- Steps: [list 3-5 setup steps]
- Aha moment: [when the user first gets value]

For each step: headline (under 8 words), description (under 25 words), button text.
Welcome screen should promise a quick win, not just say "Welcome."
Include skip option text for optional steps.
```

---

## Pricing Page Copy

- Plan names should signal audience: "Starter", "Team", "Business" — not "Bronze", "Silver", "Gold"
- Highlight the recommended plan with "Most popular" or "Best for most teams"
- Feature lists: Lead with differentiators, not shared features
- Use per-unit framing when it helps: "$8/user/month" feels smaller than "$80/month for 10 users"

See **pricing** skill for tier design and pricing strategy.

---

## Notification & Alert Copy

- Toasts: 6-10 words max. "Project saved" or "Invite sent to 3 teammates."
- Confirmation dialogs: State the action and consequence. "Delete 'Q4 Report'? This can't be undone."
- Success states: Celebrate briefly, then redirect. "You're all set. Your first report will be ready in about 2 minutes."

---

## Settings & Admin Copy

- Label everything as if the user has never seen it.
- Use helper text under form fields to explain implications.
- Toggle descriptions should state what ON means: "Email notifications — Receive an email when someone mentions you."

---

## Voice Calibration

- **Casual moments** (empty states, success, onboarding): Warmer, friendlier.
- **Critical moments** (errors, destructive actions, billing): Clear, calm, precise.
- Never use humor in error states or when the user might be frustrated.

---

## Copy Review Checklist

Before shipping any copy:

```
- [ ] Can a stranger understand this without context?
- [ ] Is every word earning its place? (cut filler)
- [ ] Benefits before features?
- [ ] Specific rather than vague?
- [ ] Active voice, not passive?
- [ ] Reads naturally aloud?
- [ ] Matches the moment's tone (casual vs. critical)?
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| "Get started" on every button | Name the specific action: "Create project", "Send invite" |
| Clever headline nobody understands | Test: would a stranger get it in 5 seconds? |
| "Something went wrong" errors | Say what happened and how to fix it |
| Empty screens with no guidance | Every empty state is an onboarding opportunity |
| Corporate voice ("We are pleased to...") | Write like a human. "Here's what happened." |
| Same CTA copy everywhere | Match CTA to the specific value of each page |

---

## Related Skills

- **landing-page** — Full page structure and section-by-section copy
- **conversion** — CRO techniques to make copy convert better
- **humanize** — Remove AI writing patterns from generated copy
- **brand-identity-generator** — Establish voice and tone before writing
