# Content Type Templates

Writing templates for each SEO content type. Each template specifies the structure, target SERP features, humanization priorities, and a skeleton to work from.

These are starting structures, not rigid formats. Break them when the content calls for it — [HUMANIZATION.md](HUMANIZATION.md) explains when and how.

---

## How-To Guide

**Search intent:** Informational ("how to [action]")
**Target SERP features:** Featured snippet (list), PAA, AI Overview
**Typical word count:** 1,500-2,500 words

### Structure

```
H1: How to [Action] [Qualifier/Context]
   (e.g., "How to Set Up Stripe Billing for a SaaS MVP")

[2-3 sentence intro: state what the reader will accomplish and why
this guide exists when others already do — your angle]

H2: What You Need Before Starting
   [Prerequisites, tools, accounts — keep it short. Skip if obvious.]

H2: [Step 1 — action-oriented heading]
   [Direct instruction. Screenshots or code if applicable.
   Include the "why" — not just what to do, but why this step matters.]

H2: [Step 2 — action-oriented heading]
   [Same format. Each step should be independently scannable.]

H2: [Step N — final action]
   [End with verification — how does the reader know it worked?]

H2: Common Mistakes (and How to Fix Them)
   [3-5 real pitfalls. This section often captures PAA queries.]

H2: [Closing thought — not a summary]
   [Next step, related task, or opinion about where this fits in
   the bigger picture.]
```

### Humanization Priorities

- Use second person throughout ("you'll need to," "click the...")
- Include at least one "when I did this, I ran into..." moment
- Name specific tools, versions, and dates
- Show the gotchas — the things that aren't in the official docs

### Featured Snippet Optimization

After the H1, include a numbered list version of the steps (5-8 items, one line each) as a quick-reference. This is your snippet bait — Google pulls concise numbered lists for "how to" queries.

---

## Comparison Page

**Search intent:** Commercial ("[Product A] vs [Product B]")
**Target SERP features:** Featured snippet (table), PAA
**Typical word count:** 2,000-3,000 words

### Structure

```
H1: [Product A] vs [Product B]: [Opinionated Qualifier]
   (e.g., "Vercel vs Netlify: Which One Ships Faster for Solo Devs")

[2-3 sentences: state who this comparison is for, and signal
that you've actually used both. Credibility is everything here.]

H2: The Quick Verdict
   [3-4 sentences. Who should use which, and why. Don't make
   the reader scroll 2,000 words for the answer.]

H2: [Category 1] Comparison
   [Table comparing the specific dimension, then 2-3 paragraphs
   of context. Include what the table can't show — the feel,
   the friction, the edge cases.]

H2: [Category 2] Comparison
   [Same format.]

H2: [Category N] Comparison

H2: Pricing Breakdown
   [Table with plan names, prices, key limits.
   Include the gotchas: "The Pro plan says unlimited, but..."]

H2: Who Should Use [Product A]
   [Bulleted profile of the ideal user. Be specific — not
   "developers" but "solo devs shipping MVPs who want zero config."]

H2: Who Should Use [Product B]
   [Same format.]

H2: What About [Product C]?
   [Brief mention of alternatives — captures long-tail
   "alternatives to X" traffic. 3-5 sentences per alternative.]
```

### Humanization Priorities

- You MUST take a position. "Both are great" is useless. Say which is better for the reader's likely situation.
- Reference specific features by name, with version/date
- Include at least one "I switched from X to Y because..." moment
- Mention the things marketing pages don't: slow support, confusing UIs, hidden limits
- If one product is yours, disclose it and be fair — biased comparison pages get destroyed in comments

### Featured Snippet Optimization

The comparison table is your snippet target. Make sure it has:
- Clean HTML table markup (not a Markdown table that renders poorly)
- Clear column headers
- 4-8 rows covering the most-searched comparison dimensions
- One of the columns is "Verdict" or "Best For" with concise answers

---

## Listicle

**Search intent:** Commercial/Informational ("best [category] tools", "top [category]")
**Target SERP features:** Featured snippet (list), PAA
**Typical word count:** 2,500-4,000 words

### Structure

```
H1: [Number] Best [Category] [Qualifier] in [Year]
   (e.g., "9 Best Email Marketing Tools for Solo Founders in 2026")

[2-3 sentence intro: who this list is for, how you chose
the tools, and what "best" means in this context.]

H2: Quick Picks
   [Bulleted list: "Best for X: [Tool]" — 3-5 entries.
   This is your snippet bait AND it respects the reader's time.]

H2: 1. [Tool Name] — Best for [Specific Use Case]
   [2-3 sentence verdict up front.]
   H3: What It Does Well
   H3: Where It Falls Short
   H3: Pricing
   [Include what plan a solo founder would actually use
   and what it costs.]

H2: 2. [Tool Name] — Best for [Different Use Case]
   [Same structure.]

...

H2: How We Chose These Tools
   [Methodology — what you tested, how long, what criteria.
   This builds E-E-A-T and differentiates from listicles that
   clearly never touched the products.]

H2: What We Left Out (and Why)
   [Mention 3-5 tools that almost made the list. This captures
   long-tail search for those tools AND shows thoroughness.]
```

### Humanization Priorities

- Use an odd number of items (7, 9, 11) — not 5 or 10 (which read as AI defaults)
- Include at least one unexpected/lesser-known pick
- State specific things you liked and disliked about each tool — not feature-list summaries
- If your product is on the list, put it in the top 3 but not #1 (credibility > promotion)
- Date the pricing — "as of March 2026" — because it changes

### Featured Snippet Optimization

The "Quick Picks" section is designed for the list snippet. Format it as:
1. Best for [use case]: [Tool]
2. Best for [use case]: [Tool]
...

---

## Landing Page

**Search intent:** Commercial/Transactional ("[category] software", "[solution] tool")
**Target SERP features:** Sitelinks, AI Overview
**Typical word count:** 800-1,500 words (tighter than editorial content)

### Structure

```
H1: [Outcome-Focused Headline]
   (e.g., "Ship Your SaaS Landing Page in 10 Minutes" —
   not "Landing Page Builder Tool")

[Subheadline: expand on H1 with specificity or social proof]

[Hero CTA]

H2: [Problem Statement — what the reader is dealing with]
   [2-3 sentences naming the pain. Be specific.]

H2: [How It Works / What You Get]
   [3-step or 3-feature breakdown. Each with a short heading
   and 2-3 sentences. Benefit-first, not feature-first.]

H2: [Social Proof Section]
   [Testimonials, logos, metrics. Real names and companies.
   Schema markup: Review or Product.]

H2: [Objection Handling]
   [FAQ format. Address the 3-5 reasons someone wouldn't
   sign up. Use FAQPage schema.]

[Final CTA with supporting reassurance copy]
```

### Humanization Priorities

- Landing pages are short — every word matters more
- Use the customer's language, not internal jargon
- Specificity is credibility: "Used by 847 teams" not "Used by hundreds"
- Testimonials should sound like a person, not a press release
- The FAQ section should include genuinely hard questions, not softballs

---

## Glossary Entry

**Search intent:** Informational ("what is [term]")
**Target SERP features:** Featured snippet (paragraph), AI Overview, Knowledge Panel
**Typical word count:** 500-1,000 words

### Structure

```
H1: What Is [Term]? [Brief Context]
   (e.g., "What Is Churn Rate? The SaaS Metric That Predicts Your Future")

[Definition in the first sentence: "[Term] is [concise definition]."
This is your snippet/AI citation target. Keep it under 50 words,
self-contained, and precise.]

H2: Why [Term] Matters
   [Connect to the reader's world. Why should they care?]

H2: How [Term] Works
   [Practical explanation with an example. Not textbook — applied.]

H2: [Term] vs [Related Term]
   [Clear differentiation. Captures comparison queries.]

H2: How to [Measure/Calculate/Apply] [Term]
   [Formula, tool recommendation, or step-by-step.
   Makes the entry actionable, not just definitional.]

H2: Common Mistakes with [Term]
   [2-3 pitfalls. Captures PAA questions.]
```

### Humanization Priorities

- The definition must be precise and original — not rephrased from Wikipedia
- Include a concrete example with real numbers
- Keep it shorter than your instinct says — glossary entries that run 2,000 words lose readers
- Link to your deeper content (guides, how-tos) from the glossary entry

### Featured Snippet Optimization

The first sentence IS the snippet. Write it as: "[Term] is [definition that directly answers 'what is [term]?']." Keep it 35-50 words. Test it: if you read just that sentence, do you understand the concept?

---

## Case Study

**Search intent:** Commercial (brand + "case study", "[industry] results")
**Target SERP features:** PAA, AI citations for industry-specific queries
**Typical word count:** 1,000-2,000 words

### Structure

```
H1: How [Customer/Company] [Achieved Specific Result] with [Product]
   (e.g., "How Acme Corp Cut Onboarding Time 60% with [Product]")

[1-2 sentence summary of the result — the number, the timeframe,
the context. This is your citation bait.]

H2: The Challenge
   [What they were dealing with before. Specific pain — not
   generic "they needed a solution." Name the tools they were
   using, the team size, the constraints.]

H2: Why They Chose [Product]
   [What alternatives they considered and why they went with you.
   Include what almost stopped them — the real objection.]

H2: The Implementation
   [What they actually did. Timeline, steps, surprises.
   This section should feel like a project retrospective.]

H2: The Results
   [Numbers. Before and after. Timeframe. Quote from the customer.
   Include results they didn't expect alongside the headline metric.]

H2: Key Takeaways
   [2-3 lessons that apply to readers in similar situations.
   This is the part that makes the case study useful beyond
   social proof for your product.]
```

### Humanization Priorities

- Use the customer's actual words — if you have quotes, use them. If not, write in a way that sounds like a specific person, not a press release.
- Include the messy middle — not just problem → solution → success. What almost went wrong?
- Real numbers with context: "60% reduction" means nothing without "from 45 minutes to 18 minutes"
- Acknowledge limitations: "This worked because [specific context]. If your situation is [different], results may vary."

---

## Choosing the Right Type

| User's Query Pattern | Content Type | Why |
|---------------------|-------------|-----|
| "How to [action]" | How-To Guide | They want instructions |
| "[A] vs [B]" | Comparison Page | They're deciding between options |
| "Best [category]" | Listicle | They want options evaluated |
| "What is [term]" | Glossary Entry | They want a definition |
| "[Product] review" / "[Product] case study" | Case Study | They want proof |
| "[Category] software" / "[Solution] tool" | Landing Page | They want to buy |

When the intent is ambiguous, check the SERP. Google already figured out what format searchers want — look at what ranks and match the format.
