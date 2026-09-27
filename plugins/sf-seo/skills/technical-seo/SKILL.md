---
name: technical-seo
description: "Use this skill to implement technical SEO optimizations in code — meta tags, schema markup, Core Web Vitals, crawlability, robots.txt, sitemaps, and GEO (Generative Engine Optimization) for AI search engines. This is the implementation skill — for strategy see seo, for content writing see seo-content, for auditing see seo-audit."
---

# Technical SEO Implementation

This skill is the implementation reference for technical SEO. Use it when you need to add, fix, or optimize SEO elements in code — meta tags, schema markup, Core Web Vitals, crawlability, and GEO.

This skill covers **how to implement in code**. For the other SEO concerns:
- **seo** — Strategy and planning (keyword research, content architecture, what to build)
- **seo-content** — Writing content (briefs, humanized prose, SERP feature targeting)
- **seo-audit** — Auditing an existing codebase (scan, diagnose, produce action plan)

---

## Metadata

Every indexable page needs these elements correct:

- **Title tag:** 50-60 chars, primary keyword front-loaded
- **Meta description:** 120-155 chars, includes CTA
- **Canonical:** self-referencing or correct target
- **Robots:** no accidental noindex
- **Open Graph:** og:title, og:description, og:image for social sharing

For detailed specs and code examples, see [ON-PAGE-SEO.md](ON-PAGE-SEO.md).

## HTML Structure

- Exactly one H1 per page, contains primary keyword
- No skipped header levels (H1 → H2 → H3)
- Semantic HTML: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`

## Crawlability

- robots.txt exists, not blocking important paths
- XML sitemap exists, all important URLs included
- Canonical tags on every page
- No orphan pages, proper internal linking

For detailed crawlability checklist, see [TECHNICAL-AUDIT.md](TECHNICAL-AUDIT.md).

## Core Web Vitals

Target metrics (2026 thresholds):

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | 2.5s - 4s | > 4s |
| **INP** (Interaction to Next Paint) | ≤ 200ms | 200ms - 500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | 0.1 - 0.25 | > 0.25 |

**Note**: INP replaced FID as a Core Web Vital in March 2024.

For optimization techniques (LCP, INP, CLS), see [TECHNICAL-AUDIT.md](TECHNICAL-AUDIT.md).

## E-E-A-T & Schema

| Signal | Implementation |
|--------|----------------|
| **Experience** | First-hand testing, case studies, original photos |
| **Expertise** | Author credentials, certifications |
| **Authoritativeness** | Quality backlinks, industry mentions |
| **Trustworthiness** | HTTPS, contact info, privacy policy, citations |

Required JSON-LD schema: Organization, WebSite, Article/BlogPosting, FAQPage, BreadcrumbList, Person (author).

For schema code examples and author bio templates, see [EEAT-AND-SCHEMA.md](EEAT-AND-SCHEMA.md).

## GEO (Generative Engine Optimization)

Optimize for AI-powered search engines:

| Aspect | Traditional SEO | GEO |
|--------|----------------|-----|
| **Goal** | Rank in search results | Be cited in AI answers |
| **Success Metric** | Click-through rate | Citation frequency |
| **Approach** | Keywords, backlinks | Entity clarity, authority signals |
| **Optimization** | Pages and snippets | Citable facts and answers |

For GEO techniques, llms.txt implementation, and AI crawler management, see [GEO.md](GEO.md).

---

## Fix Priorities

When issues are identified, fix in this order:

### Priority 1: Critical (Fix Immediately)
- 404 errors and broken links
- Missing or duplicate title tags
- Broken canonical tags
- noindex on important pages
- HTTPS/security issues
- Blocked by robots.txt

### Priority 2: High (Fix Within 1 Week)
- Core Web Vitals failures
- Missing meta descriptions
- Multiple H1 tags
- Missing alt text on key images
- Orphan pages (no internal links)
- Missing schema markup

### Priority 3: Medium (Fix Within 1 Month)
- Thin content pages
- Header hierarchy issues
- Internal link optimization
- Image optimization (format, compression)
- Anchor text improvements
- Content freshness updates

### Priority 4: Low (Ongoing Optimization)
- A/B testing improvements
- Advanced schema types
- International SEO expansion
- New content for topic clusters
- Competitive gap analysis

---

## Post-Fix Validation

After applying fixes:

1. **Re-crawl** the affected pages
2. **Verify** DOM changes are live
3. **Check** robots.txt isn't blocking new paths
4. **Validate** schema with Google's Rich Results Test
5. **Test** Core Web Vitals with Lighthouse
6. **Monitor** Search Console for indexing issues

---

## Monitoring Cadence

**Daily:** Check Search Console for crawl errors. Monitor site uptime. Review security alerts.

**Weekly:** Review Core Web Vitals trends. Check for new 404s. Monitor AI referral traffic. Review ranking changes.

**Monthly:** Full technical audit. Content freshness review. Backlink profile analysis. Schema validation.

**Quarterly:** Full SEO strategy review. GEO performance analysis. Content gap analysis.

---

## Quick Reference

### SEO Specifications

| Element | Specification |
|---------|---------------|
| Title Tag | 50-60 chars, keyword front-loaded |
| Meta Description | 120-155 chars, includes CTA |
| H1 | Exactly 1 per page, contains keyword |
| URL | Lowercase, hyphens, descriptive |
| Images | WebP/AVIF, <200KB, alt text, dimensions |
| Canonical | Self-referencing on every page |
| robots.txt | Allow important paths, block admin |
| Sitemap | All indexable URLs, lastmod dates |

### GEO Checklist

| Element | Required |
|---------|----------|
| FAQPage Schema | Yes |
| Answer-first content | Yes |
| Statistics with sources | Yes |
| Expert quotes | Recommended |
| TL;DR blocks | Recommended |
| llms.txt | Recommended |
| Fresh content (<90 days) | Yes |

---

## Supporting Files

- [TECHNICAL-AUDIT.md](TECHNICAL-AUDIT.md) — Core Web Vitals optimization, crawlability, mobile-first, HTTPS
- [ON-PAGE-SEO.md](ON-PAGE-SEO.md) — Title tags, meta descriptions, headers, images, internal linking
- [EEAT-AND-SCHEMA.md](EEAT-AND-SCHEMA.md) — E-E-A-T implementation, schema markup library (JSON-LD)
- [GEO.md](GEO.md) — Generative Engine Optimization, llms.txt, AI crawlers, framework-specific SEO

---

## Version History

- **v3.0** (March 2026): Reframed as implementation reference (auditing moved to seo-audit skill), added cross-references to seo-content and seo skills, standardized meta description spec to 120-155 chars
- **v2.0** (December 2025): Added GEO section, AI crawler management, llms.txt, GA4 AI tracking, updated Core Web Vitals (INP), expanded schema library, framework-specific guides
- **v1.0** (December 2024): Initial version with technical audit, on-page SEO, basic schema
