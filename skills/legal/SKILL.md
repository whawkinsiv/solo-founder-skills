---
name: legal
description: "Use this skill for the legal basics of a solo software business: 'LLC or C-Corp,' 'form a company,' 'terms of service,' 'privacy policy,' 'cookie consent,' 'GDPR,' 'co-founder agreement,' 'contractor agreement,' or 'do I need a lawyer.' Picks an entity, drafts plain-English terms and a privacy policy from the product's real facts, adds data export and deletion, and says what can wait. Drafts only, for a lawyer to review. Not for security in code (use secure) or for taxes and bookkeeping (use finances)."
metadata:
  version: 1.0.0
---

# Legal

Get the few legal pieces a solo software business needs at launch, and skip the rest until a customer or a law requires them.

Everything this skill writes is a first draft, not legal advice. A licensed lawyer reviews anything binding before it is published. Paying a lawyer \$500–1,000 to review a draft costs far less than paying for the draft itself.

## Step 1: Choose the entity

These rules are for the US. Elsewhere, ask about the local equivalent of a limited-liability company.

```
Plans to raise venture capital?     → Delaware C-Corp
Profit above about \$60K a year?    → LLC, then talk to an accountant about S-Corp tax treatment
Otherwise                           → LLC in the founder's home state
```

Forming in another state (such as Wyoming or Delaware) usually means registering in the home state too, and paying fees in both.

Formation checklist:
- [ ] File the formation documents
- [ ] Get a tax ID (EIN), which is free from the IRS
- [ ] Write an operating agreement
- [ ] Open a business bank account (see **finances**)
- [ ] Set up the payment account under the business

## Step 2: Co-founders and contractors

- **A co-founder agreement before any work starts:** the equity split, vesting (4 years with a 1-year cliff is the common default), roles, how decisions are made, what happens if one founder leaves, and code and IP assigned to the company. Hard conversations only get harder later.
- **Every contractor who writes code or content signs an agreement** that assigns the work to the business.

## Step 3: Terms of Service and Privacy Policy

Draft both from the product's real facts. Ask for what the project does not show:
- what the product does, and who it is for
- the data it collects, and every service that processes it: host, database, payments, email, analytics
- the price, the refund policy, and how cancellation works
- where customers are located

The **Terms** cover: the service, accounts, acceptable use, payment, refunds and cancellation, data ownership and export, availability, a limit on liability, termination, changes to the terms, and governing law.

The **Privacy Policy** covers: what is collected and why, who processes it (the real services, by name), how long it is kept, the user's rights and how to use them, and a contact address.

Write both in plain English. Link both in the site footer.

## Step 4: Privacy in the product

- Users can **export** their data and **delete** their account and data. Build both before launch. Customers ask for them, and laws in many places require them.
- **Cookie consent:** EU visitors must agree before any non-essential cookies are set, including most analytics, from the first visitor. A simpler path is analytics that set no cookies.
- Do not write "by using the service, you consent to data transfer." That is not a valid legal basis. List the services that process data, and rely on their standard data-transfer terms.
- US state privacy laws, such as California's, apply only above size thresholds that most solo founders do not reach. Offering export and deletion anyway is good practice.
- **Regulated data** (health, financial accounts, children, students) needs a specialist before launch (see **secure**).

## What can wait

- SOC 2, until a customer requires it.
- A data processing agreement template, until a business customer asks for one.
- Trademark registration, until the name has value. Check for conflicts before choosing a name, though (see **domain-name**).
- Patents. They are rarely relevant for software.

## Output

```
Entity:        <recommendation and why>
Checklist:     <formation items: done / to do>
Drafts:        <Terms and Privacy Policy, from the product's real facts, marked "for lawyer review">
In-product:    <data export, data deletion, cookie consent: done / to do>
```
