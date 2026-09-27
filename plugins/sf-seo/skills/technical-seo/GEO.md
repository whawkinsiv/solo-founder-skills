# GEO (Generative Engine Optimization)

How to get your content cited by AI search engines (ChatGPT, Perplexity, Google AI Overviews). This matters alongside traditional SEO — AI referrals to websites increased 357% year-over-year.

---

## SEO vs. GEO

| Aspect | Traditional SEO | GEO |
|--------|----------------|-----|
| **Goal** | Rank in search results | Be cited in AI answers |
| **Success Metric** | Click-through rate | Citation frequency |
| **Approach** | Keywords, backlinks | Entity clarity, authority signals |
| **Optimization** | Pages and snippets | Citable facts and answers |

**Key Stats (2025):**
- AI Overviews appear for 15-30% of queries
- ChatGPT has 400M+ weekly users
- Pages with FAQ schema are 3.2x more likely to appear in AI Overviews
- Content updated within 90 days gets cited 40-60% more

---

## GEO Content Techniques

The key insight: AI search engines cite content that is **directly quotable** — clear answers, specific statistics, and well-structured facts.

### Write Answer-First Content

Lead with the direct answer, then explain. AI engines extract the first clear answer they find.

**Tell AI:**
```
Restructure [page URL] for AI citation optimization:
- Lead each section with a direct, quotable answer (1-2 sentences)
- Add a TL;DR block at the top summarizing the page in 3-4 sentences
- Include statistics with source citations (e.g., "53% of traffic comes from organic search — BrightEdge, 2024")
- Use tables for any comparisons (AI extracts tabular data well)
- Define key terms explicitly ("X is defined as...")
- Add expert quotes where relevant
```

### GEO Content Checklist

- [ ] **Answer-first structure:** Lead with direct answers, not buildup
- [ ] **TL;DR blocks:** Summarize key points at section starts
- [ ] **Statistics with sources:** Include data with citations (year + source)
- [ ] **Expert quotes:** Add quotes from recognized authorities
- [ ] **FAQ schema:** Implement FAQPage markup (see [EEAT-AND-SCHEMA.md](EEAT-AND-SCHEMA.md))
- [ ] **Tables for comparisons:** AI extracts tabular data well
- [ ] **Clear entity definitions:** Define key terms explicitly
- [ ] **Fresh content:** Update within 90 days for best citation rates

---

## llms.txt

A new standard that helps AI systems understand your site. Place at `yoursite.com/llms.txt`.

**Tell AI:**
```
Create an llms.txt file for our site with:
- Company name and one-line description
- "About" section (who we are, what we do, our expertise)
- "Services/Products" section with links and descriptions
- "Key Resources" section linking to our best content
- Contact information

Place at /llms.txt with content-type text/plain, UTF-8 encoding.
```

---

## AI Crawler Management

AI crawlers fall into two categories. You want to allow search crawlers (they cite you) and optionally block training crawlers (they just scrape your content).

| Crawler | Company | Purpose | Recommend |
|---------|---------|---------|-----------|
| OAI-SearchBot | OpenAI | Real-time search results | Allow |
| ChatGPT-User | OpenAI | User browsing via ChatGPT | Allow |
| PerplexityBot | Perplexity | Search retrieval | Allow |
| GPTBot | OpenAI | Training data | Block (optional) |
| ClaudeBot | Anthropic | Training/retrieval | Block (optional) |
| CCBot | Common Crawl | Archive/training | Block (optional) |
| Google-Extended | Google | AI training | Block (optional) |

**Tell AI:**
```
Update robots.txt to manage AI crawlers:
- Allow: OAI-SearchBot, PerplexityBot, ChatGPT-User (these cite us in search results)
- Block: GPTBot, ClaudeBot, CCBot, Google-Extended (training crawlers, no direct benefit)
```

---

## Tracking AI Traffic

Set up tracking to see how much traffic comes from AI search engines.

**Tell AI:**
```
Set up AI referral tracking in our analytics:
- Create a custom channel group called "AI Tools"
- Include these referrer domains: chatgpt.com, chat.openai.com, perplexity.ai, claude.ai, gemini.google.com, copilot.microsoft.com
- Track as a separate traffic source from regular referrals
- Add a custom event that fires when a visitor arrives from an AI referrer
```

---

## When to Focus on GEO

**Start with GEO when:**
- You already have content that ranks in traditional search
- You're publishing educational/informational content (not just product pages)
- Your audience uses AI search tools (most B2B SaaS audiences do)

**Skip GEO for now if:**
- You don't have a blog or content strategy yet
- Your site is purely a web app with no public content
- You're still pre-launch

**Priority:** Get traditional SEO basics right first (see [TECHNICAL-AUDIT.md](TECHNICAL-AUDIT.md) and [ON-PAGE-SEO.md](ON-PAGE-SEO.md)), then layer in GEO techniques.
