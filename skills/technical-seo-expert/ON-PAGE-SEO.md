# On-Page SEO

Detailed specifications and code examples for title tags, meta descriptions, header hierarchy, image optimization, and internal linking.

---

## Title Tag Optimization

**Specifications:**
- Length: 50-60 characters (≤575 pixels)
- Primary keyword: Front-loaded
- Brand: At end (if included)
- Unique: One per page

```html
<!-- Good title structure -->
<title>On-Page SEO Guide 2025: Complete Optimization Strategies | Brand</title>

<!-- Bad - keyword stuffed -->
<title>SEO SEO Tips SEO Guide SEO Strategies SEO Best Practices</title>
```

---

## Meta Description

**Specifications:**
- Length: 150-160 characters
- Include: Primary keyword naturally
- Include: Clear call-to-action
- Unique: One per page

```html
<meta name="description" content="Master on-page SEO with our 2025 guide.
Covers 14 critical optimization areas including E-E-A-T and entity SEO.
Free checklist included.">
```

---

## Header Tag Hierarchy

```html
<article>
  <h1>Main Topic (exactly one per page)</h1>

  <section>
    <h2>Major Section</h2>
    <p>Content...</p>

    <h3>Subsection</h3>
    <p>Content...</p>

    <h4>Sub-subsection</h4>
    <p>Content...</p>
  </section>

  <section>
    <h2>Another Major Section</h2>
    <p>Content...</p>
  </section>
</article>
```

**Rules:**
- Exactly ONE `<h1>` per page
- No skipped levels (H1 → H2 → H3, never H1 → H3)
- Include keywords naturally in headings
- Use question-based headings for featured snippet targeting

---

## Image Optimization

```html
<!-- Responsive images with modern formats -->
<picture>
  <source type="image/avif"
          srcset="/img/hero-400.avif 400w, /img/hero-800.avif 800w, /img/hero-1200.avif 1200w"
          sizes="(max-width: 400px) 400px, (max-width: 800px) 800px, 1200px">
  <source type="image/webp"
          srcset="/img/hero-400.webp 400w, /img/hero-800.webp 800w, /img/hero-1200.webp 1200w"
          sizes="(max-width: 400px) 400px, (max-width: 800px) 800px, 1200px">
  <img src="/img/hero-800.jpg"
       alt="Descriptive alt text with relevant keywords"
       width="1200" height="600"
       loading="lazy" decoding="async">
</picture>
```

**Image Checklist:**
- [ ] Format: WebP or AVIF (25-50% smaller than JPEG)
- [ ] File size: < 200KB (ideally < 100KB)
- [ ] Dimensions: `width` and `height` attributes set (prevents CLS)
- [ ] Alt text: Descriptive, includes keyword naturally (max 125 chars)
- [ ] Filename: SEO-friendly (`seo-guide-2025.webp`, not `IMG_001.jpg`)
- [ ] Lazy loading: `loading="lazy"` for below-fold images
- [ ] LCP images: `fetchpriority="high"` and NO lazy loading

---

## Internal Linking

```html
<article>
  <h1>Complete Guide to On-Page SEO</h1>

  <!-- Contextual link with descriptive anchor text -->
  <p>Effective SEO starts with understanding
    <a href="/title-tag-optimization/">how to optimize your title tags</a>
    for maximum visibility.
  </p>

  <!-- Related content section -->
  <aside class="related-content">
    <h3>Related Guides</h3>
    <ul>
      <li><a href="/meta-description-guide/">Meta Description Best Practices</a></li>
      <li><a href="/header-tags-seo/">Header Tag Optimization Guide</a></li>
    </ul>
  </aside>
</article>
```

**Anchor Text Distribution:**
- Exact match: 10-20%
- Partial match: 30-40%
- Branded: 10-20%
- Long-tail descriptive: 20-30%
- Generic ("click here"): < 10%
