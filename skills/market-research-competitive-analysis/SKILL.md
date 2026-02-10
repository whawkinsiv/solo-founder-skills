---
name: market-research-competitive-analysis
description: "Use this skill when the user needs to size a market, analyze competitors, calculate TAM/SAM/SOM, or validate a business idea. Covers market sizing, competitive analysis frameworks, napkin math, and bottom-up revenue estimation."
---

# Market Research & Competitive Analysis

Markets matter more than ideas. This skill helps you evaluate whether your market is worth entering — and how to validate demand before you build.

## Core Principles

- A mediocre product in a great market beats a brilliant product in a dead one.
- All market sizing is wrong. The goal is order-of-magnitude clarity, not decimal precision.
- Competitors are evidence that demand exists. Zero competitors is a warning sign, not an advantage.
- The best solo-founder markets have high pain, fragmented incumbents, and willingness to pay — not the biggest TAM.
- Research is only useful if it changes a decision. Every analysis should end with a clear recommendation.

---

## Early Validation: Before You Build Anything

### Finding Your First 10 People to Talk To

Before doing market sizing, validate that real people have this problem.

**Method 1: Cold Outreach (Fastest — 1-2 weeks)**
- LinkedIn: Search for your ICP's job title → send connection request with a note
- Twitter/X: Search hashtags related to the problem → DM active posters
- Reddit: Find niche subreddits → comment helpfully → DM engaged users
- Email: Find company websites of target customers → reach out to founders/decision-makers

**Cold outreach template:**
```
Subject: Quick question about [problem area]

Hi [Name],

I'm researching how [ICP role] handles [specific problem]. I noticed you [signal that they have this problem — e.g., posted about it, work in relevant role, use a competing tool].

Would you be open to a 15-minute call this week? I'm not selling anything — just trying to understand the problem better before I build a solution.

Happy to share what I learn from the research as a thank you.

[Your name]
```

**Method 2: Communities (Higher quality — 2-4 weeks)**
- Indie Hackers: Search for threads where your ICP discusses the problem
- Facebook Groups: Search for niche groups (e.g., "Freelance Copywriters", "SaaS Founders")
- Slack communities: Industry-specific channels, FounderPath, etc.
- Discord: More engaged than most channels for technical audiences

**Method 3: Landing Page Test (Lowest effort — 2-3 weeks)**
1. Build a simple landing page describing the problem you solve (use Lovable or Claude Code)
2. Drive 100-200 visits via communities, social posts, or $100-200 in ads
3. Measure: Signups / Visitors = interest rate
4. Below 5% signup rate → positioning is unclear or demand is weak

### After 5 Conversations, Ask Yourself

- Did 3+ people independently describe the same pain? → Demand likely real
- Would they pay? Did anyone name a price unprompted? → Market likely exists
- Do they already use 2+ workarounds? → Problem is acute
- Did you learn something that surprised you? → Explore it in conversations 6-10

**Decision threshold:**
- 3+ people confirm the problem AND 2+ say they'd pay → proceed to market sizing and build
- Mixed signals after 10 conversations → either pivot your hypothesis or try a different ICP segment
- Nobody cares after 10 conversations → this isn't a real problem. Pick a different idea.

### Avoiding Analysis Paralysis

5 conversations reveal 80% of what you need to know. The other 20% you learn by building and shipping. Don't wait for certainty — it never comes.

---

## Market Sizing (Napkin Math That Matters)

### Bottom-Up (The Only Method That Matters for Solo Founders)

```
1. How many potential buyers exist?
   [Industry size] × [% that match your ICP]
   Example: 500,000 US marketing agencies × 12% that are 5-20 person = 60,000

2. What will each pay annually?
   [Price point] × [12 months]
   Example: $49/month × 12 = $588/year

3. Realistic addressable market:
   [Buyers] × [Annual price] × [Capture rate]
   Example: 60,000 × $588 × 2% = $705,600/year achievable

4. Sanity check: Does that number fund the business you want?
   Solo founder needs $200K-$500K ARR to replace income + reinvest.
   If max realistic capture is $100K, the market is too small.
```

### Top-Down (Sanity Check Only)

```
TAM = Total market revenue (all possible buyers globally)
SAM = Segment you can serve (geography, vertical, size)
SOM = What you can realistically capture in 3 years

Rule of thumb: SOM is 1-5% of SAM for a new entrant.
If SOM doesn't fund your business, stop here.
```

### Volume Estimation Sources

- Government data: Census Bureau, BLS (industry counts)
- Industry reports: IBISWorld, Statista (skim free summaries)
- LinkedIn: Search ICP job titles → count results
- Job boards: Volume of relevant roles = proxy for market size
- Competitor traffic: SimilarWeb free tier → estimate active users
- Subreddits/communities: Member counts = demand signal

---

## Competitive Analysis

### Substitute Mapping

Every product competes with four types:

1. **Direct competitors** — Same solution, same audience (Basecamp vs. Asana)
2. **Indirect competitors** — Different solution, same problem (spreadsheets vs. project tool)
3. **DIY / manual process** — They do it by hand (Post-its, email threads)
4. **Do nothing** — They tolerate the pain (this is your real enemy)

### Competitor Research Template

For each direct competitor:

```
## [Competitor Name]

**What they do**: One sentence.
**Target audience**: Who they sell to.
**Pricing**: Tiers and price points.
**Strengths**: 2-3 things they do well.
**Weaknesses**: 2-3 gaps, complaints, or underserved areas.
**Positioning**: Homepage headline — how they describe themselves.
**Traffic/Scale**: Monthly visits (SimilarWeb), review count (G2/Capterra).

### Where You Win
What specific thing will you do 10x better?
```

### Research Sources

- **Pricing**: Visit their pricing page. Screenshot it.
- **Positioning**: Read their homepage headline and subheadline.
- **Weaknesses**: G2, Capterra, Product Hunt, Reddit threads, Twitter complaints.
- **Traffic**: SimilarWeb (free tier).
- **Features**: Their docs/changelog reveal what they've built and haven't.
- **Hiring**: Job postings reveal strategic direction.

### Competitive Positioning Matrix

Build a 2×2 matrix with the two dimensions your ICP cares most about:

```
Example axes:
  X: Simple ←————→ Powerful
  Y: Cheap  ←————→ Premium

Plot competitors on this grid. Find the empty quadrant. That's your positioning opportunity.
```

---

## Solo-Founder Market Fit Assessment

Score each criterion 1-5. Minimum viable total: 25/40.

| Criterion | Score | Notes |
|-----------|-------|-------|
| **Pain intensity** — Hair-on-fire problem? | /5 | 5 = actively searching for a fix |
| **Willingness to pay** — Already pay for substitutes? | /5 | 5 = pay $50+/mo for something worse |
| **Reachable audience** — Can you find and contact them? | /5 | 5 = concentrated in known communities |
| **Fragmented competition** — No dominant monopoly? | /5 | 5 = many small players, no clear winner |
| **Small enough for solo** — Can one person serve this? | /5 | 5 = low support burden, self-serve viable |
| **Recurring need** — Will they use it monthly? | /5 | 5 = daily/weekly active use |
| **Your unfair advantage** — Domain expertise or distribution? | /5 | 5 = deep insider knowledge |
| **Technical feasibility** — Build core in 4-8 weeks? | /5 | 5 = well-understood, no R&D needed |

**Scoring:**
- 35-40: Exceptional fit. Move fast.
- 25-34: Viable. Validate the weak spots.
- Below 25: Reconsider. Weak markets kill good products.

---

## Distribution Vector Analysis

| Channel | Cost to Test | Time to Signal | Scalable? |
|---------|-------------|----------------|-----------|
| Cold outreach | $0 (time only) | 2-4 weeks | Somewhat |
| Communities | $0 (time only) | 1-3 months | Somewhat |
| Paid search | $200-500 | 1-2 weeks | Yes (if CAC works) |
| SEO / Content | $0 (time only) | 3-6 months | Yes |
| Directories | $0-200 | 1-2 months | Yes (passive) |
| Partnerships | $0 (time only) | 2-6 months | Yes |

**Rule:** Pick the ONE channel you can test in <30 days with <$500. Prove it works before diversifying.

---

## Buyer Leverage Check

Confirm your ICP can actually buy:

1. **Controls budget?** If they need 3 levels of approval, you lose.
2. **Below "just expense it" threshold?** ($50-100/mo for individuals, $500-1K for teams)
3. **Can adopt without IT?** Self-serve SaaS with optional SSO wins.
4. **Low switching cost?** If migration takes weeks, adoption stalls.
5. **One person gets value alone?** Network effects help growth but hurt initial adoption.

All five should be "yes" for a solo-founder SaaS.

---

## Output Format

1. Present findings in a clear document (not a slide deck).
2. Include specific numbers with sources cited.
3. Score the opportunity using the Solo-Founder Market Fit rubric.
4. End with a clear GO / CONDITIONAL / NO-GO recommendation.
5. If CONDITIONAL, name exactly what needs to be validated and how.
