# Common Vulnerabilities

Quick reference for checking security issues in AI-built apps.

---

## OWASP Top 10 (Simplified)

### 1. Broken Access Control

**What:** Users can access things they shouldn't

**Check:**
- Can logged-out users access protected pages?
- Can User A see User B's data?
- Can regular users access admin functions?

**Fix with AI:**
```
Add authorization check:
Verify user owns this resource before allowing access.
Return 403 if user doesn't have permission.
```

---

### 2. Cryptographic Failures

**What:** Weak encryption or exposed sensitive data

**Check:**
- Are passwords hashed (not encrypted)?
- Is HTTPS forced in production?
- Are API keys in .env (not code)?

**Fix with AI:**
```
Hash passwords with bcrypt (12 rounds).
Never store plain text passwords.
Force HTTPS in production.
```

---

### 3. Injection (SQL, NoSQL, Command)

**What:** User input executed as code

**Check:**
- Are you using raw SQL with user input?
- Are you using string concatenation for queries?

**Fix with AI:**
```
Use parameterized queries only.
Never concatenate user input into SQL.
Example: db.query('SELECT * FROM users WHERE id = ?', [userId])
```

---

### 4. Insecure Design

**What:** Missing security features from design

**Check:**
- Is there rate limiting on APIs?
- Do sessions expire?
- Is there brute force protection on login?

**Fix with AI:**
```
Add rate limiting: 100 req/min per IP.
Add login attempt limit: 5 tries, then 15min lockout.
Sessions expire after 30min idle.
```

---

### 5. Security Misconfiguration

**What:** Insecure defaults, unnecessary features enabled

**Check:**
- Are error messages showing stack traces?
- Is CORS set to wildcard "*"?
- Are default passwords still in use?

**Fix with AI:**
```
Production error handling:
- Log full errors server-side
- Show generic message to users ("Something went wrong")
- Never expose stack traces

Configure CORS to whitelist only:
- https://yourapp.com
- https://www.yourapp.com
```

---

### 6. Vulnerable Components

**What:** Using outdated libraries with known vulnerabilities

**Check:**
```bash
npm audit
# or
yarn audit
```

**Fix with AI:**
```
Update all dependencies to latest stable versions.
Fix vulnerabilities shown in npm audit.
```

---

### 7. Authentication Failures

**What:** Weak or broken authentication

**Check:**
- Can users use weak passwords?
- Is there multi-login prevention?
- Do sessions timeout?

**Fix with AI:**
```
Enforce password requirements:
- 8+ characters
- 1 uppercase, 1 lowercase
- 1 number, 1 symbol

Add session management:
- Expire after 30min idle
- Invalidate on password change
- Require re-auth for sensitive actions
```

---

### 8. Software/Data Integrity Failures

**What:** Code/data modified without verification

**Check:**
- Are dependencies verified (package-lock.json)?
- Is there backup/restore for data?

**Fix with AI:**
```
Commit package-lock.json to git.
Configure automated daily database backups.
Test restore process.
```

---

### 9. Logging Failures

**What:** Not logging security events or logging sensitive data

**Check:**
- Are failed logins logged?
- Are API errors logged?
- Are passwords being logged?

**Fix with AI:**
```
Log security events:
- Failed login attempts (with IP, timestamp)
- API authentication failures
- Permission denied events

Never log:
- Passwords (even hashed)
- API keys
- Session tokens
- Credit card numbers
```

---

### 10. Server-Side Request Forgery (SSRF)

**What:** Server makes requests to unintended locations

**Check:**
- Does your app fetch user-provided URLs?
- Can users trigger requests to internal IPs?

**Fix with AI:**
```
Validate URLs before fetching:
- Whitelist allowed domains only
- Block private IP ranges (192.168.*, 10.*, 127.*)
- Timeout requests (5 seconds max)
```

---

## Quick Vulnerability Scan

**Run these checks:**

**1. Secrets exposed:**
```bash
grep -r "api_key\|API_KEY" src/
grep -r "password\|PASSWORD" src/
# Should only find env var references
```

**2. Authentication:**
```bash
curl http://localhost:3000/api/admin
# Should return 401, not data
```

**3. Rate limiting:**
```bash
for i in {1..150}; do curl http://localhost:3000/api/endpoint; done
# Should start returning 429
```

**4. HTTPS:**
```bash
curl http://yourapp.com
# Should redirect to https://
```

---

## Platform-Specific Issues

### Vercel/Netlify
- Environment variables set in dashboard
- HTTPS automatic
- Watch for exposed API routes

### Replit
- Secrets in "Secrets" panel, not .env
- Public by default (careful with data)
- Use authentication on all routes

### Lovable
- Check what environment variables it needs
- Verify authentication on generated routes
- Test rate limiting manually

---

## When to Worry

**Low risk (handle with checklist):**
- Basic CRUD app
- < 100 users
- No payment processing
- No sensitive PII

**Medium risk (get review):**
- Using Stripe/payment processing
- 100-1000 users
- Basic PII (names, emails)
- User-generated content

**High risk (hire expert):**
- Direct payment handling
- Health/financial data
- > 1000 users
- Multi-tenant with isolation
- Regulatory requirements (HIPAA, SOC2)

---

## Emergency Response

**If you discover a vulnerability:**

1. **Assess severity:** Can it be exploited now?
2. **Hotfix immediately:** Disable feature or add auth
3. **Fix properly:** Work with AI to implement correct solution
4. **Notify users:** If data exposed, be transparent
5. **Document:** What happened, how fixed, prevention

**Quick hotfix pattern:**
```
Temporarily disable this endpoint.
Return 503 "Under maintenance" for now.
We'll fix properly and re-enable.
```