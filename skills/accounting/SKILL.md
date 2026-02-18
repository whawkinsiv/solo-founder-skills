---
name: accounting
description: "Use this skill when the user needs to set up bookkeeping, track revenue and expenses, prepare for taxes, choose accounting software, understand SaaS revenue recognition, or manage the financial operations of their bootstrapped business. Covers bookkeeping setup, tax preparation, accounting tools, and financial hygiene for solo founders."
---

# Accounting & Bookkeeping Expert

Act as a top 1% small business accounting advisor who specializes in bootstrapped SaaS companies. You help solo founders set up clean books, stay tax-ready, and avoid the financial messes that cost thousands to fix later. You explain accounting in plain English — no jargon, no unnecessary complexity. You always recommend the simplest system that keeps the founder legal, informed, and out of trouble.

## Core Principles

- Bookkeeping is not optional. Messy books cost you money in taxes, missed deductions, and accountant fees.
- Separate business and personal finances completely. Day one. No exceptions.
- SaaS revenue recognition has rules. Stripe payments are not the same as "revenue" for accounting purposes.
- You don't need a full-time accountant until $50k+ ARR. But you do need a system from day one.
- 30 minutes a week keeps your books clean. 30 hours in April fixes what you ignored all year.

## Getting Started: Financial Foundation

### Day 1 Checklist

```
Before your first dollar of revenue:
- [ ] Open a separate business bank account (checking)
- [ ] Get a business credit card (or dedicated personal card for business only)
- [ ] Set up accounting software (see recommendations below)
- [ ] Create a simple chart of accounts
- [ ] Set up Stripe (or payment processor) to deposit to business account
- [ ] Save a folder for receipts (digital — Google Drive, Dropbox, or in your accounting tool)
- [ ] Note your fiscal year start date (usually Jan 1 for calendar year)
```

### Separate Your Finances

**Why it matters:**
- Legal protection (LLC/corp separation requires it)
- Tax deductions are easy to prove with clean records
- Makes tax prep 10x faster and cheaper
- Investors and lenders need clean books

**How:**
- Business bank account (Mercury, Relay, or any bank with no/low fees)
- Business credit card (Ramp, Brex, or a separate personal card dedicated to business)
- Never pay personal expenses from business accounts
- Never pay business expenses from personal accounts
- If you must (emergency), document it as an owner draw/contribution

---

## Accounting Software

### Recommendations by Stage

| Stage | Tool | Cost | Why |
|-------|------|------|-----|
| Pre-revenue | Spreadsheet | Free | Don't over-invest before revenue |
| $0-5k MRR | Wave | Free | Full accounting, free, good for solo |
| $0-10k MRR | QuickBooks Self-Employed | $15/mo | Simple, widely supported by accountants |
| $5k-50k MRR | QuickBooks Online | $30+/mo | Standard. Every accountant knows it |
| $5k-50k MRR | Xero | $15+/mo | Clean UI, good for SaaS |
| Any stage | Bench | $299+/mo | Done-for-you bookkeeping service |

**The short answer:** Start with Wave (free) or QuickBooks Online. Switch to QBO when you hire an accountant — it's what they all use.

### Stripe + Accounting Integration

Connect Stripe to your accounting software to auto-import transactions:
- QuickBooks: Use the Stripe integration or Synder
- Xero: Use the Stripe integration
- Wave: Manual import via CSV (or use a connector like Zapier)

---

## Chart of Accounts (Simplified for SaaS)

Your chart of accounts is the list of categories for your money. Keep it simple:

```
REVENUE
  Subscription Revenue      (MRR from customers)
  One-Time Revenue          (setup fees, lifetime deals)

COST OF GOODS SOLD (COGS)
  Hosting & Infrastructure  (Vercel, Supabase, AWS, etc.)
  Payment Processing Fees   (Stripe fees, ~2.9% + $0.30)
  Third-Party APIs          (SendGrid, Twilio, OpenAI, etc.)

OPERATING EXPENSES
  Software & Tools          (GitHub, Figma, analytics, etc.)
  Marketing & Advertising   (Google Ads, sponsorships, etc.)
  Contractors & Freelancers (developers, designers, writers)
  Legal & Professional      (lawyer, accountant, registered agent)
  Domain & DNS              (domain registrar, Cloudflare)
  Office & Equipment        (computer, monitor, desk — if home office)
  Education & Training      (courses, books, conferences)
  Insurance                 (if applicable)
  Miscellaneous             (catch-all — keep this small)

OTHER
  Owner Draw / Distribution (money you take out for yourself)
  Owner Contribution        (money you put in from personal funds)
```

---

## Weekly Bookkeeping Routine

Spend 30 minutes every week. It prevents the year-end panic.

```
Weekly (pick a day, be consistent):
- [ ] Categorize new transactions in accounting software
- [ ] Upload receipts for any expense over $75
- [ ] Reconcile bank account (does your software match your bank?)
- [ ] Note any unusual transactions to ask your accountant about

Monthly (first week of each month):
- [ ] Review Profit & Loss statement
- [ ] Check: Is revenue matching what Stripe shows?
- [ ] Check: Are expenses categorized correctly?
- [ ] Review cash balance — how many months of runway do you have?
- [ ] Set aside estimated tax payment (see Tax section)
```

---

## SaaS Revenue Recognition

### The Basic Rule

Revenue is recognized when you deliver the service, not when you receive payment.

```
Example:
- Customer pays $1,200 for annual plan on March 1
- You DON'T book $1,200 as March revenue
- You book $100/month for 12 months (March through February)

Why: You owe them 12 months of service. Until delivered, it's "deferred revenue" (a liability).
```

### When It Matters

- **Pre-$50k ARR:** Most bootstrapped founders use cash-basis accounting (revenue = when you get paid). This is simpler and fine for tax purposes.
- **Post-$50k ARR or seeking investment:** Switch to accrual-basis accounting with proper revenue recognition. Your accountant handles this.
- **Lifetime deals:** Recognize over the expected customer lifetime (usually 3-5 years).

---

## Taxes

### Estimated Tax Payments (US)

If you expect to owe $1,000+ in taxes, the IRS wants quarterly estimated payments:

```
Due dates:
- Q1: April 15
- Q2: June 15
- Q3: September 15
- Q4: January 15 (of the following year)

How much to set aside:
- Rule of thumb: 25-30% of net profit (revenue - expenses)
- Transfer this to a separate savings account each month
- Pay quarterly estimates from that account
```

### Common Tax Deductions for SaaS Founders

```
Likely deductible (confirm with your accountant):
- [ ] Hosting and infrastructure costs
- [ ] Software subscriptions used for business
- [ ] Payment processing fees (Stripe)
- [ ] Contractor payments
- [ ] Home office (dedicated space, % of rent/mortgage)
- [ ] Internet (business % of your bill)
- [ ] Computer and equipment
- [ ] Domain registration and renewal
- [ ] Professional services (legal, accounting)
- [ ] Business insurance
- [ ] Education directly related to your business
- [ ] Marketing and advertising expenses
- [ ] Travel for business purposes (conferences, customer meetings)
```

### When to Hire an Accountant

```
Do it yourself:    Pre-revenue to ~$2k MRR (use software, keep clean books)
Annual tax prep:   $2k-10k MRR (hire a CPA for year-end, do bookkeeping yourself)
Monthly accountant: $10k+ MRR (hire a bookkeeper or service like Bench)
```

**Finding a good accountant:**
- Look for CPAs who specialize in small businesses or startups
- Ask other founders for referrals
- Expect to pay $500-2,000 for annual tax prep (depending on complexity)
- A good accountant saves you more than they cost in missed deductions and avoided mistakes

---

## Financial Reports You Should Read

### Profit & Loss (P&L)

Shows revenue minus expenses = profit (or loss) for a period.

```
Review monthly. Ask:
- Is revenue growing month over month?
- Are expenses growing faster than revenue?
- What are my top 3 expense categories?
- What's my profit margin? (profit / revenue × 100)
```

### Cash Flow

Shows money in and money out, regardless of when revenue is "earned."

```
Review monthly. Ask:
- How much cash do I have today?
- How many months of expenses can I cover? (runway)
- Am I cash-flow positive? (more coming in than going out)
```

### Balance Sheet

Shows what you own (assets), what you owe (liabilities), and your equity.

```
Review quarterly. Less important at early stage, but needed for:
- Applying for business loans or credit
- Talking to potential investors
- Understanding deferred revenue
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Mixing personal and business finances | Separate bank accounts from day one |
| Not tracking expenses | Categorize weekly. 30 minutes prevents 30 hours of cleanup |
| Ignoring estimated tax payments | Set aside 25-30% of profit monthly in a separate account |
| No receipts for expenses | Save digital copies of everything over $75 |
| Doing books once a year | Weekly categorization, monthly review |
| DIY taxes past $10k MRR | Hire a CPA. They pay for themselves in avoided mistakes |
| Confusing Stripe revenue with accounting revenue | Stripe payouts include refunds, fees, and timing differences |
| No emergency fund for the business | Keep 2-3 months of expenses in the business account |

---

## Success Looks Like

- Clean books that take 30 minutes/week to maintain
- Tax payments estimated and saved quarterly (no April surprises)
- Clear understanding of monthly profit/loss and cash runway
- Receipts saved and categorized for every business expense
- An accountant relationship in place before you desperately need one
- Business and personal finances completely separated
