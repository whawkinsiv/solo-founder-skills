# Solo Founder Skills

59 expert skills for non-technical founders building SaaS with AI tools (Claude Code, Lovable, Replit, Cursor).

Covers the full lifecycle of planning, building, launching, and growing a software business — actionable guides, checklists, and copy-paste prompts.

## Installation

**Note:** Installation differs by platform. Claude Code or Cursor have built-in plugin marketplaces. Codex and OpenCode require manual setup.

### Claude Code (via Plugin Marketplace)

In Claude Code, register the marketplace first:

```
/plugin marketplace add whawkinsiv/solo-founder-skills
```

Then install the plugin from this marketplace:

```
/plugin install solo-founder-skills@solo-founder-skills-marketplace
```

#### Upgrading from Solo Founder Superpowers

This plugin was renamed. The old plugin and marketplace names no longer exist, so
an existing install stops loading after an update. Remove the old install first:

```
/plugin uninstall solo-founder-superpowers@solo-founder-superpowers-marketplace
/plugin marketplace remove solo-founder-superpowers-marketplace
```

Then add the new marketplace and install the plugin with the commands above.

Manual skill invocations also changed. Replace `/solo-founder-superpowers:plan`
with `/solo-founder-skills:plan`.

### Cursor (via Plugin Marketplace)

In Cursor Agent chat, install from marketplace:

```
/plugin-add solo-founder-skills
```

### Codex (Manual Setup)

Codex discovers skills from `.agents/skills/` directories. Clone this repo into your project:

```
git clone https://github.com/whawkinsiv/solo-founder-skills.git .agents/skills/solo-founder-skills
```

Or install a single skill using the built-in skill installer:

```
$skill-installer install https://github.com/whawkinsiv/solo-founder-skills/tree/main/skills/build
```

Restart Codex after installing. Invoke skills with `$skill-name` or let Codex select them automatically.

### OpenCode (Manual Setup)

OpenCode discovers skills from `.opencode/skills/`, `~/.config/opencode/skills/`, or `~/.agents/skills/`. Clone into any of these locations:

```
git clone https://github.com/whawkinsiv/solo-founder-skills.git .opencode/skills/solo-founder-skills
```

Skills are loaded on-demand — OpenCode will show available skills and load them when relevant.

### Verify Installation

Start a new session in your chosen platform and ask for something that should trigger a skill (for example, "help me validate this idea" or "help me plan this feature"). The agent should automatically invoke the relevant solo-founder-skills skill.

## What's Inside

### Getting Started (4 skills)

| Skill | What It Covers |
|-------|----------------|
| **journey** | Where to start, what order to do things, the path from idea to launch |
| **about-me** | Founder profile and voice setup so other skills produce personalized output |
| **glossary** | Plain-English explanations of 50+ technical terms |
| **next** | What to work on next, finding high-value opportunities |

### Strategy & Validation (8 skills)

| Skill | What It Covers |
|-------|----------------|
| **validate** | Smoke tests, fake door tests, testing demand before you build |
| **customer-research** | User interviews, Jobs-to-be-Done, ideal customer profile |
| **market-research** | Market sizing, competitor analysis, TAM/SAM/SOM |
| **translate** | Turn professional expertise into a software product |
| **niche-advantage** | Use domain expertise as a competitive moat |
| **focus** | 80/20 analysis, deciding if an activity is worth your time |
| **plan** | Turn ideas into buildable specs, MVPs, feature requirements |
| **prioritize** | Feature prioritization, roadmaps, RICE scoring |

### Design & UX (6 skills)

| Skill | What It Covers |
|-------|----------------|
| **ux-design** | Information architecture, user flows, onboarding, accessibility |
| **ui-patterns** | Dashboards, data tables, settings pages, component libraries, dark mode |
| **beautify** | Visual hierarchy, whitespace, composition, color, typography |
| **brand-identity-generator** | Generates a full BRAND-IDENTITY.md: colors, type, spacing, components |
| **motion-polish** | Animations, micro-interactions, smooth transitions |
| **design-review** | Design audit and quality gate before you ship |

### Build & Technical (10 skills)

| Skill | What It Covers |
|-------|----------------|
| **build** | AI-assisted dev workflows, tool selection (Claude Code, Lovable, Replit, Cursor) |
| **database** | Schema design, Supabase setup, Row Level Security, migrations |
| **integrations** | APIs, OAuth, webhooks, connecting third-party services |
| **ai-features** | LLM APIs, RAG, AI assistants, cost management |
| **secure** | Authentication, data protection, API security, vulnerability checks |
| **test** | Test scenarios, edge cases, cross-browser testing |
| **debug** | Systematic debugging, error interpretation, diagnostics |
| **dry** | Find and remove duplication across code, schema, and workflows |
| **optimize** | Speed, bundle size, database, and hosting cost optimization |
| **compliance** | HIPAA, SOC 2, GDPR, PCI, FERPA for regulated industries |

### Ship & Operate (4 skills)

| Skill | What It Covers |
|-------|----------------|
| **go-live** | Pre-launch go/no-go checklist — the gate before you deploy |
| **deploy** | Hosting selection, custom domains, DNS, environment variables |
| **monitor** | Production monitoring, error alerts, incident response |
| **analytics** | Event tracking, funnels, key metrics, data quality |

### Launch & Growth (9 skills)

| Skill | What It Covers |
|-------|----------------|
| **launch** | Product Hunt, waitlists, beta programs, go-to-market sequencing |
| **landing-page** | Page structure, above-the-fold copy, conversion elements |
| **growth** | Product-led growth, viral loops, activation metrics |
| **conversion** | Funnel analysis, friction reduction, A/B testing |
| **sales** | Cold outreach, prospect lists, landing the first 100 customers |
| **ads** | Google Ads, ad copy, keyword selection, CAC/LTV |
| **email** | Onboarding drips, welcome sequences, behavioral triggers |
| **social-media** | Twitter/X, LinkedIn, Reddit, founder brand building |
| **community** | Discord and Slack communities, forums, community-led growth |

### Content & SEO (8 skills)

| Skill | What It Covers |
|-------|----------------|
| **seo** | Keyword research, content calendars, search intent mapping |
| **seo-content** | Blog posts, comparison pages, how-to guides built to rank |
| **seo-audit** | Codebase SEO audit with a prioritized fix-it plan |
| **technical-seo** | Meta tags, schema markup, Core Web Vitals, GEO for AI search |
| **content** | Content strategy, build in public, audience building, distribution |
| **copywriting** | Headlines, CTAs, button text, error messages, UI copy |
| **prose-writing** | Founder essays, blog posts, About pages, origin stories |
| **humanize** | Remove AI writing patterns so copy reads as human-written |

### Customers & Retention (3 skills)

| Skill | What It Covers |
|-------|----------------|
| **retention** | Churn prevention, win-back campaigns, expansion revenue |
| **support** | Help docs, knowledge bases, self-serve support |
| **feedback** | Surveys, NPS, feature requests, closing the feedback loop |

### Business & Money (6 skills)

| Skill | What It Covers |
|-------|----------------|
| **pricing** | Pricing tiers, value metrics, psychology, monetization |
| **payments** | Stripe setup, subscriptions, billing, failed payments, tax |
| **finances** | Financial models, unit economics, MRR/ARR/churn, burn rate |
| **accounting** | Bookkeeping, expense tracking, quarterly taxes, invoicing |
| **legal** | Entity formation, Terms of Service, Privacy Policy, compliance |
| **hiring** | Developer sourcing, vetting contractors, briefs, management |

### Meta (1 skill)

| Skill | What It Covers |
|-------|----------------|
| **improve** | Autonomously improves any other skill in this plugin through A/B evaluation |
### Commands

| Command | What It Does |
|---------|-------------|
| **improve-prompt** | Transforms vague coding requests into detailed, specific prompts |

## How to Use

Skills are invoked automatically when Claude Code detects a relevant request, or manually:

```
/solo-founder-skills:plan
/solo-founder-skills:launch
/solo-founder-skills:payments
```

### Recommended workflow for a new product

```
0. Orient    — journey, about-me, glossary
1. Validate  — validate, customer-research, market-research, focus
2. Plan      — plan, prioritize, pricing, finances
3. Design    — brand-identity-generator, ux-design, ui-patterns, beautify
4. Build     — build, database, integrations, secure, test, debug
5. Ship      — design-review, go-live, deploy, payments
6. Launch    — launch, landing-page, copywriting, humanize
7. Grow      — growth, content, seo, seo-content, email, ads, social-media
8. Retain    — retention, support, feedback, conversion
9. Scale     — optimize, dry, monitor, analytics, ai-features, hiring
```

## Design Philosophy

These skills assume Claude's intelligence — they focus on:

- **Non-technical founder perspective** and common mistakes
- **Tool selection criteria** (when to use Lovable vs Claude Code vs Replit)
- **Actionable checklists** and "Tell AI:" copy-paste prompts
- **What's out of scope** (preventing premature optimization)
- Concise, actionable content that avoids explaining concepts Claude already knows

## Author

Will Hawkins ([@whawkinsiv](https://github.com/whawkinsiv))
