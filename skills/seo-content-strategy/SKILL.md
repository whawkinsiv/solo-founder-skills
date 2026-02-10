---
name: seo-content-strategy
description: "Use this skill when the user needs to plan SEO content, do keyword research, build a content calendar, optimize pages for search intent, or create an internal linking strategy. Covers keyword intent analysis, content architecture, on-page optimization, and content planning for SaaS."
---

# SEO & Content Strategy

SEO is a long game that compounds. This skill helps you build a content strategy that drives organic signups — starting with the pages that matter most.

For technical SEO (site speed, schema markup, crawlability, GEO), see the **technical-seo-expert** skill.

## Core Principles

- SEO is not gaming Google — it's structuring content so it's findable and useful.
- Content quality and relevance determine rankings. Technical SEO is table stakes.
- Target intent, not just keywords. "Best CRM" and "CRM pricing" have completely different searchers.
- One page per intent. Cannibalizing your own rankings is the most common SaaS SEO mistake.
- Internal linking is your most underused lever.

---

## SEO Timeline: Set Realistic Expectations

| Timeframe | What to Expect |
|-----------|---------------|
| Month 1-2 | Pages indexed, minimal traffic. Focus on building content. |
| Month 3-4 | Long-tail keywords start ranking (page 2-3). |
| Month 5-6 | Some pages reach page 1 for low-competition terms. |
| Month 6-12 | Compound growth as domain authority builds. |

**Reality check:** SEO takes 3-6 months to show results. If you need signups this week, use paid ads or outreach. SEO is the engine you build now so you're not paying for every click forever.

---

## Content Architecture for SaaS

Build your site structure around search intent, not your org chart.

### High-Priority Pages (Build First)

| Page Type | URL Pattern | Search Intent |
|-----------|------------|---------------|
| Homepage | `/` | Branded searches, direct traffic |
| Feature pages | `/features/[feature]` | "How to [solve problem]" |
| Pricing page | `/pricing` | "[Product] pricing", "[category] pricing" |
| Comparison pages | `/compare/[competitor]` | "[Product] vs [Competitor]" |
| Use case pages | `/for/[audience]` | "[Category] for [role/industry]" |

### Content Pages (Build Over Time)

| Page Type | URL Pattern | Search Intent |
|-----------|------------|---------------|
| How-to guides | `/blog/how-to-[action]` | Tutorials that drive signups |
| Listicles | `/blog/best-[category]` | "Best [category] tools" — feature your product |
| Guides | `/blog/[topic]-guide` | Comprehensive mid-funnel content |
| Templates | `/templates/[use-case]` | "[Use case] template" — free value |
| Glossary | `/glossary/[term]` | "What is [term]?" — top-of-funnel |

**Tell AI:**
```
Create a content architecture for our SaaS product [name]:
- Product solves [problem] for [audience]
- Main features: [list features]
- Top 3 competitors: [list competitors]
Generate a sitemap with URL patterns for: homepage, feature pages, comparison pages,
use case pages, and initial blog post ideas. Prioritize by search intent value.
```

---

## Keyword Intent Mapping

Every keyword has an intent. Match your page type to the intent:

| Intent | Example Searches | Best Page Type |
|--------|-----------------|----------------|
| **Informational** | "what is [concept]", "how to [action]" | Blog post, glossary entry |
| **Navigational** | "[your brand] login", "[your brand] pricing" | Ensure YOUR pages rank #1 |
| **Commercial** | "best [category] tools", "[tool A] vs [tool B]" | Comparison page, listicle |
| **Transactional** | "[category] pricing", "buy [product]" | Pricing page, signup page |

**Tell AI:**
```
Do keyword research for our product [name] in the [category] space:
- Find 20 keywords our ICP would search for
- Classify each by intent (informational, navigational, commercial, transactional)
- Estimate competition level (low, medium, high)
- Recommend which page type to create for each keyword
- Prioritize: low competition + high intent first
```

---

## On-Page Optimization

For every page, get these elements right:

### Meta Tags

**Tell AI:**
```
Write SEO-optimized meta tags for our [page type] page about [topic]:
- Title tag: 50-60 characters, primary keyword near the front
- Meta description: 120-155 characters, include value prop and CTA language
- Open Graph tags (og:title, og:description, og:image) for social sharing
```

### Meta Tag Templates

| Page Type | Title Format | Description Format |
|-----------|-------------|-------------------|
| Homepage | `[Product] — [Value Prop] \| [Category]` | `[Product] helps [audience] [outcome]. [Differentiator]. Start free.` |
| Feature page | `[Feature] — [Benefit] \| [Product]` | `[How feature works] to help you [outcome]. Try it free.` |
| Blog post | `[Keyword-Rich Title] — [Product] Blog` | `[What reader learns]. [Why it matters]. [Specific detail for click].` |
| Comparison | `[Product] vs [Competitor] — [Year] Comparison` | `Compare [Product] and [Competitor] on [key factors]. See which is right for you.` |

### Heading Structure

- One `<h1>` per page matching the primary keyword intent
- `<h2>` headings for each major section
- `<h3>` for subsections — no skipping levels
- Headings should read as a scannable outline of the page

### Image Optimization

**Tell AI:**
```
Optimize all images on [page]:
- Add descriptive alt text (include relevant keywords naturally, max 125 chars)
- Serve in WebP or AVIF format
- Set explicit width and height to prevent layout shift
- Lazy-load images below the fold
```

---

## Internal Linking Strategy

Internal links are free and high-impact. Use them intentionally.

### Rules

- Every blog post links to at least 1 feature/product page
- Every feature page links to related features and relevant blog posts
- Use descriptive anchor text: "our workflow automation feature" not "click here"
- Create hub pages that link to all content in a topic cluster

### Topic Clusters

Group content around themes. Each cluster has:
1. **Pillar page** — Comprehensive overview (e.g., "Complete Guide to [Topic]")
2. **Cluster pages** — Specific subtopics (e.g., "How to [specific action]")
3. **Internal links** — Every cluster page links to the pillar. Pillar links to all clusters.

**Tell AI:**
```
Build an internal linking plan for our site:
- Audit existing pages and identify linking opportunities
- For each blog post, suggest 2-3 internal links to product/feature pages
- For each feature page, suggest 2-3 links to related blog posts
- Identify gaps: pages with zero internal links pointing to them
- Use descriptive anchor text (not "click here" or "learn more")
```

---

## Content Planning

### Prioritization Framework

Write content in this order:

1. **Bottom-of-funnel first:** Comparison pages, pricing page, feature pages — these convert
2. **Mid-funnel:** How-to guides, use case pages — these build authority
3. **Top-of-funnel:** Glossary, broad guides — these drive volume (but lower conversion)

### Content Calendar (Simple Version)

**Tell AI:**
```
Create a 3-month content calendar for our SaaS blog:
- Product: [name], solves [problem] for [audience]
- Goal: drive organic signups
- Mix: 2 bottom-funnel pieces, 2 mid-funnel pieces, 1 top-funnel piece per month
- For each piece: title, target keyword, intent, URL, and brief outline
```

---

## Measuring SEO Results

| Metric | Tool | What It Tells You |
|--------|------|------------------|
| Organic traffic | Google Search Console (free) | How many people find you via search |
| Keyword rankings | Google Search Console | Which queries you appear for and position |
| Click-through rate | Google Search Console | Whether your titles/descriptions earn clicks |
| Organic signups | Your analytics tool | Whether SEO traffic actually converts |

**Tell AI:**
```
Set up SEO tracking:
- Connect Google Search Console to our site
- Add UTM parameters to track organic → signup conversion
- Create a monthly report: top 10 pages by organic traffic, top 10 keywords by impressions,
  click-through rate by page, and organic signup count
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Writing content with no keyword research | Research first. Every page should target a specific keyword + intent. |
| Targeting high-competition keywords first | Start with long-tail, low-competition keywords. Build authority before going after "CRM software". |
| No internal links | Link every page to related pages. It's free and high-impact. |
| Duplicate intent across pages | One page per search intent. Don't create 3 blog posts targeting the same keyword. |
| Expecting results in 2 weeks | SEO takes 3-6 months. Track progress monthly, not daily. |
| Ignoring existing content | Update and improve old content before writing new. A refreshed page ranks faster than a new one. |
