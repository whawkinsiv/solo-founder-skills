---
name: ads
description: "Use this skill when the user needs to run Google Ads, write ad copy, select keywords, optimize CAC/LTV, or manage a small paid acquisition budget. Covers Google Ads strategy, keyword selection, ad copywriting, and conversion tracking for bootstrapped SaaS."
---

# Paid Acquisition & Ad Copy

Paid acquisition amplifies what's already working. If your landing page doesn't convert organic traffic, ads won't fix it. This skill helps you run profitable Google Ads on a small budget — from campaign setup to weekly optimization.

## Core Principles

- Paid acquisition amplifies what's already working. If your landing page doesn't convert organic traffic, ads won't fix it.
- Start with the highest-intent keywords. People searching for "[Competitor] alternative" are closer to buying than people searching for "what is [category]."
- Small budgets demand focus. $10-20/day on 5-10 exact-match keywords beats $100/day spread across 500 broad-match keywords.
- Test the message, not the channel. If Google Ads doesn't work at $10/day, the problem is usually your ad copy or landing page, not the channel.
- CAC must be less than 1/3 of LTV from day one. If the math doesn't work at small scale, it won't work at large scale.
- Every dollar should be traceable to a conversion. If you can't track it, don't spend it.

## Prerequisites (Before Spending a Dollar)

- [ ] Landing page converts organic visitors at 2%+ (signup rate)
- [ ] Analytics tracking working (can attribute signups to source)
- [ ] Payment flow works (can track ad spend → signup → payment)
- [ ] You know your activation rate (what % of signups become real users)
- [ ] You have a rough LTV estimate (even if based on pricing × estimated retention)

If any of these are missing, fix them first. Ads on a broken funnel is burning money.

## Google Ads for SaaS

### Campaign Structure for Solo Founders

Start with ONE campaign, 2-3 ad groups:

```
Campaign: [Product Name] — Search
  Budget: $10-20/day
  Bidding: Maximize conversions (once you have 15+ conversions)
           OR Manual CPC to start (set bids at $2-5 range)
  Network: Search only (NOT Display, NOT Search Partners)
  Location: Countries where your ICP lives

  Ad Group 1: Competitor Keywords (highest intent)
    Keywords:
      [competitor name] alternative
      [competitor name] vs
      [competitor name] pricing
      switch from [competitor name]
      [competitor name] review

  Ad Group 2: Problem Keywords (high intent)
    Keywords:
      [specific problem] tool
      [specific problem] software
      how to [solve specific problem]
      best [category] for [audience]
      [category] for small teams

  Ad Group 3: Solution Keywords (medium intent)
    Keywords:
      [category] software
      [category] platform
      [category] app
      online [category] tool
```

### Keyword Strategy

**Match types (start narrow, expand later):**
- **Exact match** `[keyword]`: Start here. Only shows for this exact search.
- **Phrase match** `"keyword"`: Add after exact match proves profitable.
- **Broad match**: Avoid until you have significant conversion data and use Smart Bidding.

**Negative keywords (add immediately):**
```
free
open source
tutorial
how to build
DIY
jobs
hiring
salary
reddit
github
course
template (unless you sell templates)
```

**Finding keywords:**
- Google's autocomplete: Type your problem and see what Google suggests.
- "People also ask": Search your main keyword and mine the related questions.
- Competitor's meta keywords (view source on their pages).
- Google Keyword Planner (free with a Google Ads account).
- Your own customer conversations — what words do they use to describe the problem?

### Ad Copy That Converts

**Google Search Ad structure:**
```
Headline 1 (30 chars): [Primary benefit or problem]
Headline 2 (30 chars): [Differentiator or social proof]
Headline 3 (30 chars): [CTA with specificity]
Description 1 (90 chars): [Expand on benefit, address objection]
Description 2 (90 chars): [Proof point + CTA]
```

**Templates by ad group:**

Competitor keywords:
```
H1: Tired of [Competitor]?
H2: [Product] — Built for [ICP]
H3: Try Free — No Credit Card
D1: [Specific advantage over competitor]. Switch in minutes, not days.
D2: Join [X] teams who switched from [Competitor]. Start free today.
```

Problem keywords:
```
H1: [Problem] Solved in Minutes
H2: [Product] for [Audience]
H3: Start Free — Setup in 5 Min
D1: Stop [painful manual process]. [Product] [specific outcome] automatically.
D2: [Social proof]. Free plan available. No credit card required.
```

Solution keywords:
```
H1: [Category] Built for [ICP]
H2: Simple, Fast, Affordable
H3: Free Plan Available
D1: [Product] helps [audience] [achieve outcome]. [Key differentiator].
D2: Trusted by [X] teams. Start free in under 2 minutes.
```

**Ad copy rules:**
- Include the keyword in at least one headline (improves Quality Score).
- Always mention "free" if you have a free tier or trial.
- Numbers beat adjectives: "Setup in 5 minutes" beats "Quick setup."
- Address one objection in the description: price, complexity, or switching cost.
- Write 3-4 ad variants per ad group. Let Google optimize for performance.

### Landing Pages for Ads

Do NOT send ad traffic to your homepage. Create dedicated landing pages:

```
URL structure:
  yoursite.com/vs/[competitor]     → for competitor keywords
  yoursite.com/use-case/[problem]  → for problem keywords
  yoursite.com/for/[audience]      → for audience keywords
```

Each landing page should:
- Match the ad's headline (message match = higher conversion).
- Address the specific search intent (not generic product pitch).
- Have a single CTA (signup or trial start).
- Load in <2 seconds.
- Include no navigation links away from the conversion goal.

### Tracking Setup

**Essential tracking:**
```
1. Google Ads conversion tracking
   - Signup completed (primary conversion)
   - Trial started (if separate from signup)
   - Payment completed (import from your backend if possible)

2. Google Analytics 4
   - UTM parameters on all ad URLs
   - utm_source=google&utm_medium=cpc&utm_campaign=[campaign]&utm_term=[keyword]

3. Your own database
   - Store utm_source on user signup record
   - Track: Ad click → Signup → Activation → Payment (full funnel by source)
```

## Budget Management

### Weekly Review Ritual (15 minutes)

```
| Metric              | This Week | Last Week | Target |
|---------------------|-----------|-----------|--------|
| Spend               |           |           | $70-140|
| Clicks              |           |           |        |
| CTR                 |           |           | >3%    |
| CPC (avg)           |           |           | <$3    |
| Signups from ads    |           |           |        |
| Cost per signup     |           |           | <$XX   |
| Signups → Activated |           |           | >30%   |
| Signups → Paid      |           |           | >5%    |
| CAC (paying)        |           |           | <1/3 LTV|
```

### Decision Rules

```
CTR < 2%:
  → Ad copy isn't compelling. Rewrite headlines.

CPC too high (>$5 for SMB SaaS):
  → Keywords too competitive. Go more longtail or niche.

Clicks but no signups:
  → Landing page problem. Check message match, page speed, form friction.

Signups but no activation:
  → Product/onboarding problem, not an ads problem. Pause ads and fix.

CAC > 1/3 LTV:
  → Unprofitable. Improve conversion rate, test new keywords, or pause.

Everything working:
  → Increase budget by 20-30% per week. Don't double overnight.
```

### Scaling Rules

1. Don't increase budget by more than 30% per week.
2. Add new keywords only after existing ones are profitable.
3. Expand to phrase match only after exact match has 30+ conversions.
4. Consider Meta/LinkedIn Ads only after Google Search is profitable.
5. Never spend more than you can afford to lose for 3 months with zero return.

## CAC Tracking

```
Simple CAC calculation:
  CAC = Total ad spend in period ÷ Paying customers acquired from ads in period

Blended CAC (all channels):
  Blended CAC = Total marketing spend ÷ Total new paying customers

Sustainability check:
  LTV:CAC ratio = LTV ÷ CAC
  Target: 3:1 or better

  Payback period = CAC ÷ Monthly revenue per customer
  Target: <6 months for bootstrapped
```

---

## Setting Up a Campaign

**Tell AI:**
```
Set up a Google Ads search campaign for my SaaS:
- Product: [what it does]
- Audience: [who it's for]
- Budget: [$10-20/day to start]
- Top 3 competitors: [names]
- Main problem solved: [one sentence]

Create:
1. Campaign structure with 2-3 ad groups (competitor, problem, solution keywords)
2. 10-15 exact-match keywords per ad group
3. Negative keyword list
4. 3 ad copy variants per ad group (with character counts)
5. UTM parameters for tracking
6. Landing page recommendations for each ad group
```

**Tell AI (for ad copy iteration):**
```
Write 4 Google Search ad variants for this ad group:
- Target keyword: [keyword]
- Landing page: [URL]
- Our differentiator: [what makes us different]
- Social proof: [user count, notable customers, specific results]

Follow Google Ads limits: H1-H3 (30 chars each), D1-D2 (90 chars each).
Include the keyword in at least one headline.
Show character counts for each line.
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Running ads before landing page converts | Get 2%+ organic conversion rate first |
| Broad match keywords from day one | Start with exact match. Expand after 30+ conversions |
| No negative keywords | Add the standard exclusion list on day one |
| Sending traffic to homepage | Create dedicated landing pages per ad group |
| No conversion tracking | Set up Google Ads conversion tracking before spending |
| Scaling too fast | Increase budget max 30% per week |
| CAC > 1/3 of LTV | Pause and fix conversion rate before spending more |

---

## Related Skills

- **landing-page** — Build dedicated landing pages for each ad group
- **conversion** — Optimize the signup flow that ads drive traffic to
- **analytics** — Track ad spend → signup → payment attribution
- **copywriting** — Write stronger ad headlines and descriptions
- **seo** — Build organic traffic so you're not paying for every click
