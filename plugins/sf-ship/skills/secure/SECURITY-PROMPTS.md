# Security Prompts for AI

How to ask AI tools to implement security features correctly.

---

## Authentication

### Add Basic Auth
```
Implement authentication:
- bcrypt password hashing (12 rounds)
- JWT tokens (expire in 1 hour)
- Refresh tokens (expire in 7 days)
- Email verification required
- Password reset via email

Password requirements:
- 8+ characters
- 1 uppercase, 1 lowercase
- 1 number, 1 symbol
```

### Protect Routes
```
Add authentication middleware to these routes:
- /api/dashboard
- /api/settings
- /api/admin/*

Return 401 if no valid token.
Include WWW-Authenticate header.
```

### Session Management
```
Implement session management:
- Expire after 30 minutes idle
- Extend on activity
- Invalidate on logout
- Invalidate all sessions on password change
- Store in Redis with TTL
```

---

## Data Protection

### Environment Variables
```
Move these to environment variables:
- DATABASE_URL
- JWT_SECRET
- STRIPE_API_KEY
- SENDGRID_API_KEY

Access via process.env.VARIABLE_NAME
Add .env.example with dummy values
Add .env to .gitignore
```

### Hash Passwords
```
Update password handling:
- Hash with bcrypt (12 rounds minimum)
- Never store plain text
- Never log password (even hashed)
- Verify password: bcrypt.compare(input, stored)
```

### Sanitize Input
```
Sanitize user input before storing:
- Strip HTML tags (except allowed: <p>, <b>, <i>)
- Escape special characters
- Limit length: 500 chars for bio, 100 for name
- Reject scripts and dangerous content
```

---

## API Security

### Rate Limiting
```
Add rate limiting to all API routes:
- 100 requests/minute per IP
- 1000 requests/hour per user
- Return 429 with Retry-After header
- Use sliding window (not fixed)
- Whitelist: health check endpoint
```

### Input Validation
```
Validate API inputs:
- Email: valid format, max 255 chars
- Password: meets requirements
- Username: alphanumeric + underscore, 3-20 chars
- URLs: valid format, https only

Return 400 with specific field errors.
```

### Error Handling
```
Production error handling:
- Catch all errors
- Log full details server-side
- Return generic message: "An error occurred"
- Never expose: stack traces, DB errors, file paths
- Include error ID for support requests
```

---

## Database Security

### Prevent SQL Injection
```
Update database queries:
- Use parameterized queries ONLY
- Never concatenate user input into SQL
- Use ORM query builders (Prisma, TypeORM)

Example:
db.query('SELECT * FROM users WHERE id = ?', [userId])
NOT: db.query(`SELECT * FROM users WHERE id = ${userId}`)
```

### Connection Security
```
Secure database connection:
- Use SSL/TLS
- Minimum TLS 1.2
- Store connection string in .env
- Use connection pooling
- Set timeout: 30 seconds
```

---

## File Upload Security

### Validate Uploads
```
Secure file uploads:
- Whitelist types: jpeg, png, pdf only
- Max size: 5MB
- Scan filenames: no path traversal (../)
- Generate random filenames (UUID)
- Store outside web root
- Serve via CDN (not direct)
```

### Image Processing
```
Process uploaded images:
- Strip EXIF data
- Re-encode to remove malicious content
- Resize to max dimensions (2048x2048)
- Convert to safe format (jpeg/png)
```

---

## CORS Configuration

### Production CORS
```
Configure CORS:
- Whitelist exact origins:
  - https://yourapp.com
  - https://www.yourapp.com
- Allow credentials: true
- Allowed methods: GET, POST, PUT, DELETE
- Allowed headers: Content-Type, Authorization
- Max age: 3600

NOT: origin: "*" (never use wildcard in production)
```

---

## Headers & HTTPS

### Security Headers
```
Add security headers (use helmet.js):
- Strict-Transport-Security: max-age=31536000
- X-Frame-Options: DENY
- X-Content-Type-Options: nosniff
- X-XSS-Protection: 1; mode=block
- Content-Security-Policy: [your policy]
- Referrer-Policy: strict-origin-when-cross-origin
```

### Force HTTPS
```
Enforce HTTPS in production:
- Redirect HTTP to HTTPS
- Set Secure flag on cookies
- Use HSTS header
- No mixed content (all resources via HTTPS)
```

---

## Logging & Monitoring

### Security Event Logging
```
Log security events:
- Failed login attempts (IP, timestamp, username)
- Successful logins (IP, timestamp)
- Password changes
- Permission denied (403)
- Rate limit hits (429)
- Invalid tokens

Format: JSON with timestamp, event_type, user_id, IP, details
```

### Sensitive Data Redaction
```
Redact sensitive data in logs:
- Replace passwords with "[REDACTED]"
- Truncate tokens: show first/last 4 chars only
- Hash emails for privacy
- Never log: credit cards, SSN, health data
```

---

## Admin & Privileged Access

### Admin Routes
```
Protect admin routes:
- Require admin role check (not just auth)
- Separate middleware: requireAdmin()
- Log all admin actions
- Add 2FA for admin accounts
- IP whitelist for admin access (optional)
```

### Role-Based Access
```
Implement RBAC:
- Roles: admin, user, viewer
- Check role on every protected route
- Store roles in JWT or session
- Default: lowest privilege (viewer)
- Require admin approval for role upgrades
```

---

## Third-Party Integrations

### API Key Security
```
Secure third-party API keys:
- Store in environment variables
- Rotate keys every 90 days
- Use separate keys for dev/staging/prod
- Revoke immediately if exposed
- Monitor usage for anomalies
```

### Webhook Security
```
Verify webhooks (e.g., Stripe):
- Verify signature (HMAC-SHA256)
- Check timestamp (prevent replay)
- Use HTTPS endpoints only
- Rate limit webhook endpoints
- Log all webhook events
```

---

## Quick Security Checklist

```
Pre-deployment security:
- [ ] All secrets in environment variables
- [ ] Passwords hashed with bcrypt
- [ ] HTTPS forced in production
- [ ] Rate limiting on all APIs
- [ ] Input validation server-side
- [ ] SQL injection prevented (parameterized queries)
- [ ] XSS prevented (sanitized output)
- [ ] CORS configured (not wildcard)
- [ ] Error messages generic (no stack traces)
- [ ] Sessions expire (30-60 min)
- [ ] File uploads validated
- [ ] Security headers set (helmet.js)
```

---

## Testing Security Implementation

**Verify authentication:**
```bash
# Should fail
curl http://localhost:3000/api/protected

# Should succeed with token
curl -H "Authorization: Bearer $TOKEN" http://localhost:3000/api/protected
```

**Test rate limiting:**
```bash
# Should return 429 after 100 requests
for i in {1..150}; do curl http://localhost:3000/api/endpoint; done
```

**Check for secrets:**
```bash
# Should find nothing
grep -r "api_key\|password\|secret" src/
```