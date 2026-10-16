---
name: secure
description: "Use this skill to find and fix the security holes that AI-built apps most often ship with: 'is my app secure,' 'security check,' 'check my app for security holes,' 'can users see each other's data,' 'did I leak my API keys,' or 'I'm worried about hackers.' Claude runs the audit on the codebase: exposed keys, data isolation between users, auth on every route, webhook signatures, rate and spend limits, and dependencies. Not for the full pre-launch checklist (use go-live) or for privacy policy and legal terms (use legal)."
metadata:
  version: 1.0.0
---

# Secure

Run a security audit on the codebase and fix what matters first. AI-built apps fail in a few predictable places. Check those places, prove each finding, and fix it.

## Step 1: Map the app

Read the code and list, briefly:
- the framework, and where the server code runs
- the database, and whether the browser talks to it directly
- how users log in
- every API route, server action, and webhook endpoint
- every third-party key the app uses
- every call that costs money: AI models, email, SMS

## Step 2: Run the checks, worst damage first

**1. Secrets**
- Search the code and the git history for keys and passwords.
- Check that `.env` files are in `.gitignore`.
- List every environment variable that reaches the browser. Most frameworks mark these with a public prefix. None of them may hold a secret.
- A database key that bypasses access rules (an admin or service key) must never reach the browser.
- A secret that was ever committed must be rotated. Deleting the file does not remove it from git history.

**2. Data isolation: one customer can never see another's data**
- Every query that returns customer data must filter by the signed-in user or account on the server.
- If the browser queries the database directly, the database's own access rules must cover every table, for read, create, update, and delete.
- **Prove it:** create two accounts. As account A, request one of B's records by changing the ID in the URL or the API call. The request must fail. This is the most damaging bug in AI-built apps, and it is invisible in normal use.

**3. Auth on every route**
- Every route and server action checks that the user is signed in.
- Every route and server action checks that the user owns the object it touches.
- Admin pages check the user's role on the server. Hiding the link is not protection.

**4. Payments and webhooks**
- Webhook endpoints verify the signature before they act.
- Paid access is granted from the verified webhook, never from the "thank you" page that the browser loads (see **payments**).

**5. Abuse and cost**
- Rate-limit sign-in, sign-up, password reset, and every endpoint that costs money.
- Put a daily per-user cap on AI calls, and a spending limit or alert at the AI provider. One script hitting an open AI endpoint can cost more in a night than the business makes in a month.

**6. Input and output**
- Validate input on the server.
- Use parameterized queries or the ORM, never strings built from user input.
- Never render user input as raw HTML.
- Check the type and size of uploaded files.

**7. Dependencies**
Run the package manager's audit command. Fix the high and critical findings.

**8. Errors and logs**
- Users never see stack traces.
- Logs never contain passwords, tokens, card numbers, or more personal data than needed.

## Step 3: The regulated-data gate

If the app stores health records, financial account data, children's data, or student records, stop and tell the founder plainly that special rules apply. For example, US health data requires a signed agreement with every host that stores it. Recommend a review by a specialist before launch. This checklist is not enough for that data.

## Step 4: Fix

Fix the critical findings now, with the founder's approval. After each fix, re-run the check that found it. List the rest with a plain-language risk for each.

## Rules

- **Prove each finding before you report it.** A finding without evidence wastes the founder's time and teaches them to ignore you.
- **Use a well-known auth library or service.** Never build password storage or sessions from scratch.
- **Not yet:** a paid penetration test (wait for sensitive data or about 1,000 users), single sign-on (wait until customers ask), or a web application firewall (the host covers the basics).

## Output

```
| Severity | Finding | Where (file:line) | Proof | Fix | Status |
```

Severity: **Critical** (data or money can leak now), **High** (likely to be exploited), **Low** (fix when convenient). End with one sentence on whether the app is safe to put in front of paying customers.
