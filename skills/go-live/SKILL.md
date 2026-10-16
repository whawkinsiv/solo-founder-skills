---
name: go-live
description: "Use this skill for the go/no-go check before real customers use the app and pay: 'am I ready to launch,' 'is it ready to go live,' 'pre-launch checklist,' 'deploy my app,' 'set up my domain,' 'how do I know if my site goes down,' or 'set up backups.' Checks the core flow, payments, security basics, backups with a restore test, error tracking, uptime alerts, and rollback, then gives a verdict. Not for the launch announcement itself (use first-customers) or for a full security audit (use secure)."
metadata:
  version: 2.0.0
---

# Go Live

A gate, not a process. Check the app the way a stranger with a credit card would meet it. Pass, and the founder lets customers in. Fail, and the founder fixes the showstoppers first.

## Step 1: Deploy, if not live yet

- Use a managed host that deploys from git, so every push deploys.
- Production has its own environment variables, set in the host's dashboard or CLI, and its own database, separate from development.
- Connect the custom domain at the host. The host lists the DNS records to add.
- Skip a staging environment until there are paying customers.
- The first deploy should take under 30 minutes. If it takes hours, simplify.
- "Works locally, broken in production" is usually a missing environment variable. Check those first.

## Step 2: Showstoppers (all must pass)

1. **The core flow works for a stranger.** In a fresh private browser window, get access (sign up, or the manual onboarding the founder uses), do the key action, and get the result.
2. **Write one automated smoke test** for that flow, if the project can run browser tests, and run it. Re-run it before every deploy.
3. **Taking money works.** Make one real payment with a real card, then refund it. A payment link counts at this stage. Full billing can come later.
4. **Security basics pass.** Run the secrets check and the two-account data-isolation check from **secure**.
5. **HTTPS works** on the real domain.
6. **Backups run automatically, and one restore has worked.** Restore a backup to a test copy once. A backup that was never restored is a hope, not a backup.

## Step 3: Should pass (fix this week)

- **Error tracking** is installed, and a test error has arrived.
- **An uptime check** emails or texts the founder when the site is down.
- **Rollback:** the founder can return to the previous version in under 5 minutes. Find out how on their host and write it down.
- It works on a real phone, not only a resized browser window.
- A helpful 404 page and error page, a page title, description, share image, and favicon.
- Terms and a privacy policy are linked in the footer (**legal**).
- A support address reaches the founder (**email**).
- **Numbers:** track three things: visits, sign-ups or purchases, and where visitors came from. Until that is set up, a weekly spreadsheet is enough. Skip dashboards.

## Step 4: Fresh-eyes test

Watch one person who has never seen the app try the core flow. Do not help. Note where they hesitate, what they click that you did not expect, and whether they can say what the app does after two minutes. This finds more than a week of testing alone.

## Step 5: Re-test after every fix

After each fix, re-check two things: the thing you fixed, and the core flow. Fixes often break something else.

## Rules

- **Imperfect polish is fine. Broken payments, broken access, or leaked data are not.**
- **In the first week live, check daily:** new errors, whether sign-ups or purchases complete, and whether the site stayed up.
- **Do not add monitoring tools beyond error tracking and an uptime check** until the free tiers run out.

## Output

```
Showstoppers:  <each: pass / fail, with the fix if failed>
Should pass:   <each: pass / fail>
Verdict:       GO / NO-GO
This week:     <the fixes, in order>
```
