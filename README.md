# Solo Founder Skills

Expert skills for non-technical founders building SaaS with AI tools (Claude Code, Lovable, Replit, Cursor).

Covers the full lifecycle of planning, building, launching, and growing a software business — actionable guides, checklists, and copy-paste prompts. The skills ship as 10 focused plugins, so you install only what you need.

## Installation

**Note:** These skills use the [Agent Skills](https://agentskills.io) open format, so they work in Claude Code, Codex, Cursor, Gemini CLI, Copilot and other agents that read it. Only the install step differs. Claude Code and Cursor have built-in plugin marketplaces. Everything else uses `install.sh`.

**Install the plugins you need, not all of them.** Agents load every installed skill's name and description at startup. Codex caps that list at 2% of the model's context window, or 8,000 characters when it cannot tell — past the cap it shortens descriptions and can leave skills out. All 61 skills total about 25,000 characters. Any single plugin fits comfortably.

### Claude Code (via Plugin Marketplace)

Register the marketplace, then install `sf-core` first:

```
/plugin marketplace add whawkinsiv/solo-founder-skills
/plugin install sf-core@solo-founder-skills-marketplace
```

`sf-core` holds the `journey` and `next` skills. They tell you which plugin to install for each step.

Then install the plugins for the work you are doing now:

| Plugin | The job it does | Install |
|--------|-----------------|---------|
| **sf-core** | Orientation and routing. Install this first. | `/plugin install sf-core@solo-founder-skills-marketplace` |
| **sf-strategy** | Turn an idea into a buildable spec. | `/plugin install sf-strategy@solo-founder-skills-marketplace` |
| **sf-design** | Make it look and feel right. | `/plugin install sf-design@solo-founder-skills-marketplace` |
| **sf-build** | Write and fix the code. | `/plugin install sf-build@solo-founder-skills-marketplace` |
| **sf-ship** | Get it live and keep it up. | `/plugin install sf-ship@solo-founder-skills-marketplace` |
| **sf-copy** | Write the words. | `/plugin install sf-copy@solo-founder-skills-marketplace` |
| **sf-seo** | Rank in search and get cited by AI. | `/plugin install sf-seo@solo-founder-skills-marketplace` |
| **sf-channels** | Reach people. | `/plugin install sf-channels@solo-founder-skills-marketplace` |
| **sf-customers** | Win and keep customers. | `/plugin install sf-customers@solo-founder-skills-marketplace` |
| **sf-business** | Run the company. | `/plugin install sf-business@solo-founder-skills-marketplace` |

Why separate plugins? Claude Code loads the description of every installed skill into every session. Fewer installed skills means less context used and fewer wrong skills competing for the same request.

#### Upgrading from the single `solo-founder-skills` plugin

Version 3 was one plugin with every skill in it. That plugin no longer exists. Remove it, refresh the marketplace, then install the plugins you want:

```
/plugin uninstall solo-founder-skills@solo-founder-skills-marketplace
/plugin marketplace update solo-founder-skills-marketplace
/plugin install sf-core@solo-founder-skills-marketplace
```

Manual skill invocations changed. Replace `/solo-founder-skills:plan` with `/sf-strategy:plan`. The table under "What's Inside" shows the plugin for each skill.

#### Upgrading from Solo Founder Superpowers

Remove the old install and the old marketplace first, then follow the install steps above:

```
/plugin uninstall solo-founder-superpowers@solo-founder-superpowers-marketplace
/plugin marketplace remove solo-founder-superpowers-marketplace
```

### Cursor (via Plugin Marketplace)

In Cursor Agent chat, install from marketplace:

```
/plugin-add solo-founder-skills
```

### Codex

Codex reads personal skills from `~/.codex/skills/` and project skills from `.codex/skills/` and `.agents/skills/`. Clone the repo, then run `install.sh` with the plugins you want:

```
git clone https://github.com/whawkinsiv/solo-founder-skills.git
cd solo-founder-skills
./install.sh --list                          # see the plugins
./install.sh --codex sf-core sf-strategy     # into ~/.codex/skills/
```

Use `--agents` instead to install into `./.agents/skills/` in the current project.

The script prints the startup description cost and warns you when it goes over the cap. Add plugins as you need them — run it again with more names.

To install one skill only, use the built-in installer:

```
$skill-installer install https://github.com/whawkinsiv/solo-founder-skills/tree/main/plugins/sf-build/skills/build
```

Restart Codex after installing. Invoke skills with `$skill-name` or let Codex select them automatically.

### OpenCode and other agents

OpenCode reads skills from `.opencode/skills/`, `~/.config/opencode/skills/`, or `~/.agents/skills/`. Point `install.sh` at whichever one you use:

```
git clone https://github.com/whawkinsiv/solo-founder-skills.git
cd solo-founder-skills
./install.sh --dest .opencode/skills sf-core sf-strategy
```

`--dest` takes any path, so the same command works for any agent that reads a folder of skills. Skills load on demand: the agent sees their names and descriptions, and reads the full instructions only when it picks one.

### Verify Installation

Start a new session in your chosen platform and ask for something that should trigger a skill (for example, "where do I start?" or "help me plan this feature"). The agent should automatically invoke the relevant skill.

## What's Inside

### sf-core — Start here (6 skills)

| Skill | What It Covers |
|-------|----------------|
| **journey** | Where to start, what order to do things, the path from idea to launch |
| **next** | What to work on next, finding high-value opportunities |
| **about-me** | Founder profile and voice setup so other skills produce personalized output |
| **focus** | 80/20 analysis, deciding if an activity is worth your time |
| **prioritize** | Feature prioritization, roadmaps, RICE scoring |
| **glossary** | Plain-English explanations of 50+ technical terms |

### sf-strategy — Strategy & Validation (8 skills)

| Skill | What It Covers |
|-------|----------------|
| **translate** | Turn professional expertise into a software product |
| **validate** | Smoke tests, fake door tests, testing demand before you build |
| **is-this-an-app** | Decide what form an idea should take (web app, extension, automation, agent skill, or no build) before you build it |
| **customer-research** | User interviews, Jobs-to-be-Done, ideal customer profile |
| **market-research** | Market sizing, competitor analysis, TAM/SAM/SOM |
| **niche-advantage** | Use domain expertise as a competitive moat |
| **plan** | Turn ideas into buildable specs, MVPs, feature requirements |
| **domain-name** | Judge domain name ideas for a product and check whether they are available |

### sf-design — Design & UX (6 skills)

| Skill | What It Covers |
|-------|----------------|
| **brand-identity-generator** | Generates a full BRAND-IDENTITY.md: colors, type, spacing, components |
| **ux-design** | Information architecture, user flows, onboarding, accessibility |
| **ui-patterns** | Dashboards, data tables, settings pages, component libraries, dark mode |
| **beautify** | Visual hierarchy, whitespace, composition, color, typography |
| **motion-polish** | Animations, micro-interactions, smooth transitions |
| **design-review** | Design audit and quality gate before you ship |

### sf-build — Build (7 skills)

| Skill | What It Covers |
|-------|----------------|
| **build** | AI-assisted dev workflows, tool selection (Claude Code, Lovable, Replit, Cursor) |
| **database** | Schema design, Supabase setup, Row Level Security, migrations |
| **integrations** | APIs, OAuth, webhooks, connecting third-party services |
| **ai-features** | LLM APIs, RAG, AI assistants, cost management |
| **debug** | Systematic debugging, error interpretation, diagnostics |
| **dry** | Find and remove duplication across code, schema, and workflows |
| **optimize** | Speed, bundle size, database, and hosting cost optimization |

### sf-ship — Ship & Operate (7 skills)

| Skill | What It Covers |
|-------|----------------|
| **test** | Test scenarios, edge cases, cross-browser testing |
| **secure** | Authentication, data protection, API security, vulnerability checks |
| **compliance** | HIPAA, SOC 2, GDPR, PCI, FERPA for regulated industries |
| **go-live** | Pre-launch go/no-go checklist — the gate before you deploy |
| **deploy** | Hosting selection, custom domains, DNS, environment variables |
| **monitor** | Production monitoring, error alerts, incident response |
| **analytics** | Event tracking, funnels, key metrics, data quality |

### sf-copy — Copy (4 skills)

| Skill | What It Covers |
|-------|----------------|
| **copywriting** | Headlines, CTAs, button text, error messages, UI copy |
| **prose-writing** | Founder essays, blog posts, About pages, origin stories |
| **humanize** | Remove AI writing patterns so copy reads as human-written |
| **landing-page** | Page structure, above-the-fold copy, conversion elements |

### sf-seo — SEO (4 skills)

| Skill | What It Covers |
|-------|----------------|
| **seo** | Keyword research, content calendars, search intent mapping |
| **seo-content** | Blog posts, comparison pages, how-to guides built to rank |
| **seo-audit** | Codebase SEO audit with a prioritized fix-it plan |
| **technical-seo** | Meta tags, schema markup, Core Web Vitals, GEO for AI search |

### sf-channels — Channels (6 skills)

| Skill | What It Covers |
|-------|----------------|
| **launch** | Product Hunt, waitlists, beta programs, go-to-market sequencing |
| **content** | Content strategy, build in public, audience building, distribution |
| **social-media** | Twitter/X, LinkedIn, Reddit, founder brand building |
| **email** | Onboarding drips, welcome sequences, behavioral triggers |
| **ads** | Google Ads, ad copy, keyword selection, CAC/LTV |
| **community** | Discord and Slack communities, forums, community-led growth |

### sf-customers — Customers (6 skills)

| Skill | What It Covers |
|-------|----------------|
| **growth** | Product-led growth, viral loops, activation metrics |
| **conversion** | Funnel analysis, friction reduction, A/B testing |
| **retention** | Churn prevention, win-back campaigns, expansion revenue |
| **sales** | Cold outreach, prospect lists, landing the first 100 customers |
| **support** | Help docs, knowledge bases, self-serve support |
| **feedback** | Surveys, NPS, feature requests, closing the feedback loop |

### sf-business — Business & Money (6 skills)

| Skill | What It Covers |
|-------|----------------|
| **pricing** | Pricing tiers, value metrics, psychology, monetization |
| **payments** | Stripe setup, subscriptions, billing, failed payments, tax |
| **finances** | Financial models, unit economics, MRR/ARR/churn, burn rate |
| **accounting** | Bookkeeping, expense tracking, quarterly taxes, invoicing |
| **legal** | Entity formation, Terms of Service, Privacy Policy, compliance |
| **hiring** | Developer sourcing, vetting contractors, briefs, management |

### Commands

| Command | Plugin | What It Does |
|---------|--------|-------------|
| **improve-prompt** | sf-core | Transforms vague coding requests into detailed, specific prompts |

## How to Use

Skills are invoked automatically when Claude Code detects a relevant request, or manually with `/<plugin>:<skill>`:

```
/sf-strategy:plan
/sf-channels:launch
/sf-business:payments
```

### Recommended workflow for a new product

```
0. Orient    — journey, about-me, glossary
1. Validate  — validate, customer-research, market-research, focus, domain-name
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
