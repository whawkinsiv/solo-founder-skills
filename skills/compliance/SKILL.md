---
name: compliance
description: "Use this skill when the user is building software for a regulated industry and needs to understand compliance requirements. Also use when the user mentions 'HIPAA,' 'FERPA,' 'SOC 2,' 'PCI,' 'GDPR,' 'compliance,' 'regulated industry,' 'healthcare app,' 'fintech,' 'edtech,' or asks 'do I need to worry about [regulation]?' Covers what regulations mean for your tech stack — not legal theory, but concrete technical requirements."
---

# Industry Compliance

If you're building for healthcare, finance, education, or any regulated industry, there are rules about how you handle data. You probably already know the regulations from your professional life — but you don't know what they mean for software. This skill translates compliance requirements into concrete technical decisions.

**This skill is for understanding what regulations mean for your tech stack.** For implementing security controls (auth, encryption, rate limiting), use **secure**. For writing legal documents (ToS, Privacy Policy), use **legal**. For payment processing and PCI, use **payments**.

> **Disclaimer:** This skill covers common compliance patterns. It is not legal advice. Consult a compliance specialist for your specific situation, especially before handling sensitive data in production.

## Core Principles

- Compliance is not optional in regulated industries. Getting it wrong can kill your business.
- Most compliance requirements boil down to: who can see data, how is it stored, and what happens when something goes wrong.
- The right tech stack choices handle 80% of compliance for you. Don't reinvent the wheel.
- Compliance is cheaper to build in from the start than to retrofit later.
- You don't need SOC 2 certification at $0 MRR. But you do need to make decisions now that don't block certification later.

### Don't Do Yet

- **Don't pay for a SOC 2 audit** ($15K-50K) until enterprise customers require it. Just follow the practices.
- **Don't hire a compliance officer.** A one-time consultation ($1K-5K) is enough until $10K+ MRR.
- **Don't build compliance features nobody asked for.** Cookie consent is required. A full data governance dashboard is not — yet.
- **Don't use compliance as a reason to delay launch.** Make compliant tech choices, launch, then iterate. Perfection is the enemy of shipped.

---

## Find Your Requirements

**Tell AI:**
```
I'm building a SaaS product for [industry/profession].
My product handles this type of data: [describe the data — patient records, student info, financial transactions, etc.]
My users are in: [countries/regions]

What compliance requirements apply to me?
For each one, tell me:
1. What it is (one sentence)
2. Whether I need it before launch or can add it later
3. What it means for my tech stack (specific technical requirements)
4. Whether I need a certification/audit or just need to follow the rules
```

---

## Compliance by Industry

### Healthcare (HIPAA)

**Applies when:** Your software stores, processes, or transmits Protected Health Information (PHI) — patient names, conditions, treatment records, billing info tied to health data.

**What it means for your tech stack:**

| Requirement | What to Do |
|------------|-----------|
| Data encryption at rest | Use a database that encrypts stored data (Supabase, AWS RDS with encryption enabled) |
| Data encryption in transit | HTTPS everywhere (all modern hosting does this) |
| Access controls | Role-based access, audit logs of who accessed what |
| Business Associate Agreement (BAA) | Your hosting and database provider must sign one. Not all do. |
| Audit trail | Log every access to PHI: who, when, what |
| Minimum necessary | Only show users the data they need for their role |
| Breach notification | Have a plan for what happens if data leaks |

**Hosting that offers BAAs:**
- AWS (free tier eligible)
- Google Cloud
- Microsoft Azure
- Supabase (on Team plan and above)
- Render (on request)
- Heroku (enterprise)

**Hosting that does NOT offer BAAs (don't use for PHI):**
- Vercel (no BAA available)
- Netlify (no BAA available)
- Railway (no BAA currently)
- Free tiers of most services

**Tell AI:**
```
I'm building a healthcare SaaS that stores [type of health data].
Set up the tech stack for HIPAA compliance:
- Database: needs encryption at rest and BAA support
- Hosting: needs BAA support
- Auth: role-based access with audit logging
- Add an audit log table that tracks every PHI access
- Ensure all API endpoints require authentication
- No PHI in URL parameters, logs, or error messages
```

---

### Finance (PCI-DSS, SOC 2)

**PCI-DSS applies when:** You handle credit card numbers directly.

**The shortcut:** Use Stripe. Stripe handles PCI compliance for you. Never store card numbers in your database. Never let card numbers touch your server. Use Stripe Elements or Checkout — the card data goes directly from the user's browser to Stripe, bypassing your server entirely.

If you use Stripe correctly, PCI is handled. See **payments** skill for implementation.

**SOC 2 applies when:** Enterprise customers ask for it (usually $50K+ deals). You don't need it at launch.

**Plan for SOC 2 later by doing these now:**
- Use a reputable hosting provider (AWS, GCP, Azure)
- Enable logging and audit trails
- Use SSO/OAuth for authentication (not custom auth)
- Document your security practices
- See **secure** skill for security checklist

---

### Education (FERPA)

**Applies when:** Your software handles student education records — grades, enrollment, disciplinary records, financial aid.

| Requirement | What to Do |
|------------|-----------|
| Written consent for disclosure | Parents/students must consent before you share their data |
| Access controls | Only authorized school officials see student records |
| Directory information opt-out | Students can opt out of directory info sharing |
| Data minimization | Only collect what you need |
| Audit trail | Track who accessed student records |

**Tell AI:**
```
I'm building an edtech product that handles [type of student data].
Set up FERPA-compliant data handling:
- Role-based access: [teacher, admin, student, parent] with different data visibility
- Consent tracking: record when parents/students consented to data use
- Audit log for all access to student records
- Data export and deletion capability (for student/parent requests)
- No student data in analytics, logs, or error tracking
```

---

### Real Estate

**Less regulated technically, but watch for:**
- Fair Housing Act: marketing and algorithms must not discriminate by protected classes
- State licensing requirements: some states regulate real estate software
- MLS data rules: if you use MLS data, each MLS has its own terms of use
- Wire fraud prevention: if your tool touches transactions, security is critical (real estate wire fraud is a $400M+/year problem)

---

### Legal

**Attorney-client privilege considerations:**
- Client communications stored in your software may be privileged
- Use encryption at rest and in transit
- Access controls: only authorized users see case data
- Data residency: some jurisdictions require data stored locally
- Bar association ethics opinions may apply to cloud storage of client files

---

### General (Everyone)

**GDPR (if you have EU users):**

| Requirement | What to Do |
|------------|-----------|
| Consent before collecting data | Cookie consent banner, clear privacy policy |
| Right to access | Users can request all their data |
| Right to deletion | Users can request data deletion ("right to be forgotten") |
| Data portability | Users can export their data in a standard format |
| Privacy by design | Only collect data you actually need |
| Breach notification | Notify authorities within 72 hours of a breach |

**Tell AI:**
```
Add GDPR compliance features to our app:
- Cookie consent banner that blocks tracking until consent is given
- "Download my data" feature in account settings (export as JSON/CSV)
- "Delete my account" feature that actually deletes all user data
- Privacy policy page explaining what data we collect and why
- Data processing records (log what data we collect, why, and how long we keep it)
```

**CCPA/CPRA (if you have California users):**
Similar to GDPR. The main additional requirement is a "Do Not Sell My Personal Information" link.

---

## Compliance Checklist (Before Launch)

```
Minimum for any SaaS:
- [ ] Privacy policy published
- [ ] Terms of service published
- [ ] HTTPS on all pages (usually automatic with modern hosting)
- [ ] Passwords hashed (never stored in plain text)
- [ ] No sensitive data in logs, URLs, or error messages
- [ ] User data export capability
- [ ] User data deletion capability
- [ ] Cookie consent if you use analytics/tracking

Add if regulated industry:
- [ ] Identified which regulations apply to your data
- [ ] Hosting provider supports required compliance (BAA, certifications)
- [ ] Encryption at rest enabled on database
- [ ] Role-based access controls implemented
- [ ] Audit log tracking data access
- [ ] Breach notification plan documented
- [ ] Consulted a compliance specialist for your specific situation
```

---

## When to Get Professional Help

| Stage | What to Do |
|-------|-----------|
| Pre-launch | Read this skill. Make compliant tech stack choices. |
| First paying customers | Get a compliance consultant to review your setup (one-time, $1K-5K) |
| $10K+ MRR or enterprise customers | Consider formal certification (SOC 2 audit: $15K-50K) |
| Handling highly sensitive data (PHI, financial) | Consult before launch, not after |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Ignoring compliance until an enterprise customer asks | Make compliant tech choices from day 1 — it's free |
| Storing credit card numbers in your database | Use Stripe. Card data never touches your server. |
| Using a hosting provider without a BAA for healthcare data | Check BAA availability before choosing your stack |
| "We'll add compliance later" for regulated data | Retrofitting compliance is 10x more expensive than building it in |
| Over-investing in certification at $0 MRR | You need compliant practices, not a $50K audit, until you have enterprise customers |
| Putting sensitive data in error logs or analytics | Scrub PII from all logging. This is the most common compliance violation. |

---

## Related Skills

- **secure** — Technical security implementation (OWASP, auth, API protection)
- **legal** — Business entity, Terms of Service, Privacy Policy
- **database** — Schema design with RLS and audit trails
- **deploy** — Hosting selection with compliance in mind
- **payments** — Stripe setup (handles PCI compliance for you)
