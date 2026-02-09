# Technical SEO Audit

Detailed technical audit procedures, Core Web Vitals optimization, crawlability, mobile-first indexing, and HTTPS configuration.

---

## Technical Audit Phase

When asked to "audit for SEO", follow this comprehensive sequence:

### Step 1: Crawl & Render Check

Visit the target URL and verify:

```javascript
// Technical SEO Crawl Checklist
const technicalChecklist = {
  metadata: {
    title: { minChars: 50, maxChars: 60, check: 'Front-loaded keyword' },
    metaDescription: { minChars: 150, maxChars: 160, check: 'Includes CTA' },
    canonical: { required: true, check: 'Self-referencing or correct target' },
    robots: { check: 'No accidental noindex' }
  },
  structure: {
    h1: { count: 1, check: 'Contains primary keyword' },
    headerHierarchy: { check: 'No skipped levels (H1->H2->H3)' },
    semanticHTML: { check: '<header>, <nav>, <main>, <article>, <section>' }
  },
  crawlability: {
    robotsTxt: { exists: true, check: 'Not blocking important paths' },
    sitemapXml: { exists: true, check: 'All important URLs included' },
    internalLinks: { check: 'No orphan pages, proper anchor text' }
  }
};
```

### Step 2: Schema.org Validation

Check for and validate JSON-LD structures:
- `Organization` - Company/brand identity
- `WebSite` - Site-level info with SearchAction
- `Article` / `BlogPosting` - Content pages
- `Product` - E-commerce items
- `FAQPage` - FAQ sections (critical for GEO)
- `BreadcrumbList` - Navigation path
- `Person` - Author credentials (E-E-A-T)
- `HowTo` - Step-by-step content

---

## Core Web Vitals Optimization

### LCP Optimization (Target: < 2.5s)

```html
<!-- Preload critical LCP image -->
<link rel="preload" as="image" href="/hero-image.webp" fetchpriority="high">

<!-- Hero image with high priority -->
<img src="/hero.webp" fetchpriority="high" alt="Description" width="1200" height="600">

<!-- Preconnect to critical third-parties -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://cdn.example.com" crossorigin>
```

### INP Optimization (Target: < 200ms)

```javascript
// Yield to main thread for heavy operations
async function handleClick() {
  // Immediate visual feedback
  button.classList.add('active');

  // Yield to allow browser to paint
  await scheduler.yield();

  // Then perform heavy work
  performExpensiveOperation();
}

// Use requestIdleCallback for non-urgent tasks
requestIdleCallback(() => {
  analytics.track('event', data);
});

// Code split heavy modules
button.addEventListener('click', async () => {
  const { heavyModule } = await import('./heavy-module.js');
  heavyModule.process();
});
```

### CLS Optimization (Target: < 0.1)

```html
<!-- Always set explicit dimensions -->
<img src="/photo.webp" width="800" height="600" alt="Photo">
<video width="1920" height="1080" poster="/thumb.jpg"></video>

<!-- Use aspect-ratio for responsive elements -->
<style>
.responsive-image { aspect-ratio: 16 / 9; width: 100%; height: auto; }
.ad-container { min-height: 250px; } /* Reserve space for ads */
.font-loading { font-display: optional; } /* Prevent layout shift from fonts */
</style>
```

---

## Crawlability & Indexability

### robots.txt Best Practices (2025)

```
# robots.txt - SEO + GEO Optimized

User-agent: *
Allow: /
Disallow: /admin/
Disallow: /cart/
Disallow: /checkout/
Disallow: /account/
Disallow: /api/
Disallow: /*?utm_
Disallow: /*?session=

# Traditional Search Engines
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# AI Search Crawlers (Allow - provides citations)
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ChatGPT-User
Allow: /

# AI Training Crawlers (Block if desired - no direct SEO benefit)
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Google-Extended
Disallow: /

Sitemap: https://example.com/sitemap.xml
```

### XML Sitemap Requirements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>https://example.com/page</loc>
    <lastmod>2025-12-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://example.com/images/page.webp</image:loc>
      <image:title>Page Image Title</image:title>
    </image:image>
  </url>
</urlset>
```

### Canonical Tag Implementation

```html
<!-- Self-referencing canonical (every page needs one) -->
<link rel="canonical" href="https://example.com/current-page">

<!-- Parameter handling - point to clean URL -->
<!-- URL: https://example.com/page?color=blue&utm_source=email -->
<link rel="canonical" href="https://example.com/page">
```

---

## Mobile-First Indexing

```html
<!-- Required viewport meta tag -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

```css
/* Mobile-first CSS approach */
.container { width: 100%; padding: 1rem; }

/* Touch targets - minimum 48x48px */
.button, .link { min-height: 48px; min-width: 48px; padding: 12px 24px; }

/* Readable font size - minimum 16px */
body { font-size: 16px; line-height: 1.6; }

/* Tablet breakpoint */
@media (min-width: 768px) {
  .container { max-width: 720px; margin: 0 auto; }
}

/* Desktop breakpoint */
@media (min-width: 1024px) {
  .container { max-width: 1200px; }
}
```

---

## HTTPS & Security

```nginx
# Nginx SSL Configuration
server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers off;

    # HSTS (HTTP Strict Transport Security)
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;

    # Security headers
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name example.com;
    return 301 https://$server_name$request_uri;
}
```

---

## Common Fix Patterns

### Fix Missing Meta Tags

```javascript
// Search for pages with missing/short titles
async function findMetaIssues(urls) {
  const issues = [];
  for (const url of urls) {
    const page = await puppeteer.goto(url);
    const title = await page.$eval('title', el => el.textContent);
    const metaDesc = await page.$eval('meta[name="description"]', el => el.content).catch(() => '');

    if (!title || title.length < 30) {
      issues.push({ url, issue: 'title_too_short', value: title });
    }
    if (title && title.length > 60) {
      issues.push({ url, issue: 'title_too_long', value: title.length });
    }
    if (!metaDesc || metaDesc.length < 70) {
      issues.push({ url, issue: 'meta_desc_too_short', value: metaDesc });
    }
  }
  return issues;
}
```

### Convert Non-Semantic HTML

```html
<!-- Before (non-semantic) -->
<div class="header">...</div>
<div class="navigation">...</div>
<div class="content">...</div>
<div class="sidebar">...</div>
<div class="footer">...</div>

<!-- After (semantic) -->
<header>...</header>
<nav>...</nav>
<main>
  <article>...</article>
</main>
<aside>...</aside>
<footer>...</footer>
```

### Implement Lazy Loading

```html
<!-- Before -->
<img src="/image.webp" alt="Description">

<!-- After -->
<img src="/image.webp" alt="Description" loading="lazy" decoding="async" width="800" height="600">

<!-- Exception: LCP/above-fold images -->
<img src="/hero.webp" alt="Hero" fetchpriority="high" width="1200" height="600">
```

---

## SEO Audit Report Template

When delivering audit results, use this structure:

```markdown
# SEO Audit Report: [Website]
**Date:** [Date]
**Auditor:** [Name]

## Executive Summary
- Overall SEO Score: [X/100]
- Critical Issues: [X]
- High Priority Issues: [X]
- Medium Priority Issues: [X]

## Core Web Vitals
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| LCP    | X.Xs    | <2.5s  | pass/fail |
| INP    | Xms     | <200ms | pass/fail |
| CLS    | X.XX    | <0.1   | pass/fail |

## Critical Issues (Fix Immediately)
1. [Issue] - [Page] - [Recommendation]
2. ...

## High Priority Issues
1. [Issue] - [Page] - [Recommendation]
2. ...

## GEO Readiness
- FAQPage Schema: yes/no
- Answer-first content: yes/no
- E-E-A-T signals: yes/no
- AI crawler accessibility: yes/no

## Recommendations
1. [Recommendation with expected impact]
2. ...

## Next Steps
1. [Action item]
2. ...
```
