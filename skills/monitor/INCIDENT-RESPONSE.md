# Incident Response

How to respond when monitoring alerts fire.

---

## Alert Severity Levels

### Critical (Act Immediately)

**Examples:**
- Site completely down
- Payment processing failing
- Database unreachable
- All users can't log in

**Response time:** Drop everything, fix now

**Actions:**
1. Acknowledge alert
2. Check dashboard (confirm it's real)
3. Assess impact (how many users?)
4. Quick fix or rollback
5. Deploy hotfix
6. Monitor for 30 minutes
7. Post-mortem later

### High (Act Within Hour)

**Examples:**
- Error rate spike (10x normal)
- API endpoint failing
- Some users can't log in
- Key feature broken

**Response time:** Within 1 hour

**Actions:**
1. Acknowledge alert
2. Assess scope (which users? which features?)
3. Investigate root cause
4. Plan fix
5. Deploy fix
6. Monitor for hour
7. Update users if needed

### Medium (Act Within Day)

**Examples:**
- Slow performance (2x normal)
- Error rate elevated (2x normal)
- Non-critical feature broken
- Warning thresholds hit

**Response time:** Within 24 hours

**Actions:**
1. Note in issue tracker
2. Investigate when possible
3. Fix in next regular deploy
4. Monitor after deploy

### Low (Act Eventually)

**Examples:**
- Minor performance degradation
- Low-frequency errors
- Edge case bugs
- Cosmetic issues

**Response time:** Next sprint/week

**Actions:**
1. Add to backlog
2. Fix when prioritized

---

## Response Playbooks

### Site Down

```
1. Check monitoring (confirmed down?)
2. Try accessing yourself (different network)
3. Check platform status page (Vercel/Netlify)
4. Check recent deploys (rollback option?)

If platform issue:
- Wait for platform recovery
- Update users via Twitter/status page

If your code:
- Rollback to last working deploy
- Investigate error logs
- Fix and redeploy
- Monitor closely

Timeline: Fix within 5-15 minutes
```

### Error Rate Spike

```
1. Open error tracking (Sentry)
2. Identify most frequent error
3. Check when started
4. Check recent deploys
5. Note: New error or existing?

If new error:
- Recent deploy caused it
- Rollback if critical
- Fix root cause
- Redeploy

If existing error:
- What changed to make it spike?
- Increased traffic? New usage pattern?
- Fix underlying issue

Timeline: Fix within 1 hour
```

### Performance Degradation

```
1. Check which part is slow (API? Frontend? Database?)
2. Check resource usage (CPU, memory, disk)
3. Check for traffic spike
4. Check recent changes

Quick fixes:
- Restart service
- Clear cache
- Add caching
- Scale up resources

Longer fixes:
- Optimize queries
- Add indexes
- Code optimization

Timeline: Quick fix within hour, optimize later
```

### Payment Failing

```
CRITICAL - Act immediately

1. Check Stripe dashboard
2. Check error message
3. Test payment yourself
4. Check webhook logs

Common causes:
- Stripe API key wrong
- Webhook endpoint changed
- Code bug in payment flow
- Stripe service issue

Fix immediately:
- Restore working code
- Fix configuration
- Test payment works
- Monitor all payments for hour

Timeline: Fix within 15 minutes
```

### Database Issues

```
1. Check database status (host dashboard)
2. Check connection pool
3. Check disk space
4. Check slow query log

Quick fixes:
- Restart database service
- Kill long-running queries
- Increase connection pool
- Clear old data

Critical:
- Database down: Contact host immediately
- Disk full: Delete logs/old data

Timeline: Fix within 30 minutes
```

---

## Rollback Procedure

### When to Rollback

**Rollback if:**
- Critical feature broken after deploy
- Error rate 10x higher
- Can't quickly identify fix
- Site unusable

**Don't rollback if:**
- Minor issue
- Know quick fix
- Only affects edge cases
- Can hotfix faster than rollback

### How to Rollback

**Vercel/Netlify:**
```
1. Dashboard → Deployments
2. Find last working deployment
3. Click → Promote to Production
4. Confirm
5. Wait 1-2 minutes
6. Verify working

Duration: 2-3 minutes
```

**Git-based deploy:**
```
git revert HEAD
git push origin main
# Triggers redeploy

Or:
git reset --hard [last-working-commit]
git push --force origin main
# Dangerous, know what you're doing

Duration: 5-10 minutes
```

**After rollback:**
```
1. Verify site working
2. Investigate what broke
3. Fix in development
4. Test thoroughly
5. Redeploy

Don't rush redeploy - fix properly
```

---

## Communication Templates

### Internal (Team Slack)

**Incident started:**
```
🚨 INCIDENT: [Brief description]
Severity: [Critical/High/Medium]
Impact: [Who/what affected]
Status: Investigating
Owner: [Your name]

Updates: [This thread]
```

**Incident update:**
```
UPDATE: [What we learned]
Status: [Investigating/Fixing/Monitoring]
ETA: [When expect resolution]
```

**Incident resolved:**
```
✅ RESOLVED: [Brief description]
Duration: [Start to end time]
Root cause: [What happened]
Fix: [What we did]
Prevention: [What we'll do differently]
```

### External (Users)

**Status page update:**
```
We're investigating reports of [issue].
- Started: [time]
- Impact: [which features]
- Status: Working on fix

Updates: [link to status page]
```

**Resolution message:**
```
Issue resolved. [Brief description] is now working normally.

What happened: [Simple explanation]
When: [Duration]
Affected: [Scope]

We apologize for the disruption.
```

### Email to Affected Users

```
Subject: Service disruption resolved

Hi [Name],

You may have experienced [issue] between [start] and [end] today.

The issue has been resolved and everything is working normally now.

What happened: [Simple explanation]
What we did: [How we fixed it]
Preventing future issues: [What we're changing]

We apologize for any inconvenience.

[Your Name]
```

---

## Post-Incident Review

**After every major incident:**

```
Incident Post-Mortem

Date: [When]
Duration: [How long]
Severity: [Critical/High]

What happened:
- [Timeline of events]
- [Root cause identified]
- [Why it happened]

Impact:
- Users affected: [Number/percentage]
- Features impacted: [Which]
- Duration: [How long]

Response:
- Detection: [How we found out]
- Time to fix: [How long]
- What went well: [Good things]
- What went poorly: [Bad things]

Prevention:
- [ ] [Action item 1]
- [ ] [Action item 2]
- [ ] [Action item 3]

Monitoring improvements:
- [ ] Add alert for [X]
- [ ] Monitor [Y] metric
- [ ] Test [Z] regularly
```

---

## On-Call Checklist

**If you're "on-call" (monitoring production):**

```
Before your shift:
- [ ] Phone charged and notifications on
- [ ] Access to all dashboards
- [ ] Access to deployment tools
- [ ] Know how to rollback
- [ ] Know escalation contacts

During shift:
- [ ] Check dashboard morning and evening
- [ ] Phone with you always
- [ ] Respond to critical alerts within 15 min
- [ ] Log all incidents

After incident:
- [ ] Write post-mortem
- [ ] Identify prevention measures
- [ ] Update documentation
- [ ] Brief next on-call person
```

---

## False Alarm Response

**When alert fires but nothing wrong:**

```
1. Acknowledge alert
2. Verify false alarm (check manually)
3. Document why false alarm
4. Adjust monitoring:
   - Threshold too sensitive?
   - Monitoring wrong metric?
   - Expected behavior not excluded?

Goal: Reduce false alarms to <5% of alerts
```

---

## Escalation Procedures

### When to Escalate

**Escalate if:**
- Can't fix within response time
- Don't understand root cause
- Need specialized expertise
- Security incident suspected
- Data corruption possible

### Who to Escalate To

```
Level 1: You (founder)
- Initial response
- Simple fixes
- Rollbacks

Level 2: Technical co-founder / CTO
- Complex issues
- Architecture changes
- Security issues

Level 3: External expert
- Critical issues can't solve
- Security breaches
- Data recovery

Have contact info ready before needed
```

---

## Weekend/Night Incidents

**For non-critical issues:**
```
Can it wait until Monday?
- YES: Note it, fix during business hours
- NO: Fix now

Remember: Most things can wait.
Don't burn out on minor issues.
```

**Critical incidents (site down, payments failing):**
```
Fix immediately, any time.
These are business-critical.
```

**Set expectations with users:**
```
Support hours: 9am-5pm PST
Emergency response: 24/7 for critical issues
Response time: <1 hour during business hours

Be clear what's "emergency"
```

---

## Recovery Verification

**After fixing incident:**

```
Verification Checklist:
- [ ] Original issue resolved
- [ ] Error rate back to normal
- [ ] Performance back to baseline
- [ ] No new errors introduced
- [ ] Monitoring shows green
- [ ] Test main user flows
- [ ] Monitor for 30-60 minutes

Don't close incident until verified stable.
```

---

## Learning from Incidents

**Track patterns:**
```
Common incidents:
- Same error keeps appearing → Fix root cause
- Same service keeps failing → Improve reliability
- Same user action breaks app → Better validation

After 3 similar incidents:
Stop treating as one-off.
Invest in permanent fix.
```

---

## Quick Reference

**Critical Incident (5-minute response):**
```
1. Check monitoring (confirmed?)
2. Assess impact (how many users?)
3. Quick fix or rollback
4. Deploy
5. Monitor for 30 min
6. Post-mortem later
```

**High Incident (1-hour response):**
```
1. Acknowledge
2. Investigate root cause
3. Plan fix
4. Deploy fix
5. Monitor
6. Update users if needed
```

**Medium Incident (24-hour response):**
```
1. Note in tracker
2. Investigate when possible
3. Fix in next deploy
4. Monitor after deploy
```