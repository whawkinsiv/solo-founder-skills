# GEO (Generative Engine Optimization)

Optimizing for AI-powered search engines, llms.txt implementation, AI crawler management, tracking AI traffic, international SEO, and framework-specific SEO guides.

---

## What is GEO?

GEO optimizes content for AI-powered search engines (ChatGPT, Perplexity, Google AI Overviews, Claude). The goal shifts from ranking on SERPs to **becoming the source AI systems cite**.

| Aspect | Traditional SEO | GEO |
|--------|----------------|-----|
| **Goal** | Rank in search results | Be cited in AI answers |
| **Success Metric** | Click-through rate | Citation frequency |
| **Approach** | Keywords, backlinks | Entity clarity, authority signals |
| **Optimization** | Pages and snippets | Citable facts and answers |

**Key Statistics (2025):**
- AI Overviews appear for 15-30% of queries
- ChatGPT has 400M+ weekly users
- AI referrals to websites increased 357% YoY
- Traditional search volume predicted to drop 25% by 2026

---

## GEO Optimization Techniques

### Answer-First Content Structure

```html
<article>
  <!-- Direct answer immediately -->
  <h1>What is On-Page SEO?</h1>

  <!-- TL;DR block - highly citable -->
  <aside class="tldr">
    <strong>TL;DR:</strong> On-page SEO is the practice of optimizing individual
    web pages to rank higher in search engines. Key elements include title tags,
    meta descriptions, headers, content quality, and internal linking.
  </aside>

  <!-- Main definition - quotable -->
  <p><strong>On-page SEO</strong> refers to all optimization measures taken
  directly within a website to improve its position in search rankings.
  According to industry expert Rand Fishkin, "On-page SEO is the foundation
  upon which all other SEO efforts are built."</p>

  <!-- Statistics with citations -->
  <h2>Key Statistics</h2>
  <ul>
    <li><strong>53%</strong> of website traffic comes from organic search (BrightEdge, 2024)</li>
    <li>Title tags are the <strong>#1 on-page ranking factor</strong> (Moz, 2025)</li>
    <li>Pages with FAQ schema are <strong>3.2x more likely</strong> to appear in AI Overviews</li>
  </ul>
</article>
```

### GEO Content Checklist

- [ ] **Answer-first structure**: Lead with direct answers
- [ ] **TL;DR blocks**: Summarize key points at section starts
- [ ] **Statistics with sources**: Include data with citations
- [ ] **Expert quotes**: Add quotes from recognized authorities
- [ ] **FAQ schema**: Implement FAQPage markup
- [ ] **Tables for comparisons**: AI extracts tabular data well
- [ ] **Clear entity definitions**: Define key terms explicitly
- [ ] **Recent updates**: Content updated within 90 days cites 40-60% more

---

## llms.txt Implementation

Create `/llms.txt` at your domain root:

```markdown
# Company Name

> Brief description of your company/site in 1-2 sentences.

## About
Comprehensive description of who you are, what you do, and your expertise.

## Services
- [Service 1](/services/service-1): Brief description
- [Service 2](/services/service-2): Brief description

## Key Resources
- [Resource 1](/resources/guide): Description of this resource
- [Resource 2](/blog/important-article): Description

## Contact
- Email: contact@example.com
- Phone: +1-800-555-1234
```

**Technical Requirements:**
- Location: `yoursite.com/llms.txt`
- HTTP Status: 200
- MIME Type: text/plain
- Encoding: UTF-8

---

## AI Crawler Management

**Major AI Crawlers (2025):**

| Crawler | Company | Purpose |
|---------|---------|---------|
| GPTBot | OpenAI | Training data |
| OAI-SearchBot | OpenAI | Real-time search |
| ChatGPT-User | OpenAI | User browsing |
| ClaudeBot | Anthropic | Training/retrieval |
| PerplexityBot | Perplexity | Search retrieval |
| Google-Extended | Google | AI training |
| CCBot | Common Crawl | Archive/training |

**Strategic robots.txt (Allow search, block training):**

```
# AI Search (Allow - provides citations)
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ChatGPT-User
Allow: /

# AI Training (Block - no direct SEO benefit)
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Google-Extended
Disallow: /
```

---

## Tracking AI Traffic in GA4

### Custom Channel Group Setup

1. Navigate to: Admin > Data settings > Channel groups
2. Create category: "AI Tools"
3. Add regex rule:
```regex
(chatgpt\.com|chat\.openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|copilot\.microsoft\.com)
```
4. Place above default "Referral" rule

### AI Referral Tracking Script

```javascript
// Track AI referral sources
(function() {
  const aiReferrers = [
    'chat.openai.com', 'chatgpt.com', 'perplexity.ai',
    'claude.ai', 'gemini.google.com', 'copilot.microsoft.com'
  ];

  const referrer = document.referrer.toLowerCase();
  const isAIReferral = aiReferrers.some(source => referrer.includes(source));

  if (isAIReferral && typeof gtag !== 'undefined') {
    gtag('event', 'ai_referral', {
      'ai_source': referrer.split('/')[2],
      'referrer_url': referrer
    });
  }
})();
```

---

## International SEO

### Hreflang Implementation (HTML Method)

```html
<head>
  <link rel="alternate" hreflang="en-us" href="https://example.com/page">
  <link rel="alternate" hreflang="en-gb" href="https://example.co.uk/page">
  <link rel="alternate" hreflang="de-de" href="https://example.de/seite">
  <link rel="alternate" hreflang="x-default" href="https://example.com/page">
</head>
```

### Hreflang Implementation (Sitemap Method for Large Sites)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://example.com/page</loc>
    <xhtml:link rel="alternate" hreflang="en-us" href="https://example.com/page"/>
    <xhtml:link rel="alternate" hreflang="en-gb" href="https://example.co.uk/page"/>
    <xhtml:link rel="alternate" hreflang="de-de" href="https://example.de/seite"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/page"/>
  </url>
</urlset>
```

**Rules:**
- Every page must reference ALL language versions (including itself)
- Always include `x-default` for unmatched users
- Hreflang must be reciprocal (A→B means B→A required)

---

## Framework-Specific SEO

### Next.js (App Router, 14+)

```typescript
// app/page.tsx
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Page Title | Brand',
  description: 'Page description under 160 characters',
  alternates: {
    canonical: 'https://example.com/page',
  },
  openGraph: {
    title: 'OG Title',
    description: 'OG Description',
    images: ['/og-image.jpg'],
  },
};

export default function Page() {
  return <main>...</main>;
}
```

### Next.js Dynamic Metadata

```typescript
// app/blog/[slug]/page.tsx
export async function generateMetadata({ params }): Promise<Metadata> {
  const post = await getPost(params.slug);

  return {
    title: post.title,
    description: post.excerpt,
    alternates: {
      canonical: `https://example.com/blog/${params.slug}`,
    },
  };
}
```

### Next.js JSON-LD

```typescript
// app/layout.tsx
export default function RootLayout({ children }) {
  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: 'Example Company',
    url: 'https://example.com',
  };

  return (
    <html>
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

### React SPA SEO

For client-side React apps, use pre-rendering or SSR:

```javascript
// Using react-helmet-async
import { Helmet } from 'react-helmet-async';

function ProductPage({ product }) {
  return (
    <>
      <Helmet>
        <title>{product.name} | Brand</title>
        <meta name="description" content={product.description} />
        <link rel="canonical" href={`https://example.com/products/${product.slug}`} />
        <script type="application/ld+json">
          {JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'Product',
            name: product.name,
            // ... rest of schema
          })}
        </script>
      </Helmet>
      <main>...</main>
    </>
  );
}
```
