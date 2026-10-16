# Solo Founder Skills

Claude Code skills for a solo, bootstrapped founder who builds a software business alone.

The skills follow one order: **sell before you build**. Get the first 10 paying customers by hand, build the smallest version they need, ship it safely, then grow to 100.

## Install

In Claude Code:

```
/plugin marketplace add whawkinsiv/solo-founder-skills
/plugin install solo-founder@solo-founder-skills-marketplace
```

Not sure where to start? Ask "where do I start?" The `journey` skill finds your stage and names your next step.

### Upgrading from the `sf-*` plugins

Version 4 replaces the ten `sf-*` plugins with one plugin of 21 skills. Remove the old plugins, refresh the marketplace, and install `solo-founder`:

```
/plugin uninstall sf-core@solo-founder-skills-marketplace
/plugin uninstall sf-strategy@solo-founder-skills-marketplace
# repeat for each sf-* plugin you installed
/plugin marketplace update solo-founder-skills-marketplace
/plugin install solo-founder@solo-founder-skills-marketplace
```

Manual invocations change from `/sf-strategy:validate` to `/solo-founder:validate`.

## What's inside

| Stage | Skill | What it does |
|---|---|---|
| Start | **journey** | Finds your stage from paying customers, not code, and names the next step |
| Start | **focus** | Is this activity, purchase, or feature worth it? One verdict and a plan for this week |
| Start | **about-me** | Captures your writing voice in ABOUT-ME.md, so content sounds like you |
| Idea | **validate** | Finds a problem, tests demand with the cheapest experiment, scores the evidence, and gives a dated verdict |
| Idea | **is-this-an-app** | Decides what form the idea should take, including "no build at all" |
| Idea | **domain-name** | Names the product and checks domain availability |
| Sell | **pricing** | One simple price before 10 customers, tiers after |
| Sell | **landing-page** | A page that sells: one offer, one price, one action, real proof only |
| Sell | **email** | A branded address on your domain that lands in inboxes |
| Sell | **first-customers** | The first 10 paying customers by hand, then 100. Launch after 10, not before |
| Sell | **payments** | Payment links first, then Stripe Checkout, the customer portal, and webhooks |
| Build | **build** | Scopes the first version from what you already do by hand, then builds it one tested piece at a time |
| Build | **beautify** | Makes an AI-built app look designed, handle every UI state, and pass a design review |
| Ship | **secure** | Finds the security holes AI-built apps ship with, and fixes them |
| Ship | **go-live** | The go/no-go check: the core flow, payments, backups, alerts, and rollback |
| Grow | **content** | One platform, building in public, and writing in your own voice |
| Grow | **seo** | Audits your code for search and AI-answer visibility, then fixes it |
| Grow | **retention** | Onboarding, customer conversations, support, and cancellations, by hand first |
| Grow | **humanize** | Removes AI writing patterns without inventing facts |
| Run | **finances** | Your quit number, your runway, and whether the business survives without outside money |
| Run | **legal** | Entity, terms, privacy policy, and data rights, drafted for a lawyer to review |

Skills load automatically when your request matches them. You can also call one directly, for example `/solo-founder:validate`.

## Design rules

- **Each skill changes what Claude does.** A skill that would only repeat what Claude already knows does not ship.
- **Short.** Each SKILL.md has 150 lines or fewer. The detail goes into a reference file, only where the skill needs one.
- **Instructions to Claude, not prompts to paste.** You work inside Claude Code, and Claude does the work.
- **No vendor lock-in.** A skill names a vendor only when the vendor is the advice, as with Stripe for payments.

## Author

Will Hawkins ([@whawkinsiv](https://github.com/whawkinsiv)). MIT license.
