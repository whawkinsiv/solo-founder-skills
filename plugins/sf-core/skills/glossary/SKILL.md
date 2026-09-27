---
name: glossary
description: "Use this skill when the user doesn't understand a technical term, asks 'what is a [technical concept],' 'what does [term] mean,' seems confused by jargon in another skill, or is encountering developer concepts for the first time. Covers the 50+ technical terms non-technical founders encounter most, explained in plain English with no jargon."
---

# Technical Glossary

Plain-English definitions for every technical term you'll encounter while building your SaaS. No jargon. No condescension.

---

## The Basics

**API (Application Programming Interface)**
A way for two pieces of software to talk to each other. When your app gets weather data from a weather service, it's using an API. When you connect Stripe for payments, you're using Stripe's API. Think of it as a menu at a restaurant — it tells you what you can order (request) and what you'll get back (response).

**Database**
Where your app stores information. Users, their data, settings — everything lives in a database. Think of it as a collection of spreadsheets that your app can read and write to. The most common type for SaaS is PostgreSQL (often shortened to "Postgres").

**Frontend**
The part of your app that users see and interact with — buttons, pages, forms, menus. Built with HTML, CSS, and JavaScript. When someone says "React app" or "Next.js app," they're talking about frontend frameworks.

**Backend**
The part of your app that users don't see — the logic, data processing, and database connections that happen on a server. When a user clicks "Save," the frontend sends the data to the backend, which stores it in the database.

**Server**
A computer that runs your app and responds to requests from users. When someone visits your website, their browser sends a request to your server, which sends back the page. Modern hosting (Vercel, Railway, etc.) manages servers for you — you don't need to set one up.

**Framework**
A pre-built structure for building software, so you don't start from scratch. Like using a house kit instead of cutting every board yourself. Common ones: React (frontend), Next.js (full app), Django (Python backend), Express (Node.js backend).

---

## Building & Deploying

**Repository (Repo)**
A folder for your project's code, tracked by Git (version control). Think of it as a Google Doc with infinite undo and version history. Usually hosted on GitHub.

**Git**
A system that tracks every change to your code. If you break something, you can go back to any previous version. GitHub is a website that hosts your Git repositories.

**Deploy / Deployment**
The process of putting your app on the internet so anyone can use it. "Deploying to Vercel" means uploading your code to Vercel's servers so it's live at a URL.

**Environment Variables**
Secret settings (API keys, passwords, database connections) stored outside your code. Like a locked file cabinet that your app can open at runtime. You set these in your hosting provider's dashboard — never put them in your code.

**Build**
The process of converting your source code into the optimized version that runs in production. When you "build" a Next.js app, it compiles everything into fast, minified files ready to serve to users.

**CI/CD (Continuous Integration / Continuous Deployment)**
Automatic building and deploying. When you push code to GitHub, CI/CD automatically tests it and deploys it. Most modern hosting (Vercel, Netlify) does this for you.

---

## Web & Networking

**DNS (Domain Name System)**
The internet's phone book. Translates "yourapp.com" into the IP address of the server that runs your app. When you "configure DNS," you're telling the internet where your domain points.

**SSL / HTTPS**
Encryption between the user's browser and your server. The padlock icon in the browser. All modern hosting provides this automatically. If your site shows "Not Secure," SSL isn't set up yet.

**Domain**
Your website's address (yourapp.com). You buy one from a registrar (Namecheap, Cloudflare) for ~$10/year and point it at your hosting.

**URL**
The full address of a specific page: `https://yourapp.com/dashboard`. The domain is part of the URL.

**CORS (Cross-Origin Resource Sharing)**
A security rule that controls which websites can talk to your API. If your frontend is at `app.com` and your API is at `api.app.com`, you need to configure CORS to allow them to communicate. When something "works locally but not in production," CORS is often the culprit.

---

## Database Terms

**Schema**
The structure of your database — what tables exist, what columns each table has, and how tables relate to each other. Designing your schema means deciding how to organize your data.

**Migration**
A versioned change to your database structure. Adding a new column, creating a new table, or changing a field type. Like git for your database — each change is tracked and can be applied in order.

**Query**
A request to read or write data in the database. "Get all users who signed up this week" is a query. Written in SQL (Structured Query Language).

**Row Level Security (RLS)**
A database feature that restricts which rows each user can see. Essential for SaaS: User A should never see User B's data. The database itself enforces this, not just your app code.

**Foreign Key**
A link between tables. If a "projects" table has a `user_id` column that points to the "users" table, that's a foreign key. It says "this project belongs to this user."

**Index**
A lookup optimization for your database. Like an index in a textbook — instead of scanning every row, the database can jump directly to the rows it needs. Add indexes to columns you search or filter by frequently.

---

## Authentication & Security

**Authentication (Auth)**
Verifying who a user is. Login, signup, password reset — that's authentication. "Are you who you say you are?"

**Authorization**
Determining what a user is allowed to do. After logging in, can they edit this document? Can they access admin settings? "Are you allowed to do this?"

**OAuth**
A way to let users log in with an existing account (Google, GitHub, etc.) instead of creating a new password. "Sign in with Google" uses OAuth.

**Token**
A small piece of data that proves a user is logged in. After you log in, your browser stores a token. Every request to the server includes this token so the server knows who you are without asking for your password again.

**Encryption**
Scrambling data so only authorized parties can read it. "At rest" means stored data is encrypted. "In transit" means data moving between browser and server is encrypted (HTTPS).

---

## APIs & Integrations

**Endpoint**
A specific URL that does a specific thing. `POST /api/users` creates a user. `GET /api/projects` returns a list of projects. Each endpoint is like a function your API offers.

**Webhook**
A notification from one service to another. When a Stripe payment succeeds, Stripe sends a webhook to your server saying "payment completed." Instead of your app constantly asking "did they pay yet?", Stripe tells you when it happens.

**REST API**
The most common API style. Uses standard HTTP methods: GET (read), POST (create), PUT (update), DELETE (remove). If someone says "REST API," they mean an API that follows these conventions.

**JSON**
A text format for sending data between systems. Looks like: `{"name": "Jane", "email": "jane@example.com"}`. Almost every API sends and receives JSON.

**Rate Limiting**
Restricting how many API calls a user or system can make in a time period. "100 requests per minute" is a rate limit. Prevents abuse and controls costs.

---

## Hosting & Infrastructure

**CDN (Content Delivery Network)**
A network of servers around the world that stores copies of your static files (images, CSS, JavaScript). When a user in Tokyo loads your app, they get files from a server in Tokyo instead of one in Virginia. Makes your app faster globally. Vercel, Netlify, and Cloudflare all include CDNs.

**Serverless**
A hosting model where you don't manage servers. You write functions, upload them, and the hosting provider runs them when needed. You pay per execution, not per server. Vercel and Netlify use serverless for API routes.

**Container / Docker**
A way to package your app with everything it needs to run, so it works the same everywhere. Railway and Fly.io use containers. You usually don't need to think about this — your hosting provider handles it.

**Uptime**
The percentage of time your app is accessible. 99.9% uptime means ~8.7 hours of downtime per year. Monitoring tools like BetterUptime or UptimeRobot track this for you.

---

## SaaS-Specific Terms

**Multi-tenant**
One instance of your app serves multiple customers, with each customer's data isolated. Almost every SaaS is multi-tenant. The alternative (single-tenant) means running a separate copy of the app for each customer — expensive and unnecessary for most products.

**MRR / ARR**
Monthly Recurring Revenue / Annual Recurring Revenue. If 10 customers pay $50/month, your MRR is $500 and ARR is $6,000.

**Churn**
The rate at which customers cancel. 5% monthly churn means you lose 5 out of every 100 customers each month.

**Activation**
When a new user completes the key action that delivers value for the first time. "Activation rate" measures what percentage of signups actually use the product.

**Webhook** *(Stripe context)*
Stripe sends your server a message when something happens — payment succeeded, subscription cancelled, card declined. Your server listens for these messages and updates your database accordingly.

---

## Quick Lookup

| When you see... | It means... |
|----------------|------------|
| `npm install` | Install project dependencies (like getting ingredients before cooking) |
| `npm run dev` | Start the app in development mode (on your computer, not live) |
| `npm run build` | Compile the app for production |
| `git push` | Upload your code changes to GitHub |
| `git pull` | Download the latest code changes from GitHub |
| `.env` file | Where environment variables (secrets) are stored locally |
| `localhost:3000` | Your app running on your own computer at port 3000 |
| `404` | Page not found |
| `500` | Server error (something crashed) |
| `CORS error` | Your frontend isn't allowed to talk to your backend (configuration issue) |
