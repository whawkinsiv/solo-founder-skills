# E-E-A-T & Schema Markup

How to build trust signals that Google (and AI search engines) use to evaluate your content. Plus schema markup you should add — all via "Tell AI:" prompts.

---

## E-E-A-T: Why It Matters

Google evaluates content quality using four signals. These affect your rankings and whether AI search engines cite you.

| Signal | What It Means | How to Show It |
|--------|--------------|----------------|
| **Experience** | You've actually done/used what you're writing about | Case studies, original screenshots, "I tested this by..." |
| **Expertise** | You know your subject deeply | Author credentials, certifications, detailed explanations |
| **Authoritativeness** | Others recognize your expertise | Backlinks, industry mentions, expert citations |
| **Trustworthiness** | Your site is reliable and honest | HTTPS, contact info, privacy policy, accurate citations |

---

## Implementing E-E-A-T

### Author Pages

Every blog post or content page should link to an author page showing credentials.

**Tell AI:**
```
Create an author bio section for blog posts that includes:
- Author name with link to full author page
- Job title and relevant experience
- A 2-sentence bio
- Links to social profiles (LinkedIn, Twitter)
- "Last updated" date on every article

Also create a full /about or /authors/[name] page with:
- Detailed background and qualifications
- Areas of expertise
- Links to published content
```

### Trust Signals Checklist

- [ ] HTTPS active on all pages
- [ ] Contact information visible (email, form, or phone)
- [ ] Privacy policy linked in footer
- [ ] Terms of service linked in footer
- [ ] Content includes citations with sources
- [ ] Dates on all articles (published and last updated)
- [ ] Author attribution on all content

---

## Schema Markup (JSON-LD)

Schema tells search engines what your content IS, not just what it says. Claude Code can add all of these for you.

### Required Schema (Add These First)

**Tell AI:**
```
Add JSON-LD schema markup to the site:

1. Organization schema on homepage:
   - Company name, URL, logo
   - Social media profile links
   - Contact information

2. FAQPage schema on any page with FAQ content:
   - Each question and answer as structured data
   - This is critical for featured snippets and AI citations

3. Article schema on blog posts:
   - Headline, author, publisher
   - Date published and date modified
   - Author with credentials (Person schema)

4. BreadcrumbList on all pages:
   - Home > Category > Current Page path

Validate with Google's Rich Results Test after adding.
```

### FAQPage Schema (Most Important for AI Citations)

FAQPage schema makes your Q&A content machine-readable. Pages with FAQ schema are 3x more likely to appear in AI Overviews.

**Tell AI:**
```
Add FAQPage schema to [page URL] for these questions:
- [Question 1]
- [Question 2]
- [Question 3]

Each answer should be a complete, standalone response (2-3 sentences).
Output as JSON-LD in a script tag.
```

### Optional Schema (Add When Relevant)

| Schema Type | Add When... |
|-------------|------------|
| Product | You sell a product or SaaS with pricing |
| HowTo | Content includes step-by-step instructions |
| VideoObject | You embed videos on pages |
| SoftwareApplication | You have a SaaS product page |

**Tell AI:**
```
Add [Product/HowTo/VideoObject] schema to [page URL]:
- Include all required fields for Google Rich Results
- Validate with Rich Results Test
- Include pricing, ratings, or step information as applicable
```
