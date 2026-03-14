# GTM Skill — Design Spec

## Overview

A strategic orchestrator skill that helps solo founders choose a go-to-market model, define positioning, and sequence their plan-validate-build-launch-grow phases into a concrete playbook. Produces a GTM Playbook document through an interactive decision-tree workflow.

The skill is a **strategist, not an executor**. It connects positioning decisions to tactical execution by routing founders to the right existing skills (`launch`, `sales`, `growth`, `content`, `ads`, `pricing`, `landing-page`, `email`, `social-media`) at the right time.

## Skill Identity

- **Directory:** `skills/gtm/`
- **Name (frontmatter):** `gtm`
- **Description (frontmatter):** "Use this skill when the user needs a go-to-market strategy, wants to choose between PLG/content/sales/community-led approaches, needs to sequence their plan-validate-build-launch-grow phases, or wants to connect positioning decisions to tactical execution across channels."

### Persona

SKILL.md should open with: "Act as a top 1% go-to-market strategist who has launched 50+ SaaS products and knows that distribution beats product every time. You help solo founders pick the right GTM model, define sharp positioning, and sequence their moves so nothing is wasted."

### Core Principles

SKILL.md should include these core principles after the persona:

1. **Positioning first, tactics second** — Every channel, message, and price decision flows from your position. Get this right or everything downstream is noise.
2. **Match the model to the founder** — The best GTM strategy is one you'll actually execute. Your strengths matter more than best practices.
3. **One channel until it works** — Prove one acquisition channel before adding another. Spreading thin is the #1 GTM killer for solo founders.
4. **Exit criteria, not timelines** — Move to the next phase when the milestones say so, not the calendar.
5. **Pivot signals > sunk costs** — If it's not working after a real effort, change the model. Don't double down on a losing strategy because you already started.

### When to Use

- Before starting any go-to-market activity
- When you have a product idea but no distribution plan
- When you've built something but don't know how to get users
- When your current approach isn't working and you need to rethink

### When NOT to Use

- For launch week tactics (use `launch`)
- For specific channel execution (use `ads`, `content`, `sales`, etc.)
- For market sizing or competitive analysis (use `market-research`)
- When you don't have a product idea yet — GTM requires at least a rough concept of what you're selling and to whom

### Relationship to Existing Skills

GTM is the strategic layer that sits above tactical skills. It does not duplicate them.

| Skill | Relationship |
|-------|-------------|
| `launch` | GTM sequences when to launch and why; `launch` handles launch week execution |
| `sales` | GTM decides if sales-led is your model; `sales` handles outreach tactics |
| `growth` | GTM decides if PLG is your model; `growth` handles viral loops and activation |
| `content` | GTM decides if content-led is your model; `content` handles content creation |
| `ads` | GTM decides if/when to add paid; `ads` handles campaign execution |
| `pricing` | GTM informs pricing positioning; `pricing` handles tier design |
| `landing-page` | GTM cascades positioning into messaging direction; `landing-page` handles page structure |
| `email` | GTM sequences when email enters the mix; `email` handles drip design |
| `social-media` | GTM decides channel priority; `social-media` handles posting strategy |
| `market-research` | GTM uses market insights for positioning; `market-research` handles the research itself |
| `validate` | GTM defines validation criteria for the chosen model; `validate` handles validation execution |
| `analytics` | GTM defines which metrics matter per phase; `analytics` handles instrumentation |

---

## Interactive Workflow

The skill walks founders through four decision stages before producing a strategy document. Each stage is completed as a separate conversation turn — Claude asks the stage's questions, waits for answers, summarizes what it heard, then moves to the next stage.

### Interaction Protocol

1. Claude presents one stage at a time with its questions
2. Founder answers (can be brief or detailed)
3. Claude summarizes what it understood and confirms before proceeding
4. At Stage 3 (model selection), Claude presents its recommendation with reasoning — founder can accept or override
5. After Stage 4, Claude generates the full GTM Playbook document

If the founder gives short answers, Claude should probe ("Tell me more about..." or "When you say X, do you mean..."). If answers are thorough, move on. The goal is enough signal to make a good recommendation, not an interrogation.

### Stage 1: Founder Profile

Quick self-assessment (3-5 questions):

- What are you comfortable doing? (writing, sales calls, building in public, community management)
- Do you have an existing audience or network in this market?
- What's your runway / time commitment?
- Are you technical or using AI tools to build?

Purpose: Weight GTM model recommendations toward what the founder can actually execute. A technical founder who can write but hates sales calls gets a content-led playbook, not a cold outreach plan.

### Stage 2: Positioning

- Who is this for? (specific buyer, not "everyone")
- What's the alternative they use today? (competitor, manual process, nothing)
- What's your angle? (simpler, cheaper, specialized, modern, integrated)
- Output: One-sentence position statement — "[Product] is the [angle] [category] for [buyer]"

Purpose: Every downstream decision (model, channels, messaging, pricing) flows from positioning. Get this right first.

### Stage 3: GTM Model Selection

Based on Stages 1 + 2, recommend a primary model. See [GTM-MODELS.md](GTM-MODELS.md) for detailed model reference.

| Model | Signals That Point Here |
|-------|------------------------|
| Product-led (PLG) | Low price, self-serve, founder is technical, product has viral hooks |
| Content-led | Founder can write/teach, longer sales cycle, expertise-driven market |
| Sales-led | Higher price point, B2B, founder has sales experience or network |
| Community-led | Network effects, niche market, founder enjoys community building |
| Hybrid | Clear signals for two models, enough bandwidth to execute both |

Present recommendation with reasoning. Let the founder override if they disagree — but explain the tradeoffs.

### Stage 4: Phase Sequencing

Map the five phases to the chosen model, with exit criteria for each. See [PHASE-PLAYBOOK.md](PHASE-PLAYBOOK.md) for model-specific phase details.

| Phase | Exit Criteria |
|-------|---------------|
| Plan | Position statement defined, GTM model chosen, first 3 channels identified |
| Validate | Problem confirmed with 10+ target users, willingness to pay signal |
| Build | Core product works, landing page live, tracking in place |
| Launch | First paying users acquired, primary channel producing leads |
| Grow | Repeatable acquisition channel, unit economics positive |

Phases are not time-bound. Move to the next phase when you hit the exit criteria, not when the calendar says so. A founder with a hot product might blast through in 6 weeks; another might spend 3 months in Plan + Validate.

---

## Phase-to-Skill Mapping

Each phase maps to specific plugin skills. The GTM model determines emphasis.

| Phase | Primary Skills | What GTM Adds |
|-------|---------------|---------------|
| Plan | `plan`, `market-research`, `pricing` | Positioning framework, model selection, channel architecture |
| Validate | `validate`, `customer-research` | Validation criteria tailored to chosen GTM model |
| Build | `build`, `landing-page`, `pricing` | Position-to-execution mapping (messaging cascades from positioning) |
| Launch | `launch`, `sales`, `ads`, `email` | Sequencing logic, channel mix based on model, milestone gates |
| Grow | `growth`, `content`, `social-media`, `analytics` | When to double down vs. add channels, model pivot signals |

---

## GTM Models — Detail

### Product-Led (PLG)

- **Channel priority:** Product virality, freemium/free trial, SEO, integrations
- **Founder focus:** Build a product so good it sells itself; invest in onboarding and activation
- **Key metric per phase:** Plan: none. Validate: signup intent. Build: activation rate. Launch: free-to-paid conversion. Grow: viral coefficient.
- **Example companies:** Calendly, Notion, Canva

### Content-Led

- **Channel priority:** Blog/SEO, social media (written), email newsletter, educational content
- **Founder focus:** Become the expert voice in your niche; teach your way to customers
- **Key metric per phase:** Plan: none. Validate: content engagement. Build: email list size. Launch: content-to-trial conversion. Grow: organic traffic growth.
- **Example companies:** Basecamp, Buffer, Ahrefs

### Sales-Led

- **Channel priority:** Outbound email, LinkedIn, referrals, partnerships
- **Founder focus:** Talk to prospects directly; close deals through relationships
- **Key metric per phase:** Plan: none. Validate: meeting acceptance rate. Build: pipeline value. Launch: close rate. Grow: deal size expansion.
- **Example companies:** Close, PandaDoc, Salesforce (early days)

### Community-Led

- **Channel priority:** Forums, Discord/Slack, events, user-generated content
- **Founder focus:** Build a space where your users connect with each other, not just with you
- **Key metric per phase:** Plan: none. Validate: community join rate. Build: active member count. Launch: community-to-customer conversion. Grow: member-driven acquisition.
- **Example companies:** Figma, Discord, Notion (community layer)

### Hybrid

- Combines two models (e.g., PLG + sales-assist, content-led + community-led)
- Only recommended when: founder has bandwidth for both, and there are clear signals for two models
- Risk: spreading too thin. The skill should warn against hybrid unless signals are strong.

---

## Strategy Document Output

After the interactive workflow, the skill produces a GTM Playbook. Claude should instruct the user: "I'll save your GTM Playbook. Where would you like it? (default: `docs/gtm-playbook.md`)" If the target directory doesn't exist, create it.

### "Tell AI:" Prompts

Since GTM is a strategist skill, it does not include "Tell AI:" prompts for channel execution (those live in the tactical skills). Instead, each phase in the playbook includes a "Next step" directive pointing to the right skill:

```
Next step: Run the `launch` skill to plan your launch week.
```

For positioning work that happens within GTM itself, the playbook includes "Tell AI:" prompts for refining the position statement:

```
Tell AI:
  Review my position statement: "[Product] is the [angle] [category]
  for [buyer]." Pressure-test it: Is the buyer specific enough?
  Is the angle defensible? Would a competitor's customer understand
  why mine is different? Suggest 2-3 sharper alternatives.
```

### Playbook Template

```
## Your GTM Playbook

### Positioning
- Target buyer: [specific persona]
- Alternative they use today: [competitor/manual process]
- Your angle: [simpler/cheaper/specialized/etc.]
- Position statement: "[Product] is the [angle] [category] for [buyer]"

### GTM Model: [Primary model]
Why this fits: [2-3 sentences linking founder profile + product + market]

### Phase Plan

#### Phase 1: Plan
- [ ] Define position statement (done above)
- [ ] Run `market-research` skill to validate market size
- [ ] Run `pricing` skill to set initial pricing
- [ ] Identify primary + 1-2 supporting channels
- Exit criteria: Position defined, model chosen, channels identified
- Next step: Run the `validate` skill

#### Phase 2: Validate
- [ ] Identify 20 target users to talk to
- [ ] Run `customer-research` skill for interview framework
- [ ] Test willingness to pay (pre-sell, waitlist with payment intent, or landing page with pricing)
- [ ] Document what you learned — confirm or revise positioning
- Exit criteria: Problem confirmed with 10+ users, willingness to pay signal
- Gut check: "Do 10+ people want this?" If no → pivot the idea or kill it.
- Next step: Run the `build` skill

#### Phase 3: Build
- [ ] Build core product (MVP only — what proves the value prop)
- [ ] Run `landing-page` skill — messaging cascades from your position statement
- [ ] Run `analytics` skill to set up tracking
- [ ] Run `pricing` skill to finalize pricing tiers
- Exit criteria: Product works, landing page live, tracking in place
- Next step: Run the `launch` skill

#### Phase 4: Launch
- [ ] Run `launch` skill for launch week execution
- [ ] Activate primary channel: [model-specific channel]
- [ ] Run `[sales/ads/email]` skill as needed for chosen model
- [ ] Track: [model-specific key metric]
- Exit criteria: First paying users, primary channel producing leads
- Gut check: "Can I acquire users repeatably?" If no → revisit GTM model.
- Next step: Move to Grow phase

#### Phase 5: Grow
- [ ] Double down on primary channel — optimize before adding new ones
- [ ] Run `growth` skill for activation and retention loops
- [ ] Run `content` / `social-media` skill to add supporting channels
- [ ] Run `analytics` skill to track unit economics
- Exit criteria: Repeatable acquisition, unit economics positive
- Gut check: "Are unit economics positive after 3 months?" If no → revisit pricing.

### Channel Mix
Primary channel: [based on model]
Supporting channels: [1-2 others]
Skip for now: [channels that don't fit your model/strengths]

### Milestones & Gut Checks
- After Validate: "Do 10+ people want this?" If no → pivot or kill.
- After Launch: "Can I acquire users repeatably?" If no → revisit model.
- After 3 months in Grow: "Are unit economics positive?" If no → revisit pricing.

### Your Skills to Use
[Ordered list of which plugin skills to run, in what sequence]
```

---

## File Structure

```
skills/gtm/
├── SKILL.md              # Entry point — persona, principles, workflow, common mistakes
├── GTM-MODELS.md          # The 5 models with selection criteria and signal matching
└── PHASE-PLAYBOOK.md      # Phase definitions, exit criteria, and skill mappings per model
```

**Content split:**
- **SKILL.md:** Frontmatter, persona, core principles, when to use/not use, the 4-stage interactive workflow (summary level — references supporting files for detail via `See [GTM-MODELS.md](GTM-MODELS.md)` and `See [PHASE-PLAYBOOK.md](PHASE-PLAYBOOK.md)` links), output format overview, common mistakes, success criteria.
- **GTM-MODELS.md:** Deep reference on each model — what it looks like in practice, founder profile fit, channel priorities per model, example companies, key metrics per phase, and when to pivot between models. Referenced from Stage 3 of the workflow.
- **PHASE-PLAYBOOK.md:** Detailed phase definitions for each GTM model (a content-led Plan phase looks different from a sales-led Plan phase), exit criteria variations by model, and the skill-to-phase mapping table. Referenced from Stage 4 of the workflow.

Follows plugin convention: SKILL.md first, supporting files one level deep.

---

## Cross-Skill References

When the GTM skill routes to other skills, it uses "Next step: Run the `[skill]` skill" directives in the playbook. This is distinct from "Tell AI:" prompts — "Next step" means "go use that skill now," while "Tell AI:" means "paste this prompt to get a specific thing done."

| Phase | Routes To |
|-------|-----------|
| Plan | `plan`, `market-research`, `pricing` |
| Validate | `validate`, `customer-research` |
| Build | `build`, `landing-page`, `pricing`, `analytics` |
| Launch | `launch`, `sales`, `ads`, `email` |
| Grow | `growth`, `content`, `social-media`, `analytics` |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Picking a GTM model because it sounds impressive | Match model to your strengths and product, not aspiration |
| Trying to be on every channel at once | Pick one primary channel, prove it works, then add |
| Skipping positioning ("we're for everyone") | No positioning = no differentiation = competing on price alone |
| Jumping to Grow before Launch exit criteria are met | Scaling a broken funnel wastes money. Validate the motion first. |
| Copying a competitor's GTM without understanding why it works for them | Their model fits their founder, product, and market — yours might not |
| Refusing to pivot models when signals say it's not working | If 3 months of content-led produces nothing, try sales-led or PLG |

---

## Success Looks Like

After using `gtm`, you should:

- Have a clear position statement you can say in one sentence
- Know which GTM model fits your product, market, and strengths
- Have a phased plan with concrete exit criteria for each phase
- Know which channels to focus on and which to skip
- Have an ordered list of plugin skills to run next
- Know what "it's not working" looks like and when to pivot
- Have a saved GTM Playbook document you can reference as you execute

---

## Implementation Notes

- **Plugin manifest:** Adding `gtm` brings the skill count to 49. Update `.claude-plugin/plugin.json` and `CLAUDE.md` accordingly.
- **Playbook file creation:** The skill instructs Claude to save the playbook. If the target directory doesn't exist, create it. Default location: `docs/gtm-playbook.md`.

---

## Design Decisions

1. **Orchestrator, not executor** — GTM tells you what to do and when; existing skills tell you how. No duplication.
2. **Founder profile up front** — Strategy that ignores founder strengths produces plans that don't get executed.
3. **Phase-based, not time-based** — Solo founders don't operate on corporate timelines. Exit criteria > calendar dates.
4. **Five GTM models** — PLG, content-led, sales-led, community-led, hybrid. Covers the realistic options without overcomplicating.
5. **Interactive workflow → document output** — Forces founders to think through each decision rather than skimming a wall of strategy. Produces a concrete deliverable.
6. **Position-to-execution cascade** — Positioning is the root decision. Everything else (model, channels, messaging, pricing angle) flows from it.
7. **"Next step" routing over "Tell AI:" prompts** — GTM is strategic, not tactical. It routes to skills rather than providing execution prompts, except for positioning refinement which happens within GTM itself.
