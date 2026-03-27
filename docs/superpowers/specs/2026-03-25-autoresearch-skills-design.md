# Autoresearch for Skills — Design Spec

**Date:** 2026-03-25
**Inspired by:** [karpathy/autoresearch](https://github.com/karpathy/autoresearch)

## Problem

53 skills with overlapping descriptions. Triggering accuracy — whether the right skill activates for a given user prompt — is critical but untested. The SEO skill cluster (`seo`, `seo-audit`, `seo-content`, `technical-seo`) is especially prone to mis-triggers.

## Core Idea

Adapt the autoresearch pattern: an autonomous agent modifies skill descriptions, evaluates triggering accuracy against test cases, keeps improvements, discards regressions, and repeats. The human reviews only the winners.

## Key Constraint: Preserve Originals

The `skills/` directory is NEVER modified by the loop. All experiments write to `eval/experiments/`. The human promotes winners manually after reviewing the winners report.

## Mapping to Autoresearch

| autoresearch | skills analog |
|---|---|
| `train.py` (modified by agent) | `SKILL.md` description field |
| `prepare.py` (fixed eval harness) | test case YAML files |
| `val_bpb` (lower = better) | triggering score (higher = better) |
| `program.md` (agent instructions) | `eval/program.md` |
| `results.tsv` | `eval/results.tsv` |
| 5-min GPU training run | Claude Code eval pass |
| git branch isolation | shadow directory (`eval/experiments/`) |

## Directory Structure

```
eval/
  program.md                  ← agent instructions (the "skill")
  test-cases/
    seo.yaml                  ← trigger/no-trigger test prompts
    seo-audit.yaml
    seo-content.yaml
    pricing.yaml
  experiments/                ← shadow copies of modified skills
    seo/SKILL.md
    seo-audit/SKILL.md
    seo-content/SKILL.md
    pricing/SKILL.md
  results.tsv                 ← full experiment log
  winners-report.md           ← generated summary of improvements
```

The entire `eval/` directory is in `.gitignore`. It's local tooling, not part of the plugin.

## Metric: Triggering Accuracy

### v1 — Description Triggering

Each skill has a YAML test case file with:
- **should_trigger**: 5+ prompts where this skill is the correct choice
- **should_not_trigger**: 5+ prompts where a different skill should trigger (with annotation of which one)

The eval presents all pilot skill descriptions + one test prompt to Claude and asks "which ONE skill would you select?" Score = correct / total.

### Cross-Skill Constraint

All skills in the pilot set are evaluated together, every time. If improving `seo` steals triggers from `seo-content`, that's a regression even if `seo`'s individual score went up. The loop only keeps changes where:
- The modified skill's score improved
- No other skill's score decreased

### v2 — Output Quality (Future)

Layer in LLM-judge scoring of actual skill output. Not in scope for the pilot.

## Test Case Format

```yaml
skill: seo
description_source: skills/seo/SKILL.md

should_trigger:
  - "how do I improve my SEO"
  - "help me rank higher on Google"
  - "SEO strategy for my SaaS"

should_not_trigger:
  - prompt: "audit my site for SEO issues"
    expected: seo-audit
  - prompt: "write a blog post optimized for search"
    expected: seo-content
  - prompt: "fix my meta tags and sitemap"
    expected: technical-seo
```

## The Loop (program.md)

Runs in a dedicated Claude Code session. The user starts it with something like "run the autoresearch loop on the pilot skills."

```
1. BASELINE
   - Read all 4 original SKILL.md files from skills/
   - Copy them to eval/experiments/ as starting points
   - Score all 4 against their test cases
   - Log baseline scores to results.tsv

2. PICK a skill (lowest-scoring, or round-robin if tied)

3. MODIFY the experiment copy in eval/experiments/<skill>/SKILL.md
   - v1: only modify the description field
   - Preserve all other content exactly

4. EVAL all 4 skills together
   - Use experiment descriptions for all skills (not originals)
   - Test every prompt across every skill
   - Score each skill

5. DECIDE
   - If modified skill improved AND no other skill regressed → KEEP
   - Otherwise → DISCARD (revert experiment file to previous best)

6. LOG to results.tsv:
   experiment#  skill  score_before  score_after  status  description_of_change

7. REPEAT from step 2

STOP when: 3 full rounds across all skills with no improvement (converged),
           or human interrupts.
```

## Results Format

### results.tsv

```
experiment	skill	score_before	score_after	status	change_description
1	baseline	-	7/10	baseline	original descriptions
2	seo	7/10	8/10	keep	added exclusion for audit scenarios
3	seo-audit	9/10	9/10	discard	tried broader description, no change
```

### winners-report.md

Generated when the loop finishes. Only surfaces improvements:

```markdown
# Autoresearch Results — 2026-03-25

## Summary
- Skills tested: 4
- Experiments run: 23
- Improvements found: 2

## Improved: seo
- Baseline: 7/10 → New: 9/10
- What changed: [summary]
- Review: eval/experiments/seo/SKILL.md

## No improvement: seo-audit, pricing
- Already scoring 9/10 and 10/10 respectively
```

## How to Use It

### Running the loop
1. Open a new Claude Code session (separate terminal tab)
2. Say: "Read eval/program.md and run the autoresearch loop"
3. Walk away

### Reviewing results
1. Come back, read `eval/winners-report.md`
2. For each winner, review the experiment file vs original
3. Say "promote seo" → Claude copies experiment to skills/
4. Or "show me the seo diff" → Claude shows side-by-side

### Adding more skills later
1. Write a new YAML test case in `eval/test-cases/`
2. Re-run the loop with the expanded set

## Runtime

Runs entirely within Claude Code. No API key, no external tooling, no git branch management. The agent reads files, writes to `eval/experiments/`, and uses its own judgment for triggering evaluation.

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Loop overwrites originals | `skills/` is never touched; all writes go to `eval/experiments/` |
| Bad metric leads to worse descriptions | Human reviews all winners before promotion; originals preserved |
| Cross-skill regression | All skills evaluated together every iteration |
| Loop runs forever | Auto-stops after 3 rounds with no improvement |
| Eval is subjective (LLM judging LLM) | Test cases are human-written with clear expected answers |
