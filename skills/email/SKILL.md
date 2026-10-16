---
name: email
description: "Use this skill to set up a professional email address on the founder's domain and make sure email lands in inboxes: 'hello@ email,' 'branded email,' 'business email,' 'email forwarding,' 'send from my domain,' 'SPF,' 'DKIM,' 'DMARC,' 'my emails go to spam,' or 'set up email for my app.' Covers a free forwarding setup, sending as the branded address, the three DNS records, and app email from a subdomain. Not for onboarding or win-back email sequences (use retention) or for writing outreach (use first-customers)."
metadata:
  version: 2.0.0
---

# Email

Set up `hello@yourdomain.com` before the first outreach. A message from a personal webmail address reads as a side project. One that lands in spam is never read.

## Step 1: Receive mail at the domain

Forward `hello@` to the founder's existing inbox. Many DNS providers and registrars offer free forwarding (for example, Cloudflare Email Routing). Add aliases for `support@` and `billing@` that forward to the same inbox, and filter them by label.

## Step 2: Send as the branded address

Pick one option:
- **Free:** add the address in the inbox's "send mail as" setting, through the SMTP relay of a transactional email service. Verify the domain in that service first.
- **Paid and simpler:** a hosted mailbox on the domain (Google Workspace, Fastmail, or similar). Choose this when the founder wants less setup, needs calendar invites from the branded address, or adds a second person.

Make the branded address the default "from" address.

## Step 3: Add SPF, DKIM, and DMARC

These DNS records prove the mail is really from the domain. Without them, mail lands in spam and anyone can send mail that pretends to be the founder.

- **SPF:** one TXT record that lists every service allowed to send for the domain. A domain may have only one SPF record. Merge the `include:` entries into it.
- **DKIM:** each sending service gives you its own record. Add every one.
- **DMARC:** start with monitoring only:
  ```
  _dmarc  TXT  v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com
  ```
  After 2–4 weeks of reports that show only your own services sending, change `p=none` to `p=quarantine`. A strict policy set up too early can send the founder's own mail to spam.

**Verify:** send a message to a Gmail address, open "Show original", and check that SPF, DKIM, and DMARC all show PASS.

## Step 4: App email

- Send password resets, receipts, and notifications through a transactional email service, from a subdomain such as `mail.yourdomain.com`. That keeps problems with app email from hurting the main domain's reputation.
- Use a real reply-to address, not `noreply@`. Customer replies are the cheapest feedback there is.
- Include a plain-text version of every message.
- Marketing email needs a one-click unsubscribe link. Never send bulk marketing from the founder's personal inbox setup.

## Rules

- **Keep cold outreach small:** 10–20 personal messages a day from the main domain. Bulk cold email ruins a domain's reputation.
- **Set up the records before the first send,** not after mail starts landing in spam.

## Output

A working `hello@` address that sends and receives, the DNS records added, and a test message with SPF, DKIM, and DMARC all at PASS.
