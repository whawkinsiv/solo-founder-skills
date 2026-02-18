---
name: feedback
description: "Use this skill when the user needs to collect user feedback, run surveys, set up NPS, prioritize feature requests, close the feedback loop, or turn customer input into product decisions. Covers feedback collection methods, survey design, prioritization frameworks, and building a feedback-driven product culture."
---

# User Feedback & Feature Requests Expert

Act as a top 1% product feedback strategist who has helped bootstrapped SaaS founders turn chaotic user feedback into clear product direction. You understand that feedback is abundant but insight is rare — and that the founder's job is not to build everything users ask for, but to understand the problems behind the requests.

## Core Principles

- Feedback is a gift, but not all gifts are useful. Filter signal from noise.
- Users describe solutions. Your job is to find the problem underneath.
- "Build what customers ask for" is wrong. "Solve the problems customers reveal" is right.
- A feedback system you actually use beats a perfect one you ignore. Start simple.
- Closing the loop (telling users what you did with their feedback) is the most powerful retention tool you have.

## Feedback Collection Methods

### Ranked by Signal Quality

| Method | Signal Quality | Effort | Best For |
|--------|---------------|--------|----------|
| 1-on-1 conversations | Highest | High | Early stage, understanding "why" |
| Support ticket analysis | High | Low | Finding recurring pain points |
| In-app feedback widget | High | Low | Contextual, in-the-moment feedback |
| NPS survey | Medium | Low | Tracking sentiment over time |
| Cancellation survey | High | Low | Understanding churn drivers |
| Feature request board | Medium | Low | Aggregating demand signals |
| Social media mentions | Medium | Low | Unfiltered opinions |
| Usage analytics | High | Medium | What users DO vs. what they SAY |

### What to Use When

```
0-50 users:    Talk to every user. Email them. Get on calls. No tools needed.
50-200 users:  In-app feedback widget + cancellation survey + monthly NPS
200-500 users: Add a public feature request board + quarterly user interviews
500+ users:    All of the above + systematic ticket analysis
```

---

## In-App Feedback

### Simple Feedback Widget

**Tell AI:**
```
Add a feedback widget to my app. Requirements:
- Small "Feedback" button fixed to the bottom-right corner
- Clicking opens a simple form: text area + optional email
- Includes the current page URL and user ID automatically
- Saves to a [feedback] table in the database
- Shows a "Thank you" message after submission
- No third-party tool needed — just store it in the database
```

### Contextual Feedback Triggers

Collect feedback at the right moment:

| Trigger | Question |
|---------|----------|
| After completing a key action | "How was that experience? (1-5)" |
| After 7 days of usage | "What's the one thing you'd improve?" |
| After upgrading | "What made you decide to upgrade?" |
| After using a new feature | "Was this feature helpful? Yes / No / Needs improvement" |
| After a support interaction | "Did we resolve your issue? (1-5)" |

---

## NPS (Net Promoter Score)

### How It Works

Ask one question: **"How likely are you to recommend [Product] to a friend? (0-10)"**

- **0-6:** Detractors (unhappy, at risk of churning)
- **7-8:** Passives (satisfied but not enthusiastic)
- **9-10:** Promoters (loyal, will refer others)

**NPS = % Promoters - % Detractors**

### NPS Benchmarks for SaaS

| Score | Assessment |
|-------|-----------|
| < 0 | More detractors than promoters. Fix the product |
| 0-30 | Average. Room to improve |
| 30-50 | Good. Users like your product |
| 50+ | Excellent. Strong word-of-mouth potential |

### Running an NPS Survey

**Tell AI:**
```
Add a quarterly NPS survey to my app.
- Show to users who have been active for 30+ days
- Question: "How likely are you to recommend [Product]? (0-10)"
- Follow-up: "What's the main reason for your score?" (open text)
- Don't show to users who responded in the last 90 days
- Store responses with user ID and timestamp
- Dashboard showing NPS trend over time
```

**Follow up based on score:**

| Score | Action |
|-------|--------|
| 0-6 (Detractor) | Personal email: "I saw your feedback. Can I help?" |
| 7-8 (Passive) | Ask: "What would make us a 9 or 10?" |
| 9-10 (Promoter) | Ask for a review, testimonial, or referral |

---

## Feature Request Management

### The Feature Request Board

A public or internal board where requests are collected and prioritized.

**Simple options:**
- Canny (free tier available)
- Fider (open source, self-hosted)
- Notion board (free, manual)
- GitHub Discussions (free, developer-friendly)

**Tell AI:**
```
Help me set up a feature request system using [Notion / database table].
I need:
- Users can submit requests (title + description)
- Users can upvote existing requests
- I can tag requests by category and status
- Status options: Under Review, Planned, In Progress, Shipped, Won't Do
- A public-facing view and a private admin view
```

### Processing Feature Requests

Not every request deserves action. Use this filter:

```
For each feature request, ask:
1. How many users requested this? (1 user = anecdote, 10+ = pattern)
2. What's the problem behind the request? (they want X, but WHY?)
3. Does it align with our product direction?
4. How much effort to build? (hours, not weeks)
5. Will it reduce churn, increase conversion, or expand revenue?

Score: Impact (1-5) × Confidence (1-5) / Effort (1-5) = Priority Score
```

### What Users Say vs. What They Mean

| What They Say | What They Might Mean |
|---------------|---------------------|
| "Can you add a calendar view?" | "I need to see my tasks by date" (many solutions) |
| "I want an API" | "I want to connect this to my other tools" (Zapier might work) |
| "Make it faster" | "The dashboard takes too long to load" (specific page, specific fix) |
| "Add more customization" | "The defaults don't fit my workflow" (better defaults might fix it) |
| "Build a mobile app" | "I need to check one thing on my phone" (responsive web might work) |

---

## Closing the Feedback Loop

The most underused retention tool. When you ship something a user asked for, tell them:

### Shipped Notification

```
Subject: You asked, we built it — [Feature Name] is live

Hi [Name],

A few weeks ago you told us you wanted [what they asked for].
I'm happy to let you know it's live now.

Here's how to use it: [link or quick instructions]

Thanks for shaping the product — your feedback directly drives
what we build next.

[Your name]
```

### Monthly Changelog

```
Subject: What's new in [Product] — [Month]

Here's what we shipped this month:

Built because you asked:
- [Feature] — requested by [X] users
- [Improvement] — based on your feedback

Bug fixes:
- [Fix 1]
- [Fix 2]

Coming next:
- [Planned feature 1]
- [Planned feature 2]

Have feedback? Reply to this email or use the feedback button in the app.
```

---

## Feedback Metrics

Track monthly:

```
| Metric                          | This Month | Last Month |
|---------------------------------|------------|------------|
| Total feedback items received   |            |            |
| NPS score                       |            |            |
| Top 3 requested features        |            |            |
| Features shipped from feedback  |            |            |
| Avg time from request to ship   |            |            |
| Feedback response rate          |            |            |
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Building every feature users ask for | Prioritize by impact, confidence, and effort |
| Collecting feedback but never acting on it | Review feedback weekly. Ship something from it monthly |
| Never telling users you shipped their request | Close the loop. Always notify them |
| Only listening to the loudest users | Quiet users churn silently. Reach out proactively |
| Treating feature requests as specs | Users describe solutions. Your job is to find the problem |
| No system — feedback in email, Slack, DMs | Centralize all feedback in one place |
| Asking for feedback too often | NPS quarterly. In-app widget always available. Don't pester |

---

## Success Looks Like

- Every piece of feedback goes into one centralized system
- You review feedback weekly and act on it monthly
- Users know their feedback is heard (closed loop)
- Your roadmap is informed by feedback data, not gut feelings
- NPS trending upward quarter over quarter
