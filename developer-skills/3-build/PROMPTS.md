# Effective Prompting Patterns

## Core Patterns

### Pattern 1: Reference Existing
```
Build Settings page.
Reference Dashboard layout (src/pages/Dashboard.tsx).
Use same Card/Button components.
```

### Pattern 2: Visual Reference
```
Pricing page with 3 tiers.
Like Linear's pricing - clean, minimal, centered.
```

### Pattern 3: Constraint-Based
```
Build profile page.
Must: Work offline, load <2s, WCAG AA
```

### Pattern 4: Step-by-Step
```
Password reset flow:
1. User clicks "Forgot Password"
2. Shows email input
3. User enters email → "Check email" message
4. User clicks email link → "Set New Password"
5. User enters password → "Updated! Redirecting..."

Edge cases:
- Email not found: "If email exists, we sent link"
- Link expired: "Link expired. Request new one"
```

---

## Bug Fix Template

```
Issue with [feature].

Tried: [action]
Expected: [result]
Got: [what happened]
Error: [message if any]
```

---

## Iteration Template

```
[Feature] works, but needs:
1. [Specific change]
2. [Specific change]

Current: [what it does]
Want: [what it should do]
```

---

## Common Mistakes

**Bad:** "Make it better"  
**Good:** "Increase heading to 32px, add 24px margin below"

**Bad:** "Fix the button"  
**Good:** "Submit button on checkout does nothing when clicked. Should process payment."

**Bad:** "Add profile page and fix login and change colors"  
**Good:** "First fix login bug: [describe]. Then we'll do profile page."

---

## Tool-Specific

**Claude Code:**
```
Add user search to dashboard.
Follow pattern in Projects search (src/features/projects/Search.tsx).
Use same SearchInput and debounce hook.
```

**Lovable:**
```
Landing page with:
- Hero + CTA
- 3 feature cards
- Pricing (3 tiers)
- Footer

Like Linear - modern, clean.
```

**Replit:**
```
Todo app: add, check, delete todos.
Store in localStorage.
React.
```

---

## When to Stop Prompting

✅ Stop when:
- Feature works as specified
- Edge cases handled
- Performance acceptable

❌ Don't prompt for:
- <2px tweaks
- Premature optimization
- Features beyond spec
