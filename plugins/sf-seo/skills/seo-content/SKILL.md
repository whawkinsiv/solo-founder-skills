---
name: seo-content
description: "Use this skill when the user needs to write SEO content — blog posts, landing pages, feature pages, comparison pages, how-to guides, or any content meant to rank in search and get cited by AI. Covers content briefs, humanized writing that avoids AI detection, SERP feature targeting, entity optimization, content refresh, and quality self-checks. This is the writing skill — for strategy see seo, for technical implementation see technical-seo, for auditing see seo-audit."
---

# SEO Content Generation

You write SEO content that ranks in Google, gets cited by AI search engines, and reads like a sharp human wrote it — because the fastest way to get penalized or ignored is to publish content that smells like AI.

This skill covers the full content production workflow: brief the piece, write it with humanization baked in, optimize for SERP features and AI citations, then self-check before delivery.

For content strategy and keyword research, see **seo**. For technical implementation (schema, meta tags, CWV), see **technical-seo**. For auditing an existing site, see **seo-audit**.

---

## The Workflow

Every piece of content follows this sequence:

1. **Brief** — Research the keyword, analyze the SERP, find the angle
2. **Write** — Draft with humanization rules applied from the start (not bolted on after)
3. **Optimize** — Target SERP features, structure for AI citation, handle entity SEO
4. **Check** — Run the quality self-check before delivering

Never skip the brief. Writing without a brief produces generic content that ranks nowhere.

---

## Step 1: Content Brief

Before writing a single word, produce a brief. This is the most important step — it determines whether the content has a reason to exist.

### Brief Template

```
## Content Brief: [Working Title]

**Target keyword:** [primary keyword]
**Secondary keywords:** [3-5 related terms to include naturally]
**Search intent:** [informational / commercial / transactional]
**Monthly search volume:** [if known, or estimate as low/medium/high]

**SERP analysis:**
- What currently ranks: [describe the top 3-5 results — format, length, angle]
- What's missing: [the gap you'll fill — what do all top results fail to cover?]
- SERP features present: [featured snippet? PAA? video carousel? AI overview?]

**Content angle:** [your unique take — why should THIS piece exist when 10 others already do?]
  Angle types: original data, first-person experience, contrarian position,
  deeper expertise, newer information, better structure, specific audience focus

**Content type:** [how-to / comparison / listicle / guide / landing page / case study]
**Target word count:** [based on what's ranking — match or beat by 20%]

**Outline:**
- H1: [title — keyword-front-loaded, compelling]
- H2: [section] — targets [SERP feature or PAA question]
  - H3: [subsection]
- H2: [section]
  ...

**Internal links:** [2-3 existing pages to link TO from this content]
**Link TO this from:** [1-2 existing pages that should link to this new piece]
**CTA placement:** [where and what — e.g., "inline CTA after section 3 → free trial"]

**Featured snippet target:** [the specific query + format: paragraph/list/table]
**AI citation target:** [the specific question this content should be cited for]
```

### Finding the Angle

The angle is everything. Without one, you're writing content that already exists.

| Angle Type | When to Use | Example |
|-----------|-------------|---------|
| **Original data** | You have data nobody else does | "We analyzed 2,847 SaaS pricing pages. Here's what converts." |
| **First-person experience** | You've actually done the thing | "I migrated 3 production apps from Heroku to Railway. Here's what broke." |
| **Contrarian position** | The consensus is wrong or incomplete | "Stop obsessing over domain authority. Here's what actually moves rankings." |
| **Deeper expertise** | Top results are shallow | "Every guide says 'use schema markup.' None show you the 6 schemas that actually trigger rich results." |
| **Newer information** | Top results are outdated | "Google's March 2026 update changed everything about [topic]. Here's what works now." |
| **Specific audience** | Top results are generic | "CI/CD for solo developers — not the enterprise playbook, the one-person-team playbook." |

**If you can't articulate the angle, don't write the piece.** You'll produce another mediocre article that fights for position 11.

---

## Step 2: Write with Humanization

This is the core of the skill. The humanization rules are not a post-processing step — they're how you write from the first sentence.

For the full humanization framework and anti-detection patterns, see [HUMANIZATION.md](HUMANIZATION.md).

For writing templates by content type, see [CONTENT-TYPES.md](CONTENT-TYPES.md).

### The Non-Negotiable Rules

These apply to every piece of content:

**1. Vary your rhythm.**
Mix sentence lengths aggressively. Some sentences are three words. Others stretch to thirty, with embedded clauses and asides that give the reader a sense of a mind actually thinking through the problem rather than outputting pre-formed paragraphs.

**2. Have a point of view.**
Take positions. "This approach is wrong and here's why" is more valuable than "there are pros and cons to consider." Humans have opinions. AI hedges.

**3. Use first-person experience.**
"I tested this" beats "testing reveals." "We found that" beats "research shows." If you don't have personal experience to draw from, use the founder's — ask them what they've seen, done, or learned.

**4. Be specific, not comprehensive.**
"Vercel deploys in 8 seconds on a cold start" beats "modern hosting platforms offer fast deployment times." Name the tool. Cite the number. Date the experience.

**5. Write ugly sentences on purpose.**
Not every sentence should parse cleanly. Start some with "And" or "But." Use fragments. Interrupt yourself with a dash — then finish the thought. This is how humans actually write when they're not trying to impress an English teacher.

**6. Kill the AI tells.**
No "In today's fast-paced world." No "It's important to note." No "Let's dive in." No "In conclusion." No "Whether you're a beginner or an expert." These are the fingerprints of machine-generated text. See [HUMANIZATION.md](HUMANIZATION.md) for the complete list.

**7. Front-load the answer.**
The first 1-2 sentences of every section should directly answer the question the heading asks. Then elaborate. This serves both featured snippets and AI citations.

**8. Earn every paragraph.**
If a paragraph restates what the previous one said, delete it. If a section summarizes the article so far, delete it. Humans don't recap themselves every 300 words.

---

## Step 3: Optimize

After the draft exists, optimize for discoverability.

### SERP Feature Targeting

Different SERP features require different content structures:

**Featured Snippet (paragraph):**
- Trigger: question-based query ("what is...", "how does...")
- Format: answer the question in 40-60 words immediately after the H2/H3
- The answer must be self-contained — it should make sense without the surrounding text

**Featured Snippet (list):**
- Trigger: "how to...", "steps to...", "best..." queries
- Format: numbered or bulleted list with 5-8 items, each 1 line
- Use an H2 that matches the query, immediately followed by the list

**Featured Snippet (table):**
- Trigger: comparison queries, "vs", pricing, specs
- Format: HTML table with clear column headers
- Keep to 3-5 columns, 4-8 rows

**People Also Ask (PAA):**
- Use PAA questions as H2 or H3 headings verbatim
- Answer in the first 1-2 sentences (50-80 words), then elaborate
- Include 3-5 PAA-style question headings per article
- Find real PAA questions by searching your target keyword in Google

**AI Overviews / AI Citations:**
- Lead with citable facts: "[Thing] is [definition/claim]. According to [source], [statistic]."
- Include statistics with source and year: "53% of web traffic comes from organic search (BrightEdge, 2025)"
- Use FAQ schema on question-answer pairs (see technical-seo skill)
- Add TL;DR blocks that can be extracted as standalone answers

### Entity & Semantic Optimization

Google and AI models understand content through entities, not just keywords.

**Entity rules:**
- **Define entities on first mention.** "INP (Interaction to Next Paint) is a Core Web Vital that measures how quickly a page responds to user interactions." Don't assume the reader (or the crawler) knows what your acronyms mean.
- **Use consistent terminology.** Don't synonym-swap for variety. If you call it "content brief" in paragraph 1, don't switch to "content outline" in paragraph 4. Synonym swapping confuses entity recognition.
- **Co-occur related entities naturally.** When writing about "Core Web Vitals," naturally mention "LCP," "INP," "CLS," "PageSpeed Insights," "Lighthouse" — these entities belong together and signal topical depth.
- **Reference authoritative entities.** Cite Google's documentation, not random blog posts. Mention recognized tools by name. Link to primary sources.
- **Write clear subject-verb-object for key claims.** "Google uses INP to measure page responsiveness" is unambiguous. "Page responsiveness, as measured through various metrics including those from Google, is important" is entity soup.

### Passage Optimization

Google indexes individual passages, not just pages. Each section should be able to rank independently.

- Every H2 section should be self-contained enough to answer its heading question without context from other sections
- Key claims should appear in clean, extractable sentences — not buried in complex paragraphs
- Use the heading as the question, the first 1-2 sentences as the answer, and the rest of the section as evidence

---

## Step 4: Quality Self-Check

Run this checklist against every piece before delivering. If any item fails, fix it.

### Content Quality

- [ ] The piece has a clear angle that differentiates it from what already ranks
- [ ] Every section adds information — no filler, no restating previous sections
- [ ] Word count is within 20% of what's ranking for this keyword
- [ ] Internal links point to 2+ relevant pages on the site
- [ ] At least one CTA is present (soft or hard, context-appropriate)
- [ ] Statistics include source and year
- [ ] The piece would be useful to the target reader even if the product didn't exist

### Humanization Check

- [ ] Sentence length varies — some under 8 words, some over 25
- [ ] Paragraph length varies — some 1 sentence, some 4-5
- [ ] Contains at least one first-person reference ("I," "we," "our testing showed")
- [ ] Contains at least one opinion or stance (not just balanced pros/cons)
- [ ] No AI-tell phrases (see [HUMANIZATION.md](HUMANIZATION.md) kill list)
- [ ] At least 3 specific, named examples (tools, companies, numbers, dates)
- [ ] Starts at least 2 sentences with "And," "But," or "So"
- [ ] Contains at least one conversational aside (parenthetical, dash interjection, or direct reader address)
- [ ] Does NOT summarize the article in the conclusion — ends with a forward-looking statement or CTA

### SEO Check

- [ ] H1 contains the primary keyword (naturally, not stuffed)
- [ ] Primary keyword appears in the first 100 words
- [ ] Secondary keywords appear at least once each
- [ ] H2/H3 headings include question-format headings for PAA targeting
- [ ] At least one featured-snippet-formatted answer (40-60 words after a question heading)
- [ ] At least one table or structured comparison
- [ ] Images have descriptive alt text with relevant keywords
- [ ] Meta title is 50-60 characters, keyword-front-loaded
- [ ] Meta description is 120-155 characters, includes value prop and CTA language

### AI Citation Check

- [ ] Key claims are written as clean, extractable, quotable sentences
- [ ] At least one TL;DR or summary block exists
- [ ] Definitions use explicit "[Term] is [definition]" format
- [ ] FAQ-style Q&A pairs exist (ideally with FAQPage schema)

---

## Content Refresh Protocol

Existing content decays. Refreshing a declining page is 3-5x more efficient than writing a new one.

### When to Refresh

| Signal | What It Means | Action |
|--------|--------------|--------|
| Impressions dropping 20%+ over 3 months | Content is losing relevance | Full refresh |
| CTR declining but impressions stable | Title/description are stale | Rewrite meta tags |
| Position slipping from page 1 to page 2 | Competitors updated | Add new sections, update stats |
| Content is 6+ months old with dated stats | Freshness penalty risk | Update statistics, add recent examples |
| New subtopics emerged since publishing | Content gap vs. newer competitors | Add sections covering new subtopics |

### How to Refresh

1. **Don't change the URL.** Ever. You'll lose all accumulated authority.
2. **Don't rewrite from scratch** unless the entire angle is wrong. Preserve what's working (check Search Console for which queries the page already ranks for).
3. **Update the date** — both the visible "last updated" date and the `dateModified` in schema markup.
4. **Add new information** — new statistics, recent examples, new tools, new sections for emerging subtopics.
5. **Refresh the intro** — the first 2-3 paragraphs matter most for both ranking and AI citation.
6. **Improve the angle** — if the original angle was weak, sharpen it. Add first-person experience if it was missing.
7. **Re-check the SERP** — the competitive landscape may have shifted. New SERP features may have appeared.
8. **Update internal links** — link to newer content published since the original.

---

## Supporting Files

- [HUMANIZATION.md](HUMANIZATION.md) — Complete humanization framework: AI-tell kill list, rhythm patterns, voice calibration, anti-detection writing techniques
- [CONTENT-TYPES.md](CONTENT-TYPES.md) — Writing templates for each content type: how-to guides, comparison pages, listicles, landing pages, glossary entries, case studies
