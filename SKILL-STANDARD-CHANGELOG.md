# SKILL-STANDARD changelog

## v2 — rebuilt against Anthropic's published guidance

Version 1 was written by reverse-engineering `github.com/coreyhaines31/makerskills`. That was the wrong source. Anthropic publishes both a guide and a runnable validator, and v1 contradicted them in six places.

Sources: **[A]** the 33-page guide (`~/business-brain/The-Complete-Guide-to-Building-Skill-for-Claude.pdf`), **[B]** `skill-creator/SKILL.md`, **[C]** `skill-creator/scripts/quick_validate.py`.

### Corrections

| # | v1 said | Anthropic says | Where | v2 |
|---|---|---|---|---|
| 1 | `references/` is a competitor convention; use ALL-CAPS files at the skill root | `references/` is the official directory, alongside `scripts/` and `assets/` | [A p5, p10, p13, p27], [B:80-83] | Corrected. `references/` is standard; the repo's ALL-CAPS convention is the deviation. |
| 2 | Descriptions 400–900 characters | No target length. Hard cap 1024. Level-1 budget ~100 words. | [C:83], [B:89] | Range removed. Only the cap is real. |
| 3 | (follow-up msg) Cap descriptions at 400 characters | Claude *under*triggers; descriptions should be "a little bit pushy" | [B:67] | Reversed. Terseness is the risk, not verbosity. |
| 4 | SKILL.md under 250 lines | Under 500 lines ideal; under 5,000 words | [B:96], [A p27] | Corrected. 58 of 59 skills were already compliant. |
| 5 | Require a `## When NOT to use this skill` body section | *All* "when to use" info goes in the description, not the body | [B:67] | Moved to the description, where it can affect routing. Body text loads only after the skill has already triggered. |
| 6 | 14 mandatory checklist items, MUST-style | All-caps MUST/ALWAYS/NEVER is a "yellow flag"; explain the reasoning instead | [B:302] | Checklist split into machine-checked vs human-judged; rules carry reasons. |

### Additions v1 missed entirely

| Added | Why | Where |
|---|---|---|
| `scripts/` directory | "Code is deterministic; language interpretation isn't." Bundle checks rather than describing them. | [A p26], [B:304] |
| `assets/` directory | Templates, fonts, icons used in output. | [A p5] |
| `## Examples` section | Part of the recommended body structure. | [A p12] |
| `## Troubleshooting` section | Same. | [A p12] |
| Functional + performance testing | Three test layers, not one. Performance comparison (tokens/turns with vs without the skill) is what proves a skill earns its context cost. | [A p15-16] |
| Description diagnostic | Ask Claude "when would you use the X skill?" — it quotes the description back. | [A p25] |
| `quick_validate.py` as a gate | A runnable, objective pass/fail. | [C] |
| Near-miss negative test queries | Obviously-irrelevant negatives prove nothing. | [B:356-358] |

### Kept from v1, relabelled

Archive discipline, business-brain write-back, voice rules, and `metadata.version` are **not** in Anthropic's guidance. They are house rules. v2 marks them `[H]` and confines them to Part 6 so the specification and our opinions are not mixed.

### Validator results at time of writing

```
solo-founder-skills (ours)   PASS 59 / FAIL  0
marketingskills (his)        PASS 32 / FAIL  1
makerskills (his)            PASS  9 / FAIL 11
```

Reproduce:

```bash
SC=~/.claude/plugins/cache/claude-plugins-official/skill-creator/unknown/skills/skill-creator
for d in skills/*/; do python3 $SC/scripts/quick_validate.py "$d" | grep -q valid || echo "FAIL $d"; done
```
