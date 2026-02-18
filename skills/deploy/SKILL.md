---
name: deploy
description: "Use this skill when the user needs to deploy their app, choose a hosting provider, connect a custom domain, set up environment variables, manage a production database, configure DNS, or go from 'it works locally' to 'it's live on the internet.' Covers hosting selection, deployment workflows, domain setup, and production operations for non-technical founders."
---

# Deployment & Going Live Expert

Act as a top 1% deployment specialist who has helped hundreds of non-technical founders get their apps live on the internet. You understand that "deployment" is the scariest part for someone who built their app in Lovable, Replit, or with Claude Code — the gap between "it works on my screen" and "anyone can use it" feels enormous. You make it simple.

## Core Principles

- The best hosting platform is the one that matches how you built. Don't migrate unless you have to.
- Managed beats self-managed every time for solo founders. Pay more, worry less.
- Your first deployment should take under 30 minutes. If it's taking hours, you're overcomplicating it.
- Custom domains are not optional for a real business. yourapp.vercel.app is not professional.
- Backups are not optional. If you don't have them, you don't have a business.

## Choose Your Hosting

### If You Built With These Tools

| Built With | Deploy To | Why |
|-----------|-----------|-----|
| **Lovable** | Lovable's built-in hosting | Already deployed. Just connect your domain. |
| **Replit** | Replit Deployments | One-click deploy from your Repl. Built in. |
| **Bolt / Stackblitz** | Netlify or Vercel | Export code, connect git repo, auto-deploys. |
| **Claude Code (Next.js, React)** | Vercel | Built for Next.js. Git push = deploy. |
| **Claude Code (any framework)** | Railway | Supports everything. Simple dashboard. |
| **Claude Code (static site)** | Netlify or Cloudflare Pages | Free tier is generous. Fast global CDN. |
| **Claude Code (Python/Django/Flask)** | Railway or Render | Good Python support with managed databases. |

### Hosting Comparison for Solo Founders

| Platform | Free Tier | Ease | Database | Custom Domain | Best For |
|----------|-----------|------|----------|---------------|----------|
| **Vercel** | Generous | Very easy | No (use Supabase) | Yes | Next.js, React apps |
| **Railway** | $5 credit/mo | Easy | Yes (Postgres) | Yes | Full-stack apps, any framework |
| **Netlify** | Generous | Very easy | No | Yes | Static sites, JAMstack |
| **Render** | Free tier | Easy | Yes (Postgres) | Yes | Full-stack, background jobs |
| **Fly.io** | Limited free | Moderate | Yes (Postgres) | Yes | Global distribution, Docker |
| **Cloudflare Pages** | Very generous | Easy | No (use D1 or Supabase) | Yes | Static sites, edge functions |
| **Replit** | Included | Easiest | Yes (built-in) | Yes | Apps built in Replit |
| **Lovable** | Included | Easiest | Yes (Supabase) | Yes | Apps built in Lovable |

**Recommendation for most solo founders:** Vercel (for Next.js) or Railway (for everything else).

---

## Deployment: Step by Step

### Path 1: Lovable / Replit (Already Deployed)

Your app is already running. You just need a custom domain:

1. Buy a domain (Namecheap, Cloudflare, or Google Domains)
2. In your Lovable/Replit dashboard, go to Settings → Custom Domain
3. Add your domain name
4. Update DNS records at your domain registrar (they'll tell you what to add)
5. Wait 5-30 minutes for DNS propagation
6. SSL certificate is automatic — your site will be HTTPS

### Path 2: Vercel (Next.js / React)

```
Deployment Checklist — Vercel:
- [ ] Push your code to a GitHub repository
- [ ] Go to vercel.com → "Add New Project"
- [ ] Connect your GitHub repo
- [ ] Vercel auto-detects framework and configures build settings
- [ ] Add environment variables (Settings → Environment Variables)
- [ ] Click "Deploy"
- [ ] Connect custom domain (Settings → Domains)
- [ ] Update DNS (Vercel gives you the records)
- [ ] Verify HTTPS is working
```

**Tell AI:**
```
Help me deploy my Next.js app to Vercel. My app uses:
- Framework: [Next.js version]
- Database: [Supabase/PlanetScale/etc.]
- Environment variables I need: [list them]
Walk me through the steps and tell me what environment variables
to set in the Vercel dashboard.
```

### Path 3: Railway (Any Framework)

```
Deployment Checklist — Railway:
- [ ] Push code to GitHub repository
- [ ] Go to railway.app → "New Project"
- [ ] Choose "Deploy from GitHub Repo"
- [ ] Select your repo
- [ ] Add environment variables in the Railway dashboard
- [ ] If you need a database: click "New" → "Database" → "PostgreSQL"
- [ ] Railway gives you a DATABASE_URL — add it to your app's env vars
- [ ] Click "Deploy"
- [ ] Connect custom domain (Settings → Networking → Custom Domain)
- [ ] Update DNS records
```

---

## Environment Variables

Environment variables store secrets (API keys, database passwords) that should never be in your code.

### What Goes in Environment Variables

```
Common Environment Variables:
DATABASE_URL=postgresql://user:password@host:5432/dbname
STRIPE_SECRET_KEY=sk_live_...
STRIPE_PUBLISHABLE_KEY=pk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
SUPABASE_SERVICE_ROLE_KEY=eyJ...
EMAIL_API_KEY=re_...
NEXTAUTH_SECRET=random-string-here
NEXTAUTH_URL=https://yourdomain.com
NODE_ENV=production
```

### Rules

- **Never commit secrets to git.** Add `.env` and `.env.local` to `.gitignore`.
- **Each environment (dev/staging/prod) has its own variables.** Don't share them.
- **Use your hosting platform's dashboard** to set production variables. Not a file on a server.
- **Rotate keys if you accidentally commit them.** Immediately. Git history preserves secrets even if you delete the file.

**Tell AI:**
```
List all the environment variables my app needs for production deployment.
My app uses: [list your services — Supabase, Stripe, email provider, etc.]
Show me which ones are public (safe for client-side) and which are secret
(server-only).
```

---

## Custom Domains

### Buying a Domain

- **Namecheap** or **Cloudflare Registrar** — cheapest, no markup
- Get a `.com` if possible. `.io` and `.co` are fine for SaaS
- Avoid hyphens, numbers, and hard-to-spell names
- Budget: $10-15/year for a .com

### DNS Setup

Your hosting platform will tell you exactly which DNS records to add. Typical setup:

| Record Type | Name | Value | Purpose |
|------------|------|-------|---------|
| A | @ | 76.76.21.21 (example) | Points root domain to host |
| CNAME | www | cname.vercel-dns.com (example) | Points www to host |

**Where to add DNS records:** Log in to wherever you bought your domain (Namecheap, Cloudflare, etc.) → DNS Settings → Add the records your hosting platform gives you.

**DNS propagation** takes 5 minutes to 48 hours (usually under 30 minutes). Be patient.

### SSL / HTTPS

- Every modern hosting platform provides free SSL certificates automatically
- If your site shows "Not Secure" after connecting a domain, wait 30 minutes for SSL to provision
- If it still doesn't work after an hour, check that your DNS records are correct

---

## Database in Production

### If You're Using Supabase

Supabase is already hosted. Your production app connects to the same Supabase project (or a separate one for production):

```
Production Database Checklist — Supabase:
- [ ] Create a separate Supabase project for production (don't share with dev)
- [ ] Run your migrations on the production database
- [ ] Enable Row Level Security (RLS) on all tables
- [ ] Set up database backups (Supabase Pro plan includes daily backups)
- [ ] Use the production URL and keys in your production env vars
```

### If You Need a Hosted Database

| Service | Free Tier | Best For |
|---------|-----------|----------|
| **Supabase** | 500MB, 2 projects | Postgres + auth + storage |
| **Railway Postgres** | Included with $5 credit | Apps already on Railway |
| **PlanetScale** | 1 billion row reads/mo | MySQL, branching workflow |
| **Neon** | 512MB | Serverless Postgres |
| **Render Postgres** | 1GB, 90-day limit | Apps already on Render |

---

## Backups

If you don't have backups, a single mistake can destroy your business.

```
Backup Checklist:
- [ ] Database backups enabled (daily minimum)
- [ ] Verified you can restore from a backup (test this!)
- [ ] Code is in a git repository (GitHub/GitLab)
- [ ] Environment variables documented (not in code, but you know what they all are)
- [ ] File uploads stored in cloud storage (S3, Supabase Storage, Cloudflare R2)
```

**Database backups by platform:**
- **Supabase:** Daily backups on Pro plan. Point-in-time recovery on Team plan.
- **Railway:** Daily backups included. One-click restore.
- **Render:** Daily backups. 7-day retention on paid plans.
- **PlanetScale:** Automatic backups with branching.

---

## Monitoring Your Live App

Once deployed, set up basic monitoring (see monitor skill for full guidance):

```
Minimum Viable Monitoring:
- [ ] Uptime check — Use BetterUptime, UptimeRobot (free), or Checkly
- [ ] Error tracking — Use Sentry (free tier) to catch production errors
- [ ] Alerts — Get notified by email or Slack when your site goes down
- [ ] Check your app once daily — log in and use it like a customer
```

---

## When Things Go Wrong

### "My site is down"

1. Check your hosting dashboard for deploy errors or resource limits
2. Check your database — is it running? Is it full?
3. Check environment variables — did any API keys expire?
4. Check Stripe/Supabase/other service status pages
5. If you can't figure it out within 30 minutes, check your hosting platform's logs

**Tell AI:**
```
My app at [URL] is showing [error]. I'm hosted on [platform] with
[database]. Here are the error logs: [paste logs]. Help me figure out
what's wrong and how to fix it.
```

### "I deployed but it looks broken"

- **Blank page:** Check browser console (F12) for JavaScript errors. Usually a missing environment variable.
- **API errors:** Environment variables are probably not set in production.
- **Works locally but not in production:** 99% of the time it's environment variables.
- **Styling looks wrong:** Check that your CSS/Tailwind build step is running in the deploy.

### "I need to roll back"

- **Vercel:** Dashboard → Deployments → click on previous deployment → "Promote to Production"
- **Railway:** Dashboard → Deployments → click on previous deployment → "Rollback"
- **Netlify:** Dashboard → Deploys → click on previous deploy → "Publish deploy"

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Committing API keys to GitHub | Add `.env` to `.gitignore`. Rotate any leaked keys immediately |
| Using the same database for dev and production | Create separate environments. One bad query shouldn't break production |
| No backups | Enable database backups today. Not tomorrow. Today |
| Skipping custom domain | Buy one. $10/year. yourapp.com builds trust |
| Overcomplicating deployment | Use the platform that matches your build tool. Don't migrate unnecessarily |
| Not testing after deploy | Always click through your app after every deployment |
| Ignoring deploy logs | When something breaks, logs tell you why. Learn to read them |

---

## Success Looks Like

- Your app is live at your custom domain with HTTPS
- Deploys happen automatically when you push code (or click a button)
- Environment variables are set in the hosting dashboard, not in code
- Database is backed up daily
- You get an alert within 5 minutes if your site goes down
- You can roll back to a previous version in under 2 minutes
