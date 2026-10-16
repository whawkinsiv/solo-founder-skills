---
name: build
description: "Use this skill when a solo founder is about to build or add to their product with Claude Code: 'build my MVP,' 'let's build this,' 'add this feature,' 'write a spec,' 'scope the first version,' 'Claude keeps breaking things,' or 'we're going in circles.' Checks that someone has paid first, scopes the first version from the steps the founder already does by hand, writes a short spec, and builds one piece at a time with a re-test after each piece. Not for deciding what form the product takes (use is-this-an-app) or for the pre-launch check (use go-live)."
metadata:
  version: 2.0.0
---

# Build

Build the smallest version that paying customers need, one piece at a time. Every piece is tested before the next one starts.

## Step 1: Check the gate

Ask: "How many people pay for this today, and do you deliver it by hand now?"

- **Paying customers and written manual steps:** continue.
- **No paying customers:** say once, plainly, that building first is the most common way founders lose months, and suggest the manual delivery test in **validate** and **first-customers**. If the founder still wants to build, build. It is their decision.

## Step 2: Scope the first version

Start from the founder's written manual steps, if they exist. The first version automates **the one step that takes the most time per customer**. Every other step stays manual, or uses a tool the founder already has: a form, a spreadsheet, a payment link, email.

Ask these five questions to cut the scope:
1. What is the one problem this version solves?
2. Who is the one person who has it most?
3. What is the least they must see and do to get the result?
4. What can stay manual or rough behind the scenes?
5. What is the fastest path to a real customer doing a real task?

Target: the first version ships in about a week. If it is bigger, cut until it is not.

## Step 3: Write a short spec

Write it in the conversation and get the founder's agreement before you build:

```
What users do: <2-3 sentences: action and outcome>
Main flow: <3-5 steps when everything goes right>
What can go wrong: <2-4 cases, and what the user sees for each>
Not in this version: <the list that prevents scope creep>
```

Describe what the user sees and does, not how the code works. The founder judges behavior. The code is your job.

## Step 4: Build one piece at a time

A piece takes 1–3 hours: sign-up, one core workflow, one settings page. "The dashboard with all integrations" is not a piece.

For each piece:
1. Build it.
2. Run it and use it the way a customer would.
3. Check that the earlier pieces still work: sign up, do the core action, see the result. New code often breaks old features. Catch it now.
4. Commit, with a message that says what works now.
5. Tell the founder what to try, in one or two plain sentences.

Before the first customer uses it, make sure these exist. AI-built apps often ship without them:
- error tracking, so the founder knows when something breaks
- a helpful 404 page and error page instead of a blank screen or a stack trace
- loading, empty, and error states on every screen that shows data (see **beautify**)
- a page title, description, and share image, so links look right when shared
- a favicon
- a visible way for customers to contact the founder

## Step 5: When stuck

- **After 2 failed fixes,** stop fixing. The diagnosis is probably wrong. Re-read the error, check what changed recently, and say what you now think the cause is.
- **After 3 failed fixes,** change the approach: a simpler design, or a workaround that ships, with the proper fix later.
- **If you are going in circles,** start a fresh session. Hand over three things: what exists, what works, and what is next.
- **If a fresh session also fails,** suggest a small paid task for a human developer. Define the task, and pay for a few hours, not a project.

## Rules

- **Use what the project already uses.** For a new project, choose a common, well-documented stack and say why in one sentence. Do not switch tools in the middle of a build.
- **Build integrations only when 3 or more paying customers ask.** Until then, an automation tool or a manual step is enough.
- **Do not build for scale.** There is no scale yet. Speed and clarity beat clever architecture.
- **Do not add features beyond the spec.** Note them under "Not in this version" and move on.

## Output

After each piece:

```
Built: <what works now, in plain words>
Try it: <the steps the founder should click through>
Checked: <the earlier pieces still work: yes / what broke>
Next piece: <one item>
```
