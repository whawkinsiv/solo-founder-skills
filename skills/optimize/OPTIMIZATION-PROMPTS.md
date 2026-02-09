# Optimization Prompts for AI

Specific prompts for common performance issues.

---

## Database Optimization

### Add Indexes

```
Analyze this query and add appropriate indexes:
[paste slow query]

Add indexes to:
- WHERE clause columns
- JOIN columns (foreign keys)
- ORDER BY columns

Show CREATE INDEX statements.
Estimate performance improvement.
```

### Fix N+1 Queries

```
This code has N+1 query problem:
[paste code that loads list]

Fix using:
- Eager loading / JOIN
- Include related data in single query
- Reduce total queries to 1-2 maximum

Show before/after query count.
```

### Optimize Query

```
This query is slow (2 seconds):
[paste query or endpoint]

Optimize by:
- Using SELECT only needed columns (not *)
- Adding WHERE clause to filter early
- Using appropriate JOIN type
- Adding indexes if missing
- Paginating if returning many rows
```

---

## Caching

### Add Redis Cache

```
Add Redis caching to this endpoint:
GET /api/dashboard

Cache for 5 minutes.
Cache key: "dashboard:userId:{id}"
Invalidate on: user data update, settings change
Return fresh data if cache miss.
```

### Cache Strategy

```
Design caching strategy for:
- User profile (changes rarely)
- Dashboard metrics (updates often)
- Search results (varies by query)

Specify:
- Cache duration for each
- Invalidation triggers
- Cache key patterns
```

### In-Memory Cache

```
Add in-memory caching (no Redis needed):
- Cache user settings (15 minutes)
- Cache static configuration (1 hour)
- Use LRU eviction (max 1000 items)
- Clear on deployment
```

---

## Image Optimization

### Convert to WebP

```
Convert all images to WebP:
- Quality: 80%
- Create fallback JPEGs for compatibility
- Use <picture> element with sources
- Serve appropriate format based on browser
```

### Lazy Loading

```
Add lazy loading to images:
- Load images below fold only when scrolled into view
- Show placeholder while loading
- Use Intersection Observer API
- Prioritize above-fold images (eager load)
```

### Image Compression

```
Set up automatic image compression:
- On upload, compress to 80% quality
- Resize to max width 1920px
- Strip EXIF data
- Generate thumbnails (200px, 400px, 800px)
- Store optimized versions
```

---

## Code Splitting

### Route-Based Splitting

```
Implement code splitting by route:
- Lazy load all routes except home
- Use React.lazy() and Suspense
- Show loading spinner during load
- Preload next likely route on hover

Routes to split:
- /dashboard
- /settings
- /admin
```

### Component-Based Splitting

```
Code split these heavy components:
- Chart library (only load on dashboard)
- Rich text editor (only load when editing)
- PDF viewer (only when viewing PDFs)

Use dynamic imports.
```

---

## API Optimization

### Batch API Calls

```
Combine these API calls into single request:
- GET /api/user
- GET /api/user/settings
- GET /api/user/notifications

New endpoint:
GET /api/user/complete
Returns: { user, settings, notifications }
```

### Pagination

```
Add pagination to this endpoint:
GET /api/items (currently returns 1000+ items)

Implement:
- Page size: 50 items
- Cursor-based pagination (not offset)
- Return total count
- Include next/prev cursor
```

### Response Compression

```
Enable gzip compression for API responses:
- Compress responses > 1KB
- Use compression middleware
- Set appropriate headers
- Test compression ratio
```

---

## Database Connection

### Connection Pooling

```
Configure database connection pooling:
- Pool size: 10 connections
- Max idle: 5 connections
- Idle timeout: 30 seconds
- Connection timeout: 5 seconds
- Reuse connections efficiently
```

### Query Timeout

```
Add query timeout to prevent hanging:
- Query timeout: 5 seconds
- Connection timeout: 10 seconds
- Log slow queries (> 1 second)
- Gracefully handle timeouts
```

---

## Frontend Optimization

### Reduce Render Time

```
Optimize this component that re-renders unnecessarily:
[paste component]

Improvements:
- Add React.memo() where appropriate
- Use useMemo for expensive calculations
- Use useCallback for function props
- Move static data outside component
```

### Bundle Size Reduction

```
Analyze bundle and reduce size:
- Remove unused dependencies
- Use tree shaking
- Replace large libraries (moment → date-fns)
- Import only needed functions

Target: < 200KB total bundle
```

### Prefetching

```
Add prefetching for likely next page:
- On hover over link, prefetch route
- On dashboard load, prefetch settings
- On login, prefetch dashboard data
- Use <link rel="prefetch">
```

---

## Asset Optimization

### Font Loading

```
Optimize font loading:
- Use font-display: swap
- Preload critical fonts
- Subset fonts (Latin only if possible)
- Limit font weights (regular + bold only)
```

### CSS Optimization

```
Optimize CSS delivery:
- Inline critical CSS
- Defer non-critical CSS
- Remove unused CSS (PurgeCSS)
- Minify CSS
```

### JavaScript Loading

```
Optimize JavaScript loading:
- Defer non-critical scripts
- Async load third-party scripts
- Move scripts to end of body
- Use type="module" with defer
```

---

## Monitoring & Logging

### Performance Monitoring

```
Add performance monitoring:
- Log API response times (server-side)
- Track page load times (client-side)
- Log slow database queries (> 100ms)
- Send metrics to logging service

Alert if:
- API > 1 second
- Query > 500ms
- Page load > 5 seconds
```

### APM Integration

```
Integrate application performance monitoring:
- Track request duration
- Track database query times
- Track external API calls
- Track error rates
- Dashboard for visualization
```

---

## Load Balancing

### Horizontal Scaling

```
Prepare app for horizontal scaling:
- Make stateless (no in-memory sessions)
- Use Redis for sessions
- Use external queue (Bull, BullMQ)
- Database connection pooling
- Health check endpoint
```

### CDN Configuration

```
Configure CDN for static assets:
- Serve images from CDN
- Serve JS/CSS from CDN
- Set long cache headers (1 year)
- Invalidate cache on deployment
- Use CDN edge functions if available
```

---

## Specific Scenarios

### Slow Dashboard Load

```
Dashboard takes 8 seconds to load.

Debug:
1. Check Network tab for slow requests
2. Check which API calls are slowest
3. Check bundle size

Then optimize:
- Cache dashboard API response (1 minute)
- Lazy load charts
- Show skeleton while loading
- Paginate tables if showing many rows
```

### Slow Search

```
Search takes 3+ seconds.

Optimize:
- Add database index on search column
- Implement search debouncing (300ms delay)
- Show "Searching..." message
- Limit results to 50
- Consider full-text search (Elasticsearch)
```

### Slow Form Submit

```
Form submission takes 5+ seconds.

Optimize:
- Show optimistic update (assume success)
- Process in background if possible
- Show progress bar
- Validate client-side first
- Return response quickly, process async
```

---

## Testing Optimization

### Before/After Comparison

```
Measure performance before optimization:
[specific metric]

Apply optimization:
[specific change]

Measure after:
[metric again]

Document improvement:
Before: X seconds
After: Y seconds
Improvement: Z%
```

---

## Progressive Optimization

### Phase 1 (Quick Wins)
```
Low-hanging fruit optimizations:
1. Add caching (5 minute TTL)
2. Optimize images (WebP, compress)
3. Add database indexes (foreign keys)
4. Enable gzip compression
5. Implement pagination

Complete in order. Measure after each.
```

### Phase 2 (Deeper Optimization)
```
After Phase 1, if still slow:
1. Code splitting by route
2. Advanced caching strategy
3. Database query optimization
4. CDN for static assets
5. Bundle size reduction

Only if metrics show need.
```

### Phase 3 (Advanced)
```
Only if > 10,000 users and still issues:
1. Load balancing
2. Database read replicas
3. Microservices architecture
4. Advanced CDN strategies
5. Hire performance expert

Most MVPs never need this.
```