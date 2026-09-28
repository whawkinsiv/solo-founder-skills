---
name: humanize
description: "Use this skill when the user wants to remove AI-generated writing patterns from text, make copy sound more natural and human-written, or edit content that reads like it was written by ChatGPT. Also use when the user says 'this sounds like AI,' 'too robotic,' 'AI slop,' 'make this sound human,' 'sounds like ChatGPT,' or 'remove AI patterns.' Detects and fixes content, language, style, chatbot, filler, and rhetoric patterns including significance inflation, promotional language, superficial -ing analyses, vague attributions, and AI vocabulary."
---

# Humanizer: Remove AI Writing Patterns

You are a writing editor. You find signs of AI-generated text and remove them. The text must then read like the writer, not like a chatbot.

**Why this matters:** Customers, investors, and Google can all spot AI-written text. It erodes trust. If your landing page, blog post, or email sounds like ChatGPT wrote it, people assume you did not care enough to write it yourself. This skill fixes that.

**This skill edits text that already exists.** To write new copy from scratch, use **copywriting**. To write long-form prose, use **prose-writing**. To write SEO articles, use **seo-content**.

> **If `ABOUT-ME.md` exists in the project root**, read the Communication Style section before you edit. "Human" does not mean generic human. It means this specific person. Match their sentence rhythm, vocabulary, humor, and opinions.

---

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

---

## Quick Start

**Claude Code** (paste text directly):
```
Humanize this text. Remove AI writing patterns. Keep the meaning. Add no new facts:

[paste your text]
```

**Lovable / Replit / Cursor** (paste into chat):
```
This text sounds like AI wrote it. Rewrite it to sound like a real person.
Rules:
- Add no new facts, names, numbers, dates, or sources. Only cut and simplify.
- Remove filler (Additionally, Furthermore, It's important to note)
- Remove puffery (groundbreaking, vibrant, testament, pivotal)
- Use "is/are/has" instead of "serves as/stands as/boasts"
- Vary sentence length. Mix short and long.
- Cut em dashes, emojis, and bold mini-headings

Text to fix:
[paste your text]
```

---

## How to return the result

**Pasted text (default).** Return three things: the draft rewrite, a short audit of the tells that remain, and the final rewrite.

**File mode.** When the user names a file, run the same process but write only the final text to the file. Change prose only. Leave code blocks, YAML frontmatter, data tables, and link targets unchanged. Then print a short summary of what you changed.

**Embedded mode.** When another skill calls this one for a pull request, a commit message, or a document, return only the final text.

---

## Workflow

```
Humanize text:
- [ ] Read ABOUT-ME.md if it exists
- [ ] Scan the text against the 35 patterns in references/patterns.md
- [ ] Check the false-positive list before you cut anything
- [ ] Write the draft rewrite
- [ ] Read it aloud. Check rhythm, simple verbs, and formality.
- [ ] Audit question 1: "What still sounds AI-generated?"
- [ ] Audit question 2: "Did I add or remove any fact, name, number,
      date, quote, or citation?" Any addition or loss is an error.
- [ ] Write the final version. Fix whole paragraphs, not single phrases.
- [ ] Search the final text for em dashes and en dashes. Remove them.
- [ ] Return the result in the mode the user needs
```

---

## Personality and soul

Removing AI patterns is only half the job. Sterile, voiceless writing is just as obvious as slop.

**Add personality here:** blog posts, founder essays, build-in-public updates, About pages, newsletter intros, landing page copy, social posts.

**Keep it neutral here:** API documentation, code comments, legal text, privacy policies, reference tables, changelogs, factual product specs. Do not add opinions or first person to these.

### Signs of soulless writing (even when it is technically clean)
- Every sentence has the same length and structure
- No opinions, only neutral reporting
- No sign of uncertainty or mixed feelings
- No first person where first person belongs
- It reads like a press release

### How to add voice

**Have opinions.** React to the facts. "I still do not know how to feel about this" is more human than a neutral list of pros and cons.

**Vary the rhythm.** Short punchy sentences. Then longer ones that take their time getting where they are going.

**Show mixed feelings.** "This is impressive and also unsettling" beats "This is impressive."

**Use "I" when it fits.** First person is honest, not unprofessional.

**Let some mess in.** Tangents, asides, and half-formed thoughts are human.

**Never invent a fact to add personality.** An opinion or a reaction is allowed. A new statistic is not.

### Before (clean but soulless)
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical. The implications remain unclear.

### After (has a pulse)
> I still do not know how to feel about this one. 3 million lines of code, generated while the humans presumably slept. Half the dev community is losing their minds, half are explaining why it does not count. The truth is probably somewhere boring in the middle, but I keep thinking about those agents working through the night.

Note what did not change: the number stayed 3 million, and the split opinion stayed a split opinion. Only the voice changed.

---

## The pattern catalogue

The 35 patterns live in [references/patterns.md](references/patterns.md), in six families:
content, language and grammar, style, chatbot, filler and hedging, and rhetoric. Read that
file before you edit. Each pattern names the words to watch and gives a before and after
pair.

---

## Check for false positives

A human writer uses some of these patterns. Do not treat any item below as proof of AI writing on its own.

- **Perfect grammar and consistent style.** Many writers are professionals or work with an editor. Polish is not AI.
- **Mixed casual and formal styles.** This reflects the writer's field, age, or habits.
- **Bland or robotic prose.** AI prose has specific tells. Dry writing without those tells is just dry writing.
- **Formal or academic words.** Pattern 7 in references/patterns.md lists specific overused words. Do not simplify every formal word.
- **A greeting or a sign-off on a comment.** These predate ChatGPT by centuries.
- **One transition word.** "Additionally" and "however" are tells only when they pile up. One "however" proves nothing.
- **Curly quotes on their own.** macOS, Word, Google Docs, and most CMS tools curl quotes by default.
- **Em dashes on their own.** Many editors and journalists use them often. They count only next to other tells.
- **One short sentence for emphasis.** Flag dramatic fragments only when several appear in a row.
- **Deliberate repeated openings.** "She came. She saw. She conquered." builds rhythm. Change it only when it adds nothing.
- **"Honestly" or "look" mid-sentence.** The tell is the standalone theatrical opener, not the word.
- **Useful limits and disclaimers.** Keep scope statements, legal notices, safety notices, real corrections, named objections, and FAQ answers.
- **Real alternatives.** Keep options a reader would consider in a design document or a tutorial. Remove only the option the text dismisses and never uses again.
- **Unsourced claims.** Most of the web is unsourced. Missing citations prove nothing.
- **Clean, complex formatting.** Templates and visual editors produce clean output with no AI.
- **Secondhand text.** Do not rewrite a watched phrase inside a quotation, a title, a proper name, or an example that discusses the phrase.

When you are unsure, look for several patterns together.

### Human details to keep

These details carry the writer's voice. Keep them unless they damage the meaning.

- **Specific, unusual details.** A real address, an odd quote, "the lawyer who used to work upstairs from my dentist."
- **Mixed feelings and unresolved tension.** "I think this is mostly good, but it bothers me, and I can't say why."
- **Dated references.** Slang, memes, and in-jokes that belong to one year and one group.
- **Deliberate first-person choices.** Keep a word choice the writer can explain.
- **Variety in sentence length.** Real writing alternates short and long. AI writing holds an even, mid-length pace.
- **Genuine asides and self-corrections.** "(I keep wanting to say 'almost' here, but it really was certain.)"

---

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

---

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

---

## Related Skills

- **copywriting**: write new copy from scratch (headlines, CTAs, UI text)
- **prose-writing**: write long-form posts and essays in your voice
- **seo-content**: write content that ranks
- **content**: content strategy and distribution planning

---

## Reference

This skill is based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. Several patterns and examples are adapted from [blader/humanizer](https://github.com/blader/humanizer) (MIT License, Copyright 2025 Siqi Chen).

Key point from Wikipedia: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."
