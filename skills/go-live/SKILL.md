---
name: go-live
description: "Use this skill when the user is about to launch, thinks they're ready to go live, wants a pre-launch checklist, or asks 'am I ready to launch?' This is the quality gate between building/testing and deploying/launching — a single go/no-go decision that checks whether the product is actually ready for real users and real money."
---

# Go-Live Checklist

You've built it. You've tested it. Before you put it in front of real users paying real money, run through this checklist. Every item takes minutes to check — and catching a problem here saves you from catching it in front of customers.

## Core Principles

- This is a gate, not a process. If you pass, launch. If you don't, fix the gaps and come back.
- "It works for me" is not the same as "it works." Test as if you're a stranger visiting for the first time.
- Skipping items here is borrowing from your future self. You'll fix them eventually — it's cheaper to fix them now.
- Perfect is the enemy of launched. But "payments don't work" is not a perfectionism issue — it's a showstopper.

---

## The Checklist

### Showstoppers (Must Pass)

These will directly lose you customers or money if broken. Do not launch without them.

```
Showstoppers:
- [ ] Core flow works end-to-end: signup → key action → value delivered
- [ ] Payments work: can complete a real purchase (use Stripe test mode, then one real transaction)
- [ ] Auth works: can sign up, log in, log out, reset password
- [ ] HTTPS is on: no "Not Secure" warning in browser
- [ ] No secrets in code: API keys are in environment variables, not committed to git
```

### User Experience (Should Pass)

These won't break your app, but they'll make users bounce or lose trust.

```
User Experience:
- [ ] Mobile works: tested on an actual phone, not just browser resize
- [ ] 404 page exists: broken links show a helpful page, not a blank screen or error
- [ ] 500 page exists: server errors show "Something went wrong," not a stack trace
- [ ] Loading speed: pages load in under 3 seconds (test at pagespeed.web.dev)
- [ ] Error messages make sense: users see "Email already taken," not "Error 422"
```

### Operations (Should Have)

These keep you informed and protected once real users show up.

```
Operations:
- [ ] Error tracking live: Sentry or similar installed, catching real errors
      → See **monitor** skill for setup
- [ ] Analytics tracking: you know where visitors come from and what they do
      → See **analytics** skill for setup
- [ ] Uptime monitoring: you get alerted if the site goes down
      → See **monitor** skill for setup
- [ ] Backups enabled: database is backed up automatically (daily minimum)
      → See **deploy** skill for database backup setup
```

### Professional Polish (Should Have)

These signal "real business" vs. "side project."

```
Professional Polish:
- [ ] Custom domain connected: yourproduct.com, not yourapp.vercel.app
      → See **deploy** skill for domain setup
- [ ] Social/OG tags set: links look good when shared on LinkedIn, Twitter, Slack
- [ ] Favicon set: browser tab shows your icon, not a blank square
- [ ] Legal docs published: Terms of Service and Privacy Policy are linked in footer
      → See **legal** skill for templates
```

### Industry-Specific (If Applicable)

```
If you're in a regulated industry:
- [ ] Compliance requirements met (HIPAA, SOC2, PCI, FERPA, etc.)
      → See **compliance** skill for your industry's requirements
- [ ] Data handling matches your Privacy Policy
- [ ] Required disclosures are visible
```

---

## How to Use This Checklist

**Tell AI:**
```
I'm about to launch my SaaS app. Go through this pre-launch checklist with me:

My app: [what it does, one sentence]
Built with: [Lovable / Claude Code / Replit / Cursor]
Hosted on: [Vercel / Railway / Netlify / Lovable / Replit / other]
Payments: [Stripe / Lemon Squeezy / none yet]

For each item, check whether it's set up. For anything missing,
tell me the fastest way to fix it with my specific stack.
```

---

## Go / No-Go

```
All Showstoppers pass?
  → YES: You can launch. Fix User Experience and Operations items this week.
  → NO:  Do not launch. Fix showstoppers first.
```

Launching with imperfect polish is fine. Launching with broken payments, broken auth, or exposed secrets is not.

---

## After You Launch

Your go-live checklist becomes your post-launch monitoring list. In week 1, check daily:

- Are errors showing up in Sentry? Fix them.
- Are users completing signup? If not, the flow is broken.
- Are payments processing? If not, you're working for free.
- Is the site staying up? If not, check your hosting.

---

## Related Skills

- **test** — Structured QA workflow to find bugs before launch
- **deploy** — Get your app live on a custom domain
- **secure** — Security checklist (HTTPS, auth, secrets, input validation)
- **monitor** — Error tracking, uptime alerts, and performance monitoring
- **legal** — Terms of Service, Privacy Policy, and business entity setup
- **analytics** — Set up tracking so you know what users do
- **launch** — Plan and execute your launch once you pass this gate
