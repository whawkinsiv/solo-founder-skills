---
name: about-me
description: "Use this skill when the user wants to create a founder profile, establish their personal voice for content, or set up context so other skills produce personalized output instead of generic AI copy. Also use when the user says 'set up my voice,' 'create my profile,' 'who am I,' 'about me,' 'my background,' 'make content sound like me,' or 'founder profile.' Creates ABOUT-ME.md in the project root — a reference file that other skills naturally use to personalize copy, strategy advice, and outreach. NOT for customer personas or ICP (see customer-research). NOT for editing existing text to sound human (see humanize). NOT for visual brand identity (see brand-identity-generator)."
---

# About Me: Founder Profile

Create `ABOUT-ME.md` — a reference file that captures who you are so every other skill can personalize its output.

Without this file, skills produce generic output. With it, they produce output that sounds like a specific human with specific experience, opinions, and a communication style.

**The brain dump IS a voice sample.** How you describe yourself reveals your communication style — sentence length, formality, humor, vocabulary. This skill analyzes your writing patterns, not just what you say.

---

## Workflow

### If ABOUT-ME.md already exists

Ask the founder what changed. Update the relevant sections. Don't start over.

### If creating from scratch

**Step 1 — Collect the brain dump:**

> Tell me about yourself. Write naturally — like you're explaining to a smart friend who needs to understand who you are in order to write as you and give you advice that fits your actual situation.
>
> Cover whatever feels important, but here are areas that help the most:
> - What you do and how you got here
> - What you know deeply — your unfair expertise
> - Strong opinions you have about your industry
> - A few stories that shaped you — wins, failures, lessons
> - How you communicate (or just write naturally and I'll pick it up)
> - Where you have an existing presence or audience
> - What you're great at vs. what you'd rather not do yourself

Let them write. Don't interrupt.

**Step 1.5 — Voice signal check:**

The question is NOT "did they write enough words." The question is: **can you identify at least 4 concrete, testable writing patterns from what they gave you?**

A pattern is testable if you could check a paragraph against it and say yes or no. "Uses short sentences" — testable. "Authentic voice" — not testable. "Starts with the point, never buries the lede" — testable. "Relatable and down-to-earth" — not testable.

Try to list 4 patterns right now from their brain dump. If you can't:

> "I can see what you're saying, but I can't hear how you say it yet — there's not enough of your actual writing voice here for me to build real style rules. I need more signal. Either of these would help:"
>
> 1. **Tell a story in full.** Pick one of the stories or opinions you mentioned above and write it out — a couple paragraphs, stream of consciousness, don't edit yourself.
> 2. **Paste things you've already written.** Copy-paste 2-3 social media posts, emails, Slack rants, blog drafts, tweets — anything where you were writing as yourself. Raw and unedited is better than polished.

Do NOT proceed to Step 2 until you can identify 4+ testable patterns. This is the most important gate in the entire skill. If you fake the Communication Style section, every skill downstream — social media, outreach, copywriting — produces identical tech-bro influencer slop. "Direct and no-nonsense. Values authenticity. Shoots from the hip." That's not a person. That's a horoscope.

**Step 2 — Synthesize, don't reformat:**

This is where the skill earns its value. You are NOT a transcription service. Your job:

1. **Extract patterns the founder didn't name.** If they're building 5 products and all solve problems they personally hit — that's a "scratch your own itch" builder pattern. Name it. Don't just list the 5 products.

2. **Infer the knowledge edges.** "I submitted to 100+ directories manually" isn't expertise. What they LEARNED from doing it — that's expertise. If they didn't state the lesson, ask for it.

3. **Write voice rules, not voice adjectives.** Every line in Communication Style must be a testable rule. Before writing the section, run two checks:

   **Kill list — if ANY of these appear in your draft, delete the line and try again:**
   "direct and no-nonsense," "authentic," "relatable," "down-to-earth," "approachable yet professional," "conversational," "shoots from the hip," "tells it like it is," "not afraid to be vulnerable," "blends humor with insight," "passionate," "thought leader," "values transparency," "refreshingly honest," "real talk"

   These are the phrases AI reaches for when it has no actual signal. They describe every founder and therefore no founder.

   **Swap test — after you draft Communication Style, ask:** could you swap this section into a different founder's profile and nobody would notice? If yes, it's not specific enough. Rewrite or go back to Step 1.5 for more samples.

   Good rules look like: "Leads with the point. Uses dashes over commas. One idea per sentence. Defaults to numbered lists over paragraphs. Never uses transition words like 'furthermore' or 'additionally.' Opens emails with 'Hey —' not 'Hi [Name],'. Swears occasionally but never in headlines. Uses rhetorical questions to set up counterintuitive points."

4. **Push opinions past bumper-sticker level.** "Building > talking" is a t-shirt, not a usable opinion. "Most founders waste months planning when they could validate by shipping a v1 in a weekend" — that's something a content skill can turn into a post.

5. **Attach lessons to stories.** A story without a takeaway is just an event. "Submitted to 100+ directories" is an event. "Submitted to 100+ directories and discovered X" is a story with a lesson. If the founder didn't provide the lesson, ask: "What did this teach you?"

6. **Keep it short and signal-dense.** Every line should give a skill something it couldn't guess from context. If you're restating what the founder said in slightly different words, delete it.

**Step 3 — Ask targeted follow-up questions:**

After the brain dump, ask for the high-value details founders don't know to volunteer. Pick 3-4 based on gaps:

**Business specifics:**
- "What's a specific win — a number, a customer, a deal — that you're proud of? What made it happen?"
- "What's something you tried that completely failed? What did it cost you (time, money, reputation)?"
- "What's a skill you have that most people in your space don't? How did you get it?"
- "What are you genuinely bad at or hate doing? Be specific."

**Voice & writing:**
- "Paste 2-3 social media posts, emails, or messages you've written that sound most like you."
- "What's a piece of content you've written that felt most like 'you'?"
- "What's an opinion you have that would make some people in your industry disagree?"

**Network & reach:**
- "Roughly how big is your audience on [platform they mentioned]? Growing or stale?"
- "Who do you know that most people in your position don't? (Investors, industry people, communities)"

Don't ask more than 4. Prioritize business specifics and writing samples — those are the highest-signal gaps.

**Step 4 — Present for review:**

Show the structured ABOUT-ME.md. Ask: "Does this sound like you? Anything missing or wrong?"

Revise based on feedback. Write the file when approved.

**Step 5 — Show them how to use it:**

After creating the file, give the founder these copy-paste prompts:

> **Now that ABOUT-ME.md exists, here's how to use it:**
>
> **Write social content in my voice:**
> "Read ABOUT-ME.md, then write a LinkedIn post about [topic] in my voice."
>
> **Personalize outreach:**
> "Read ABOUT-ME.md, then write a cold email to [prospect type] that leads with my credibility in [domain]."
>
> **Get strategy advice that fits my situation:**
> "Read ABOUT-ME.md, then suggest a launch strategy given my network and strengths."
>
> **Rewrite generic AI copy:**
> "Read ABOUT-ME.md, then rewrite this to sound like me: [paste text]"

---

## ABOUT-ME.md Template

```markdown
# About Me

## Who I Am
[1-3 sentences. The narrative, not a resume. What's the pattern — why do they build what they build?]

## Domain Expertise
[What they know that most people don't. Not activities — knowledge edges.
Specific insights from experience, not descriptions of experience.]

## Communication Style
[TESTABLE writing rules, not adjectives. Every rule should be checkable against a paragraph.
Bad: "Direct and authentic." Good: "Opens with the conclusion. Uses sentence fragments for emphasis.
Never writes 'I'm excited to...' or 'I'm passionate about...' Uses 'look' and 'here's the thing' as openers."
Quote their actual phrases. List things they would NEVER say.
If you don't have enough writing samples to fill this section with real rules, it should say:
"Insufficient samples — update this section after more writing is available."]

## Opinions
[Sharp, specific, defensible opinions. The kind that could start a debate.
Not values statements — actual positions on how things should work.]

## Stories & Lessons
[Each story has: what happened, and what it proved/taught.
No events without lessons. These are raw material for content.]

## Presence & Distribution
[Platforms, audience sizes, existing channels.
If starting from zero on something, say so explicitly.]

## Strengths & Gaps
[Specific capabilities and specific holes.
"Can build a full-stack app in a weekend" not "technical."
"Hates writing marketing copy" not "prefers building."]
```

---

## Quality Check

Before presenting the draft, verify:

| Check | Test |
|-------|------|
| No parroting | Is every line synthesized or inferred — not just reformatted input? |
| Voice kill list clear | Does Communication Style contain ANY phrase from the kill list in Step 2.3? If yes, rewrite. |
| Swap test passes | Could you swap this Communication Style into another founder's profile unnoticed? If yes, it's not specific enough. |
| Sharp opinions | Would any opinion make someone disagree? If not, sharpen it. |
| Stories have lessons | Does every story end with what it proved? |
| Signal density | Could you cut any line without losing information a skill would use? |
| No padding | Is the file under 60 lines of content? Shorter = more likely to be read. |
| Follow-ups asked | Did you ask 2-3 targeted questions to fill gaps? |

---

## Using ABOUT-ME.md Across Tools

| Tool | How it works |
|------|-------------|
| **Claude Code** | Skills auto-read `ABOUT-ME.md` from the project root. No extra steps — just create it and every future skill personalizes automatically. The brain dump conversation happens right here in the terminal. |
| **Lovable / Replit** | Run the brain dump in Claude Code (best voice analysis), then copy `ABOUT-ME.md` to your Lovable/Replit project. At the start of each new chat, say: "Read ABOUT-ME.md before writing anything." |
| **Cursor** | Add `ABOUT-ME.md` to your project root. Reference it in `.cursorrules` or paste the relevant section into context when writing copy. |
| **ChatGPT / other** | Paste the full ABOUT-ME.md into a custom instruction or at the start of any conversation about your brand, content, or outreach. |

---

## Don't Do Yet

- **Don't agonize over voice before you have customers.** Your communication style will evolve as you learn what resonates. A rough ABOUT-ME.md now beats a perfect one in 3 months.
- **Don't turn this into a brand exercise.** This isn't positioning or messaging — it's a profile for personalizing AI output. For brand identity, use **brand-identity-generator**.
- **Don't write for an audience.** This file is read by AI, not humans. Be honest, not performative. The less polished, the more useful.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Reformatting input instead of synthesizing | Your job is to extract patterns, name insights, and infer what wasn't said. If the output reads like the input with headers, start over. |
| Communication Style reads like a horoscope | Run the kill list and swap test from Step 2.3. If your draft uses words like "authentic," "direct," "no-nonsense," or could belong to any founder — you don't have enough signal. Go back to Step 1.5 and get writing samples. Never fake this section. |
| Generic opinions ("I believe in quality") | Push for specific, defensible opinions that could actually offend someone. |
| Stories without lessons | Ask: "What did that teach you?" Every story needs a takeaway or it's just a fact. |
| File is too long | Target under 60 lines of content. If a skill won't read it because it's too long, it's worthless. |
| Didn't ask follow-up questions | You always need to probe for 2-3 things the founder didn't know to volunteer. |

---

## Related Skills

- **customer-research** — Creates `MY-ICP.md`, the companion file. ABOUT-ME.md is who you are. MY-ICP.md is who your customer is.
- **social-media** — The skill where founder voice matters most. Reads ABOUT-ME.md to write posts that sound like you.
- **brand-identity-generator** — Creates `BRAND-IDENTITY.md` for visual identity. ABOUT-ME.md is the personality counterpart.
