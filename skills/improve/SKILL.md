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
   experiment	skill	dimension	score_before	score_after	status	change_description
   ```

6. **Run the baseline diagnosis.** Score the original against the rubric (see below). Log it as experiment 0.

7. **Show scores and ask for focus.** Print the rubric scores in a compact table, then ask:
   > "I'll focus on the lowest-scoring dimensions. Want me to auto-prioritize (default) or focus on specific areas?"

   If the user says "go," "auto," or anything non-specific → auto-prioritize by lowest score.
   If the user names specific dimensions → focus the loop on those, skip others.

---

## Rubric: Diagnosing Weaknesses

Score the skill on each dimension (0-3 scale: 0=missing, 1=weak, 2=adequate, 3=strong):

### Description Quality
- **Trigger precision:** Does the description activate for the right prompts and NOT for neighbor skills' prompts?
- **Trigger phrases:** Does it include phrases users actually say (natural language, not jargon)?
- **Boundary clarity:** Does it explicitly state what this skill is NOT for and where to go instead?

### Content Quality
- **Founder perspective:** Is it written for a non-technical founder, not a developer?
- **Actionable checklists:** Does it have concrete workflows with checkboxes?
- **"Tell AI:" prompts:** Does it include copy-paste prompts founders can use with any AI tool?
- **Tool-specific guidance:** Does it differentiate advice by tool (Claude Code vs Lovable vs Replit)?
- **Common mistakes:** Does it cover what founders typically get wrong?
- **Out of scope:** Does it explicitly say what NOT to do (preventing premature optimization)?
- **Conciseness:** Does it avoid explaining concepts Claude already knows?

### Structure Quality
- **Progressive disclosure:** SKILL.md first, supporting files for depth?
- **Scannable:** Headers, tables, short paragraphs — not walls of text?
- **Cross-references:** Links to related skills where relevant?

**Focus the loop on the LOWEST-scoring dimensions.** Don't polish what's already strong.

---

## The Loop

```
REPEAT:
  1. PICK the lowest-scoring rubric dimension (or user-specified focus area)

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
     experiment#  skill  dimension_targeted  score_before  score_after  status  change_description

  6. RE-SCORE the full rubric after every KEEP (do this internally, don't print)

  7. PRINT the experiment summary + scoreboard line (see Output Rules)

  8. CHECK stopping condition
```

### Stopping Condition

Stop when ANY of:
- **Converged:** 3 consecutive experiments with no improvement (all discarded)
- **Experiment cap reached:** default 8 experiments. User can override: "improve seo with 12 experiments max"
- **All dimensions scoring 3:** nothing left to improve
- **User interrupts**

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
- Experiments run: [N]
- Improvements kept: [N]
- Dimensions improved: [list]

## Changes Made (in order)

### 1. [Dimension]: [what changed]
- Why: [weakness identified]
- Change: [1-2 sentence description]
- A/B result: Modified won 2/3 prompts

### 2. [Dimension]: [what changed]
...

## Rubric Score
| Dimension | Before | After |
|-----------|--------|-------|
| Trigger precision | 1 | 3 |
| Actionable checklists | 2 | 3 |
| ... | ... | ... |

## Review the result
The improved version is at: eval/experiments/[skill]/SKILL.md

To accept: "promote the improved [skill]"
To compare: "show me the diff for [skill]"
To reject: "discard the [skill] improvements"
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

### During the loop

**DO print** (per experiment — 5 lines max):
```
Experiment 3 — Actionable checklists
  Change: Added 7-step workflow checklist after intro
  Result: KEEP (won 2/3 prompts)
  Score: 30/42 → 33/42
[3/8] actionable checklists → KEEP | 33/42 | Kept: 3 Discarded: 0 | Streak: 0
```

**DO NOT print:**
- A/B reasoning (which prompt, which version won, why)
- Rubric re-scoring details
- Prompt generation reasoning
- File edit explanations

**DO log to file:** Write the full A/B reasoning, prompt details, and rubric re-scoring to `eval/experiments/<name>/experiment-log.md`. Append each experiment. This file is the audit trail if the user wants to review later.

### Scoreboard format

After each experiment, print one scoreboard line:
```
[N/MAX] dimension → KEEP|DISCARD | score/total | Kept: N Discarded: N | Streak: N
```
- `N/MAX` = experiment number out of the cap (default 8)
- `Streak` = consecutive discards (3 = convergence stop). Resets to 0 after a KEEP.

### After the loop

Print the winners report summary to the terminal (not just to file). Then offer promote/discard.

---

## What This Skill Does NOT Do

- Rewrite skills from scratch (it makes incremental improvements)
- Modify multiple skills at once (one skill per run)
- Change the skill's fundamental purpose or scope
- Add features or sections the original author didn't intend
- Auto-promote changes (the human always decides)
