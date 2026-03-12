# Code Quality Skill — Design Spec

## Overview

A diagnostic skill that scans a web app's codebase against 17 widely-recognized best practices and produces a compliance score on a 1-100 scale. Designed for two audiences: non-technical founders who need plain-English verdicts, and developers who want technical detail with actionable fixes.

The skill is a **scanner, not a fixer**. It diagnoses and scores. Remediation is handled by existing skills (`secure`, `test`, `optimize`, `monitor`, `database`) or self-contained "Tell AI:" prompts.

## Skill Identity

- **Directory:** `skills/code-quality/`
- **Name (frontmatter):** `code-quality`
- **Description (frontmatter):** "Use this skill when the user wants to assess their codebase's health, score code quality against best practices, or identify technical debt. Also use before handoffs, hiring a developer, scaling, or any time the founder needs to know 'is my code any good?' Covers 17 categories across security, architecture, maintainability, and developer experience."

### When to Use

- First-time codebase health check
- Before launching to production
- Before hiring a developer or handing off code
- After significant AI-assisted development
- As a pre-deploy quality gate (diff scan)
- When evaluating a specific feature area (targeted scan)

### When NOT to Use

- Mid-build on an incomplete feature — finish it first, then scan
- During initial MVP prototyping — ship first, score later
- To fix issues — this skill diagnoses only; use the linked skills to fix
- On code you don't control (third-party libraries, vendor code)

### Relationship to Existing Skills

| Skill | Relationship |
|-------|-------------|
| `optimize` | `code-quality` flags performance footguns and dependency issues; links to `optimize` for remediation |
| `secure` | `code-quality` flags security gaps; links to `secure` for hardening |
| `test` | `code-quality` flags missing coverage; links to `test` for setup |
| `monitor` | `code-quality` flags missing observability; links to `monitor` for setup |
| `database` | `code-quality` flags database concerns; links to `database` for fixes |

Categories without a matching skill (DRY, Single Responsibility, Naming & Readability, Dead Code, File/Project Structure, Separation of Concerns, API Design Consistency, Critical Path Documentation) always produce self-contained "Tell AI:" prompts for remediation.

---

## Categories

17 categories across 3 tiers.

### Critical Tier (score multipliers)

These can hurt users or lose data. Poor scores here drag down the entire score. Critical categories are **not included in the base score** — they affect the final score only through the multiplier and hard cap.

| Category | What It Scans For |
|----------|-------------------|
| Security Basics | Hardcoded secrets, injection vectors, missing auth checks, exposed endpoints |
| Error Handling | Unhandled promises, empty catch blocks, silent failures, missing error boundaries |
| Data Validation & Contracts | No input validation at boundaries, missing type checks, unvalidated API responses |
| State & Concurrency Safety | Race conditions, shared mutable state, missing transaction boundaries |

### Important Tier (standard weighted scoring)

These create tech debt. Poor scores here lower the score proportionally.

| Category | What It Scans For |
|----------|-------------------|
| DRY | Duplicated logic blocks, copy-pasted functions, repeated patterns |
| Single Responsibility | Files/functions doing multiple things, god components, 500+ line files |
| Separation of Concerns | Business logic in UI components, API routes doing data formatting, mixed layers |
| Testing Coverage | No tests, untested critical paths (auth, payments, data mutations) |
| Configuration Management | Hardcoded URLs/values, missing env vars, environment-specific logic inline |
| Performance Footguns | N+1 queries, missing pagination, unbounded data fetches, no caching on hot paths |
| API Design Consistency | Mixed naming conventions, inconsistent response shapes, no error format standard |

### Nice-to-Have Tier (light scoring)

These affect developer experience. Poor scores contribute but won't tank the result.

| Category | What It Scans For |
|----------|-------------------|
| Naming & Readability | Unclear names, inconsistent conventions, single-letter vars outside loops |
| Dead Code | Unused imports, unreachable branches, commented-out blocks |
| Dependency Hygiene | Unused packages, vulnerable deps, duplicated functionality |
| File / Project Structure | No clear organization, deeply nested, inconsistent patterns |
| Observability | No logging on critical paths, no error tracking, no health checks |
| Critical Path Documentation | Zero docs on auth flow, payment flow, or deployment process |

---

## Scoring Mechanics

### Per-Category Scoring

Each category is scored 0-10 based on what the scan finds:

- **9-10:** Excellent. Best practices consistently followed.
- **7-8:** Good. Minor issues, nothing urgent.
- **5-6:** Fair. Patterns present but inconsistently applied.
- **3-4:** Poor. Significant gaps that need attention.
- **0-2:** Critical. Major violations or category entirely absent.

### Color Indicators

| Score | Color | Meaning |
|-------|-------|---------|
| 0-4 | Red | Needs immediate attention |
| 5-6 | Yellow | Room for improvement |
| 7-10 | Green | In good shape |

### Overall Score Calculation

1. **Base score:** Calculated from Important and Nice-to-Have categories only (Critical categories are excluded — they feed the multiplier). Each Important category is equally weighted within a 60% share. Each Nice-to-Have category is equally weighted within a 40% share. Formula: `base = (sum_important / 70) * 60 + (sum_nice_to_have / 60) * 40`
2. **Critical multiplier:** Linear mapping from average Critical score to a 0.4–1.0 range. Formula: `multiplier = 0.4 + 0.06 * avg_critical_score`. Examples: avg 10 = 1.0, avg 5 = 0.7, avg 0 = 0.4.
3. **Hard cap (ceiling):** If any single Critical category scores 2 or below, the overall score cannot exceed 40. If the multiplied score is already below 40, it stays at the lower value — the hard cap is a ceiling, not a floor.
4. **Final score** = `min(base * multiplier, 40)` if any Critical ≤ 2, otherwise `base * multiplier`. Round to nearest integer.

### Score Interpretation

| Score | Verdict |
|-------|---------|
| 85-100 | Production-ready. Well-maintained codebase. |
| 70-84 | Solid. Some areas need attention but no blockers. |
| 50-69 | Needs work. Technical debt accumulating. Address before scaling. |
| 30-49 | Significant issues. Critical gaps likely present. Fix before adding features. |
| 0-29 | Major problems. Stop building and address fundamentals first. |

---

## Scan Modes

### Full Scan (default)

- Scans entire project from root
- Skips non-source directories: `node_modules`, `dist`, `.next`, `build`, `coverage`, vendor/third-party directories
- Focuses on source directories: `src/`, `app/`, `pages/`, `lib/`, `api/`, `components/`, and project root config files
- Produces complete 17-category report
- Best for: first-time assessment, pre-launch review, before hiring a developer

### Targeted Scan

- User specifies a directory or feature area (e.g., "scan src/api/" or "score my auth system")
- Only scores categories relevant to the scoped area
- Categories without enough context marked "N/A — not enough context in scoped area"
- Best for: evaluating a specific feature, reviewing AI-generated code for one area

### Diff Scan

- Scores only files changed since a given ref
- Default ref: last commit (`HEAD~1`)
- User can specify a branch: "diff scan against main" uses `git diff main...HEAD`
- Uses `git diff` to identify changed files, then runs category checks against only those files
- If no git repo is detected, reports an error and suggests full or targeted scan instead
- Produces a lighter report focused on what changed
- Best for: pre-deploy quality gate, PR review, checking if AI coding introduced problems

All three modes produce the same output format with scope noted at the top.

---

## Output Format

### Layer 1 — Founder Summary (always shown)

A plain-English paragraph summarizing the overall state, followed by all 17 category scores with red/yellow/green indicators and one-sentence explanations, followed by the top 3 priorities to fix in order.

Example:

```
## Code Quality Score: 62/100

Your app has solid bones but some serious gaps. Security needs
immediate attention — there are hardcoded API keys that could
expose user data. Error handling is thin in places where failures
would be invisible to you. The good news: your code structure
and organization are clean.

### Category Scores

[red]    Security Basics .............. 3/10  <- hardcoded secrets found
[red]    Error Handling ............... 4/10  <- silent failures in payments
[yellow] Data Validation .............. 5/10  <- no input validation on forms
[green]  State & Concurrency ......... 8/10

[yellow] DRY .......................... 6/10
[green]  Single Responsibility ........ 8/10
[yellow] Separation of Concerns ....... 5/10
[red]    Testing Coverage ............. 2/10
[yellow] Configuration Management ..... 6/10
[green]  Performance Footguns ......... 7/10
[green]  API Design Consistency ....... 8/10

[green]  Naming & Readability ......... 9/10
[yellow] Dead Code .................... 5/10
[green]  Dependency Hygiene ........... 7/10
[green]  File / Project Structure ..... 8/10
[yellow] Observability ................ 4/10
[red]    Critical Path Documentation .. 1/10

### Fix These First
1. Remove hardcoded secrets — API keys in 3 files need to move to env vars
2. Add error handling to payment flow — Stripe calls fail silently
3. Add basic input validation — user forms accept anything
```

### Layer 2 — Technical Deep Dive (shown on request per category)

When the user asks for details on a specific category, provide:

- Specific file:line references for each issue found
- Code examples showing the problem and the fix
- "Tell AI:" prompts for each issue (matching plugin convention)
- Links to relevant skills for systemic problems (or self-contained prompts for categories without a matching skill)

Example:

```
## Security Basics: 3/10

### Issues Found

**Hardcoded API keys (severity: critical)**
- src/lib/stripe.ts:14 — Stripe secret key in source
- src/lib/supabase.ts:3 — Service role key committed
- src/api/email.ts:7 — SendGrid key inline

Fix: Move to environment variables.

Tell AI:
  Move all hardcoded API keys, secrets, and credentials to
  environment variables. Check every file for strings that look
  like keys (sk_, pk_, SG., etc). Update .env.example with
  placeholder names. Add .env to .gitignore if not already there.

**Missing auth checks (severity: high)**
- src/api/admin/users.ts:22 — no auth middleware
- src/api/admin/billing.ts:8 — no auth middleware

Fix: Add auth middleware to all admin routes.

See the `secure` skill for comprehensive security hardening.
```

---

## File Structure

```
skills/code-quality/
├── SKILL.md              # Entry point — usage, scan modes, founder-friendly overview
├── CATEGORIES.md          # All 17 categories: detailed scan criteria and examples
└── SCORING.md             # Tier system, multiplier formula, score interpretation
```

**Content split:**
- **SKILL.md:** Frontmatter, when to use/not use, how to run each scan mode, output format overview, common mistakes, success criteria. This is what the founder reads.
- **CATEGORIES.md:** Detailed per-category reference — what constitutes a 0, a 5, and a 10 for each category, with code examples. This is the technical reference Claude uses during scanning.
- **SCORING.md:** The full scoring formula, tier definitions, multiplier math, hard cap rules, and score interpretation table. Transparent so users can understand and audit their score.

Follows plugin convention: SKILL.md first, supporting files one level deep.

---

## Cross-Skill References

When `code-quality` finds issues, it points to existing skills rather than fixing things itself:

| Category Finding | Links To |
|-----------------|----------|
| Security gaps | `secure` skill |
| Missing tests | `test` skill |
| Performance footguns | `optimize` skill |
| No monitoring/logging | `monitor` skill |
| Dependency issues | `optimize` (Dependencies section) |
| Database concerns | `database` skill |

Categories without a matching skill (DRY, Single Responsibility, Naming & Readability, Dead Code, File/Project Structure, Separation of Concerns, API Design Consistency, Critical Path Documentation) always produce self-contained "Tell AI:" prompts with specific fixes.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Running a scan mid-feature and panicking about low scores | Finish the feature first, then scan |
| Trying to fix everything at once | Follow the "Fix These First" priorities in order |
| Obsessing over Nice-to-Have scores while Critical scores are low | Critical tier exists for a reason — fix red items first |
| Scanning and never re-scanning | Run diff scans before deploys to catch regressions |
| Treating the score as pass/fail | It's a health indicator, not a grade. Trend matters more than absolute number. |

---

## Success Looks Like

After using `code-quality`, you should:

- Know your codebase's strengths and weaknesses in plain English
- Have a prioritized list of what to fix first
- Understand which issues are dangerous vs. cosmetic
- Have "Tell AI:" prompts ready to start fixing the top issues
- Be able to track improvement over time by re-scanning

---

## Design Decisions

1. **Scanner, not fixer** — Keeps the skill focused and avoids duplicating existing skills.
2. **Tiered scoring with hard cap** — Prevents a high score from masking dangerous gaps. A codebase with hardcoded secrets cannot score above 40.
3. **Two-layer output** — Serves both audiences without forcing technical detail on non-technical founders.
4. **Three scan modes** — Full for assessment, targeted for feature review, diff for quality gates.
5. **17 categories** — Comprehensive enough to be meaningful, specific enough to be actionable.
6. **Explicit formulas** — Scoring math is fully specified and transparent so users can understand and audit their scores.
