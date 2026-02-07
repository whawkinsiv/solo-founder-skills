# Performance Testing & Measurement

How to measure and test performance without technical expertise.

---

## Browser Testing (Chrome DevTools)

### Page Load Speed

**Open DevTools:**
1. Right-click page → Inspect
2. Click "Network" tab
3. Reload page (Cmd+R)

**Check metrics:**
- **DOMContentLoaded:** Should be < 2 seconds
- **Load:** Should be < 3 seconds
- **Finish:** All resources loaded

**Red flags:**
- Any single file > 1MB
- More than 50 requests on initial load
- Requests taking > 2 seconds

### API Response Time

**Monitor API calls:**
1. Open DevTools → Network tab
2. Filter: XHR
3. Perform action (click button, load page)
4. Check time column

**Targets:**
- < 200ms: Excellent
- 200-500ms: Good
- 500ms-1s: Needs optimization
- > 1s: Problem

### Lighthouse Score

**Run Lighthouse:**
1. Open DevTools
2. Click "Lighthouse" tab
3. Select "Performance"
4. Click "Generate report"

**Targets:**
- 90-100: Excellent
- 70-89: Good
- 50-69: Needs improvement
- < 50: Poor

**Focus on:**
- First Contentful Paint (< 1.8s)
- Time to Interactive (< 3.8s)
- Speed Index (< 3.4s)

---

## Database Query Performance

### Check Query Times

**Tell AI to add logging:**
```
Log all database queries with execution time.
Log queries taking > 100ms as warnings.
Format: [QUERY] [TIME] [SQL]
```

**Review logs:**
```bash
# Find slow queries
grep "QUERY" logs.txt | grep -v "SELECT" | sort -k2 -nr | head -20
```

**Red flags:**
- Any query > 1 second
- Same query repeated many times (N+1 problem)
- Full table scans (missing indexes)

### N+1 Query Detection

**Symptom:** 
- Loading 10 users makes 11 queries (1 for users, 1 per user for related data)

**Check:**
```
Enable query logging
Load a list page
Count queries in logs
Should be 1-3 queries total, not 1 per item
```

**Fix with AI:**
```
Prevent N+1 queries:
Use JOIN or eager loading
Include related data in single query
Example: User.findAll({ include: [Posts, Comments] })
```

---

## Image Optimization

### Check Image Sizes

```bash
# Check image sizes
ls -lh public/images/

# Find large images
find public/images -size +500k
```

**Targets:**
- Thumbnails: < 50KB
- Regular images: < 200KB
- Hero images: < 500KB

### Check Image Format

**Modern formats:**
- WebP: Best compression, modern browsers
- AVIF: Better than WebP, limited support
- JPEG: Universal, good for photos
- PNG: Universal, good for graphics

**Tell AI:**
```
Convert images to WebP:
- Quality: 80%
- Fallback to JPEG for old browsers
- Serve via <picture> element
```

---

## Bundle Size Analysis

### JavaScript Bundle

**Check size:**
```bash
npm run build
# Look for "bundle size" in output
```

**Targets:**
- < 100KB: Excellent
- 100-200KB: Good
- 200-500KB: Large, consider optimization
- > 500KB: Too large, needs code splitting

**Analyze bundle:**
```bash
npm install --save-dev webpack-bundle-analyzer
npm run build -- --analyze
# Opens visualization of bundle
```

### Code Splitting Check

**Should lazy load:**
- Admin pages (if regular users don't access)
- Settings/profile pages
- Large libraries (charts, editors)
- Routes not on landing page

**Tell AI:**
```
Implement code splitting:
- Lazy load routes with React.lazy()
- Dynamic import for large libraries
- Split by route, not by component
```

---

## Caching Verification

### Check Cache Headers

```bash
curl -I https://yourapp.com/api/endpoint
```

**Look for:**
```
Cache-Control: max-age=300
```

**Targets:**
- Static assets: max-age=31536000 (1 year)
- API data: max-age=60-300 (1-5 minutes)
- User-specific: private, max-age=60

### Redis Cache Hit Rate

**Tell AI to log cache hits:**
```
Log cache hits and misses:
- "CACHE_HIT: /api/dashboard"
- "CACHE_MISS: /api/dashboard"

Calculate hit rate hourly.
Target: > 80% hit rate
```

---

## Load Testing

### Simple Load Test

**Test API endpoint:**
```bash
# 100 concurrent requests
for i in {1..100}; do
  curl https://yourapp.com/api/endpoint &
done
wait

# Should complete in < 10 seconds total
```

### Artillery (For serious testing)

```bash
npm install -g artillery

# Create test.yml:
# config:
#   target: 'https://yourapp.com'
# scenarios:
#   - duration: 60
#     arrivalRate: 5
#     flow:
#       - get:
#           url: "/api/dashboard"

artillery run test.yml
```

**Interpret results:**
- Median response: < 500ms
- 95th percentile: < 1s
- No errors

---

## Real User Monitoring

### Basic Analytics

**Track in application:**
- Page load time
- API response time
- Error rates

**Tell AI:**
```
Add performance tracking:
- Measure and log page load time
- Measure API response times
- Send to analytics (aggregate, don't spam)
```

### Free Tools

**Vercel Analytics:**
- Automatic for Vercel deployments
- Real user metrics
- Core Web Vitals

**Cloudflare Analytics:**
- Free tier includes performance metrics
- Global latency tracking

**Google PageSpeed Insights:**
- Free
- Tests from different locations
- Mobile and desktop scores

---

## Performance Budget

### Set Targets

```
Performance Budget:
- Page load: 3 seconds
- API response: 500ms
- Bundle size: 200KB
- Image size: 500KB max each
- Database query: 100ms
```

### Enforce in CI/CD

**Tell AI:**
```
Add performance checks to CI:
- Fail build if bundle > 200KB
- Fail if Lighthouse score < 70
- Fail if any image > 500KB
```

---

## Database Index Analysis

### Check Existing Indexes

**Tell AI:**
```
List all database indexes.
Show table, column, and index type.
```

### Identify Missing Indexes

**Check slow query log for patterns:**
- WHERE clauses on non-indexed columns
- ORDER BY on non-indexed columns
- JOIN on non-indexed foreign keys

**Tell AI:**
```
Analyze slow queries and suggest indexes.
Show CREATE INDEX statements.
Explain impact (estimated speedup).
```

---

## Mobile Performance

### Test on Real Devices

**Minimum tests:**
- iPhone (Safari)
- Android phone (Chrome)
- Slow 3G network (Chrome DevTools can throttle)

### Mobile-Specific Issues

**Check for:**
- Images not responsive (serving desktop size to mobile)
- Too many fonts loaded
- Blocking JavaScript on initial load
- No lazy loading of images

**Tell AI:**
```
Optimize for mobile:
- Serve responsive images (srcset)
- Reduce font loading (subset or system fonts)
- Defer non-critical JavaScript
- Lazy load all images below fold
```

---

## Quick Daily Checks

**30-second performance check:**

1. Open app in incognito mode
2. Open DevTools → Network
3. Reload page
4. Check "Load" time (< 3s?)
5. Click around, check API times (< 500ms?)

**If times creeping up:** Time to optimize.

---

## When Numbers Don't Matter

**Focus on user experience, not absolute numbers:**

Good metrics but bad UX:
- Fast load but then nothing works
- Quick API but spinner shows for 5 seconds
- Small bundle but everything feels janky

Bad metrics but good UX:
- 4 second load but progressive rendering
- 800ms API but optimistic updates
- Large bundle but instant interactions

**Balance:** Fast technical performance + Good perceived performance.
