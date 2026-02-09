# E-E-A-T & Schema Markup

E-E-A-T implementation guidelines and a complete JSON-LD schema markup library for SEO.

---

## E-E-A-T Components

| Signal | Implementation |
|--------|----------------|
| **Experience** | First-hand testing, case studies, original photos, "I tested this by..." |
| **Expertise** | Author credentials, certifications, years of experience |
| **Authoritativeness** | Quality backlinks, industry mentions, expert citations |
| **Trustworthiness** | HTTPS, contact info, privacy policy, accurate content, citations |

---

## Author Schema Implementation

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Complete On-Page SEO Guide for 2025",
  "author": {
    "@type": "Person",
    "name": "John Smith",
    "url": "https://example.com/authors/john-smith",
    "jobTitle": "Senior SEO Specialist",
    "description": "10+ years experience in technical SEO",
    "sameAs": [
      "https://twitter.com/johnsmith",
      "https://linkedin.com/in/johnsmith"
    ],
    "knowsAbout": ["SEO", "Technical SEO", "Content Strategy"]
  },
  "publisher": {
    "@type": "Organization",
    "name": "Example Company",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "datePublished": "2025-01-15",
  "dateModified": "2025-12-30"
}
</script>
```

---

## Author Bio Template

```html
<footer class="author-bio">
  <img src="/authors/john-smith.jpg" alt="John Smith, SEO Expert">
  <div class="author-details">
    <strong>About the Author</strong>
    <p><a href="/authors/john-smith">John Smith</a> is a Senior SEO Specialist
    with 10+ years of experience in technical SEO and content optimization.
    He holds certifications from Google Analytics and has been featured in
    Search Engine Journal and Moz Blog.</p>
    <p><em>Last updated: December 30, 2025</em></p>
  </div>
</footer>
```

---

## Schema Markup Library

### Organization

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Example Company",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "sameAs": [
    "https://twitter.com/example",
    "https://linkedin.com/company/example",
    "https://facebook.com/example"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-800-555-1234",
    "contactType": "customer service"
  }
}
```

### FAQPage (Critical for GEO)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is on-page SEO?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "On-page SEO is the practice of optimizing individual web pages to rank higher in search engines. It includes optimizing content, HTML elements like title tags and meta descriptions, internal linking, and page speed."
      }
    },
    {
      "@type": "Question",
      "name": "How long should a title tag be?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Title tags should be 50-60 characters or approximately 575 pixels wide. Place your primary keyword at the beginning for maximum impact."
      }
    }
  ]
}
```

### Product (E-commerce)

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Widget Pro",
  "image": "https://example.com/widget-pro.webp",
  "description": "Professional-grade widget for enterprise use",
  "brand": { "@type": "Brand", "name": "Example Brand" },
  "sku": "WIDGET-PRO-001",
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/products/widget-pro",
    "priceCurrency": "USD",
    "price": "299.99",
    "availability": "https://schema.org/InStock",
    "priceValidUntil": "2025-12-31"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "256"
  }
}
```

### BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com/" },
    { "@type": "ListItem", "position": 2, "name": "Products", "item": "https://example.com/products/" },
    { "@type": "ListItem", "position": 3, "name": "Widget Pro" }
  ]
}
```

### HowTo

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Optimize Title Tags for SEO",
  "description": "Step-by-step guide to creating SEO-optimized title tags",
  "totalTime": "PT10M",
  "step": [
    { "@type": "HowToStep", "position": 1, "name": "Research Keywords", "text": "Identify your primary keyword using keyword research tools" },
    { "@type": "HowToStep", "position": 2, "name": "Front-Load Keyword", "text": "Place your primary keyword at the beginning of the title" },
    { "@type": "HowToStep", "position": 3, "name": "Keep Under 60 Characters", "text": "Ensure title is under 60 characters to prevent truncation" },
    { "@type": "HowToStep", "position": 4, "name": "Add Compelling Hook", "text": "Include power words or numbers to increase CTR" }
  ]
}
```

### VideoObject

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Complete SEO Guide 2025",
  "description": "Learn all essential SEO techniques for 2025",
  "thumbnailUrl": "https://example.com/thumbnails/seo-guide.jpg",
  "uploadDate": "2025-01-15T08:00:00+00:00",
  "duration": "PT15M30S",
  "contentUrl": "https://example.com/videos/seo-guide.mp4",
  "embedUrl": "https://www.youtube.com/embed/VIDEO_ID"
}
```
