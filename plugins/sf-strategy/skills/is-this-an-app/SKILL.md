---
name: is-this-an-app
description: "Use this skill when a founder has a new product idea and is about to build it, to decide what form the idea should take: a web app, a mobile app, a browser extension, an automation, an agent skill, an API, or no build at all. Also use when the user says 'is this an app,' 'does this need to be a web app,' 'should this be a SaaS,' 'web app or Chrome extension,' 'could this just be a Zapier or a GPT,' 'mobile app or web app,' 'what should I build this as,' or describes an idea and says they are about to open Lovable, Replit, or Claude Code to build it. Use it even when they do not ask about form: a founder who says 'I want to build an app that...' should check the form first. Scores the idea on a 14-dimension weighted matrix and returns a verdict with the best form, the code and infrastructure it needs, and the build risk. Do NOT use to test whether anyone wants the idea (use validate), to write the spec once the form is chosen (use plan), or to choose between AI coding tools (use build)."
metadata:
  version: 1.0.0
---

# Is this an app?

Not every idea needs to be a full web app. This skill scores a new idea on a 14-dimension weighted matrix and recommends the form the idea should take, before the founder builds anything.

## Step 1 — Get the idea

If the founder has not described the idea, ask what it does, who it is for, and how they will use it.

## Step 2 — Score the matrix

Read `references/matrix.md`. Score each of the 14 dimensions 0–5 against its anchors. Use the test question for each dimension to score consistently.

If you cannot score a dimension from what the founder said, ask. If the founder wants an answer now, make your best guess and mark that score as a guess.

## Step 3 — Run the script for the weighted total

The script lives beside this file, so call it by its own path:

```bash
python3 "$CLAUDE_PLUGIN_ROOT/skills/is-this-an-app/scripts/score.py" \
    --interface 1 --agent 5 --visual 1 --workflow 2 --background 0 \
    --state 1 --integration 0 --device 1 --judgment 2 --collaboration 0 \
    --latency 1 --distribution 5 --extensibility 0 --audit 0
```

If `$CLAUDE_PLUGIN_ROOT` is unset, use the path this SKILL.md was loaded from.

The script prints a table with each score, its weight, and its points, and a total out of 100. A higher total means the idea leans more toward a standalone app.

The script counts two dimensions in reverse: agent substitutability and distribution-context fit. A high score on either one argues against a standalone app, so a plain sum would count it toward one.

## Step 4 — Decide the form

For each dimension, read the directional signal for its score in the matrix. When signals point to different forms, the signal from the higher-weight dimension wins. The signals make the decision. The weighted total supports the decision, but it does not make it.

Name one specific form, for example "a portable agent skill packaged as a plugin," not "some kind of tool."

## Step 5 — Write the answer

Use this format:

```
IS THIS AN APP?
<Yes, No, or a short qualified answer>

Best form: <one specific form>
Interface: <where the user meets the product>
Code required: <how much code, and what it does>
Infrastructure required: <what must run>
Useful extra: <one small addition that adds value without changing the form>
Possible later addition: <what could come later, and why>
Build risk: <what building a heavier form than this would add, and how little it would add to the core value>
```

Below the answer, show the table from the script. Add a column with the directional signal that each score triggered, and mark any guessed score as a guess. The founder can then see which scores drove the answer and challenge any of them.

## Step 6 — Save and hand off

Write the answer to `${SOLO_FOUNDER_CONFIG:-$HOME/.config/solo-founder}/is-this-an-app/archive/<YYYY-MM-DD>-<slug>.md`, and append one line to `INDEX.md` in the same folder. Do not write inside the skill folder, because plugin updates replace it. If `${BUSINESS_BRAIN:-$HOME/business-brain}/` exists, record the decision there and follow its `AGENTS.md`. If it does not exist, skip it.

Then offer the next step:

- No evidence yet that anyone wants the idea → `validate`
- Ready to define the chosen form → `plan`

## Example

User says: "I want to build a tool that scores a new product idea against a decision matrix and tells founders what form to build."

Result:

```
IS THIS AN APP?
No.

Best form: portable agent skill packaged as a plugin.
Interface: the user's existing agent conversation.
Code required: essentially none.
Infrastructure required: none.
Useful extra: explicit /is-this-an-app invocation.
Possible later addition: a small public website solely for discovery, explanation, and demonstrating the matrix—not because the product requires a website.
Build risk: turning the framework into a questionnaire SaaS would add accounts, persistence, UI, hosting and maintenance while contributing almost nothing to its core value.
```

Then the score table, with the directional signal for each score.

## Troubleshooting

### The script fails

**Cause:** A score is outside 0–5, a flag is missing, or `$CLAUDE_PLUGIN_ROOT` is unset. **Solution:** The error message names the bad flag. All 14 flags are required. If the path fails, call `scripts/score.py` from the folder this SKILL.md was loaded from.
