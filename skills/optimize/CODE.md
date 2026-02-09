# Code Optimization

Detailed patterns for finding and removing unused code in AI-built applications.

---

## Why Code Accumulates

When building with AI tools:
- Iteration creates abandoned components
- Copy-paste creates duplication
- Feature pivots leave dead code
- "I might need this later" prevents deletion

**Result:** Codebase grows faster than features.

---

## Types of Code Waste

### 1. Dead Components

Components created but never imported.

**How to find:**
```
Find all React/Vue/Svelte components.
For each, check if it's imported anywhere.
List components with zero imports.
```

**Common locations:**
- `src/components/` - UI components
- `src/pages/` - Page components
- `src/features/` - Feature modules

### 2. Orphaned Utilities

Helper functions nothing calls.

**How to find:**
```
Find all exported functions in utils/, helpers/, lib/.
For each, search codebase for usage.
List functions with zero usages outside their own file.
```

**Common locations:**
- `src/utils/` - Utility functions
- `src/helpers/` - Helper functions
- `src/lib/` - Library code

### 3. Abandoned Features

Half-built features that were never finished or removed.

**Signs:**
- Folder with few files, old modification dates
- TODO comments that were never completed
- Feature flags that are always false

**How to find:**
```
List folders in src/ with files not modified in 30+ days.
Check if those files are imported anywhere.
List folders with zero external imports.
```

### 4. Duplicate Code

Same logic implemented multiple ways.

**How to find:**
```
Find functions with similar names (formatDate, dateFormat, formatDateTime).
Find components that do similar things (Button, PrimaryButton, ActionButton).
Find utilities that overlap (api.js, fetch.js, http.js).
```

**Common duplications:**
- Date formatting (multiple implementations)
- API calls (different wrappers)
- Form validation (repeated patterns)
- String manipulation (similar utilities)

### 5. Commented-Out Code

Code that was disabled but never removed.

**How to find:**
```
Search for large comment blocks (10+ lines).
Search for commented function definitions.
Search for commented imports.
```

**Rule:** If it's in git history, delete it. You can always get it back.

---

## Audit Workflow

### Step 1: Generate Inventory

**Tell AI:**
```
Create an inventory of all code in src/:
- List all components with import count
- List all utility functions with usage count
- List all files with last modified date
- Flag anything with zero imports/usages
```

### Step 2: Identify Candidates

**Tell AI:**
```
From the inventory, identify cleanup candidates:

High confidence (safe to delete):
- Components imported nowhere
- Functions called nowhere
- Files not modified in 60+ days with zero imports

Medium confidence (verify first):
- Functions used in only 1 place
- Components used in only 1 page
- Duplicate implementations

Flag but keep:
- Test files (may be needed)
- Config files (may be loaded dynamically)
- Type definitions (may be used implicitly)
```

### Step 3: Verify Before Deleting

**For each candidate:**
```
Before deleting [filename]:
1. Search entire codebase for references
2. Check if it's loaded dynamically (lazy imports)
3. Check if it's referenced in config files
4. Check git history for why it was created

If truly unused, mark for deletion.
If uncertain, mark for review.
```

---

## Safe Deletion Process

### Option A: Delete and Verify

```
1. Delete the file
2. Run: npm run build
3. If build succeeds, delete was safe
4. If build fails, restore and investigate
```

### Option B: Comment and Test

```
1. Comment out all exports from file
2. Run: npm run build && npm test
3. If passes, delete the file
4. If fails, restore and investigate
```

### Option C: Gradual Removal

For large cleanup:
```
1. Add deprecation comment to file
2. Wait one release cycle
3. If no issues reported, delete
4. If issues found, restore and fix
```

---

## Common Patterns in AI-Built Apps

### Pattern: Multiple Button Variants

**What you find:**
```
src/components/Button.tsx
src/components/PrimaryButton.tsx
src/components/SecondaryButton.tsx
src/components/ActionButton.tsx
src/components/SubmitButton.tsx
```

**What you need:**
```
src/components/Button.tsx (with variant prop)
```

**Tell AI:**
```
Consolidate button components into single Button with variants:
- variant="primary" | "secondary" | "ghost" | "destructive"
- Remove duplicate button files
- Update all imports to use unified Button
```

### Pattern: Multiple API Wrappers

**What you find:**
```
src/lib/api.ts
src/utils/fetch.ts
src/helpers/http.ts
src/services/client.ts
```

**What you need:**
```
src/lib/api.ts (single API client)
```

**Tell AI:**
```
Consolidate API utilities into single module:
- Keep the most complete implementation
- Migrate usages from other files
- Delete redundant files
```

### Pattern: Scattered Utilities

**What you find:**
```
src/utils/formatDate.ts
src/helpers/dateUtils.ts
src/lib/dates.ts
formatDate() in 3 different files
```

**What you need:**
```
src/utils/date.ts (all date utilities)
```

**Tell AI:**
```
Consolidate date utilities:
- Merge all date functions into src/utils/date.ts
- Remove duplicates (keep most robust version)
- Update all imports
- Delete empty files
```

---

## Tools for Code Analysis

### ESLint Rules

```json
{
  "rules": {
    "no-unused-vars": "error",
    "no-unused-imports": "error",
    "@typescript-eslint/no-unused-vars": "error"
  }
}
```

### TypeScript Strict Mode

```json
{
  "compilerOptions": {
    "noUnusedLocals": true,
    "noUnusedParameters": true
  }
}
```

### VS Code Extensions

- **Import Cost** - Shows size of imports
- **ESLint** - Highlights unused code
- **TypeScript** - Grays out unused variables

---

## Prevention Checklist

After cleanup, set up guards:

```
- [ ] ESLint rule: no-unused-vars (error, not warn)
- [ ] ESLint rule: no-unused-imports
- [ ] TypeScript: noUnusedLocals and noUnusedParameters
- [ ] Pre-commit hook: lint check
- [ ] CI pipeline: fail on unused code warnings
- [ ] Code review: check for abandoned code in PRs
```

---

## When NOT to Delete

**Keep even if unused:**
- Public API exports (external consumers)
- Test utilities (only used in tests)
- Type definitions (TypeScript may not show usage)
- Config files (loaded dynamically)
- Scripts (run from command line)

**Verify before deleting:**
- Lazy-loaded components (dynamic imports)
- Components in routing config
- Functions called via string names
- Event handlers registered globally
