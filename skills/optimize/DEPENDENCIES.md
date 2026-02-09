# Dependencies Optimization

Detailed patterns for reducing package bloat and managing dependencies.

---

## Why Dependencies Accumulate

When building with AI tools:
- AI adds packages to solve problems quickly
- Experiments leave unused packages behind
- Multiple packages for same purpose
- Transitive dependencies multiply

**Result:** Slow installs, large bundles, security vulnerabilities.

---

## Types of Dependency Waste

### 1. Unused Packages

Packages in package.json that aren't imported anywhere.

**How to find:**
```bash
npx depcheck
```

**Common unused packages:**
- Packages from abandoned features
- Packages replaced by alternatives
- Dev tools no longer used
- Packages added "just in case"

### 2. Duplicate Packages

Same package at different versions, or multiple packages doing the same thing.

**How to find:**
```bash
npm ls --all | grep -E "^├|^│.*├"
```

**Common duplications:**
- `lodash` + `lodash-es` + `underscore`
- `moment` + `dayjs` + `date-fns`
- `axios` + `node-fetch` + `got`
- `uuid` + `nanoid` + `cuid`

### 3. Heavy Packages

Packages that add significant bundle size.

**How to find:**
```bash
npx webpack-bundle-analyzer
# or
npx source-map-explorer build/static/js/*.js
```

**Common heavy packages:**
| Package | Size | Lighter Alternative |
|---------|------|---------------------|
| moment | 290KB | dayjs (7KB) |
| lodash | 70KB | lodash-es (tree-shakeable) |
| axios | 29KB | fetch (built-in) |
| jquery | 87KB | vanilla JS |

### 4. Outdated Packages

Packages with available updates, especially security patches.

**How to find:**
```bash
npm outdated
npm audit
```

### 5. Dev Dependencies in Production

devDependencies that accidentally ended up in dependencies.

**How to find:**
```
Check package.json dependencies section for:
- Testing libraries (jest, mocha, cypress)
- Linters (eslint, prettier)
- Build tools (webpack, babel configs)
- Type definitions (@types/*)
```

---

## Audit Workflow

### Step 1: Check Unused

```bash
# Install depcheck
npm install -g depcheck

# Run analysis
depcheck

# Output shows:
# - Unused dependencies
# - Unused devDependencies
# - Missing dependencies
```

### Step 2: Check Bundle Size

```bash
# Build and analyze
npm run build

# For detailed breakdown (React/webpack)
npx webpack-bundle-analyzer build/stats.json

# For Next.js
npx @next/bundle-analyzer
```

### Step 3: Check Security

```bash
# Check for vulnerabilities
npm audit

# Check for outdated
npm outdated

# Check for deprecated
npm ls 2>&1 | grep -i deprecated
```

### Step 4: Generate Report

**Tell AI:**
```
Analyze package.json and generate report:
- Unused packages (from depcheck output)
- Largest packages by bundle size
- Packages with security vulnerabilities
- Packages with major updates available
- Duplicate functionality packages

For each, recommend: keep, remove, or replace.
```

---

## Safe Removal Process

### For Unused Packages

```bash
# Step 1: Verify not used
grep -r "package-name" src/

# Step 2: Remove from package.json
npm uninstall package-name

# Step 3: Test
npm run build && npm test

# Step 4: If tests pass, commit
```

### For Package Replacement

```bash
# Step 1: Install alternative
npm install dayjs

# Step 2: Update imports
# Change: import moment from 'moment'
# To: import dayjs from 'dayjs'

# Step 3: Update usage
# Change: moment().format('YYYY-MM-DD')
# To: dayjs().format('YYYY-MM-DD')

# Step 4: Remove old package
npm uninstall moment

# Step 5: Test thoroughly
npm run build && npm test
```

### For Major Updates

```bash
# Step 1: Check changelog for breaking changes
# Visit package's GitHub releases page

# Step 2: Update one package at a time
npm install package-name@latest

# Step 3: Test
npm run build && npm test

# Step 4: Fix any breaking changes
# Step 5: Commit before next update
```

---

## Common Replacements

### Date/Time

| Instead of | Use | Size Reduction |
|------------|-----|----------------|
| moment | dayjs | 290KB → 7KB |
| moment | date-fns | 290KB → tree-shakeable |

```javascript
// moment → dayjs (mostly compatible API)
import dayjs from 'dayjs';
dayjs().format('YYYY-MM-DD');

// moment → date-fns (function-based)
import { format } from 'date-fns';
format(new Date(), 'yyyy-MM-dd');
```

### HTTP Requests

| Instead of | Use | Size Reduction |
|------------|-----|----------------|
| axios | fetch | 29KB → 0KB (built-in) |
| request | fetch | deprecated → built-in |

```javascript
// axios → fetch
const response = await fetch('/api/data');
const data = await response.json();

// With error handling
const response = await fetch('/api/data');
if (!response.ok) throw new Error(response.statusText);
const data = await response.json();
```

### Utilities

| Instead of | Use | Size Reduction |
|------------|-----|----------------|
| lodash | lodash-es | 70KB → tree-shakeable |
| lodash | native JS | 70KB → 0KB |
| underscore | native JS | 25KB → 0KB |

```javascript
// lodash _.map → native
array.map(x => x.value);

// lodash _.filter → native
array.filter(x => x.active);

// lodash _.find → native
array.find(x => x.id === targetId);

// lodash _.uniq → native
[...new Set(array)];

// If you need lodash, import individual functions
import debounce from 'lodash/debounce';
```

### UUIDs

| Instead of | Use | Size Reduction |
|------------|-----|----------------|
| uuid | nanoid | 12KB → 1KB |
| uuid | crypto.randomUUID() | 12KB → 0KB |

```javascript
// uuid → nanoid
import { nanoid } from 'nanoid';
const id = nanoid();

// uuid → native (browsers/Node 19+)
const id = crypto.randomUUID();
```

---

## Prevention Patterns

### Bundle Size Budget

Add to CI pipeline:

```json
// package.json
{
  "scripts": {
    "build": "next build",
    "check-bundle": "bundlesize"
  },
  "bundlesize": [
    {
      "path": ".next/static/chunks/*.js",
      "maxSize": "200 KB"
    }
  ]
}
```

### Dependabot

Create `.github/dependabot.yml`:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
```

### Import Cost Extension

VS Code extension that shows import size inline:

```javascript
import moment from 'moment';  // 290KB
import dayjs from 'dayjs';    // 7KB
```

### Pre-commit Check

Add to `.husky/pre-commit`:

```bash
#!/bin/sh
npm audit --audit-level=high
if [ $? -ne 0 ]; then
  echo "Security vulnerabilities found. Fix before committing."
  exit 1
fi
```

---

## Package.json Hygiene

### Correct Placement

```json
{
  "dependencies": {
    // Runtime packages only
    "react": "^18.0.0",
    "next": "^14.0.0"
  },
  "devDependencies": {
    // Build/test/dev tools only
    "typescript": "^5.0.0",
    "jest": "^29.0.0",
    "eslint": "^8.0.0",
    "@types/react": "^18.0.0"
  }
}
```

### Version Pinning

```json
{
  "dependencies": {
    // Exact versions for critical packages
    "react": "18.2.0",

    // Caret for minor updates OK
    "lodash": "^4.17.21",

    // Never use * or latest
    "bad-practice": "*"  // DON'T DO THIS
  }
}
```

### Lock Files

- **Always commit** `package-lock.json` (npm) or `yarn.lock` (yarn)
- **Never delete** lock file without understanding consequences
- **Regenerate** by deleting `node_modules` + lock file, then `npm install`

---

## Cleanup Checklist

```
- [ ] Run depcheck for unused packages
- [ ] Run npm audit for vulnerabilities
- [ ] Run npm outdated for updates
- [ ] Analyze bundle size
- [ ] Remove unused packages
- [ ] Replace heavy packages with lighter alternatives
- [ ] Update packages with security issues
- [ ] Move dev tools to devDependencies
- [ ] Set up Dependabot
- [ ] Add bundle size check to CI
- [ ] Delete node_modules and reinstall fresh
- [ ] Verify build and tests pass
```
