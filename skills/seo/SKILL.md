---
name: seo
description: "Use this skill to audit a site's code for search and AI-answer visibility and fix what matters: 'audit my SEO,' 'how do I rank,' 'why don't I show up on Google,' 'SEO review,' 'optimize for AI answers,' 'what pages should I create for SEO,' or 'meta tags and sitemap.' Claude scans the codebase, grades it, writes a prioritized plan with file paths, and offers to make the fixes. Not for writing blog posts in the founder's voice (use content) or for the sales page itself (use landing-page)."
metadata:
  version: 2.0.0
---

# SEO

Audit the codebase for search and AI-answer visibility, then fix what matters. Give a prioritized plan of concrete changes, not a lecture on SEO.

**Set expectations first.** SEO takes 3–6 months to bring traffic. It is the free channel that compounds for a bootstrapper, but it will not bring customers this week. For customers now, use **first-customers**.

## Step 1: Understand the project

1. Read CLAUDE.md or README to learn what the product is and who it is for.
2. Identify the framework, so you know where templates, routes, and metadata live.
3. Map the site structure from the top 3 levels of the directory tree.

## Step 2: Audit

For each area, note what is present, missing, or broken. Check quality, not only existence.

**Technical foundation**
- One `<h1>` per indexable page, and heading levels in order.
- Semantic HTML: main, article, nav, section.
- `robots.txt` and a sitemap exist. Important pages are not accidentally set to `noindex`. Canonical tags are correct.
- Images have width and height, a modern format, lazy loading below the fold, and alt text.
- No render-blocking scripts. Fonts use a swap strategy.

**Pages and intent**
- Titles of about 50–60 characters, with the main phrase first. Meta descriptions of about 120–155 characters. Open Graph tags for sharing.
- Titles and headings name problems the customer searches for, not just brand names. "How to stop no-shows" beats "Acme Scheduler."
- **One page per search intent.** Two pages that target the same query compete with each other.
- **Bottom-of-funnel pages exist,** because they convert first: pricing, "[competitor] alternative", "[product] vs [competitor]", and "[product] for [audience]".
- Internal links connect related pages. No page is orphaned.

**Authority and AI answers**
- Structured data that fits the page: Organization, SoftwareApplication or Product, Article, BreadcrumbList.
- Who wrote it, and why they know: an author or founder bio on content pages.
- Informational pages answer the question in the first 1–2 sentences, then explain. AI answers quote pages that do this.
- Clear structure: short paragraphs, descriptive headings, and tables for comparisons.
- Claims with real sources. Never add statistics that you cannot source.

**Tracking**
- Search Console is verified, or a step to verify it is listed.
- An analytics script is present.

## Step 3: Write the plan

Grade the site A to F. Then list:
1. **Critical:** anything that blocks indexing or ranking now. For each: what is wrong, where (file path), and the fix.
2. **High impact:** improvements ordered by effort against impact, quick wins first.
3. **Content gaps:** pages that should exist, each with the search intent it targets. Bottom-of-funnel pages come first.
4. **Ongoing:** a short monthly checklist.

Ask how the founder wants the plan saved. The default is a Markdown file in a folder the founder names.

## Step 4: Offer to fix

Offer to make the code fixes now: tags, headings, structured data, the sitemap, `robots.txt`, image attributes. Make them with the founder's approval, then re-check each one.

## Rules

- **Lead with leverage.** A solo founder has little time. Put the highest-impact items first, and do not bury them under nitpicks.
- **Be specific.** "Add structured data" is useless. "Add this block to `app/layout.tsx`" is useful. Name the file and show the change.
- **Use the framework's own pattern** for metadata and sitemaps.
- **Do not invent problems.** If an area is fine, say so and move on.
- **Not yet:** buying links, an SEO agency, or 50 posts at once. Start with 5 high-intent pages, measure, and then add more.

## Output

The grade, the prioritized plan with file paths, and the fixes made with the founder's approval.
