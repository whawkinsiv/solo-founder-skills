# Claude Code Skills for Non-Technical Founders

Complete software development lifecycle skills optimized for non-technical founders building SaaS applications with AI tools (Lovable, Replit, Claude Code).

---

## Complete Skill Set

### 1. Scope - Specification
**Purpose:** Turn ideas into AI-ready specs  
**Files:** 3 (663 lines total)
- SKILL.md (180 lines) - Overview and workflow
- QUICK-SPEC.md (195 lines) - 10-15 minute feature specs
- PROJECT-SCOPE.md (288 lines) - Full project scoping

**When to use:** Before building anything new

---

### 2. Design - User Experience
**Purpose:** UX/UI best practices for SaaS  
**Files:** 3 (1,106 lines total)
- SKILL.md (255 lines) - Core principles and workflow
- LAWSOFUX.md (333 lines) - Laws of UX reference
- COMPONENTS.md (518 lines) - SaaS component patterns

**When to use:** Planning UI, reviewing AI-built interfaces

---

### 3. Build - Development
**Purpose:** Effective AI-assisted development  
**Files:** 3 (438 lines total)
- SKILL.md (209 lines) - Build workflow and iteration
- TOOLS.md (111 lines) - Tool comparison matrix
- PROMPTS.md (118 lines) - Prompting patterns

**When to use:** Implementing features, iterating with AI

---

### 4. Security - Protection
**Purpose:** Protect app and users  
**Files:** 3 (860 lines total)
- SKILL.md (244 lines) - Security checklist and basics
- COMMON-VULNS.md (293 lines) - OWASP Top 10 simplified
- SECURITY-PROMPTS.md (323 lines) - Security implementation prompts

**When to use:** Building auth, handling data, pre-deployment

---

### 5. Performance - Speed
**Purpose:** Make it fast and responsive  
**Files:** 3 (1,223 lines total)
- SKILL.md (370 lines) - Performance targets and quick wins
- PERFORMANCE-CHECKS.md (396 lines) - Testing and measurement
- OPTIMIZATION-PROMPTS.md (457 lines) - Optimization patterns

**When to use:** App feels slow, before scaling

---

### 6. Test - Quality Assurance
**Purpose:** Test before users find bugs  
**Files:** 4 (1,699 lines total)
- SKILL.md (424 lines) - Testing workflow and checklist
- TEST-SCENARIOS.md (428 lines) - Common testing scenarios
- EDGE-CASES.md (371 lines) - Edge case testing list
- BREAKING-THINGS.md (476 lines) - Intentional bug hunting

**When to use:** Feature built, before deploying

---

### 7. Debug - Bug Fixing
**Purpose:** Fix bugs systematically  
**Files:** 4 (2,034 lines total)
- SKILL.md (476 lines) - Debug workflow and common issues
- DEBUG-CHECKLIST.md (505 lines) - Systematic debugging steps
- DEBUG-PROMPTS.md (521 lines) - Debugging prompts for AI
- ERROR-MESSAGES.md (532 lines) - Common error interpretation

**When to use:** Something breaks, users report issues

---

### 8. Monitor - Production Health
**Purpose:** Track app health, catch issues early  
**Files:** 3 (1,546 lines total)
- SKILL.md (463 lines) - Monitoring basics and daily routine
- MONITORING-SETUP.md (545 lines) - Setup instructions
- INCIDENT-RESPONSE.md (538 lines) - Handling alerts and incidents

**When to use:** After deployment, ongoing

---

## Skill Statistics

**Total:** 26 files, 9,569 lines

**By lifecycle phase:**
- Planning (Scope, Design): 1,769 lines
- Development (Build): 438 lines  
- Quality (Security, Performance, Test): 3,782 lines
- Operations (Debug, Monitor): 3,580 lines

**All SKILL.md files under 500 lines** ✓

---

## Design Principles

### 1. Progressive Disclosure
- SKILL.md = Quick reference and checklist
- Supporting files = Detailed patterns and examples
- Never more than 1 level deep from SKILL.md

### 2. Assumes Claude Intelligence
- No explaining basic concepts Claude knows
- Focus on context Claude doesn't have:
  - Non-technical founder perspective
  - Tool selection criteria
  - When to use vs not use
  - Common founder mistakes

### 3. Concise Over Comprehensive
- Every line must be essential
- Challenge: "Does Claude really need this?"
- Reference files can be longer if they contain:
  - Copy-pasteable code/commands
  - Comprehensive checklists
  - Multiple scenario examples

### 4. Actionable Focus
- Checklists over explanations
- Templates over theory
- "Tell AI:" prompts throughout
- Quick wins before complex solutions

---

## Using the Skills

### Basic Workflow

```
1. Scope: Write feature spec (10-15 min)
2. Design: Reference UX patterns (as needed)
3. Build: Give spec to AI, iterate (1-3 hours)
4. Security: Check security checklist (15 min)
5. Performance: Quick performance check (5 min)
6. Test: Test happy path + edge cases (15 min)
7. Debug: Fix any issues found (varies)
8. Monitor: Set up monitoring (if first deploy)
```

### For MVPs

**Minimum viable workflow:**
- Scope: Quick spec only
- Build: Focus on happy path
- Security: Basic checklist
- Test: Happy path + 3-4 edge cases
- Monitor: Uptime + errors only

**Skip/minimize for MVP:**
- Performance optimization (unless actually slow)
- Comprehensive edge case testing
- Advanced monitoring

### For Production Apps

**Full workflow:**
- All skills used
- Comprehensive testing
- Full monitoring stack
- Regular performance reviews

---

## Skill Cross-References

### Common Flows

**New Feature:**
1. Scope → Design → Build → Test → Deploy

**Bug Report:**
1. Debug → Test (verify fix) → Monitor (ensure no recurrence)

**Performance Issue:**
1. Monitor (detect) → Performance → Test → Deploy

**Security Concern:**
1. Security → Test → Monitor (verify no issues)

**Pre-Launch:**
1. Scope (all features) → Security → Performance → Test → Monitor setup

---

## Tool Integration

### Claude Code
- Use Build skill for feature development
- Use Debug skill for systematic fixes
- Reference all skills via file paths

### Lovable
- Use Scope skill for detailed specs
- Use Design skill for component patterns
- Use Build skill for iteration patterns

### Replit
- Use Build skill (simplified approach)
- Use Test skill for manual testing
- Use Debug skill for console errors

---

## Success Metrics

**You're using these skills effectively when:**

✅ **Scope:** AI builds closer to spec on first try  
✅ **Design:** Users say "this looks professional"  
✅ **Build:** Features work in 2-4 iterations (not 10+)  
✅ **Security:** No secrets in code, auth works properly  
✅ **Performance:** Pages load <3s, APIs respond <500ms  
✅ **Test:** Catching bugs before users report them  
✅ **Debug:** Fixing bugs on first or second attempt  
✅ **Monitor:** Knowing about issues before users complain  

---

## Common Patterns Across Skills

### 1. Checklist-First
Every skill starts with actionable checklist

### 2. "Tell AI" Prompts
Specific prompts to copy-paste to AI tools

### 3. Common Mistakes
What founders typically get wrong

### 4. When Not To Use
Prevents premature optimization

### 5. Free Tools
Focus on $0-30/month tools for MVPs

---

## Quick Reference by Situation

**"I have an idea"** → Scope  
**"How should this look?"** → Design  
**"Build this feature"** → Build  
**"Is this secure?"** → Security  
**"Why is it slow?"** → Performance  
**"Does it work?"** → Test  
**"Something broke"** → Debug  
**"Is production healthy?"** → Monitor  

---

## File Naming Convention

All skills follow consistent pattern:
- `SKILL.md` - Main overview (always under 500 lines)
- `[TOPIC].md` - Supporting reference files
- ALL CAPS with hyphens for multi-word

Examples:
- `QUICK-SPEC.md` not `quick-spec.md`
- `DEBUG-PROMPTS.md` not `debug_prompts.md`

---

## Version Info

**Created:** January 2025  
**Target Audience:** Non-technical founders  
**Tools:** Claude Code, Lovable, Replit, Cursor  
**Format:** Markdown optimized for Claude Code skills system  

**Philosophy:** 
Make building software with AI accessible to founders without coding backgrounds by providing systematic workflows, avoiding premature optimization, and focusing on shipping working products.
