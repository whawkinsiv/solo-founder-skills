# Monitoring Setup Guide

Step-by-step setup for production monitoring.

---

## Setup Priority

**Start here (15 minutes):**
1. Uptime monitoring
2. Error tracking
3. Basic alerts

**Add later (optional):**
4. Performance monitoring
5. Analytics
6. Advanced alerting

---

## Uptime Monitoring Setup

### UptimeRobot (Recommended)

**1. Sign up:**
- Go to uptimerobot.com
- Free account (50 monitors)

**2. Add monitor:**
```
Monitor Type: HTTPS
Friendly Name: YourApp Production
URL: https://yourapp.com
Monitoring Interval: 5 minutes (free tier)
```

**3. Configure alerts:**
```
Alert Contacts:
- Email: your@email.com
- SMS: your-phone (if offered)

Alert When:
- Down
- Seems down (slow to respond)

Don't alert:
- Planned maintenance (you can pause monitoring)
```

**4. Test:**
```
1. Monitoring starts immediately
2. Check dashboard shows "Up"
3. Pause monitor (test alert)
4. Should get email/SMS
5. Resume monitoring
```

### Alternative: Pingdom

**Similar setup:**
- Limited free tier (10 checks)
- More detailed reporting
- Better for multiple sites

---

## Error Tracking Setup

### Sentry (Recommended)

**1. Sign up:**
- Go to sentry.io
- Free tier: 5,000 errors/month

**2. Create project:**
```
Platform: JavaScript (if React/Next.js)
Or: Node.js (if backend only)
Project name: yourapp-production
```

**3. Get DSN:**
```
Sentry provides DSN (Data Source Name)
Example: https://abc123@sentry.io/456789
Copy this
```

**4. Tell AI to integrate:**
```
Add Sentry error tracking:

DSN: [paste your DSN]

Capture:
- All JavaScript errors
- All unhandled promise rejections
- API errors (4xx, 5xx)
- Console errors

Include context:
- User ID (if logged in)
- Page URL
- Browser info
- User action that triggered error

Don't capture:
- Expected validation errors
- 404s on assets
- Passwords or sensitive data
```

**5. Verify:**
```
Tell AI:
"Add test error button (dev only) that throws error.
Let's verify Sentry catches it."

Click button → Error appears in Sentry dashboard
```

**6. Configure alerts:**
```
In Sentry dashboard:
Settings → Alerts

New Alert:
- When: New issue appears
- Send to: Your email
- Frequency: Immediately

Another alert:
- When: Issue happens 10+ times in 1 hour
- Send to: Your email/SMS
- Frequency: At most once per hour
```

---

## Performance Monitoring

### Vercel Analytics (if using Vercel)

**Setup:**
```
1. Vercel project → Analytics tab
2. Enable Web Analytics
3. Automatically tracks:
   - Page views
   - Web Vitals (performance)
   - Visitor data
```

**Free tier:** Included with Vercel

### Cloudflare Analytics (any hosting)

**Setup:**
```
1. Site through Cloudflare (free)
2. Dashboard → Analytics
3. Automatic tracking:
   - Requests
   - Bandwidth
   - Threats blocked
   - Response times
```

**Free tier:** Basic analytics included

### Google PageSpeed Insights

**Manual checks:**
```
1. Go to pagespeed.web.dev
2. Enter: https://yourapp.com
3. Run test
4. Check scores (aim for 90+)
5. Review suggestions
```

**Not automatic** - run weekly

---

## Logging Setup

### Platform Logs

**Vercel:**
```
Dashboard → Deployments → [Recent] → Logs
- Real-time logs
- Filter by level
- Search functionality
```

**Netlify:**
```
Dashboard → Functions → [Function] → Logs
- Function logs
- Build logs
- Deploy logs
```

**Railway/Render:**
```
Dashboard → Logs
- Application logs
- Build logs
- Live tail
```

### Application Logging

**Tell AI:**
```
Add structured logging:

Format: JSON with fields:
- timestamp: ISO 8601
- level: ERROR, WARN, INFO
- message: Human readable
- context: {userId, action, etc}

Log:
- All errors with stack traces
- API requests (method, path, status, duration)
- Authentication events (login, logout, failed attempts)
- Slow operations (>1 second)

Don't log:
- Passwords
- Credit cards
- API keys
- Session tokens

Examples:
{
  "timestamp": "2025-01-13T10:30:45Z",
  "level": "ERROR",
  "message": "API request failed",
  "context": {
    "userId": "123",
    "endpoint": "/api/dashboard",
    "status": 500,
    "error": "Database timeout"
  }
}
```

---

## Alert Configuration

### Critical Alerts (Text/Call)

**Set up for:**
```
1. Site completely down (UptimeRobot)
2. Error rate spike (>10x normal in Sentry)
3. Payment processing failing (Stripe webhook)
4. Database connection lost

Delivery:
- SMS to phone
- PagerDuty (if team)
- Slack (urgent channel)

Frequency:
- Immediately
- Repeat every 15 min until acknowledged
```

### Important Alerts (Email)

**Set up for:**
```
1. Error rate elevated (2x normal)
2. API response time slow (>2s)
3. Disk space warning (>80%)
4. Failed email deliveries
5. Failed payments

Delivery:
- Email to you
- Slack (if team)

Frequency:
- Within 1 hour
- Don't repeat unless worsens
```

### Informational (Daily Digest)

**Set up for:**
```
1. Error summary (new error types)
2. Performance summary (trends)
3. Traffic summary (peak times)
4. User activity (new signups)

Delivery:
- Email digest
- Dashboard

Frequency:
- Once daily (morning)
```

---

## Dashboard Setup

### Single Dashboard View

**Combine metrics:**
```
Use Notion/Spreadsheet/Dashboard tool

Track daily:
- Uptime % (from UptimeRobot)
- Error count (from Sentry)
- Active users (from analytics)
- Response time (from platform)

5-minute daily check.
```

### Recommended Layout

```
YourApp Production Health
Last updated: [Auto]

Status:
🟢 Uptime: 99.98% (24hr)
🟢 Errors: 12 (24hr)
🟢 Response: 245ms avg
🟢 Users: 145 active (24hr)

Recent Issues:
- None

Recent Deploys:
- 2025-01-13 09:30 - Feature X deployed
```

---

## Monitoring for Key Features

### Authentication

**Monitor:**
```
- Failed login attempts
- Account lockouts
- Password reset requests
- Successful logins

Alert when:
- Failed logins spike (potential attack)
- Password resets spike (potential breach)
```

### Payments

**Monitor:**
```
- Successful payments
- Failed payments
- Refunds requested
- Subscription cancellations

Alert when:
- Payment success rate <95%
- Any failed payment (critical)
```

### API Endpoints

**Monitor:**
```
- Response times per endpoint
- Error rates per endpoint
- Request volume per endpoint

Alert when:
- Any endpoint >2s response
- Any endpoint >5% error rate
```

---

## Third-Party Monitoring

### Stripe Monitoring

**Setup webhook alerts:**
```
Tell AI:
"Configure Stripe webhooks:
- charge.failed → Alert immediately
- payment_intent.payment_failed → Alert
- customer.subscription.deleted → Log

Send alerts to [email/slack]"
```

### SendGrid Monitoring

**Setup in SendGrid:**
```
Alerts → Email Activity
Configure alerts for:
- Bounces >5% (daily)
- Spam reports >0.1% (daily)
- Blocks >1% (daily)
```

### Database Monitoring

**Tell AI:**
```
Add database monitoring:
- Connection pool size (alert if >80%)
- Slow queries (log if >1s)
- Failed connections (alert immediately)
- Disk space (alert if >80%)

Report hourly stats to logs.
```

---

## Testing Your Monitoring

### Test Uptime Alerts

```
1. Pause UptimeRobot monitor
2. Wait 5 minutes
3. Should receive "Down" alert
4. Resume monitor
5. Should receive "Up" alert

If no alerts: Check alert contacts configured
```

### Test Error Tracking

```
Tell AI:
"Add test endpoint: /api/test-error
Throws error when called (dev/staging only)
Remove before production."

1. Call endpoint
2. Check Sentry dashboard
3. Error should appear
4. Alert should fire (if configured)

If no error in Sentry: Check DSN configuration
```

### Test Performance Monitoring

```
1. Open site in incognito
2. Check DevTools → Network
3. Record load time
4. Compare to monitoring dashboard
5. Should be similar

If different: Check monitoring integration
```

---

## Monitoring Checklist

**Before launch:**
```
- [ ] Uptime monitoring configured
- [ ] Error tracking integrated
- [ ] Critical alerts set up (SMS/email)
- [ ] Logs capturing errors
- [ ] Test alerts working
- [ ] Dashboard accessible
- [ ] Know how to respond to alerts
```

**After launch:**
```
- [ ] Check monitoring daily
- [ ] Review weekly trends
- [ ] Adjust alerts (reduce noise)
- [ ] Add monitoring for new features
```

---

## Monitoring Costs

**Free tier sufficient for:**
- < 1,000 users
- < 5,000 errors/month
- < 50 uptime checks
- Basic analytics

**When to upgrade:**
- Growing fast
- Need more detailed data
- Need faster alerts
- Need longer retention

**Typical costs:**
- Sentry Pro: $26/mo
- UptimeRobot Plus: $7/mo
- LogRocket: $99/mo (optional)

**Total: ~$30-40/mo for serious monitoring**

---

## Quick Reference

**15-Minute Monitoring Setup:**
```
1. UptimeRobot account (5 min)
   - Add monitor
   - Configure email alert

2. Sentry account (5 min)
   - Create project
   - Get DSN
   
3. Tell AI to integrate (5 min)
   - Add Sentry to app
   - Test error capture
   
Done. You're now monitoring.
```