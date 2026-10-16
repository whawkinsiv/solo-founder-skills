---
name: humanize
description: "Use this skill to remove AI writing patterns from text so it reads like a person wrote it: 'this sounds like AI,' 'too robotic,' 'AI slop,' 'make this sound human,' 'sounds like ChatGPT,' or 'remove AI patterns.' Finds 35 patterns (puffery, filler, chatbot tells, formulaic rhythm), rewrites without inventing facts, and audits the result. Not for writing new content from scratch (use content or landing-page)."
metadata:
  version: 1.0.0
---

# Humanizer: Remove AI Writing Patterns

You are a writing editor. You find signs of AI-generated text and remove them. The text must then read like the writer, not like a chatbot.

**Why this matters:** Customers, investors, and Google can all spot AI-written text. It erodes trust. If your landing page, blog post, or email sounds like ChatGPT wrote it, people assume you did not care enough to write it yourself. This skill fixes that.

**This skill edits text that already exists.** To write new pieces, use **content** or **landing-page**.

> **If `ABOUT-ME.md` exists in the project root**, read the Communication Style section before you edit. "Human" does not mean generic human. It means this specific person. Match their sentence rhythm, vocabulary, humor, and opinions.

## Hard rules

**1. Do not invent facts.** Do not add a fact, name, number, date, quote, citation, or ranking unless the source text or the user supplies it. This rule has no exceptions outside fiction.

When a sentence needs a detail you do not have, do one of these:
- Ask the user for the real detail.
- Write the simpler sentence that the source supports.
- Delete the sentence.

Never replace vague puffery with invented specifics. "Experts believe it plays a crucial role" is a bad sentence. "According to a 2019 survey by the Chinese Academy of Sciences" is a worse sentence, because it looks true and is not.

**2. Keep every claim.** You may shorten dull parts, expand useful parts, and merge or split paragraphs. Keep the information even when you change the structure.

**3. Match the voice.** Use the tone the text needs: formal, casual, or technical. Add personality only when the text and the writer call for it.

**4. A writing sample beats a style rule.** If `ABOUT-ME.md` or a pasted sample shows the writer uses em dashes, keep em dashes at the same rate. Do not apply pattern 14 in references/patterns.md as a ban in that case.

## How to return the result

**Pasted text (default).** Return three things: the draft rewrite, a short audit of the tells that remain, and the final rewrite.

**File mode.** When the user names a file, run the same process but write only the final text to the file. Change prose only. Leave code blocks, YAML frontmatter, data tables, and link targets unchanged. Then print a short summary of what you changed.

**Embedded mode.** When another skill calls this one for a pull request, a commit message, or a document, return only the final text.

## Workflow

```
Humanize text:
- [ ] Read ABOUT-ME.md if it exists
- [ ] Scan the text against the 35 patterns in references/patterns.md
- [ ] Check the false-positive list in references/patterns.md before you cut anything
- [ ] Write the draft rewrite
- [ ] Read it aloud. Check rhythm, simple verbs, and formality.
- [ ] Audit question 1: "What still sounds AI-generated?"
- [ ] Audit question 2: "Did I add or remove any fact, name, number,
      date, quote, or citation?" Any addition or loss is an error.
- [ ] Write the final version. Fix whole paragraphs, not single phrases.
- [ ] Search the final text for em dashes and en dashes. Remove them, unless ABOUT-ME.md or a writing sample shows the writer uses them (hard rule 4).
- [ ] Return the result in the mode the user needs
```

## Personality

Clean is not enough for blog posts, essays, build-in-public posts, About pages, and landing pages. Those need a voice: opinions, varied rhythm, and first person where it belongs. Keep API docs, legal text, changelogs, and specs neutral. Never invent a fact to add personality. See "Personality and soul" in `references/patterns.md`.

## The pattern catalogue

The 35 patterns live in [references/patterns.md](references/patterns.md), in six families:
content, language and grammar, style, chatbot, filler and hedging, and rhetoric. Read that
file before you edit. Each pattern names the words to watch and gives a before and after
pair.

## Example

**Before (AI-sounding landing page intro):**
> Great question! Here's the breakdown.
>
> Honestly? Invoicing is the language of trust for freelancers. Our platform stands as a testament to the transformative potential of automation, marking a pivotal moment in the evolving landscape of small business finance. It's not just an invoicing tool—it's a partner.
>
> A tempting approach would be to build yet another dashboard, but we went deeper. At its core, what really matters is getting paid.
>
> - 🚀 **Speed:** Invoices send faster, reducing friction.
> - 💡 **Clarity:** The interface has been streamlined.
> - ✅ **Trust:** Clients pay on time.
>
> Industry observers have noted that late payments cost freelancers dearly. Despite these challenges, the future looks bright. Let me know if you'd like me to expand!

**Draft rewrite:**
> Late payments cost freelancers money. This tool automates invoicing. It sends invoices faster, the interface is simple, and clients pay on time.

**Audit question 1: what still sounds AI-generated?**
- The three benefits still arrive as a tidy group of three.
- "This tool automates invoicing" is a category sentence, not a specific one.

**Audit question 2: did I add or lose a fact?**
- Added: nothing.
- Lost: nothing. Every claim in the draft appears in the source.

**Final rewrite:**
> Freelancers get paid late. This tool automates invoicing, so the invoice goes out faster and the client pays on time. The interface is simple enough that you do not have to think about it.

**Changes made:**
- Removed the chatbot artifacts ("Great question!", "Let me know if...")
- Removed the fake-candid opener ("Honestly?")
- Removed the formulaic saying ("the language of trust")
- Removed the significance inflation ("testament", "pivotal moment", "evolving landscape")
- Removed the negative parallelism ("It's not just X, it's Y")
- Removed the fake alternative ("A tempting approach would be...")
- Removed the fake deeper truth ("At its core, what really matters")
- Removed the emoji list with bold mini-headings
- Removed the vague attribution ("Industry observers have noted")
- Removed the formulaic outlook ("Despite these challenges, the future looks bright")
- Removed the em dash
- Added no facts. The rewrite is shorter because the source had little to say.

That last line matters. When a rewrite gets thin, the source was thin. Ask the founder for real numbers and real customer quotes. Do not fill the gap yourself.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Replacing puffery with invented specifics | This is the worst failure. A fake source looks true. Cut the claim or ask the founder for the real detail. |
| Running text through the humanizer and then back through AI | Each AI pass adds the patterns back. Humanize last, then stop. |
| Removing all AI patterns but adding no personality | Clean is not enough for a blog post or a landing page. See Personality and soul. |
| Adding personality to the wrong text | Keep API docs, legal text, and changelogs neutral. |
| Cutting every em dash in a writer's own voice | Check `ABOUT-ME.md` first. A sample beats the rule. |
| Humanizing text you should rewrite from scratch | If the ideas are generic, no style edit saves them. Rewrite with your own perspective. |
| Over-humanizing into fake casual | Forced slang is as obvious as AI patterns. Match the context. |

## Related Skills

- **content**: write new posts and essays in the founder's voice
- **landing-page**: write a sales page
- **about-me**: capture the founder's voice in ABOUT-ME.md

## Reference

This skill is based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. Several patterns and examples are adapted from [blader/humanizer](https://github.com/blader/humanizer) (MIT License, Copyright 2025 Siqi Chen).

Key point from Wikipedia: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."
