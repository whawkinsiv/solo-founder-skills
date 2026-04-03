---
name: dry
description: "Use this skill to find and eliminate duplication across your codebase — UI components, database schema, and workflow logic. Also use when the codebase feels bloated, features take longer to build, changes break in unexpected places, or after significant AI-assisted development. Covers code deduplication, component reuse, database normalization, and modular architecture."
---

# Don't Repeat Yourself

Find and eliminate duplication across your codebase. Every duplicate is a future bug — when you fix something in one place but forget the copy, users hit the unfixed version.

**This skill audits and refactors.** For building features, use **build**. For general performance optimization, use **optimize**. For database schema design from scratch, use **database**. For UI component selection, use **ui-patterns**.

## Two Modes

| Mode | When | Scope | Time |
|------|------|-------|------|
| **Quick scan** | After building a feature, or on request | Recent changes vs. existing codebase | 2-5 minutes |
| **Deep audit** | Codebase feels bloated, periodic cleanup | Entire codebase, all three domains | 15-30 minutes |

**Choose quick scan** after implementing features, adding new pages, or building new API endpoints. **Choose deep audit** when the codebase has grown through many rounds of AI-assisted iteration, or quarterly as hygiene.

---

## Quick Scan Workflow

Run this after building or modifying a feature.

```
Quick DRY scan:
- [ ] Identify what was just built or changed
- [ ] Search for similar patterns in existing codebase
- [ ] Flag any duplication with specific file locations
- [ ] Refactor: extract shared code, reuse existing components
- [ ] Verify nothing broke after refactoring
```

### Process

1. **Identify the change** — What files were just created or modified?
2. **Search for siblings** — For each new component, function, or query: does something similar already exist?
3. **Decide: reuse or extract** — If a near-duplicate exists, reuse it. If two things are now similar, extract a shared version.
4. **Refactor** — Make the change, run build and tests.

### What to Search For

- New component created → search for components with similar props, layout, or purpose
- New utility function → search for functions with similar signatures or logic
- New API endpoint → search for endpoints with similar query patterns or response shapes
- New database query → search for queries hitting the same tables with similar conditions

---

## Deep Audit Workflow

Run this for comprehensive deduplication across the full codebase.

```
Deep DRY audit:
- [ ] Audit UI components for duplication
- [ ] Audit database schema for normalization issues
- [ ] Audit workflow logic for duplicate functions and patterns
- [ ] Generate findings with specific refactoring actions
- [ ] Apply fixes domain by domain, testing after each
```

See [AUDIT-CHECKLIST.md](AUDIT-CHECKLIST.md) for detailed search patterns and refactoring recipes per domain.

---

## Domain 1: UI Components

### What to Find

- **Near-duplicate components** — Two card components, two modal wrappers, two form layouts with slight differences
- **Repeated inline styles** — Same padding, colors, or layout CSS copied across components instead of using shared tokens or classes
- **Same-purpose components** — `UserList` and `MemberList` that do essentially the same thing with different prop names
- **Reimplemented patterns** — Custom dropdown when the component library already has one

### How to Fix

1. **Identical components** → Delete one, update imports to point to the survivor
2. **Near-duplicates** → Extract a shared component with props for the differences
3. **Repeated styles** → Extract into shared CSS classes, design tokens, or a utility class
4. **Reimplemented patterns** → Replace with the component library version

### AI-Tool-Specific Patterns

| Tool | Common Duplication | Why |
|------|-------------------|-----|
| Lovable | Each prompt creates new Card/Button/Modal variants | Lovable doesn't reference existing components by default |
| Replit | Inline styles duplicated across pages | Fast iteration favors copy-paste |
| Cursor | Similar components in different feature folders | File-scoped context misses cross-feature reuse |
| Claude Code | Utility components recreated in new feature branches | Context window doesn't always include existing shared components |

**Tell AI (for other tools):**
```
Search my codebase for duplicate UI components:
- Find components with similar JSX structure or props
- Find repeated inline styles or CSS classes
- Find components that render the same kind of data differently
For each duplicate: show both versions side-by-side and propose a single shared component.
```

---

## Domain 2: Database Schema

### What to Find

- **Denormalized data** — User's email stored in both `users` table and `orders` table instead of joining
- **Missing foreign keys** — IDs stored as plain integers/strings without proper references
- **Repeated column groups** — `created_at`, `updated_at`, `created_by` defined inconsistently across tables
- **Enum values in columns** — Status strings like `'active'`, `'inactive'` repeated instead of using a lookup table
- **Duplicate lookup data** — Category names stored as strings in every row instead of referencing a categories table

### How to Fix

1. **Denormalized data** → Remove the duplicate column, add a JOIN where needed
2. **Missing foreign keys** → Add proper FK constraints with ON DELETE behavior
3. **Repeated column groups** → Standardize naming and types across all tables
4. **String enums** → Create a lookup table or use a database enum type (for values that won't change)
5. **Duplicate lookup data** → Extract into a reference table, replace with foreign key

### Red Flags in AI-Generated Schemas

AI tools often create self-contained tables per feature. Watch for:
- A `projects` table with `owner_name` and `owner_email` instead of `owner_id` referencing `users`
- An `invoices` table with `customer_name`, `customer_email`, `customer_address` instead of `customer_id`
- Multiple tables with their own `status` VARCHAR column using the same string values

**Tell AI (for other tools):**
```
Audit my database schema for normalization issues:
- Find columns that store data already available in another table
- Find ID columns without foreign key constraints
- Find string columns that should be lookup tables
- Find inconsistent column naming across tables
For each: explain the problem and write the migration to fix it.
```

---

## Domain 3: Workflow Logic

### What to Find

- **Duplicate utility functions** — Two `formatDate()` functions in different files
- **Repeated API patterns** — Same fetch-try-catch-error-handle boilerplate across endpoints
- **Copy-pasted validation** — Email validation logic in signup, settings, and invite flows
- **Duplicate business logic** — Price calculation in checkout, invoice generation, and dashboard
- **Repeated data transforms** — Same array mapping/filtering logic in multiple components

### How to Fix

1. **Duplicate utilities** → Keep one, move to a shared `utils/` or `lib/` directory, update all imports
2. **API boilerplate** → Extract a shared API client or wrapper function
3. **Repeated validation** → Create a shared validation module (e.g., `lib/validators.ts`)
4. **Business logic** → Extract into a service or domain module (e.g., `lib/pricing.ts`)
5. **Data transforms** → Extract into named functions near the data type they operate on

### Search Strategy

```
Find duplicate logic:
1. Search for functions with identical or near-identical bodies
2. Search for repeated import patterns (same 3+ imports in multiple files)
3. Search for similar try/catch blocks around API calls
4. Search for the same regex or validation pattern in multiple files
5. Search for string literals used in more than 2 files (often config that should be a constant)
```

**Tell AI (for other tools):**
```
Audit my codebase for duplicate workflow logic:
- Find functions with similar names or identical logic in different files
- Find repeated error handling patterns
- Find validation logic that appears in more than one place
- Find business calculations done in more than one place
For each: show all locations and propose a single shared implementation.
```

---

## What NOT to Deduplicate

Not all duplication is bad. Don't over-abstract.

| Leave It Alone | Why |
|---------------|-----|
| Two functions that look similar but serve different business purposes | They'll diverge. Premature abstraction creates coupling. |
| Test setup code that repeats across test files | Test readability matters more than test DRYness. |
| Simple one-liners used twice | Extracting adds indirection without meaningful reuse. |
| Code that's similar today but will evolve differently | Shared abstractions should reflect stable, shared concepts. |
| Configuration that's the same across environments by coincidence | Config should be explicit per environment, not shared. |

**Rule of three:** If something appears in 3+ places, extract it. If it's only in 2 places, wait until the third occurrence to confirm it's a real pattern, not coincidence.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Creating a `utils.ts` mega-file | Group by domain: `lib/pricing.ts`, `lib/validation.ts`, `lib/formatting.ts` |
| Abstracting before the pattern stabilizes | Wait for 3+ occurrences. Two similar things might diverge. |
| Breaking working code to "clean it up" | Run build and tests after every refactoring step |
| Over-parameterizing a shared component | If a component needs 10 props to handle all cases, it's doing too much |
| Deduplicating across feature boundaries prematurely | Features that share code today might need to diverge tomorrow |

---

## Success Looks Like

After a DRY audit, you should see:

- Each UI component exists once with clear props for variation
- Database tables reference each other via foreign keys instead of duplicating data
- Shared logic lives in clearly named modules under `lib/` or `utils/`
- No function body is copy-pasted across files
- New features can reuse existing components and utilities instead of recreating them

---

## Related Skills

- **optimize** — Performance and cleanup (speed, dependencies, dead code)
- **database** — Schema design, RLS, migrations, query patterns
- **ui-patterns** — Component selection, state matrix, page composition
- **build** — Feature development workflow and AI tool prompting
- **debug** — When deduplication breaks something
