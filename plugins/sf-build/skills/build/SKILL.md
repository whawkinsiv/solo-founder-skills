---
name: build
description: "Use this skill when the user needs to build features with AI coding tools, choose between Claude Code, Lovable, Replit, or Cursor, write effective prompts for code generation, or iterate on AI-generated code. Covers tool selection, prompting strategies, and development workflows for non-technical founders."
---

# Build

## Tool Selection

**Starting from scratch?** → Lovable (fastest MVP)  
**Existing codebase?** → Claude Code (best context)  
**Learning to code?** → Replit (educational)  
**Already code?** → Cursor (power features)

See [TOOLS.md](TOOLS.md) for detailed comparison.

---

## Build Workflow

```
- [ ] Start with spec (use scope skill)
- [ ] Give spec to AI tool
- [ ] Test happy path + edge cases
- [ ] Give specific feedback on issues
- [ ] Iterate (expect 2-4 rounds)
- [ ] Deploy when working
```

---

## Giving AI Your Spec

### Claude Code
```
Build this feature: [paste spec]

Codebase: React + TypeScript + Tailwind
Reference: src/components/Button.tsx for button patterns
```

### Lovable
```
Build: [paste simplified spec focusing on outcome]
Make it look like Linear (minimal, clean)
```

### Replit
```
Create: [paste spec emphasizing what user sees]
Use React. Keep simple.
```

See [PROMPTS.md](PROMPTS.md) for patterns.

---

## Build in Pieces, Not All at Once

The biggest mistake non-technical founders make: giving AI the entire spec and hoping it comes back perfect. It won't. AI tools work best in focused chunks.

**The Build Loop:**
```
1. Pick ONE piece (a single feature or flow)
2. Give AI a clear spec for just that piece
3. Test it — does the piece work?
4. Fix any issues before moving on
5. Pick the next piece → repeat
```

**Good pieces** (1-3 hours each):
- User signup and login
- Dashboard showing key metrics
- Settings page with profile editing
- One core workflow (e.g., "create an invoice")

**Bad pieces** (too big):
- "Build the whole app"
- "Build the dashboard with all integrations"
- "User management with roles, permissions, and team features"

### Quality Gate Between Pieces

Before building the next feature, check: **Does the previous feature still work?** Can you sign up, do the core action, and see the result? AI tools sometimes break existing features while adding new ones. Catch that early.

### When to Start a Fresh Session

Start a new chat/session with your AI tool when:
- AI has made **3+ attempts** at the same fix without success — context is polluted
- You're seeing **new bugs appear** every time a bug is fixed
- The AI is **going in circles** (suggesting things it already tried)
- You want to **add a new feature** after finishing the current one

When starting fresh, give AI a clear description of: what exists, what works, and what you need next. Don't assume it remembers.

### Things AI Won't Add Unless You Ask

AI-built projects routinely ship without these. Add them explicitly:

```
Ask Your AI Tool to Add:
- [ ] Error tracking (Sentry) — so you know when things break
- [ ] Analytics snippet (Plausible, PostHog, or GA4) — so you know who visits
- [ ] Proper 404 page — so broken links don't show a blank screen
- [ ] Proper 500 page — so server errors show a helpful message
- [ ] Favicon — so your browser tab has an icon, not a blank square
- [ ] Meta tags (title, description, OG image) — so links look good when shared
- [ ] Loading states — so users know something is happening
```

---

## Reviewing What AI Built

Test, don't just run:

```
- [ ] Looks right?
- [ ] Happy path works?
- [ ] Edge cases work?
- [ ] Works on mobile?
- [ ] Error messages clear?
```

---

## Giving Feedback

**Bad:** "This doesn't work"  
**Good:** "Clicking 'Save' does nothing. Expected: 'Saved!' message"

**Template:**
```
What I tried: [action]
Expected: [outcome]
Got: [what happened]
```

---

## Iteration Expectations

**Normal:** 2-4 rounds per feature  
**First build:** AI builds from spec, you find 3-5 issues  
**Second build:** Fixes those, you find 1-2 more  
**Third build:** Final polish

**Stop when:**
- Happy path works
- Edge cases handled
- Mobile works
- No obvious bugs

**Don't iterate for:**
- Perfection
- Features beyond spec
- Premature optimization

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| No spec | Use scope skill first |
| "Build a dashboard" | Specify what's on it |
| Skip edge case testing | Try breaking it |
| Accept without review | Always test |
| Add features mid-build | Finish current feature first |
| Fix code yourself | Describe problem, let AI fix |

---

## Right-Sizing Work

**Too big:** "Build entire app"  
**Too small:** "Add one button"  
**Right:** "Build user auth flow" (1-3 hours)

**Good chunks:**
- User login/signup flow
- Dashboard with 4 metrics
- Settings page with profile editing

---

## When Stuck

**AI keeps breaking things:**
→ Break into smaller piece, start fresh session

**Can't figure out complex feature:**
→ Ask: "What's simplest way?" Accept simpler solution

**Each fix breaks something else:**
→ Stop. Ask: "Better approach?" Consider starting over

---

## Working with Existing Code

```
Add [feature] to existing project.

Stack: [React, Next.js, etc]
Patterns: Check src/components for examples
Style: Tailwind + custom design system
Follow existing code style
```

---

## Prompting Patterns

**Reference existing:**
```
Build Settings page.
Reference Dashboard page layout.
Use same Card/Button components.
```

**Provide examples:**
```
Pricing page with 3 tiers.
Like Linear's pricing - clean, minimal.
```

**Specify constraints:**
```
Build profile page.
Must work offline.
Load under 2 seconds.
WCAG AA accessible.
```

See [PROMPTS.md](PROMPTS.md) for more.

---

## Review for Non-Technical Founders

**Check:**
- Does it match spec?
- Buttons work?
- Forms validate?
- Looks like design reference?
- Works on mobile?
- Error messages clear?

**Don't check:**
- Code cleanliness
- Optimization
- "Best practices"

AI handles code quality. You handle requirements.

---

## Success Looks Like

✅ Features match specs  
✅ 2-4 iterations (not 10+)  
✅ Can explain what's wrong  
✅ Building faster each week
