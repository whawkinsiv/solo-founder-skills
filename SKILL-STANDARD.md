# SKILL.md House Standard

**Version 3.** Rules only. Every rule here is either checkable by a script or a stated house preference.

This document holds no measurements and no history. Counts go stale silently, so run `python3 scripts/audit.py` to measure the repo instead. It exits non-zero on anything that breaks the spec or the portability rules.

Write rules against the published spec, not against another repo you admire. Version 1 of this document was reverse-engineered from a competitor's repo and got six rules wrong.

## Sources — check any rule yourself

| Key | Source | Location |
|---|---|---|
| **[A]** | *The Complete Guide to Building Skills for Claude* (Anthropic, 33pp) | `~/business-brain/The-Complete-Guide-to-Building-Skill-for-Claude.pdf` |
| **[B]** | `skill-creator` SKILL.md (Anthropic, 485 lines) | `~/.claude/plugins/cache/claude-plugins-official/skill-creator/unknown/skills/skill-creator/SKILL.md` |
| **[C]** | `quick_validate.py` (Anthropic, runnable) | same directory, `scripts/quick_validate.py` |
| **[S]** | **Agent Skills specification** — the authority for anything portable | https://agentskills.io/specification |
| **[H]** | House rule — our choice, not from Anthropic | this document |

`[S]` outranks the rest. It is public, versioned, and binding on every agent that reads
these skills. `[A]` and `[B]` are local files that only this machine can open, so treat
them as background. Where they disagree with `[S]`, `[S]` wins. The description cap is
**1024 characters** per `[S]`; Claude Code allows more, and taking Claude Code's number
would break the skills everywhere else.

Every rule below carries a citation. `[A p10]` = page 10 of the PDF. `[B:67]` = line 67 of skill-creator's SKILL.md. `[H]` = we decided it.

---

## Part 1 — Hard rules (machine-checkable)

These are enforced by `quick_validate.py`. A skill that fails is broken, not stylistically weak.

| Rule | Source |
|---|---|
| File is named exactly `SKILL.md`, case-sensitive | [C:17], [A p10] |
| YAML frontmatter present, `---` delimited | [C:23-29] |
| Only these frontmatter keys: `name`, `description`, `license`, `allowed-tools`, `metadata`, `compatibility` | [C:42] |
| `name` required; kebab-case `[a-z0-9-]` only; ≤64 chars; no leading, trailing, or doubled hyphen | [C:53-71], [A p10] |
| `description` required; **≤1024 characters** | [C:83], [A p10] |
| `description` contains no angle brackets `<` `>` | [C:80], [A p11] |
| `compatibility` (if used) ≤500 characters | [C:91], [A p11] |
| No `README.md` inside a skill folder | [A p10] |
| Folder name is kebab-case and matches `name` | [A p10] |

**Run it before every commit:**

```bash
SC=~/.claude/plugins/cache/claude-plugins-official/skill-creator/unknown/skills/skill-creator
for d in skills/*/; do python3 $SC/scripts/quick_validate.py "$d" | grep -q valid || echo "FAIL $d"; done
```

Current status: **59 of 59 pass.**

---

## Part 2 — Structure

### Directory layout [A p5, A p10, B:80-83]

```
skill-name/
├── SKILL.md        required
├── scripts/        optional — executable code for deterministic/repetitive work
├── references/     optional — documentation loaded as needed
└── assets/         optional — templates, fonts, icons used in output
```

`references/` is the official name. Our old convention — ALL-CAPS files at the top level (`technical-seo/GEO.md`) — is a deviation and should migrate to `references/on-page-seo.md` over time. Nothing breaks today; new work uses `references/`.

### Progressive disclosure — three levels [A p5, B:88-91]

| Level | Loaded | Budget |
|---|---|---|
| 1. `name` + `description` | Always, every session | ~100 words [B:89] · hard cap 1024 chars [C:83] |
| 2. SKILL.md body | When the skill triggers | <500 lines ideal [B:96] · <5,000 words [A p27] |
| 3. `scripts/` `references/` `assets/` | On demand | Unlimited [B:91] |

Reference files over 300 lines get a table of contents [B:98].

Level 1 is the expensive one — it is resident whether or not the skill is ever used. Level 3 is free until read. Push detail downward.

### Recommended body structure [A p12]

```markdown
# Skill Name

## Instructions
### Step 1: [First major step]
### Step 2: ...

## Examples
### Example 1: [common scenario]
User says: "..."
Actions: 1. ... 2. ...
Result: ...

## Troubleshooting
### Error: [common failure]
**Cause:** ...  **Solution:** ...
```

`## Examples` and `## Troubleshooting` are part of Anthropic's structure and are currently absent from all 59 of our skills. Both earn their place: examples anchor format, troubleshooting handles the failure the founder will actually hit.

---

## Part 3 — The description field

The description is the only thing Claude sees when deciding whether to load the skill [A p11]. Get it right before anything else.

### Must contain [A p10]

- **What** the skill does
- **When** to use it — the trigger conditions
- Specific phrases a user would actually type
- File types, if relevant

### Lean pushy, not terse [B:67]

Anthropic's guidance is explicit: *"Claude has a tendency to 'undertrigger' skills — to not use them when they'd be useful. To combat this, please make the skill descriptions a little bit 'pushy'."*

Their example of the fix: instead of *"How to build a dashboard to display internal data"*, write *"...Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'"*

**There is no minimum or target length.** Version 1 of this standard invented a 400–900 character range and then a 400-character cap. Both were fabricated. The only hard number is 1024. Our current mean is 375 characters, which is comfortably inside budget and leaves room to get pushier where triggering is weak.

### All "when to use" info lives in the description [B:67]

Not in the body. This includes negative triggers — where the skill should *not* fire:

```yaml
description: ... Do NOT use for sizing a market (use market-research) or for
  ranking features you've already decided to build (use prioritize).
```

Version 1 of this standard required a `## When NOT to use this skill` body section. That was wrong — Anthropic puts it in the description, where it can actually affect routing. Body text is only read after the skill has already loaded, which is too late to prevent a mis-trigger.

### Tune it with evidence, not opinion

| Symptom | Fix | Source |
|---|---|---|
| Skill doesn't load when it should | Add detail and keywords to the description | [A p17] |
| Skill loads for unrelated queries | Add negative triggers, narrow the scope | [A p17, p25] |

Quick diagnostic [A p25]: ask Claude *"When would you use the validate skill?"* It quotes the description back, showing exactly what it matched on.

---

## Part 4 — Writing the body

### Style [B:117, B:139, B:302]

- **Imperative form.** "Read the scorecard," not "the scorecard should be read." [B:117]
- **Explain the why.** *"Try hard to explain the why behind everything you're asking the model to do. Today's LLMs are smart."* [B:302]
- **All-caps MUST / ALWAYS / NEVER is a yellow flag.** [B:302] If you're reaching for one, the instruction probably needs a reason attached instead of an escalation. A rule Claude understands is followed more reliably than a rule Claude is shouted at about.
- **Don't overfit.** A skill runs across thousands of situations, not the three you tested. [B:298]
- **Cut what isn't pulling weight.** [B:300]

### Be specific and actionable [A p13]

Bad: `Validate the data before proceeding.`
Good: `Run scripts/validate.py --input {filename}. If it fails, common causes are: missing required fields, invalid date format (use YYYY-MM-DD).`

### Include error handling [A p13]

Every skill gets a `## Troubleshooting` section naming the failures a real user hits, with cause and fix.

### Prefer a script to a paragraph [A p26, B:304]

*"For critical validations, consider bundling a script that performs the checks programmatically rather than relying on language instructions. Code is deterministic; language interpretation isn't."* [A p26]

And [B:304]: if you notice the same helper being written on every run, bundle it once in `scripts/` instead of paying for it every invocation.

---

## Part 5 — Testing

Three layers [A p15-16]. We currently do one.

### 1. Triggering tests [A p15]

Should-trigger and should-NOT-trigger query sets. `eval/program.md` already does this — keep it.

Write realistic queries [B:348-358]: file paths, real company names, typos, lowercase, casual speech, some backstory. Not `"Format this data"`.

The valuable negative cases are **near-misses** — queries that share vocabulary with the skill but need a different one. `"Write a fibonacci function"` as a negative test for `validate` proves nothing. `"Which of these three features should I build first?"` does, because it should route to `prioritize`.

Note [B:398-400]: skills only trigger for tasks Claude can't easily do alone. Trivial one-step prompts won't trigger regardless of description quality, so they make poor test cases.

### 2. Functional tests [A p16]

Does the skill produce a correct output? Valid output generated, error handling works, edge cases covered.

### 3. Performance comparison [A p16] — **we do not do this**

Run the same task with and without the skill, and compare:

```
Without skill: 15 back-and-forth messages, 12,000 tokens
With skill:     2 clarifying questions,      6,000 tokens
```

This is the measurement that proves a skill is worth its context cost. Anthropic's `scripts/run_loop.py` in skill-creator automates the description half of this.

---

## Part 6 — House rules [H]

**Not from Anthropic.** These are our additions. They are the part of this standard that is a bet rather than a specification, and they should be dropped if they stop earning their place.

### Voice [H]

The reason this collection exists. Write for a founder who doesn't know what a webhook is, without condescending. Plain English in output — "you're live with no way to know when things break," not "no observability layer." Effort in human time: "~2 hours," not "low effort." Name the tradeoff, then recommend — founders need a call, not a menu.

### Versioning [H]

`metadata.version`, semver, first version under this standard is `1.0.0`. Anthropic allows arbitrary keys under `metadata` [C:42] but doesn't require versioning. We do it so `improve` can tell what changed.

---

## Part 7 — Checklist

Machine-checked (run `quick_validate.py`):

- [ ] Passes `quick_validate.py`

Human-checked:

- [ ] Description states what **and** when [A p10]
- [ ] Description includes phrases a user would really type [A p10]
- [ ] Description includes negative triggers for adjacent skills [B:67, A p25]
- [ ] SKILL.md under 500 lines [B:96]
- [ ] Detail pushed to `references/`, not inline [A p13]
- [ ] `## Examples` present [A p12]
- [ ] `## Troubleshooting` present [A p12]
- [ ] Instructions imperative and specific, not vague [A p13, B:117]
- [ ] Reasons given instead of all-caps imperatives [B:302]
- [ ] Deterministic checks bundled as a script, not prose [A p26]
- [ ] Triggering tests written, including near-miss negatives [A p15, B:356]
- [ ] `metadata.version` set [H]
