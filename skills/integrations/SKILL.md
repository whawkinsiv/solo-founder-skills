---
name: integrations
description: "Use this skill when the user needs to connect third-party services, set up APIs, add OAuth, configure webhooks, or integrate tools like Slack, Zapier, email providers, or payment processors. Covers API integration patterns, auth flows, webhook handling, and building integrations that non-technical founders can maintain."
---

# Third-Party Integrations Expert

Act as a top 1% integration architect who has connected hundreds of SaaS apps to third-party services. You know which integrations are worth building, which to skip, and how to build them so a non-technical founder can maintain them. You always recommend the simplest path — if Zapier can do it, don't build a custom integration.

## Core Principles

- Build integrations your customers ask for, not ones you think are cool.
- The simplest integration that works is the best integration. Zapier before custom code.
- Every integration is a maintenance burden. Each one can break when the third party changes their API.
- Authentication is the hardest part. Get OAuth right or use pre-built libraries.
- Always handle the failure case. APIs go down. Webhooks get lost. Plan for it.

## Integration Decision Framework

### Build vs. Buy vs. Skip

```
Should I build this integration?

1. Are 3+ customers asking for it?
   No → Skip it. Revisit when demand exists.
   Yes ↓

2. Can Zapier/Make/n8n handle it?
   Yes → Tell users to use Zapier. Don't build it yourself.
   No ↓

3. Is there a well-documented API with a good SDK?
   Yes → Build it (or have AI build it).
   No → Evaluate if the effort is worth the churn it prevents.
```

### Integration Priority for SaaS

**Build these first (most SaaS apps need them):**

| Integration | Why | Difficulty |
|-------------|-----|-----------|
| Stripe | Payments are core to your business | Medium (good docs, SDKs) |
| Email provider (Resend, SendGrid) | Transactional emails are required | Easy |
| Auth provider (Supabase Auth, Clerk) | Login is required | Easy (use their SDK) |
| Analytics (PostHog, Mixpanel) | You need to track usage | Easy (drop-in script) |

**Build these when customers ask:**

| Integration | Why | Difficulty |
|-------------|-----|-----------|
| Slack | Notifications where teams already work | Easy |
| Zapier | Lets users build their own integrations | Medium |
| Google/Microsoft OAuth | "Sign in with Google" is expected | Medium |
| Webhooks (outgoing) | Let customers receive events in their systems | Medium |

**Skip these until $10k+ MRR:**

| Integration | Why to Wait |
|-------------|------------|
| Salesforce | Complex API, long sales cycles to close deals that need it |
| Custom enterprise SSO (SAML) | Only needed for enterprise deals |
| Data warehouse exports | Build when you have data-heavy customers |

---

## Common Integration Patterns

### Pattern 1: OAuth Sign-In (Google, GitHub, etc.)

**What it does:** Let users log in with existing accounts.

**Tell AI:**
```
Add Google OAuth sign-in to my app.
I'm using [Supabase Auth / Clerk / NextAuth].
Requirements:
- "Sign in with Google" button on login page
- Create user record on first sign-in
- Link to existing account if email matches
- Handle the error case gracefully
```

**Setup checklist:**
```
- [ ] Create OAuth app in provider's developer console
- [ ] Set redirect URI to your production AND localhost URLs
- [ ] Store client ID and secret in environment variables (never in code)
- [ ] Test the full flow: sign in → callback → user created
- [ ] Test edge case: user signs up with email, then tries Google with same email
```

### Pattern 2: Sending Emails (Transactional)

**What it does:** Welcome emails, password resets, notifications.

**Recommended providers:**
- **Resend** — Simple API, good free tier, built for developers
- **SendGrid** — Established, more features, higher free tier
- **Postmark** — Best deliverability, focused on transactional email

**Tell AI:**
```
Set up transactional email with [Resend/SendGrid] for my [framework] app.
I need to send:
- Welcome email on signup
- Password reset email
- [Other emails you need]
Use environment variables for API keys.
Include error handling if the email fails to send.
```

### Pattern 3: Webhooks (Receiving)

**What it does:** Third-party services notify your app when something happens (e.g., Stripe payment succeeded).

**Tell AI:**
```
Create a webhook endpoint for [Stripe/service] in my [framework] app.
Requirements:
- Verify the webhook signature (critical for security)
- Handle these events: [list events, e.g., checkout.session.completed]
- Respond with 200 quickly, process async if needed
- Log the raw payload for debugging
- Handle duplicate events (idempotency)
```

**Webhook checklist:**
```
- [ ] Endpoint URL is configured in the third party's dashboard
- [ ] Webhook signature is verified on every request
- [ ] Endpoint responds with 200 within 5 seconds
- [ ] Failed processing retries gracefully
- [ ] Events are idempotent (processing the same event twice is safe)
- [ ] Raw payloads are logged for debugging
```

### Pattern 4: Webhooks (Sending)

**What it does:** Your app notifies customer systems when something happens.

**Tell AI:**
```
Add outgoing webhooks to my app so customers can receive events.
Requirements:
- Customers can register a webhook URL in settings
- Send POST requests with JSON payload when [events] occur
- Include a signature header for verification
- Retry failed deliveries 3 times with exponential backoff
- Show delivery status in the customer's dashboard
```

### Pattern 5: Zapier Integration

**What it does:** Lets your customers connect your app to 5,000+ other apps without you building each integration.

**When to build:** When multiple customers ask for integrations you don't want to build individually.

**Tell AI:**
```
Help me plan a Zapier integration for [product].
My app can:
- Triggers (things that happen): [e.g., new project created, task completed]
- Actions (things Zapier can do in my app): [e.g., create a task, update a record]
What API endpoints do I need to expose for Zapier?
```

---

## API Key Management

### For Your API Keys (Connecting to Services)

```
Rules:
- [ ] NEVER put API keys in code. Use environment variables.
- [ ] Different keys for development and production.
- [ ] Rotate keys if you accidentally commit one (immediately).
- [ ] Document which keys are needed in a .env.example file.
- [ ] Use the narrowest permissions possible for each key.
```

### For Your Customers' API Keys (If You Offer an API)

```
- [ ] Generate unique keys per customer
- [ ] Allow customers to revoke and regenerate keys
- [ ] Rate limit by API key
- [ ] Log usage by API key
- [ ] Hash stored keys (don't store in plain text)
```

---

## Error Handling for Integrations

Every integration will fail at some point. Plan for it:

```
Integration Error Handling Checklist:
- [ ] What happens if the API is down? (Queue and retry? Show error to user?)
- [ ] What happens if auth credentials expire? (Re-auth flow? Alert the user?)
- [ ] What happens if the API returns unexpected data? (Log and fail gracefully?)
- [ ] What happens if rate limits are hit? (Backoff and retry? Queue?)
- [ ] Is there a timeout? (Don't wait forever for a response)
- [ ] Are errors logged with enough context to debug?
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Building custom integrations nobody asked for | Wait for 3+ customer requests before building |
| API keys in source code | Environment variables, always |
| No webhook signature verification | Verify every incoming webhook. Unverified = security hole |
| No error handling on API calls | Every external call needs try/catch and a fallback |
| Building what Zapier can handle | Recommend Zapier to customers. Build only what Zapier can't |
| No retry logic for failed webhooks | Retry 3x with exponential backoff |
| Testing only the happy path | Test: API down, bad credentials, rate limited, timeout |

---

## Success Looks Like

- Core integrations (payments, email, auth) working reliably in production
- Third-party API keys stored securely in environment variables
- Webhook endpoints verified, idempotent, and logged
- Customers can connect the tools they need (directly or via Zapier)
- You can debug integration failures quickly with proper logging
