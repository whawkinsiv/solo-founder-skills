---
name: legal
description: "Use this skill when the user needs to form a business entity, choose between LLC and C-Corp, create Terms of Service, write a Privacy Policy, or handle legal compliance. Covers entity selection, legal documents, contracts, and compliance for solo-founded SaaS."
---

# SaaS Legal & Business Formation

Every SaaS needs three legal documents at launch: Terms of Service, Privacy Policy, and a basic entity structure. Everything else can wait. This skill helps you handle formation, legal docs, and compliance without overspending on attorneys.

> **Disclaimer:** This skill produces informed first drafts based on common SaaS legal patterns. Always have a licensed attorney review before publishing anything that creates binding obligations.

## Core Principles

- Legal protection is insurance. You don't need everything on day one, but you need the right things at the right time.
- Solo founders overspend on legal in two ways: paying a lawyer too early for things they don't need yet, or paying a lawyer too late after a problem they could have prevented.
- Every SaaS product needs exactly three legal documents at launch: Terms of Service, Privacy Policy, and a basic entity structure. Everything else can wait.
- Legal language should be readable. If your users can't understand your ToS, it's bad legal writing, not "standard."
- Disclaimers: This skill produces informed first drafts based on common SaaS legal patterns. Always have a licensed attorney review before publishing anything that creates binding obligations.

## Business Entity Decision
### Solo Founder Entity Comparison

**LLC (Limited Liability Company)**
- Best for: Solo founders who want simplicity and are bootstrapping.
- Liability protection: Yes — separates personal and business assets.
- Tax: Pass-through by default (income on personal return). Can elect S-Corp taxation later.
- Paperwork: Minimal. Operating agreement + annual report (varies by state).
- Cost: $50-500 to form depending on state.
- When to choose: You're bootstrapping, have no plans to raise VC, want simplicity.

**S-Corp (via LLC election)**
- Best for: Solo founders earning $60K+ in profit who want to reduce self-employment tax.
- How: Form an LLC, then file IRS Form 2553 to elect S-Corp taxation.
- Benefit: Pay yourself a "reasonable salary" (subject to payroll tax), take remaining profit as distributions (no self-employment tax).
- When to choose: Once you're consistently profitable at $5K+/month.

**C-Corp (Delaware)**
- Best for: Founders who plan to raise venture capital.
- Required for: Most VC investment, issuing stock options, accelerator programs.
- Tax: Double taxation (corporate tax + personal tax on dividends).
- Cost: $400+ to form in Delaware, plus ~$400/year franchise tax minimum.
- When to choose: Only if you intend to raise institutional money or join an accelerator that requires it.

**Decision flow:**
```
Planning to raise VC money? → C-Corp (Delaware)
                          ↓ No
Earning $60K+ annual profit? → LLC with S-Corp election
                            ↓ No
Just getting started? → LLC (your home state, or Wyoming/Delaware for privacy)
```

### Formation Checklist

- [ ] Choose entity type
- [ ] File formation documents with state (Articles of Organization for LLC)
- [ ] Get EIN from IRS (free, irs.gov, takes 5 minutes)
- [ ] Draft operating agreement (LLC) or bylaws (Corp)
- [ ] Open business bank account (Mercury, Relay, or local bank)
- [ ] Set up Stripe or payment processor under business entity
- [ ] Set up separate accounting (QuickBooks Self-Employed, Xero, or Wave)
- [ ] Register for state sales tax if required (SaaS taxability varies by state)

## Terms of Service

**Tell AI:**
```
Generate Terms of Service for my SaaS product:
- Product name: [name]
- What it does: [one sentence]
- Pricing model: [free tier / paid plans / both]
- Refund policy: [e.g., 14-day full refund]
- User-generated content: [yes/no — do users upload or create content?]
- Target geography: [US only / US + EU / global]

Use the template structure below. Write in plain English, not legalese.
I'll have an attorney review before publishing.
```

### Structure for SaaS Terms of Service

```markdown
# Terms of Service

**Last updated: [Date]**

## 1. Agreement to Terms
By accessing or using [Product Name], you agree to these Terms.
If you don't agree, don't use the service.

## 2. Description of Service
[One paragraph: what the product does, that it's provided "as is" as a
cloud service, and that features may change.]

## 3. Accounts
- You must provide accurate information.
- You're responsible for your account security.
- You must be 18+ (or age of majority in your jurisdiction).
- One person per account unless on a team plan.

## 4. Acceptable Use
You agree not to:
- Violate any laws
- Infringe on intellectual property
- Attempt to access other users' data
- Use the service to send spam or malware
- Reverse engineer or scrape the service
- Resell access without permission

## 5. Payment Terms
- Pricing is as displayed on [pricing page URL].
- Subscriptions renew automatically.
- You can cancel anytime; access continues through the paid period.
- Refund policy: [state clearly — e.g., "We offer a full refund within
  14 days of initial purchase. No refunds after 14 days."]
- We may change pricing with 30 days notice.

## 6. Intellectual Property
- We own the service and its original content.
- You own your data. We claim no ownership of content you upload.
- You grant us a limited license to host and display your content
  solely to provide the service.

## 7. Your Data
- You can export your data at any time via [method].
- Upon account deletion, we remove your data within [30/60/90] days.
- See our Privacy Policy for how we handle personal data.

## 8. Service Availability
- We target [99.9%] uptime but don't guarantee it.
- We may perform maintenance with reasonable notice.
- We're not liable for downtime caused by factors outside our control.

## 9. Limitation of Liability
To the maximum extent permitted by law, [Company] is not liable for any
indirect, incidental, or consequential damages. Our total liability is
limited to the amount you've paid us in the 12 months preceding the claim.

## 10. Termination
- You can cancel your account at any time.
- We can terminate for violation of these terms with notice.
- Upon termination, your right to use the service ends.

## 11. Changes to Terms
We may update these terms. We'll notify you via email or in-app notice
at least 30 days before material changes take effect.

## 12. Governing Law
These terms are governed by the laws of [State], [Country].

## 13. Contact
Questions? Email [support email].
```

## Privacy Policy

**Tell AI:**
```
Generate a Privacy Policy for my SaaS product:
- Product name: [name]
- Data we collect: [email, name, usage data, payment via Stripe, etc.]
- Analytics tool: [PostHog / Google Analytics / Plausible / none]
- Email service: [Resend / SendGrid / none]
- Do we serve EU users? [yes/no]
- Do we serve California users? [yes/no]

Use the template structure below. Include GDPR section if EU, CCPA if California.
Write in plain English. I'll have an attorney review before publishing.
```

### Structure for SaaS Privacy Policy

```markdown
# Privacy Policy

**Last updated: [Date]**

## What We Collect
- Account information: name, email, password (hashed)
- Usage data: pages visited, features used, timestamps
- Payment data: processed by [Stripe] — we don't store card numbers
- Device data: browser type, IP address (for security and analytics)
- Cookies: [list what cookies you use and why]

## Why We Collect It
- To provide and improve the service
- To communicate with you (transactional emails, support)
- To process payments
- To analyze usage and improve the product
- To prevent fraud and abuse

## Who We Share It With
- Payment processor: [Stripe]
- Analytics: [PostHog/Google Analytics]
- Email service: [name]
- Hosting: [name]
- We do NOT sell your personal data. Ever.

## Data Retention
- Account data: retained while your account is active + [30/90] days after deletion
- Usage analytics: aggregated and anonymized after [12] months
- Payment records: retained as required by tax law

## Your Rights
- Access: Request a copy of your data
- Correction: Update inaccurate data
- Deletion: Request account and data deletion
- Export: Download your data in [format]
- Objection: Opt out of non-essential data processing
To exercise these rights, email [privacy email].

## Security
We implement industry-standard security measures including
[encryption at rest, encryption in transit, access controls, etc.].

## Children
We do not knowingly collect data from children under 13.

## International Transfers
Data is processed in [country]. By using the service,
you consent to this transfer.

## GDPR (if applicable)
[If you serve EU users]:
- Legal basis for processing: contract performance, legitimate interest
- Data controller: [Company name and address]
- DPO contact: [email] (if applicable)

## CCPA (if applicable)
[If you serve California residents]:
- Categories of data collected: [list]
- We do not sell personal information
- Right to know, delete, and opt out

## Changes
We'll notify you of material changes via email 30 days in advance.

## Contact
[Company name]
[Email]
[Address]
```

## Cookie Policy (Minimal)

If you only use essential cookies and one analytics tool:

```
We use cookies for:
1. Authentication (keeping you logged in)
2. Preferences (your settings)
3. Analytics ([tool name]) to understand how people use the product

We do not use advertising cookies or sell data to third parties.
You can disable cookies in your browser settings, but some features
may not work properly.
```

## SaaS Sales Tax Basics

Key facts for US-based SaaS:

- SaaS taxability varies by state. ~23 states tax SaaS as of 2025.
- You have "nexus" (tax obligation) in states where you have: physical presence, employees, or significant sales volume (economic nexus — typically $100K+ in sales).
- Use a tool like TaxJar, Avalara, or Stripe Tax to automate collection.
- Don't ignore this. States are increasingly aggressive about SaaS tax enforcement.
- Start tracking from day one even if you don't collect yet — retroactive liability is real.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Mixing personal and business finances | Open a business bank account on day one. Mercury takes 10 minutes. |
| No refund policy in ToS | State it explicitly. "14-day full refund, no refund after" prevents disputes. |
| Copying another company's ToS verbatim | Their terms are for their business, not yours. Use the template, customize it. |
| No Privacy Policy at launch | Required by law in most jurisdictions. Generate one before going live. |
| Paying a lawyer $5K for boilerplate | Use AI to draft, pay a lawyer $500-1K to review. Don't pay for first drafts. |
| Ignoring sales tax | Start tracking from day one. Retroactive SaaS tax liability is real and growing. |

---

## What You DON'T Need Yet

**Skip until $10K+ MRR or when specifically needed:**
- Data Processing Agreement (DPA) — need it when enterprise customers ask
- SOC 2 compliance — need it when selling to mid-market/enterprise
- DMCA agent registration — need it if users create/upload content
- Patent filings — rarely relevant for SaaS
- Trademark registration — nice to have, not urgent until brand has value
- Cookie consent banner — need it once you serve EU users meaningfully

## Related Skills

- **compliance** — Industry-specific regulations (HIPAA, FERPA, PCI, GDPR) for your tech stack
- **accounting** — Financial setup, bookkeeping, and tax compliance
- **payments** — Stripe setup and subscription billing
- **pricing** — Pricing strategy and tier design
- **secure** — Technical security measures alongside legal compliance
