# Deep Audit Checklist

Structured checklist for the deep DRY audit mode. Work through each domain in order, applying fixes and running tests between domains.

---

## UI Components Audit

### Search Patterns

```
# Find components with similar names
Search for files matching: *Card*, *Modal*, *Form*, *List*, *Table*, *Button*, *Badge*, *Dialog*
Group by suffix — multiple files with the same suffix are candidates.

# Find repeated JSX structure
Search for similar HTML/JSX patterns across component files:
- Same div nesting with similar class names
- Same map() rendering patterns
- Same conditional rendering blocks

# Find repeated inline styles
Search for identical style objects, className strings, or Tailwind class combinations
that appear in 3+ components.

# Find reimplemented library components
Check if custom components duplicate functionality from the project's component library
(shadcn/ui, Radix, MUI, etc.).
```

### Refactoring Actions

| Finding | Action |
|---------|--------|
| Two components with >80% similar JSX | Extract shared component, parameterize differences via props |
| Same Tailwind classes in 3+ places | Extract to a CSS class or component variant |
| Custom component that mirrors a library component | Replace with library version, migrate props |
| Components that differ only in data source | Extract component, pass data as prop |

### After UI Fixes
- Run build to catch import errors
- Visual check: do pages still look correct?
- Run any component tests

---

## Database Schema Audit

### Search Patterns

```sql
-- Find potential denormalization: columns that duplicate data from related tables
-- Look for columns like user_name, user_email, customer_name on non-user tables

-- Find missing foreign keys
-- Look for columns ending in _id that lack FK constraints

-- Find repeated string values that should be lookup tables
-- Run: SELECT DISTINCT status FROM [table] for all tables with status/type/category columns
-- If the same set of values appears across tables, it's a candidate for a shared enum or lookup

-- Find inconsistent naming
-- Compare column names across tables: created_at vs createdAt vs date_created
```

### Refactoring Actions

| Finding | Action |
|---------|--------|
| Denormalized column (e.g., `orders.user_email`) | Drop column, JOIN to source table, update queries |
| ID column without FK | Add FK constraint with appropriate ON DELETE |
| String column with fixed values | Create enum type or lookup table, migrate data |
| Inconsistent naming | Standardize to project convention (snake_case recommended), update all references |
| Duplicate data across tables | Identify the source of truth, remove copies, add JOINs |

### After Database Fixes
- Run all migrations on a test database first
- Verify application queries still work
- Check that RLS policies still apply correctly

---

## Workflow Logic Audit

### Search Patterns

```
# Find duplicate function names
Search for function/const declarations with identical names across different files.

# Find similar function bodies
Search for functions with:
- Same parameters (even if named differently)
- Same return type
- Similar logic patterns (map/filter/reduce chains, try/catch blocks)

# Find repeated imports
Search for files that import the same 3+ packages — they likely contain similar logic.

# Find repeated string literals
Search for string literals (URLs, error messages, status values) used in 3+ files.

# Find repeated validation patterns
Search for regex patterns, .test() calls, and validation functions.

# Find repeated API call patterns
Search for fetch/axios calls with similar URL patterns, headers, or error handling.
```

### Refactoring Actions

| Finding | Action |
|---------|--------|
| Same function in 2+ files | Move to `lib/[domain].ts`, update imports everywhere |
| Same API boilerplate in 3+ endpoints | Extract `lib/api-client.ts` with shared error handling |
| Same validation in 3+ places | Extract `lib/validators.ts` with reusable validation functions |
| Same string literals in 3+ files | Extract to `lib/constants.ts` |
| Same data transform in 3+ components | Extract to a named function in `lib/transforms.ts` or near the type definition |
| Same business calculation in 2+ places | Extract to `lib/[domain].ts` (e.g., `lib/pricing.ts`) |

### After Logic Fixes
- Run build to catch import errors
- Run all tests
- Manually test the affected features

---

## Reporting

After completing all three domains, summarize findings:

```
DRY Audit Results:

UI Components:
- [N] duplicates found, [N] fixed
- Key changes: [list extracted/consolidated components]

Database Schema:
- [N] normalization issues found, [N] fixed
- Key changes: [list migrations applied]

Workflow Logic:
- [N] duplicates found, [N] fixed
- Key changes: [list extracted modules]

Remaining items (deferred — rule of three not met):
- [list items with only 2 occurrences, monitored for future extraction]
```
