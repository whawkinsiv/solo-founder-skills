---
name: about-me
description: "Use this skill when the founder wants AI-written content to sound like them: 'set up my voice,' 'make content sound like me,' 'create my founder profile,' 'about me,' or 'my background.' Creates ABOUT-ME.md in the project root with testable voice rules, opinions, and stories that content, outreach, and landing-page work can use. Not for customer profiles (use validate), for editing existing text (use humanize), or for visual identity (use beautify)."
metadata:
  version: 2.0.0
---

# About Me

Create `ABOUT-ME.md`: a short file that captures how the founder writes, what they know, and what they believe. Skills that write in the founder's voice read it: content, first-customers, landing-page, and humanize.

The brain dump is itself a voice sample. Analyze how the founder writes, not only what they say.

## Steps

### If ABOUT-ME.md exists

Ask what changed. Update those sections. Do not start over.

### Step 1: Collect the brain dump

> Tell me about yourself, like you're explaining to a smart friend who needs to write as you. Cover what feels important: what you do and how you got here, what you know that most people don't, strong opinions about your industry, a few stories that shaped you, where you already have an audience, and what you're great at versus what you'd rather not do.

Let them write. Do not interrupt.

### Step 2: Check for voice signal

Can you list at least **4 testable writing patterns** from what they gave you? A pattern is testable if you could check a paragraph against it and answer yes or no.

- Testable: "Uses short sentences." "Opens with the point." "Never uses 'furthermore'."
- Not testable: "Authentic voice." "Relatable."

If you cannot list 4, ask for more signal:

> I can see what you're saying, but I can't hear how you say it yet. Either of these helps: write one of those stories out in full, stream of consciousness, or paste 2–3 things you've already written (posts, emails, Slack messages). Raw beats polished.

Do not continue until you have 4 patterns. A faked Communication Style section makes every downstream skill produce the same generic founder voice.

### Step 3: Synthesize

You are not a transcription service.

1. **Name the patterns the founder did not name.** Five products that each solve the founder's own problem is a "scratch your own itch" pattern. Say so.
2. **Turn activities into knowledge.** "Submitted to 100 directories" is an activity. What they learned from it is expertise. If they did not say what they learned, ask.
3. **Write voice rules, not adjectives.** Delete any line that uses these words or phrases: "direct and no-nonsense," "authentic," "relatable," "down-to-earth," "conversational," "passionate," "thought leader," "values transparency," "real talk." They describe every founder, so they describe no founder.
4. **Run the swap test.** Could this Communication Style section belong to another founder without anyone noticing? If yes, rewrite it, or go back to Step 2.
5. **Sharpen opinions.** "Building > talking" is a t-shirt. "Most founders waste months planning when a weekend v1 would answer the question" is an opinion a post can use.
6. **Attach a lesson to every story.**

### Step 4: Ask 3–4 follow-up questions

Pick from these, based on what is missing:
- "What's a specific win you're proud of? What made it happen?"
- "What did you try that failed? What did it cost?"
- "What's an opinion of yours that people in your field would disagree with?"
- "Paste 2–3 things you wrote that sound most like you."
- "How big is your audience on the platform you mentioned?"

### Step 5: Present and write

Show the draft and ask: "Does this sound like you? What's wrong or missing?" Revise. Write the file to the project root when the founder approves.

## Template

```markdown
# About Me

## Who I Am
[1–3 sentences. The pattern behind what they build, not a resume.]

## Domain Expertise
[What they know that most people don't. Knowledge, not activities.]

## Communication Style
[Testable rules only. Quote their real phrases. List what they would never say.
If there are not enough samples, write: "Insufficient samples — update after more writing."]

## Opinions
[Specific positions someone could disagree with.]

## Stories & Lessons
[Each story: what happened, and what it proved.]

## Presence & Distribution
[Platforms and audience sizes. Say "starting from zero" where true.]

## Strengths & Gaps
["Can build a full-stack app in a weekend," not "technical."]
```

## Rules

- **Keep the file under 60 lines of content.** A long file gets skimmed, and a skimmed file does not change the output.
- **Every line must give a skill something it could not guess.** Delete restatements of what the founder said.
- **A rough file now beats a perfect one later.** The voice will change as the founder learns what lands with customers.

## Output

`ABOUT-ME.md` in the project root, approved by the founder, with at least 4 testable Communication Style rules.
