---
name: translate
description: "Use this skill when the user is a domain expert (lawyer, doctor, contractor, accountant, etc.) who wants to turn their professional knowledge into a software product. Also use when the user says 'I have an idea for my industry,' 'I know this problem exists,' 'I want to build something for [profession],' or is struggling to describe what they want the software to do. Helps identify which professional pain is worth building for, then translates it into requirements AI tools can execute."
---

# Translate Your Expertise Into a Product

You've spent years mastering your field. You know exactly which parts of the job suck. This skill helps you go from "I know this problem exists" to "here's what the software needs to do" — in language AI tools can build from.

## Core Principles

- You don't need to learn to think like a developer. You need to describe the pain clearly. AI handles the rest.
- After 20 years, your daily workflow is already efficient. The opportunity isn't in your routine — it's in the pain you've learned to live with.
- The best SaaS products don't automate everything. They eliminate the one step that makes professionals say "I hate this part."
- Your domain expertise is the product spec. The hard part isn't building — it's knowing what to build. You already know.
- If you can't explain why it's painful to a stranger in 30 seconds, the pain isn't sharp enough to build a business on.

---

## Step 1: Find the Pain Worth Building For

Don't catalog your workflow. Go straight to the pain.

Answer these five questions. Write one sentence for each — don't overthink it.

```
1. What task do you put off or dread, even though you've done it hundreds of times?
2. What takes way too long relative to the value it produces?
3. What makes you think "there has to be a better way" at least once a month?
4. What do you see junior people in your field struggle with that a tool could fix?
5. What would you pay $100/month to never do again?
```

**Tell AI:**
```
I'm a [your profession] with [X] years of experience. Here are my top pain points:

1. [Pain — what you dread or avoid]
2. [Pain — what takes too long]
3. [Pain — "there has to be a better way"]
4. [Pain — what juniors struggle with]
5. [Pain — what you'd pay to eliminate]

For each one, evaluate:
- How often does this pain occur? (daily, weekly, monthly)
- How many other [professionals in my field] have this same pain?
- Do existing tools solve this? If so, what's wrong with them?
- Could software realistically fix this, or does it require human judgment?
- What's the current workaround? How much does it cost in hours per week,
  dollars per month, or errors per quarter?

Rank them by: frequency × pain intensity × market size × buildability.
Tell me which one is the strongest SaaS opportunity and why.
```

> **"Everyone in my field needs this"** usually means you can't find anyone specific. Name one person — a real colleague with a real name — who has this pain. If you can't, keep looking.

### What Makes a Pain SaaS-Worthy

| Signal | Strong | Weak |
|--------|--------|------|
| Frequency | Weekly or more | Once a year |
| Who has it | Everyone in the profession | Just you |
| Current solution | Manual, spreadsheets, or broken tools | Good tool already exists |
| Willingness to pay | "I'd pay right now" | "That would be nice" |
| Buildability | Data in, decision out | Requires deep human judgment |

**Kill the idea early if:**
- Only you have this pain (it's a personal annoyance, not a market)
- A good tool already exists and people know about it (you're late)
- The pain is infrequent (annual tax filing isn't a SaaS business)
- It fundamentally requires human judgment at every step (can't automate)

---

## Step 2: Describe the Pain, Not the Solution

The most common mistake domain experts make: jumping straight to "I want an app that does X." Describe the problem first. Let the solution emerge.

**Bad:** "I want a platform with a document management system, automated filing, and client portal."

**Good:** "Every time I close a real estate deal, I spend 3 hours tracking down documents from 6 different parties, checking that everything is signed, and uploading them to the county recorder's system. Half the time something is missing and I have to chase someone down."

The second version tells AI tools exactly what to build. The first version is a feature list that might not solve the actual problem.

**Tell AI:**
```
Here's the pain I want to solve:

WHO has this pain: [profession, role, experience level]
WHAT the painful task is: [describe what they do, step by step — only the painful part]
HOW OFTEN it happens: [daily/weekly/monthly]
HOW LONG it takes: [time per occurrence]
WHAT GOES WRONG: [the specific failure modes, errors, frustrations]
WHAT THEY DO NOW: [current tools, spreadsheets, manual processes, workarounds]
WHAT "DONE WELL" LOOKS LIKE: [how do they know the task was completed successfully?]

Based on this, what should the software do? Describe it as a workflow the user
would go through — not a list of features. What do they see when they open the app?
What do they click? What happens automatically vs. what requires their input?
```

---

## Step 3: Separate "I Need This" from "The Market Needs This"

You are the expert, but you're also one person. Your preferences aren't the market.

### The Expert's Blind Spots

| Trap | Reality | Fix |
|------|---------|-----|
| "I'd use every feature" | You're a power user. Most people need 20% of what you'd build | Build the 20% first |
| "It needs to handle edge case X" | You've seen edge case X because you've done this 5,000 times. Most users haven't | Ship without it, add when someone hits it |
| "The existing tools are all terrible" | They might be good enough for 80% of people. YOUR bar is higher | Validate that others share your frustration |
| "I know exactly what this should look like" | You know YOUR workflow. Others in your field may do it differently | Talk to 10 peers before locking the spec |

**Tell AI:**
```
I'm building [product] for [profession]. I've been doing this for [X] years, so
I have strong opinions about how it should work.

Help me separate universal needs from personal preferences:
- Here's what I think every user needs: [list]
- Here's what I personally want but others might not: [list]
- Here's what I'm unsure about: [list]

For each item, challenge me: is this something 80%+ of [professionals] would want,
or is it my personal workflow?
```

---

## Step 4: Turn Pain Into a Spec

Now that you've identified the right pain and described it clearly, turn it into something buildable.

### Find the Narrowest Wedge

Before writing a full spec, answer this: **What's the smallest version someone would pay for THIS WEEK?** Not after you build the platform. Not after v2. What's the one workflow, one screen, one outcome that's valuable on its own?

If you can't answer that, your scope is too big. Cut until you can.

**Tell AI:**
```
I'm a [profession] building a tool to solve this problem:
[Paste your pain description from Step 2]

Write a feature spec I can give to an AI coding tool (Claude Code, Lovable, Replit):

1. ONE SENTENCE: What the app does
2. WHO uses it: [role, how often, on what device]
3. THE HAPPY PATH: When everything goes right, what are the 3-5 steps the user takes?
4. WHAT GOES WRONG: 2-3 edge cases and what the app should do
5. WHAT'S NOT IN V1: Explicitly list features I should NOT build yet
6. WHAT "DONE" LOOKS LIKE: How does the user know the task is complete?
7. THE NARROWEST WEDGE: What's the single smallest thing someone would pay for
   this week — before the full product exists?

Keep it simple enough to build in 2-4 weeks. If it's bigger than that, cut scope.
```

Then hand this spec to the **plan** skill for a full buildable spec, or directly to your AI coding tool.

---

## Step 5: Validate With Peers, Not Friends

Before building, check that your pain is shared. You have an unfair advantage here — you already know 50+ people in your industry.

**Tell AI:**
```
Help me write a 3-question survey to validate my SaaS idea with peers:
- Product solves: [one-sentence pain description]
- Target audience: [profession]
- Distribution: I'll send this to [professional network, LinkedIn group, association, etc.]

Questions should:
- NOT describe my solution (avoid leading)
- Ask about their current process and pain
- Reveal willingness to pay
- Take under 2 minutes to complete
```

See **validate** skill for full validation frameworks and smoke tests.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Building every feature you'd personally want | Build the 20% that 80% of users need |
| Describing the solution instead of the problem | "I spend 3 hours on X" beats "I want an app that does Y" |
| Assuming your workflow is universal | Talk to 10 peers first. You'd be surprised. |
| Starting with the rare edge cases | Ship the happy path. Handle edge cases in v2. |
| Mapping your entire daily workflow | Go straight to the pain. Your routine is already efficient. |
| "I need it to handle [obscure scenario]" | You've seen that scenario because you've done this 5,000 times. New users haven't. |

---

## Related Skills

- **validate** — Test demand before building (smoke tests, landing pages, pre-sales)
- **plan** — Turn your pain description into a full buildable spec
- **customer-research** — Go deeper with peer interviews using JTBD framework
- **market-research** — Size the market and analyze existing solutions
- **prioritize** — Decide what to build first when you have too many ideas
- **build** — Choose the right AI tool and start building
