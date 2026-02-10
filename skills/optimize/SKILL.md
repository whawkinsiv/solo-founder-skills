---
name: optimize
description: "Use this skill when the user's app feels slow, the codebase feels bloated, or after significant development work. Optimizes across four dimensions: Speed (page load, API response), Code (unused files, dead code), Database (orphaned data, schema hygiene), and Dependencies (package bloat, bundle size)."
---

# Optimize

Reduce waste and improve efficiency. **Only optimize after you have real users and real problems** — premature optimization is the most common waste of founder time.

## When to Optimize (and When NOT To)

**Don't optimize when:**
- Building your MVP
- Fewer than ~100 active users
- Everything works fine
- You haven't measured the problem

**Optimize when:**
- Users complain about slowness (Speed)
- Bundle size warnings or security alerts appear (Dependencies)
- App noticeably slower than when you launched (Speed/Database)
- You're paying for hosting you shouldn't need (Speed/Database)

**Rule:** Make it work → get users → measure → THEN make it lean.

---

## Priority Order

When multiple things need work:

1. **Speed** — Users feel this immediately. Slow = churn.
2. **Dependencies** — Security vulnerabilities are urgent. Bundle bloat affects speed.
3. **Database** — Affects long-term performance and hosting costs.
4. **Code** — Affects maintainability. Lowest user impact.

---

## Speed Optimization

### Targets

| Metric | Good | Bad |
|--------|------|-----|
| Page load | < 3s | > 5s |
| API response | < 500ms | > 1s |
| Time to interactive | < 5s | > 8s |

### Step 1: Measure

**Quick manual check:**
- Open your app in Chrome → Right-click → Inspect → Network tab → Reload
- Look at the "Load" time at the bottom. That's your page load time.
- Click a button that calls your API. Look for the request time in the Network tab.

**Tell AI:**
```
Audit app performance:
- Measure page load times for the 3 most important pages
- Log API response times for the 5 most-used endpoints
- Identify the slowest database queries
- Check total bundle size
Report findings with specific numbers.
```

### Step 2: Fix

**Tell AI:**
```
Optimize these performance issues:
[paste audit findings]

Apply fixes in this order:
1. Add caching for slow API calls
2. Add database indexes for slow queries
3. Optimize and lazy-load images
4. Code split large bundles
Run build and tests after each fix.
```

### Step 3: Prevent

**Tell AI:**
```
Add performance monitoring:
- Log API calls > 500ms
- Log database queries > 100ms
- Alert if page load > 3s
```

See [PERFORMANCE-CHECKS.md](PERFORMANCE-CHECKS.md) for detailed testing methods.

---

## Dependencies Optimization

The most relevant optimization at any stage — even pre-launch.

### Signs You Need This

- Security vulnerability warnings when you run `npm install`
- Bundle size > 500KB
- "What does this package do?"

### Audit

**Tell AI:**
```
Audit dependencies:
- List packages not imported anywhere in code
- List packages with security vulnerabilities
- Analyze bundle size by package
- Find packages with lighter alternatives

Report: package name, size impact, and recommendation.
```

### Fix

**Tell AI:**
```
Clean up dependencies:
[paste audit findings]

Steps:
- Remove unused packages from package.json
- Update packages with security vulnerabilities
- Replace heavy packages with lighter alternatives
After changes: delete node_modules, fresh npm install, run build and tests.
```

**Common replacements:**

| Heavy | Light Alternative |
|-------|-------------------|
| moment.js | date-fns or dayjs |
| lodash (full) | lodash-es (tree-shakeable) |
| axios | fetch (built-in) |

### Prevent

**Tell AI:**
```
Set up dependency hygiene:
- Add npm audit to CI pipeline
- Configure Dependabot for automatic security updates
```

See [DEPENDENCIES.md](DEPENDENCIES.md) for detailed patterns.

---

## Database Optimization

**When this matters:** After months of real usage, when queries slow down or hosting costs climb.

### Signs You Need This

- Pages that were fast are now slow
- Database hosting costs increasing
- Queries timing out under load

### Audit and Fix

**Tell AI:**
```
Audit database for optimization opportunities:
- Find missing indexes on frequently queried columns
- Find slow queries (> 100ms)
- Find orphaned records (foreign keys pointing to deleted rows)
- Find tables with no recent reads/writes

For each issue, apply the fix:
- Add indexes for slow queries
- Set up ON DELETE CASCADE for dependent records
- Create cleanup job for orphaned/soft-deleted records (> 90 days)
Always backup before making schema changes.
```

---

## Code Cleanup

**When this matters:** After your codebase has grown significantly through AI-assisted iteration. Multiple rounds of "build feature, rebuild feature" leave dead code.

### Signs You Need This

- Files you don't recognize
- Components that aren't used anywhere
- "I'm afraid to delete this"

### Audit and Fix

**Tell AI:**
```
Audit codebase for unused code:
- Find components not imported anywhere
- Find functions never called
- Find commented-out code blocks
- Find duplicate/similar code

For each: verify nothing references it, then remove it.
Run build and tests after cleanup.
```

**Safety rule:** If unsure, comment out first and test. Delete after confirming nothing breaks.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Optimizing before measuring | AUDIT first, always |
| Optimizing during MVP | Ship first, optimize when users complain |
| Updating all packages at once | Update one at a time, test each |
| Deleting code without verifying | Check imports/references before removing |
| Dropping database columns in production | Test migrations on staging first |

---

## Success Looks Like

After optimization, you should see:

- Pages load < 3 seconds
- Zero security vulnerabilities in dependencies
- No obviously unused packages
- Database queries respond < 100ms
- Automated checks catch future regressions
