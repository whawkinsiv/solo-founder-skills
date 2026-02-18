# On-Page SEO

Specifications for every on-page element, with "Tell AI:" prompts to implement each one.

---

## Title Tag

| Spec | Requirement |
|------|------------|
| Length | 50-60 characters (≤575 pixels) |
| Keyword | Primary keyword front-loaded |
| Brand | At end, if included |
| Uniqueness | One unique title per page |

**Good:** `On-Page SEO Guide 2025: Complete Optimization Strategies | Brand`
**Bad:** `SEO SEO Tips SEO Guide SEO Strategies SEO Best Practices`

**Tell AI:**
```
Review and optimize title tags for these pages: [list URLs]
Each title should:
- Be 50-60 characters
- Front-load the primary keyword
- Include brand name at end (if space allows)
- Be unique (no duplicate titles across pages)
```

---

## Meta Description

| Spec | Requirement |
|------|------------|
| Length | 150-160 characters |
| Keyword | Include primary keyword naturally |
| CTA | Include a call-to-action |
| Uniqueness | One unique description per page |

**Tell AI:**
```
Write meta descriptions for these pages: [list URLs]
Each description should:
- Be 150-160 characters
- Include the primary keyword naturally
- End with a call-to-action (Learn more, Get started, Try free)
- Be unique per page
```

---

## Header Hierarchy

**Rules:**
- Exactly ONE `<h1>` per page (contains primary keyword)
- No skipped levels (H1 → H2 → H3, never H1 → H3)
- Use question-based headings for featured snippet targeting
- Include keywords naturally in headings

**Tell AI:**
```
Check and fix header hierarchy on [page URL]:
- Ensure exactly one H1 containing the primary keyword
- Fix any skipped header levels
- Convert key headings to question format where appropriate (helps with featured snippets)
```

---

## Image Optimization

**Checklist for every image:**
- [ ] Format: WebP or AVIF (25-50% smaller than JPEG)
- [ ] File size: < 200KB (ideally < 100KB)
- [ ] Width and height attributes set (prevents layout shift)
- [ ] Alt text: Descriptive, includes keyword naturally (max 125 chars)
- [ ] Filename: SEO-friendly (`seo-guide-2025.webp`, not `IMG_001.jpg`)
- [ ] Below-fold images: `loading="lazy"` attribute
- [ ] Hero/above-fold images: `fetchpriority="high"` and NO lazy loading

**Tell AI:**
```
Optimize all images on [page URL]:
- Convert to WebP format
- Add width and height attributes to prevent layout shift
- Add descriptive alt text with relevant keywords (max 125 chars)
- Add loading="lazy" to below-fold images
- Add fetchpriority="high" to the hero image
- Rename files to be SEO-friendly (descriptive-name.webp)
```

---

## Internal Linking

Good internal linking helps search engines discover pages and distributes authority.

**Best practices:**
- Use descriptive anchor text (not "click here")
- Link from high-authority pages to pages you want to rank
- Every page should have at least 2-3 internal links pointing to it
- No orphan pages (pages with zero internal links)

**Anchor text distribution:**
- Descriptive/partial match: 60-70%
- Exact keyword match: 10-20%
- Branded: 10-20%
- Generic ("click here", "learn more"): < 10%

**Tell AI:**
```
Audit internal linking structure:
- Find orphan pages (no internal links pointing to them)
- Find pages with weak anchor text ("click here", "read more")
- Suggest 3-5 internal link additions for each key page
- Use descriptive anchor text that includes relevant keywords
```
