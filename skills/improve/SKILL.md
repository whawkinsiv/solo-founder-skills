---
name: improve
description: "Use this skill to autonomously improve any other skill in solo-founder-superpowers. Point it at a skill (e.g., 'improve the seo skill') and it runs an autoresearch-style loop: diagnoses weaknesses, experiments with improvements, evaluates each change via A/B comparison, keeps winners, discards regressions, and reports results. Originals are always preserved — nothing changes until you approve."
---

# Improve

Autonomous skill improvement loop inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch). You modify a skill, evaluate whether it got better, keep or discard, repeat.

**Your originals are always safe.** The loop works on a copy. Nothing changes until you say so.

---

## Setup

When the user says "improve [skill name]":

1. **Locate the skill.** Read `skills/<name>/SKILL.md`. If it doesn't exist, ask the user which skill they mean.

2. **Back up the original.** Copy the full `skills/<name>/` directory to `eval/experiments/<name>/`. Create `eval/experiments/` if it doesn't exist.
   ```
   mkdir -p eval/experiments/<name>
   cp skills/<name>/SKILL.md eval/experiments/<name>/SKILL.md
   cp skills/<name>/*.md eval/experiments/<name>/  (if supporting files exist)
   ```

3. **Read the design philosophy.** Read `CLAUDE.md` to ground yourself in the plugin's standards. The rubric below is derived from these.

4. **Read neighbor skills.** Identify skills with overlapping scope (check the Related Skills section, check skills in the same category from CLAUDE.md). Read their descriptions — you need to know the boundaries.

5. **Initialize the log.** Create `eval/results.tsv` (or append if it exists from a previous run):
   ```
   experiment	skill	tier	dimension	score_before	score_after	status	change_description
   ```

6. **Run the baseline diagnosis.** Score the original against the rubric (see below). Log it as experiment 0.

7. **Show scores and ask for focus.** Print the rubric scores in a compact tiered table:
   ```
   Tier 1 (Critical):  trigger-precision=1  trigger-phrases=1  checklists=2  tell-ai-prompts=2  → 6/12
   Tier 2 (Important): boundary=1  tool-specific=N/A  founder-pov=2  mistakes=1             → 4/9
   Tier 3 (Polish):    conciseness=✓  disclosure=✗  scannable=✓  cross-refs=✗
   Total: 10/21
   ```
   (Example shows a knowledge skill where tool-specific is N/A. For implementation skills, all 8 dimensions apply and max is /24.)
   Then ask:
   > "I'll focus on the lowest-scoring dimensions, Tier 1 first. Want me to auto-prioritize (default) or focus on specific areas?"

   If the user says "go," "auto," or anything non-specific → auto-prioritize (Tier 1 first, then Tier 2).
   If the user names specific dimensions → focus the loop on those, skip others.

---

## Rubric: Diagnosing Weaknesses

Score each dimension 0-3 (0=missing, 1=weak, 2=adequate, 3=strong). Dimensions are tiered by impact.

### Tier 1 — Critical (scored 0-3, experimented first)

These determine whether the skill fires and delivers value. All must reach ≥2 before moving to Tier 2.

- **Trigger precision:** Does the description activate for the right prompts and NOT for neighbor skills' prompts?
- **Trigger phrases:** Does it include phrases users actually say (natural language, not jargon)?
- **Actionable checklists:** Does it have concrete workflows with checkboxes?
- **"Tell AI:" prompts:** Does it include copy-paste prompts founders can use with any AI tool?

### Tier 2 — Important (scored 0-3, experimented after Tier 1 ≥2)

These improve quality but only matter if the skill fires correctly.

- **Boundary clarity:** Does it explicitly state what this skill is NOT for and where to go instead?
- **Tool-specific guidance (conditional):** Does it differentiate advice by tool (Claude Code vs Lovable vs Replit)? **Mark N/A** for knowledge/decision skills where the same guidance applies regardless of tool — e.g., compliance, hiring, legal, pricing, finances, market-research, customer-research, validate, analytics, retention. If the skill's advice changes depending on which tool runs it, score it. If not, skip it and reduce the denominator.
- **Founder perspective:** Is it written for a non-technical founder, not a developer?
- **Common mistakes:** Does it cover what founders typically get wrong?

### Tier 3 — Polish (binary checklist, batch pass at end)

Not scored individually. Handled as a single cleanup pass after the main loop converges.

- [ ] **Conciseness:** Avoids explaining concepts Claude already knows?
- [ ] **Progressive disclosure:** SKILL.md first, supporting files for depth?
- [ ] **Scannable:** Headers, tables, short paragraphs — not walls of text?
- [ ] **Cross-references:** Links to related skills where relevant?

**Loop score: Tier 1 + Tier 2 = applicable dimensions × 3pts.** Max is 24 when all 8 dimensions apply, 21 when tool-specific guidance is N/A.

Tier 3 is not part of the loop score. It's a yes/no sweep after convergence.

---

## The Loop

```
REPEAT:
  1. PICK the lowest-scoring dimension, respecting tier order:
     - Tier 1 dimensions below 2 → always first
     - Tier 2 dimensions → only after all Tier 1 ≥ 2
     - N/A dimensions → skip entirely, never experiment on them
     - Tier 3 → never (handled in polish pass)
     - User-specified focus areas override this order

  2. MAKE ONE CHANGE to eval/experiments/<name>/SKILL.md
     - Target the specific weakness identified
     - One focused change per iteration, not a rewrite

  3. EVALUATE via A/B comparison (do reasoning internally, log to experiment-log.md):

     a. Generate 3 representative user prompts for this skill
        (realistic things a non-technical founder would say)

     b. For each prompt, reason through what guidance the ORIGINAL
        skill would produce vs what the MODIFIED version would produce

     c. Judge: "Which version gives a non-technical founder better,
        more actionable guidance?" Score: Original wins / Modified wins / Tie

     d. Majority wins across the 3 prompts

     Write the full A/B reasoning to eval/experiments/<name>/experiment-log.md.
     Do NOT print it to the terminal. See Output Rules.

  4. DECIDE
     - Modified wins majority → KEEP the change
     - Original wins or tie → DISCARD (revert experiment file to previous version)

  5. LOG to eval/results.tsv:
     experiment#  skill  tier  dimension_targeted  score_before  score_after  status  change_description

  6. RE-SCORE the full rubric after every KEEP (do this internally, don't print)

  7. PRINT one line per experiment (see Output Rules)

  8. CHECK stopping condition
```

### Stopping Condition

Stop the main loop when ANY of:
- **Converged:** 3 consecutive experiments with no improvement (all discarded)
- **Experiment cap reached:** default 8 experiments. User can override: "improve seo with 12 experiments max"
- **All Tier 1+2 dimensions scoring 3:** nothing left to improve
- **User interrupts**

### Polish Pass

After the main loop stops, run **one** final experiment targeting all Tier 3 items at once:
- Check each Tier 3 item (conciseness, progressive disclosure, scannable, cross-references)
- Make a single batch edit addressing any that are missing or weak
- Evaluate the batch change via the same A/B process
- KEEP or DISCARD as a unit — not individually
- Show as one line in output: `P  polish  KEEP|DISCARD  score→score  summary`

The polish pass does not change the /24 loop score. It's shown as a separate line at the end.

---

## Evaluation Rules

Be honest. You are both the improver and the judge — this only works if you don't fool yourself.

- **Generate diverse prompts.** Don't write prompts that favor your change. Write prompts a real founder would type.
- **Judge from the founder's perspective.** Not "which is more technically correct" but "which helps a non-technical founder take action."
- **Preserve voice.** The original author's style and personality should survive. You're improving, not rewriting.
- **Respect neighbor boundaries.** If a change makes this skill bleed into another skill's territory, that's a regression even if the content is "better."
- **One change at a time.** If you bundle 3 changes and it wins, you don't know which change helped. Isolate variables.

---

## Winners Report

When the loop stops, generate `eval/winners-report.md`:

```markdown
# Skill Improvement Results — [skill name] — [date]

## Summary
[skill]: [before]/24 → [after]/24 (+[delta]) | [N] kept, [N] discarded, [N] skipped | [N] experiments + polish

## What Changed
- [Plain English bullet 1 — net effect, not experiment sequence]
- [Plain English bullet 2]
- ...

## Rubric Scores
### Tier 1 — Critical
| Dimension | Before | After |
|-----------|--------|-------|
| Trigger precision | 1 | 3 |
| Trigger phrases | 1 | 3 |
| Actionable checklists | 2 | 3 |
| "Tell AI:" prompts | 2 | 3 |

### Tier 2 — Important
| Dimension | Before | After |
|-----------|--------|-------|
| Boundary clarity | 1 | 2 |
| Tool-specific guidance | 2 | 3 |  ← or N/A for knowledge skills
| Founder perspective | 2 | 3 |
| Common mistakes | 1 | 2 |

### Tier 3 — Polish
- [x] Conciseness
- [x] Progressive disclosure
- [ ] Scannable
- [x] Cross-references

## Experiment Log
| # | Dimension | Result | Score | Change |
|---|-----------|--------|-------|--------|
| 1 | trigger-precision | KEEP | 12→15 | Narrowed description... |
| 2 | trigger-phrases | KEEP | 15→17 | Added natural phrases... |
| ... | ... | ... | ... | ... |
| P | polish | KEEP | — | Added cross-refs... |

## Review
The improved version is at: eval/experiments/[skill]/SKILL.md

To accept: "promote [skill]"
To compare: "show me the diff for [skill]"
To reject: "discard [skill]"
```

---

## Promoting Winners

When the user says "promote" or "accept":

1. Show a side-by-side summary of key changes (not the full file — just what's different)
2. Ask for confirmation: "This will overwrite `skills/<name>/SKILL.md` with the improved version. The original is backed up at `eval/experiments/<name>/SKILL.md.original`. Proceed?"
3. On confirmation:
   - Copy `eval/experiments/<name>/SKILL.md.original` as a backup name (rename the original backup)
   - Copy `eval/experiments/<name>/SKILL.md` → `skills/<name>/SKILL.md`
4. Confirm: "Done. The improved version is now live. Original backed up at `eval/experiments/<name>/SKILL.md.original`."

When the user says "discard":
- Do nothing. The original in `skills/` was never touched.

---

## Safety Rules

1. **NEVER modify `skills/<name>/SKILL.md` during the loop.** Only write to `eval/experiments/`.
2. **NEVER delete the original backup.**
3. **NEVER promote without explicit user approval.**
4. **Preserve all content you don't intentionally change.** If you improve the description, the rest of the file must be byte-identical.
5. **If the experiment directory already has files from a previous run,** ask the user: "Previous experiment results exist for [skill]. Start fresh or continue from where we left off?"

---

## Output Rules

The terminal is not a research paper. Print only what the user needs to see.

### How to talk to the user

The user is not reading a log file. When you speak between experiments — explaining the baseline, describing what you're focusing on, or summarizing results — use plain English.

**Do:**
- "This skill doesn't fire when someone says 'my app is slow' — that's the biggest gap, so I'll fix that first."
- "The skill gives good advice but doesn't tell you what to do step by step. Adding a checklist."
- "5 out of 8 dimensions are already solid. The weak spots are: it doesn't include ready-to-paste prompts, and it doesn't warn you about common mistakes."

**Don't:**
- "Trigger precision scored 2/3 on the baseline rubric. Targeting this dimension next."
- "Re-scoring Tier 1 dimensions after KEEP. Convergence streak reset to 0."
- "No stale references to /42. Stopping condition still references 3 consecutive discards."

The rubric is your internal tool. The user wants to know: what's wrong with this skill, what are you fixing, and did it get better. If you can't explain it without jargon, you don't understand it well enough.

### During the loop — one line per experiment

Print exactly one line per experiment. No diffs. No multi-line blocks.

```
 1  trigger-precision      KEEP   12→15  Narrowed description to exclude neighbor skill prompts
 2  trigger-phrases         KEEP   15→17  Added "my app is slow," "hosting bill too high"
 3  actionable-checklists   KEEP   17→19  Added 6-step workflow checklist at top
 4  boundary-clarity        KEEP   19→21  Routes out-of-scope to build/debug/monitor
 5  tool-specific-guidance  SKIP   21     Already scoring 3
 6  founder-perspective     DISCARD 21    Rewrite didn't improve A/B results
 P  polish                  KEEP   21→21  Added cross-refs, trimmed verbose sections
```

**Format:** `experiment#  dimension  KEEP|DISCARD|SKIP  score[→score]  one-line summary`

- `KEEP` = experiment won A/B, change retained
- `DISCARD` = experiment lost A/B, change reverted
- `SKIP` = dimension already scoring 3, no experiment run
- `P` = polish pass (Tier 3 batch, after main loop)
- Score is the Tier 1+2 total out of /24 (polish pass doesn't change it)

**DO NOT print:** A/B reasoning, rubric re-scoring, prompt details, file diffs, edit explanations.

**DO log to file:** Full A/B reasoning, prompts, and rubric details go to `eval/experiments/<name>/experiment-log.md`. This is the audit trail if the user wants to review later.

### After the loop — summary + decision

Print a compact summary, then offer promote/discard:

```
optimize: 12/24 → 21/24 (+9) | 4 kept, 1 discarded, 1 skipped | 6 experiments + polish

What changed:
- Description now triggers on "my app is slow," "hosting bill too high"
- Routes out-of-scope requests to build/debug/monitor/database
- Speed audit split: Claude Code runs directly vs Lovable/Replit manual measure
- 6-step workflow checklist at top
- Related Skills section linking to 5 adjacent skills

Diff: "show me the diff"
Accept: "promote optimize" | Reject: "discard optimize"
```

**"What changed"** is plain English grouped by theme — not by experiment number, not line-by-line diffs. Summarize the net effect, not the sequence of changes.

The detailed winners report is still written to `eval/winners-report.md` for audit, but the terminal shows only this compact summary.

---

## What This Skill Does NOT Do

- Rewrite skills from scratch (it makes incremental improvements)
- Modify multiple skills at once (one skill per run)
- Change the skill's fundamental purpose or scope
- Add features or sections the original author didn't intend
- Auto-promote changes (the human always decides)
