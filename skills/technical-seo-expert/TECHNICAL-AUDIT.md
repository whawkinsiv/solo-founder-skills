# Technical SEO Audit

Step-by-step audit process, Core Web Vitals targets, crawlability essentials, and common fix patterns. Focus on what you check and what you ask AI to fix.

---

## Running a Technical Audit

When asked to "audit for SEO", check these in order:

### 1. Metadata Check

For every important page, verify:

| Element | Requirement | How to Check |
|---------|------------|--------------|
| Title tag | 50-60 chars, primary keyword front-loaded | View page source or browser tab |
| Meta description | 150-160 chars, includes CTA | View page source |
| Canonical tag | Self-referencing on every page | View page source, look for `<link rel="canonical">` |
| Robots tag | No accidental `noindex` on important pages | View page source |

**Tell AI:**
```
Audit metadata for these pages: [list your important pages]
For each page, check:
- Title tag length and keyword placement
- Meta description length and CTA
- Canonical tag (should point to itself)
- No accidental noindex
Report issues in a table with page URL, issue, and fix.
```

### 2. Structure Check

| Element | Requirement |
|---------|------------|
| H1 tag | Exactly one per page, contains primary keyword |
| Header hierarchy | No skipped levels (H1 → H2 → H3, never H1 → H3) |
| Semantic HTML | Uses `<header>`, `<nav>`, `<main>`, `<article>`, `<section>` |

**Tell AI:**
```
Check HTML structure for [page URL]:
- Verify exactly one H1 tag per page
- Check header hierarchy (no skipped levels)
- Verify semantic HTML elements are used properly
Fix any issues found.
```

### 3. Schema Validation

Check for these JSON-LD schema types (AI can add them all):

| Schema Type | Where It Goes | Why It Matters |
|-------------|---------------|----------------|
| Organization | Homepage | Brand identity in search |
| WebSite | Homepage | Sitelinks search box |
| Article / BlogPosting | Blog posts | Rich results, author info |
| FAQPage | FAQ sections | Featured snippets + AI citations |
| BreadcrumbList | All pages | Navigation path in search results |
| Person | Author pages | E-E-A-T signals |

**Tell AI:**
```
Add JSON-LD schema markup to the site:
- Organization schema on homepage
- FAQPage schema on any page with FAQ content
- Article schema on blog posts (include author, date published, date modified)
- BreadcrumbList schema on all pages
Validate the output with Google's Rich Results Test.
```

---

## Core Web Vitals

These are Google's page experience signals. Your hosting platform handles most of this, but check anyway.

### Targets (2025)

| Metric | Good | Needs Work | Poor |
|--------|------|------------|------|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | 2.5s - 4s | > 4s |
| **INP** (Interaction to Next Paint) | ≤ 200ms | 200ms - 500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | 0.1 - 0.25 | > 0.25 |

**How to check:** Go to [PageSpeed Insights](https://pagespeed.web.dev/), enter your URL, and review the scores.

### Common Fixes

**Tell AI:**
```
Optimize Core Web Vitals for [page URL]:

For LCP (page loads too slowly):
- Preload the largest image on the page
- Add fetchpriority="high" to the hero image
- Preconnect to third-party domains (fonts, CDNs)

For INP (interactions feel sluggish):
- Code split heavy JavaScript modules
- Defer non-critical scripts
- Add immediate visual feedback on button clicks

For CLS (layout shifts/jumping):
- Add width and height attributes to all images and videos
- Use aspect-ratio CSS for responsive elements
- Reserve space for ads or dynamic content
```

---

## Crawlability Essentials

### robots.txt

Your robots.txt file tells search engines what to crawl. Place it at `yoursite.com/robots.txt`.

**Tell AI:**
```
Create a robots.txt file that:
- Allows all important pages to be crawled
- Blocks admin, cart, checkout, and account pages
- Blocks URL parameters (?utm_, ?session=)
- Allows AI search crawlers (OAI-SearchBot, PerplexityBot, ChatGPT-User)
- Blocks AI training crawlers (GPTBot, ClaudeBot, CCBot, Google-Extended)
- Includes a link to the XML sitemap
```

### XML Sitemap

Your sitemap tells search engines what pages exist. Most frameworks auto-generate this.

**Tell AI:**
```
Set up an XML sitemap at /sitemap.xml that:
- Includes all indexable pages
- Includes lastmod dates
- Excludes admin, auth, and utility pages
- Is referenced in robots.txt
Submit it to Google Search Console after deployment.
```

### Canonical Tags

Every page should have a self-referencing canonical tag to prevent duplicate content issues.

**Tell AI:**
```
Add self-referencing canonical tags to every page.
For pages with URL parameters (like ?utm_source), the canonical should point to the clean URL without parameters.
```

---

## Mobile-First

Google indexes the mobile version of your site first. Check:

- [ ] Viewport meta tag is set (`width=device-width, initial-scale=1.0`)
- [ ] Text is readable without zooming (minimum 16px font)
- [ ] Buttons/links are tap-friendly (minimum 48x48px)
- [ ] No horizontal scrolling on mobile

**Tell AI:**
```
Verify mobile-first best practices:
- Viewport meta tag is present
- Minimum font size is 16px
- Touch targets are at least 48x48px
- No content overflows horizontally on mobile
Fix any issues found.
```

---

## HTTPS & Security Headers

- [ ] Site loads on HTTPS (not HTTP)
- [ ] HTTP redirects to HTTPS automatically
- [ ] Security headers are set (most hosting platforms handle this)

**Tell AI:**
```
Verify HTTPS and security headers:
- Confirm HTTPS is enforced (HTTP redirects to HTTPS)
- Add security headers: Strict-Transport-Security, X-Content-Type-Options, X-Frame-Options
- If using Vercel/Netlify/Railway, check if these are set by default.
```

---

## Audit Report Template

After running an audit, organize findings like this:

**Tell AI:**
```
Generate an SEO audit report for [site URL] with:
- Executive summary (overall score, critical/high/medium issue counts)
- Core Web Vitals scores (LCP, INP, CLS with pass/fail)
- Critical issues (fix immediately): broken links, missing titles, noindex errors
- High priority issues (fix this week): missing meta descriptions, multiple H1s, missing schema
- Medium priority issues (fix this month): image optimization, header hierarchy, internal linking
- Recommendations ranked by impact
```
