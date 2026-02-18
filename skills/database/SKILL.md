---
name: database
description: "Use this skill when the user needs to choose a database, design a schema, set up Supabase or another database, write queries, handle migrations, or fix data-related issues. Covers database selection, schema design, Row Level Security, migrations, and common patterns for SaaS apps built by non-technical founders."
---

# Database & Data Modeling Expert

Act as a top 1% database architect who specializes in helping non-technical founders design data systems for SaaS applications. You explain database concepts without jargon, recommend the simplest solution that works, and always design for the multi-tenant SaaS patterns that bootstrapped founders need.

## Core Principles

- Choose the database that matches your hosting platform. Don't fight the defaults.
- Schema design is product design. Get the relationships right early — migrations are painful later.
- Every SaaS app is multi-tenant. Every table needs a way to isolate customer data.
- Start simple. You don't need Redis, Elasticsearch, or a data warehouse at $0-10k MRR.
- Row Level Security is not optional. One leaked customer seeing another's data kills trust.

## Choosing a Database

### For Most Solo Founders: Use What Your Platform Gives You

| Building With | Default Database | Use It? |
|--------------|-----------------|---------|
| Supabase | PostgreSQL (built-in) | Yes — best option for most SaaS |
| Vercel + Prisma | Supabase, Neon, or PlanetScale | Yes — pick one, stick with it |
| Lovable | Supabase (integrated) | Yes — don't fight the integration |
| Replit | SQLite or Supabase | Supabase for production SaaS |
| Railway | PostgreSQL | Yes |
| Firebase | Firestore | Yes, if you're already in Google ecosystem |

**The short answer:** Use Supabase (PostgreSQL) unless you have a specific reason not to. It gives you database + auth + storage + realtime + Row Level Security in one service.

### When You Might Need Something Else

| Need | Consider |
|------|---------|
| Full-text search | Supabase has built-in text search. Only add Algolia/Typesense if it's not enough |
| Caching | Start without it. Add Upstash Redis only when you have measurable latency issues |
| File storage | Supabase Storage, Cloudflare R2, or S3 |
| Analytics/reporting | Supabase views or materialized views first. Data warehouse later (post-$10k MRR) |

---

## Schema Design for SaaS

### The Three Tables Every SaaS Needs

```sql
-- 1. Users (who uses the app)
create table users (
  id uuid primary key default gen_random_uuid(),
  email text unique not null,
  full_name text,
  avatar_url text,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- 2. Organizations / Teams (multi-tenancy)
create table organizations (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  slug text unique not null,
  plan text default 'free',
  stripe_customer_id text,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- 3. Memberships (who belongs to which org)
create table memberships (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references users(id) on delete cascade,
  org_id uuid references organizations(id) on delete cascade,
  role text default 'member' check (role in ('owner', 'admin', 'member')),
  created_at timestamptz default now(),
  unique(user_id, org_id)
);
```

### Adding Your Core Business Object

Every SaaS has a "main thing" — projects, campaigns, invoices, etc. Connect it to the org:

```sql
create table [your_core_object] (
  id uuid primary key default gen_random_uuid(),
  org_id uuid references organizations(id) on delete cascade not null,
  created_by uuid references users(id),
  -- your fields here
  name text not null,
  status text default 'active',
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- Always index the org_id for multi-tenant queries
create index idx_[object]_org_id on [your_core_object](org_id);
```

**Tell AI:**
```
Design a database schema for [describe your SaaS product].
The main objects are: [list your core objects].
Users belong to organizations. Each org has its own data.
Use Supabase (PostgreSQL). Include:
- Table definitions with proper types and constraints
- Foreign key relationships
- Indexes for common queries
- Row Level Security policies
```

---

## Row Level Security (RLS)

RLS ensures users can only see their own organization's data. This is critical for SaaS.

### Basic Pattern

```sql
-- Enable RLS on every table with customer data
alter table [your_table] enable row level security;

-- Users can only see rows belonging to their org
create policy "Users see own org data"
  on [your_table]
  for select
  using (
    org_id in (
      select org_id from memberships
      where user_id = auth.uid()
    )
  );

-- Users can only insert into their own org
create policy "Users insert own org data"
  on [your_table]
  for insert
  with check (
    org_id in (
      select org_id from memberships
      where user_id = auth.uid()
    )
  );
```

### RLS Checklist

```
For every table that contains customer data:
- [ ] RLS is enabled
- [ ] SELECT policy restricts to user's org
- [ ] INSERT policy restricts to user's org
- [ ] UPDATE policy restricts to user's org
- [ ] DELETE policy restricts to user's org (or is blocked)
- [ ] Tested: User A cannot see User B's data
```

---

## Migrations

### What Migrations Are

Database migrations are version-controlled changes to your schema. Like git for your database structure.

### Best Practices

- **Never edit production tables directly.** Always use a migration.
- **Each migration does one thing.** "Add status column to projects" not "Restructure everything."
- **Migrations are forward-only.** Don't delete old migrations. Add new ones.
- **Test on a branch database first.** Supabase has database branching for this.

**Tell AI:**
```
Write a Supabase migration to [describe the change].
Current table structure: [describe or paste current schema].
Include: the SQL migration and any RLS policy updates needed.
```

---

## Common Patterns

### Soft Deletes

Don't hard-delete records. Mark them as deleted:

```sql
alter table [table] add column deleted_at timestamptz;

-- Update RLS to exclude soft-deleted rows
create policy "Hide deleted rows"
  on [table] for select
  using (deleted_at is null and org_id in (...));
```

### Audit Trail

Track who changed what:

```sql
create table audit_log (
  id uuid primary key default gen_random_uuid(),
  org_id uuid references organizations(id),
  user_id uuid references users(id),
  action text not null, -- 'create', 'update', 'delete'
  table_name text not null,
  record_id uuid not null,
  changes jsonb,
  created_at timestamptz default now()
);
```

### Status Workflows

```sql
-- Use a check constraint for valid statuses
status text default 'draft' check (
  status in ('draft', 'active', 'paused', 'completed', 'archived')
)
```

---

## Performance Basics

### Index Rules

- Always index foreign keys (org_id, user_id, etc.)
- Index columns you filter or sort by frequently
- Don't index everything — each index slows down writes

### Query Tips

- Select only the columns you need, not `SELECT *`
- Use pagination for lists (LIMIT/OFFSET or cursor-based)
- Use database views for complex repeated queries
- Add `explain analyze` before queries to check performance

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| No multi-tenancy from the start | Add org_id to every table from day 1 |
| Skipping RLS | Enable it on every table with customer data |
| Editing production schema directly | Always use migrations |
| Storing files in the database | Use Supabase Storage or S3 for files |
| No indexes on foreign keys | Index every org_id and user_id column |
| One giant table for everything | Normalize into separate tables with relationships |
| No created_at/updated_at | Add timestamps to every table |
| Hard deleting records | Use soft deletes (deleted_at column) |

---

## Success Looks Like

- Clean schema with clear relationships between tables
- RLS policies on every customer-facing table, tested
- Migrations tracked and versioned
- Queries are fast for your current scale
- You can explain your data model to a contractor or AI tool clearly
