# Database Optimization

Detailed patterns for cleaning up database schema and orphaned data.

---

## Why Database Waste Accumulates

When building with AI tools:
- Feature iterations leave abandoned tables
- Schema changes leave legacy columns
- Soft deletes accumulate without cleanup
- User deletions orphan related records

**Result:** Database grows, queries slow down.

---

## Types of Database Waste

### 1. Abandoned Tables

Tables created for features that were removed or never finished.

**How to find:**
```
List all tables.
For each table, search codebase for references.
Flag tables with zero code references.
```

**Common abandoned tables:**
- `feature_flags` - Feature removed but table remains
- `old_users` - Migration left behind
- `temp_*` - Temporary tables never deleted
- `backup_*` - Manual backups forgotten

### 2. Legacy Columns

Columns that are no longer used but weren't removed.

**How to find:**
```
For each table, list columns.
Search codebase for each column name.
Flag columns with zero code references.
Also check: columns that are always NULL.
```

**Common legacy columns:**
- `old_email` - Renamed but kept "just in case"
- `deprecated_*` - Marked but never removed
- `temp_*` - Temporary columns forgotten
- `v1_*` - Old version fields

### 3. Orphaned Records

Records pointing to deleted parent records.

**How to find:**
```sql
-- Find comments for deleted users
SELECT c.* FROM comments c
LEFT JOIN users u ON c.user_id = u.id
WHERE u.id IS NULL;

-- Find orders for deleted products
SELECT o.* FROM order_items o
LEFT JOIN products p ON o.product_id = p.id
WHERE p.id IS NULL;
```

**Common orphaned records:**
- User content after user deletion
- Order items after product deletion
- Comments after post deletion
- Settings after account deletion

### 4. Soft-Deleted Records

Records marked deleted but never purged.

**How to find:**
```sql
-- Find old soft-deleted records
SELECT table_name, COUNT(*)
FROM information_schema.tables
WHERE deleted_at IS NOT NULL
AND deleted_at < NOW() - INTERVAL '90 days';
```

**Cleanup threshold:** 90 days is typical. After that, purge.

### 5. Duplicate Data

Same information stored in multiple places.

**How to find:**
```
Compare columns across tables.
Look for: user_email in orders AND in users
Look for: product_name in order_items AND in products
Flag denormalized data that could be joined instead.
```

**When duplication is OK:**
- Performance optimization (intentional denormalization)
- Audit trails (historical snapshots)
- External system sync (different source of truth)

---

## Audit Workflow

### Step 1: Schema Inventory

**Tell AI:**
```
Create database schema inventory:
- List all tables with row counts
- List all columns with data types
- List all foreign key relationships
- List all indexes
- Flag tables > 1M rows
- Flag tables with no indexes
```

### Step 2: Usage Analysis

**Tell AI:**
```
Cross-reference schema with codebase:
- For each table, find code references
- For each column, find code references
- Flag tables/columns with zero references
- Note: check ORM models, raw queries, and migrations
```

### Step 3: Data Quality Check

**Tell AI:**
```
Analyze data quality:
- Find columns that are always NULL
- Find columns with same value in all rows
- Find orphaned records (broken foreign keys)
- Find soft-deleted records older than 90 days
- Report row counts for each issue
```

---

## Safe Cleanup Process

### For Columns

```sql
-- Step 1: Verify column is unused
SELECT COUNT(*) FROM table_name WHERE column_name IS NOT NULL;

-- Step 2: If zero or acceptable, create migration
ALTER TABLE table_name DROP COLUMN column_name;

-- Step 3: Run on staging first
-- Step 4: Backup before production
-- Step 5: Run on production during low-traffic
```

### For Tables

```sql
-- Step 1: Verify table is unused
SELECT COUNT(*) FROM table_name;
-- Also: grep codebase for table name

-- Step 2: Rename first (safer than delete)
ALTER TABLE table_name RENAME TO _deprecated_table_name;

-- Step 3: Wait 1-2 weeks for issues
-- Step 4: If no issues, drop table
DROP TABLE _deprecated_table_name;
```

### For Orphaned Records

```sql
-- Step 1: Identify orphans
SELECT c.id FROM comments c
LEFT JOIN users u ON c.user_id = u.id
WHERE u.id IS NULL;

-- Step 2: Backup orphans
CREATE TABLE _backup_orphaned_comments AS
SELECT * FROM comments WHERE user_id NOT IN (SELECT id FROM users);

-- Step 3: Delete orphans
DELETE FROM comments WHERE user_id NOT IN (SELECT id FROM users);

-- Step 4: Keep backup for 30 days, then drop
```

### For Soft-Deleted Records

```sql
-- Step 1: Identify old soft-deletes
SELECT COUNT(*) FROM users
WHERE deleted_at < NOW() - INTERVAL '90 days';

-- Step 2: Backup before purge
CREATE TABLE _backup_deleted_users_jan2025 AS
SELECT * FROM users WHERE deleted_at < NOW() - INTERVAL '90 days';

-- Step 3: Purge
DELETE FROM users WHERE deleted_at < NOW() - INTERVAL '90 days';

-- Step 4: Set up recurring job for future
```

---

## Adding Missing Indexes

### Find Slow Queries

**Tell AI:**
```
Identify queries that would benefit from indexes:
- Queries with WHERE clauses on unindexed columns
- Queries with JOIN on unindexed foreign keys
- Queries with ORDER BY on unindexed columns
- Report: query, table, suggested index
```

### Common Index Patterns

```sql
-- Foreign keys (almost always need index)
CREATE INDEX idx_comments_user_id ON comments(user_id);
CREATE INDEX idx_orders_product_id ON orders(product_id);

-- Frequently filtered columns
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_status ON orders(status);

-- Frequently sorted columns
CREATE INDEX idx_posts_created_at ON posts(created_at);

-- Compound indexes for common queries
CREATE INDEX idx_orders_user_status ON orders(user_id, status);
```

### Index Guidelines

| Query Pattern | Index Type |
|--------------|------------|
| WHERE column = value | Single column index |
| WHERE a = x AND b = y | Compound index (a, b) |
| WHERE a = x ORDER BY b | Compound index (a, b) |
| JOIN on foreign key | Index on foreign key |
| Full text search | Full text index |

---

## Prevention Patterns

### ON DELETE CASCADE

Automatically delete dependent records:

```sql
ALTER TABLE comments
ADD CONSTRAINT fk_comments_user
FOREIGN KEY (user_id) REFERENCES users(id)
ON DELETE CASCADE;
```

**Use for:** Child records that shouldn't exist without parent

### ON DELETE SET NULL

Set foreign key to NULL when parent deleted:

```sql
ALTER TABLE posts
ADD CONSTRAINT fk_posts_author
FOREIGN KEY (author_id) REFERENCES users(id)
ON DELETE SET NULL;
```

**Use for:** Records that can exist without the relationship

### Scheduled Cleanup Jobs

```javascript
// Run daily: purge soft-deleted records > 90 days
async function purgeDeletedRecords() {
  const cutoff = new Date();
  cutoff.setDate(cutoff.getDate() - 90);

  await db.users.deleteMany({
    deleted_at: { $lt: cutoff }
  });
}
```

### NOT NULL Constraints

Prevent columns from accumulating NULL values:

```sql
ALTER TABLE users
ALTER COLUMN email SET NOT NULL;
```

---

## Platform-Specific Notes

### Supabase / PostgreSQL

```sql
-- Check table sizes
SELECT relname, pg_size_pretty(pg_total_relation_size(relid))
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;

-- Check index usage
SELECT indexrelname, idx_scan
FROM pg_stat_user_indexes
ORDER BY idx_scan ASC;
```

### Firebase / Firestore

```javascript
// Orphaned documents are harder to find
// Use Cloud Functions to clean up on delete
exports.onUserDelete = functions.firestore
  .document('users/{userId}')
  .onDelete(async (snap, context) => {
    // Delete user's posts, comments, etc.
  });
```

### MongoDB

```javascript
// Find orphaned documents
db.comments.aggregate([
  { $lookup: { from: "users", localField: "userId", foreignField: "_id", as: "user" } },
  { $match: { user: { $size: 0 } } },
  { $count: "orphaned" }
]);
```

---

## Cleanup Checklist

```
- [ ] Inventory all tables and columns
- [ ] Cross-reference with codebase
- [ ] Identify unused tables/columns
- [ ] Find orphaned records
- [ ] Find soft-deleted records > 90 days
- [ ] Add missing indexes on foreign keys
- [ ] Set up ON DELETE CASCADE where appropriate
- [ ] Create scheduled cleanup job
- [ ] Test all changes on staging first
- [ ] Backup before production changes
```
