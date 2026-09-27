---
name: landing-page
description: "Use this skill when the user needs to create or improve a landing page, write above-the-fold copy, structure a sales page, or increase landing page conversion rates. Also use when the user says 'build my landing page,' 'homepage copy,' 'hero section,' or 'marketing site.' Covers page structure, headline formulas, buyer psychology, and conversion elements."
---

# Landing Page

A landing page is a sales conversation, not a brochure. You have 5 seconds to communicate what the product does and why it matters. This skill gives you the structure and copy for every section.

## Core Principles

- A landing page has ONE goal. Everything serves that goal or gets cut.
- Structure follows the buyer's internal monologue: "What is this?" -> "Is it for me?" -> "How does it work?" -> "Can I trust it?" -> "What do I do next?"
- Above the fold is the most valuable real estate on the internet.
- Long pages can outperform short pages — IF every section earns its place.

---

## Workflow

```
Landing Page Build:
- [ ] Define the ONE goal (signup, waitlist, demo request)
- [ ] Write the hero section (headline + subheadline + CTA)
- [ ] Plan sections in scroll order
- [ ] Write copy for each section
- [ ] Build the page
- [ ] Test on mobile
- [ ] Add analytics tracking (see analytics skill)
```

---

## Section-by-Section Build

### Hero (Above the Fold)

The hero has 5 elements. Get these right and the rest is easier.

1. **Headline** — State the outcome, not the product.
   - Be specific: "Cut your deploy time from 45 minutes to 45 seconds"
   - Not: "Deploy faster"
2. **Subheadline** — Add the "how" or a second benefit.
3. **Primary CTA** — High contrast, specific action text. "Start building free" not "Get started."
4. **Visual** — Product screenshot, short demo, or animated illustration. Show the product in action.
5. **Social proof bar** — Logo strip or metric: "Trusted by 15,000+ teams"

**Tell AI:**
```
Write the hero section for our landing page:
- Product: [what it does, one sentence]
- Audience: [who it's for]
- Main benefit: [the #1 outcome users get]
- Social proof: [number of users, notable customers, or key metric]

Give me:
- 3 headline options (under 10 words each, outcome-focused)
- Subheadline for each (adds "how" or second benefit)
- Primary CTA button text + anxiety reducer below it
- Social proof line
Pick the strongest option and explain why.
```

### How It Works

Exactly 3 steps. Cognitive simplicity.

Format: [Number/Icon] + [Short title] + [One sentence]

Example:
1. **Connect your repo** — Link your GitHub in one click.
2. **Configure your pipeline** — Our AI suggests the optimal setup.
3. **Ship with confidence** — Deploy automatically on every push.

### Feature Sections

Alternate layout: text-left/image-right, then text-right/image-left.

Each feature: [Eyebrow label] + [Benefit headline] + [2-3 sentence description] + [Screenshot]

Lead with benefit, not feature name:
- BAD: "Advanced Analytics Dashboard"
- GOOD: "Know exactly what's working — and what's not"

### Testimonials

- Include: Name, title, company, headshot.
- Quote should mention: a specific result, a before/after, or an emotional reaction.
  - GOOD: "We cut onboarding from 2 weeks to 2 days. New hires actually thank us now." — Sarah Chen, VP Eng @ Acme
  - BAD: "Great product, really love it!" — J.S.
- Place near objection points (security testimonial near pricing, etc.)

### FAQ

Must answer for any SaaS:
1. "Is there a free plan / trial?"
2. "How long does setup take?"
3. "Can I cancel anytime?"
4. "Is my data secure?"
5. "What integrations do you support?"
6. One or two product-specific questions.

### Final CTA

Repeat the primary CTA with a slightly different angle. Different headline, same action.

---

## Full Page Build

**Tell AI:**
```
Build a landing page for our SaaS product:
- Product: [what it does]
- Audience: [who it's for]
- Main benefit: [#1 outcome]
- Features: [list 3-4 key features]
- Social proof: [logos, metrics, testimonials you have]
- CTA: [what you want visitors to do — signup, waitlist, demo]

Use this section order:
1. Hero (headline, subheadline, CTA, social proof bar)
2. Problem agitation (articulate the pain they're feeling)
3. How it works (3 steps)
4. Feature sections (3-4, alternating layout with screenshots)
5. Testimonials (use placeholders if I don't have real ones yet)
6. Pricing preview or "See plans" CTA
7. FAQ (6-8 questions)
8. Final CTA (different angle, same action)

Make it responsive. Use [Tailwind / our existing design system].
If I'm using Lovable: keep the prompt focused on what the user sees, not implementation details.
```

---

## Improving an Existing Page

**Tell AI:**
```
Review our landing page at [URL or file path] and improve it:
- Check: Is the headline outcome-focused or feature-focused?
- Check: Is there a clear single CTA above the fold?
- Check: Does social proof appear early?
- Check: Does the page follow the buyer's monologue
  (What is this → Is it for me → How does it work → Can I trust it → What do I do)?
- Rewrite any weak sections
- Add missing sections (FAQ, testimonials, final CTA)
```

---

## Performance Requirements

- Load time: <2 seconds on 3G
- LCP (Largest Contentful Paint): <2.5 seconds
- No layout shift on load (CLS <0.1)
- Lazy load everything below the fold
- Hero image/video optimized aggressively

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| No clear CTA above the fold | One high-contrast button with specific action text |
| Feature-focused headline | State the outcome the user gets, not what the product does |
| "Get started" or "Learn more" CTAs | Be specific: "Create your first dashboard" |
| No social proof | Add logos, user count, or testimonial — even one helps |
| Missing FAQ section | Answer the 5-6 questions every buyer has |
| Desktop-only design | 50%+ of traffic is mobile. Test there first. |
| Trying to say everything | One page, one goal, one audience. Cut the rest. |

---

## Related Skills

- **copywriting** — Write stronger headlines, CTAs, and microcopy
- **conversion** — CRO techniques for higher signup rates
- **seo** — Make the landing page rank for target keywords
- **brand-identity-generator** — Establish visual identity before building
- **beautify** — Make the page look intentionally designed
