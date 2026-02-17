# Solo Founder Superpowers

A Claude Code plugin with 36 expert skills for non-technical founders building SaaS applications with AI tools (Claude Code, Lovable, Replit, Cursor).

Covers the full lifecycle of planning, building, launching, and growing a software business — all written as actionable guides, checklists, and copy-paste prompts.

## Prerequisites

You need [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and running. If you don't have it yet:

**Mac / Linux:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://claude.ai/install.ps1 | iex
```

Then run `claude` to launch it and log in with your Anthropic account (Pro, Max, Teams, or API with billing enabled).

> Plugins require Claude Code **v1.0.33+**. Check with `claude --version` and update if needed.

## Install

One command — run this inside Claude Code (at the `>` prompt):

```
/plugin install solo-founder-superpowers@claude-plugins-official
```

Or from a terminal:

```bash
claude plugin install solo-founder-superpowers@claude-plugins-official
```

### Verify it worked

```
/plugin
```

Go to the **Installed** tab — you should see `solo-founder-superpowers` listed. You can also test by typing `/solo-founder-superpowers:scope` in Claude Code.

### Updating

```bash
claude plugin update solo-founder-superpowers@claude-plugins-official
```

### Uninstalling

```bash
claude plugin uninstall solo-founder-superpowers@claude-plugins-official
```

## What's Inside

### Build Your Product (9 skills)

| Skill | What It Covers |
|-------|----------------|
| **scope** | Turn ideas into AI-ready specs (quick feature specs + full project scopes) |
| **design** | Design systems, UX patterns, Laws of UX, component libraries |
| **build** | AI-assisted dev workflows, tool selection (Claude Code, Lovable, Replit, Cursor) |
| **secure** | Security checklists, OWASP Top 10, auth and data protection |
| **optimize** | Speed, code, database, and dependency tuning |
| **test** | Test scenarios, edge cases, intentional bug hunting |
| **debug** | Systematic debugging, error interpretation |
| **monitor** | Production health, incident response, alerting |
| **deployment-going-live** | Hosting selection, custom domains, environment variables, going live |

### Launch & Grow (7 skills)

| Skill | What It Covers |
|-------|----------------|
| **launch-go-to-market** | Product Hunt, beta programs, waitlists, launch sequencing |
| **growth-plg** | Product-led growth, viral loops, activation metrics |
| **content-marketing-build-in-public** | Content strategy, build in public, audience building |
| **seo-content-strategy** | Keyword research, on-page SEO, content planning |
| **technical-seo-expert** | Technical SEO audits, Core Web Vitals, GEO for AI search |
| **paid-acquisition-ad-copy** | Google Ads, keyword selection, ad copy, small budgets |
| **founder-led-sales-outreach** | Cold outreach, prospect lists, landing the first 100 customers |

### Convert & Retain (6 skills)

| Skill | What It Covers |
|-------|----------------|
| **landing-page-strategy** | Page structure, above-the-fold copy, conversion elements |
| **onboarding-activation-design** | Aha moments, activation rates, first-run UX |
| **conversion-rate-optimization** | Funnel analysis, friction reduction, A/B testing |
| **email-lifecycle-marketing** | Welcome sequences, behavioral triggers, drip campaigns |
| **churn-prevention-retention** | At-risk identification, win-back campaigns, expansion revenue |
| **payments-billing-operations** | Stripe setup, subscriptions, tax, dunning, billing lifecycle |

### Product & Design (5 skills)

| Skill | What It Covers |
|-------|----------------|
| **ux-ui-design** | Visual hierarchy, interaction patterns, design systems |
| **information-architecture** | Navigation, content hierarchy, findability |
| **brand-identity-visual-design** | Color systems, typography, logo, visual consistency |
| **copywriting-microcopy** | Headlines, CTAs, button text, error messages, UI copy |
| **accessibility** | WCAG 2.2, ARIA patterns, screen readers, keyboard navigation |

### Strategy & Research (5 skills)

| Skill | What It Covers |
|-------|----------------|
| **product-strategy-prioritization** | RICE prioritization, MVP definition, roadmapping |
| **customer-research-personas** | Jobs-to-be-Done, user interviews, behavioral personas |
| **market-research-competitive-analysis** | Market sizing, TAM/SAM/SOM, competitive analysis |
| **pricing-monetization-strategy** | Pricing psychology, tier design, value metrics |
| **analytics-instrumentation** | Event tracking, funnels, key metrics, data quality |

### Business Operations (4 skills)

| Skill | What It Covers |
|-------|----------------|
| **saas-financial-modeling-metrics** | Unit economics, MRR/ARR/churn, burn rate, quit number |
| **saas-legal-business-formation** | LLC vs C-Corp, Terms of Service, Privacy Policy, compliance |
| **customer-support-documentation** | Help docs, knowledge base, self-serve support, scaling without hiring |
| **hiring-technical-help** | Contractor sourcing, vetting developers, briefs, management |

### Commands

| Command | What It Does |
|---------|-------------|
| **improve-prompt** | Transforms vague coding requests into detailed, specific prompts |

## How to Use

Skills are invoked automatically when Claude Code detects a relevant request, or manually:

```
/solo-founder-superpowers:scope
/solo-founder-superpowers:launch-go-to-market
/solo-founder-superpowers:payments-billing-operations
```

### Recommended workflow for a new product

```
1. Validate   — customer-research, market-research, product-strategy
2. Plan       — scope, saas-financial-modeling, pricing
3. Design     — design, ux-ui-design, brand-identity
4. Build      — build, secure, test, debug
5. Deploy     — deployment-going-live, payments-billing
6. Launch     — launch-go-to-market, landing-page, copywriting
7. Grow       — growth-plg, content-marketing, seo, email, paid-acquisition
8. Retain     — onboarding, churn-prevention, customer-support
9. Scale      — optimize, monitor, analytics, hiring-technical-help
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
