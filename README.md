# Solo Founder Superpowers

43 expert skills for non-technical founders building SaaS with AI tools (Claude Code, Lovable, Replit, Cursor).

Covers the full lifecycle of planning, building, launching, and growing a software business — actionable guides, checklists, and copy-paste prompts.

## Installation

**Note:** Installation differs by platform. Claude Code or Cursor have built-in plugin marketplaces. Codex and OpenCode require manual setup.

### Claude Code (via Plugin Marketplace)

In Claude Code, register the marketplace first:

```
/plugin marketplace add whawkinsiv/solo-founder-superpowers
```

Then install the plugin from this marketplace:

```
/plugin install solo-founder-superpowers@solo-founder-superpowers-marketplace
```

### Cursor (via Plugin Marketplace)

In Cursor Agent chat, install from marketplace:

```
/plugin-add solo-founder-superpowers
```

### Verify Installation

Start a new session in your chosen platform and ask for something that should trigger a skill (for example, "help me validate this idea" or "help me plan this feature"). The agent should automatically invoke the relevant solo-founder-superpowers skill.

## What's Inside

### Development & Technical (10 skills)

| Skill | What It Covers |
|-------|----------------|
| **build** | AI-assisted dev workflows, tool selection (Claude Code, Lovable, Replit, Cursor) |
| **database** | Data modeling, schemas, relationships, Supabase/Firebase/Airtable setup |
| **integrations** | APIs, webhooks, Zapier/Make, connecting third-party services |
| **ai-features** | Adding AI/LLM capabilities to your product, cost management |
| **deploy** | Hosting selection, custom domains, environment variables, going live |
| **secure** | Security checklists, OWASP Top 10, auth and data protection |
| **test** | Test scenarios, edge cases, cross-browser testing |
| **debug** | Systematic debugging, error interpretation, diagnostics |
| **optimize** | Speed, code, database, and dependency optimization |
| **monitor** | Production monitoring, error alerts, incident response |

### Design & UX (5 skills)

| Skill | What It Covers |
|-------|----------------|
| **design** | Design systems, UI patterns, visual hierarchy, components, mobile-first |
| **brand** | Brand identity, color palettes, typography, logos, design tokens |
| **navigation** | App navigation, content hierarchy, menus, findability |
| **onboarding** | Onboarding flows, aha moments, activation rates, first-run UX |
| **accessibility** | WCAG compliance, ARIA, screen readers, keyboard navigation |

### SEO & Content (4 skills)

| Skill | What It Covers |
|-------|----------------|
| **seo** | Keyword research, content calendars, on-page optimization |
| **technical-seo** | SEO audits, Core Web Vitals, GEO for AI search engines |
| **content** | Content strategy, build in public, audience building, distribution |
| **copywriting** | Headlines, CTAs, button text, error messages, UI copy |

### Growth & Marketing (9 skills)

| Skill | What It Covers |
|-------|----------------|
| **launch** | Product Hunt, waitlists, beta programs, GTM sequencing |
| **landing-page** | Page structure, above-the-fold copy, conversion elements |
| **growth** | Product-led growth, viral loops, activation metrics, referrals |
| **conversion** | Funnel analysis, friction reduction, A/B testing |
| **email** | Email sequences, onboarding drips, behavioral triggers |
| **ads** | Google Ads, ad copy, keyword selection, CAC/LTV optimization |
| **sales** | Cold outreach, prospect lists, landing the first 100 customers |
| **social-media** | Platform-specific tactics: Twitter/X, LinkedIn, Reddit, short-form video |
| **community** | Discord/Slack communities, user forums, community-led growth |

### Strategy & Planning (8 skills)

| Skill | What It Covers |
|-------|----------------|
| **plan** | Turn ideas into buildable specs, MVPs, feature requirements |
| **validate** | Pre-build validation: smoke tests, fake door tests, concierge MVPs |
| **customer-research** | User interviews, JTBD framework, behavioral personas |
| **market-research** | Market sizing, competitor analysis, TAM/SAM/SOM |
| **pricing** | Pricing tiers, value metrics, psychology, monetization |
| **prioritize** | Feature prioritization, roadmaps, RICE scoring, MVP definition |
| **feedback** | Post-launch feedback collection, NPS, feature requests |
| **analytics** | Event tracking, funnels, key metrics, data quality |

### Business Operations (7 skills)

| Skill | What It Covers |
|-------|----------------|
| **legal** | Entity formation, ToS, Privacy Policy, compliance |
| **finances** | Financial models, unit economics, MRR/ARR/churn, burn rate |
| **accounting** | Bookkeeping, expense tracking, quarterly taxes, invoicing |
| **payments** | Stripe setup, subscriptions, billing, tax collection |
| **hiring** | Developer sourcing, vetting contractors, briefs, management |
| **support** | Help docs, knowledge bases, self-serve support |
| **retention** | Churn prevention, win-back campaigns, expansion revenue |

### Commands

| Command | What It Does |
|---------|-------------|
| **improve-prompt** | Transforms vague coding requests into detailed, specific prompts |

## How to Use

Skills are invoked automatically when Claude Code detects a relevant request, or manually:

```
/solo-founder-superpowers:plan
/solo-founder-superpowers:launch
/solo-founder-superpowers:payments
```

### Recommended workflow for a new product

```
1. Validate   — validate, customer-research, market-research
2. Plan       — plan, prioritize, pricing, finances
3. Design     — design, brand, navigation
4. Build      — build, database, integrations, secure, test, debug
5. Deploy     — deploy, payments
6. Launch     — launch, landing-page, copywriting
7. Grow       — growth, content, seo, email, ads, social-media
8. Retain     — onboarding, retention, support, feedback
9. Scale      — optimize, monitor, analytics, ai-features, hiring
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
