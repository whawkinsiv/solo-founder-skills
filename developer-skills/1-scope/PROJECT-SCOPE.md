# Full Project Scope Template

Use this for new products, major releases, or stakeholder review (1-2 hours).

## Complete Template

```markdown
# [Product Name] - Project Scope

## 1. Introduction

**Background**
[2-3 sentences on what you're building and why]

**In Scope**
- [Major feature/capability]
- [Key user flow]
- [Critical integration]

**Out of Scope**
- [Future feature not in v1]
- [Advanced feature for later]
- [Nice-to-have for v2]

## 2. User Roles

**[Role Name]**
- [Responsibility]
- [Permission]
- [Access level]

## 3. Pages & Screens

**Public**
- [Page name] - [One-line purpose]

**Authenticated**
- [Page name] - [One-line purpose]

## 4. Core Features

**[Feature Category]**
- [Outcome-focused capability]
- [What system does automatically]
- [What users can do]

## 5. Integrations

**[Service Name]** ([Purpose])
- Purpose: [What it does]
- Complexity: [Low/Medium/High + why]
- Risk: [Concerns or none]

## 6. Milestones & Tasks

### Milestone 1: [Name]
**Goal:** [What this achieves]
- [Task description] ([hours])
- [Task description] ([hours])
**Total: [X] hours**

### Milestone 2: [Name]
**Goal:** [What this achieves]
- [Task description] ([hours])
**Total: [X] hours**

## 7. Open Questions & Assumptions

**Assumptions:**
- [Assumption you've made]

**Unresolved Questions:**
- [Decision needed before build]

## Cost Summary
- Total Hours: [X]
- At $[rate]/hour: $[low] - $[high]
- Timeline: [weeks] at [hours/week]
```

---

## Example: SaaS Analytics Dashboard

```markdown
# SaaS Analytics Dashboard - Project Scope

## 1. Introduction

**Background**
Building a customer-facing analytics dashboard for SaaS products. Users can view 
usage metrics, export reports, and set up alerts. Targets non-technical business 
users who need insights without SQL knowledge.

**In Scope**
- Pre-built charts for common SaaS metrics (MRR, churn, DAU)
- Custom date range filtering
- CSV export functionality
- Email alerts for metric thresholds
- Stripe integration for revenue data

**Out of Scope**
- Custom chart builder (use pre-built charts only)
- Advanced SQL query interface
- White-label/embed functionality
- Mobile native apps (web responsive only)
- Real-time streaming data (daily refresh sufficient)

## 2. User Roles

**Admin**
- Manages all users and workspace settings
- Views all data across organization
- Configures integrations (Stripe, webhooks)
- Sets up alerts and exports for team

**Viewer**
- Views dashboards and reports
- Exports own reports
- Cannot modify settings or add users
- Read-only access to data

## 3. Pages & Screens

**Public**
- Landing page - Convert visitors to sign-ups
- Pricing page - Display Free, Pro, Enterprise tiers
- Login/Signup - User authentication

**Authenticated**
- Overview dashboard - Key metrics summary (MRR, active users, churn)
- Metrics detail page - Individual metric with historical trends
- Reports page - List of saved/scheduled reports
- Alerts page - Configure threshold alerts
- Settings page - Account, integrations, team management
- Export history - Track CSV exports and downloads

## 4. Core Features

**Dashboard & Metrics**
- Users view pre-built charts for MRR, churn, DAU, retention
- Users filter data by date range (last 7d, 30d, 90d, custom)
- System auto-refreshes data daily at 3am UTC
- Charts show historical trends with hover tooltips

**Data Export**
- Users export any dashboard view as CSV
- Exports include filtered date range only
- Large exports (10k+ rows) delivered via email link
- Export history shows last 30 days of downloads

**Alerts**
- Users set threshold alerts (e.g., "Churn rate > 5%")
- System checks thresholds daily and emails if triggered
- Admins can set alerts for entire team
- Alert history shows last 10 triggered alerts

**Integrations**
- Stripe: Auto-sync revenue data daily
- Webhooks: Accept custom events from user's app
- CSV upload: One-time data import for historical backfill

## 5. Integrations

**Stripe** (Revenue Data)
- Purpose: Sync subscription revenue, MRR, churn calculations
- Complexity: Medium - webhook setup, retry logic, failed payment handling
- Risk: Must handle Stripe API rate limits gracefully

**SendGrid** (Email Alerts)
- Purpose: Send alert notifications and export download links
- Complexity: Low - straightforward API, transactional email only
- Risk: None

**Webhooks** (Custom Events)
- Purpose: Accept user activity events from customer apps
- Complexity: High - authentication, validation, retry queue, event schema
- Risk: High volume could impact performance, need rate limiting

## 6. Milestones & Tasks

### Milestone 1: UX/UI Design
**Goal:** Complete mockups for all core screens
- Wireframes for 6 key pages (10 hours)
- High-fidelity designs with component library (14 hours)
- Mobile responsive layouts (8 hours)
- Design review and iterations (4 hours)
**Total: 36 hours**

### Milestone 2: Core Dashboard
**Goal:** Working dashboard with authentication and basic metrics
- User authentication (email/password, password reset) (18 hours)
- Overview dashboard with 4 core metrics (20 hours)
- Date range filtering (8 hours)
- Chart rendering and hover states (12 hours)
- Admin user management (10 hours)
**Total: 68 hours**

### Milestone 3: Export & Alerts
**Goal:** Users can export data and configure alerts
- CSV export (small datasets) (10 hours)
- CSV export (large datasets via email) (12 hours)
- Alert configuration UI (8 hours)
- Alert threshold checking system (14 hours)
- Email notification system (6 hours)
**Total: 50 hours**

### Milestone 4: Integrations
**Goal:** External services connected and syncing data
- Stripe integration (OAuth, webhook, data sync) (24 hours)
- SendGrid email setup and templates (6 hours)
- Webhook endpoint (auth, validation, queue) (20 hours)
- Integration testing and error handling (10 hours)
**Total: 60 hours**

### Milestone 5: Polish & Launch
**Goal:** Production-ready with documentation
- Error handling and edge cases (12 hours)
- Loading states and empty states (8 hours)
- Help documentation (6 hours)
- Performance testing and optimization (10 hours)
- Security audit (8 hours)
**Total: 44 hours**

## 7. Open Questions & Assumptions

**Assumptions:**
- Users primarily access via desktop (mobile is secondary use case)
- Payment via credit card only (no PayPal/wire transfer in v1)
- English language only at launch
- Data refresh once daily is sufficient (no real-time requirement)
- Maximum 10,000 rows per export is acceptable limit

**Unresolved Questions:**
- Should free tier users have read-only access or no access to historical data?
- What happens to user data when subscription is canceled? (Delete after 30 days? Archive?)
- Do we need GDPR compliance features (data export, deletion) at launch?
- Should alert emails include chart images or just text + link?
- What's the maximum webhook event volume we need to support? (affects architecture)

## Cost Summary
- Total Hours: 258
- At $100/hour: $25,800
- At $150/hour: $38,700
- Timeline: 6-7 weeks at 40 hours/week (single developer)
- Timeline: 3-4 weeks at 40 hours/week (two developers)
```

---

## Tips for Writing Project Scopes

**Introduction:**
- Background: 2-3 sentences, focus on WHO and WHY
- In Scope: Major features only, not tasks
- Out of Scope: Prevents scope creep, sets expectations

**User Roles:**
- Define 2-4 key roles maximum
- Focus on permissions and access differences
- Include one concrete example per role

**Pages & Screens:**
- List EVERY page users will see
- One-line purpose keeps it scannable
- Group by public/authenticated helps visualize flow

**Core Features:**
- Group by feature category
- Use outcome language: "Users can..." not "System has..."
- Include what system does automatically

**Integrations:**
- Always include Purpose, Complexity, Risk
- Low complexity: simple API, few edge cases
- High complexity: auth, webhooks, retry logic
- Risk: performance, security, cost concerns

**Milestones:**
- Group by logical phases (Design, Core, Integrations, Polish)
- Each task: clear deliverable + hour estimate
- Sum hours per milestone
- Pad estimates 20-30% for unexpected issues

**Open Questions:**
- Surface assumptions explicitly
- List decisions needed before build
- Forces conversations early vs. surprises late
