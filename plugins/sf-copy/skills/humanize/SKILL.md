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

**4. A writing sample beats a style rule.** If `ABOUT-ME.md` or a pasted sample shows the writer uses em dashes, keep em dashes at the same rate. Do not apply pattern 14 as a ban in that case.

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
- [ ] Scan the text against the 35 patterns below
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

## CONTENT PATTERNS

### 1. Undue emphasis on significance, legacy, and broader trends

**Words to watch:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted

**Problem:** AI writing claims that ordinary details mark a major change or reflect a broad trend.

**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.

**After:**
> The Statistical Institute of Catalonia was established in 1989, part of a wider decentralization of administrative functions in Spain.

---

### 2. Undue emphasis on notability and media coverage

**Words to watch:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence

**Problem:** AI writing lists well-known publications or follower counts to prove that a person matters. The list gives no useful context.

**Before:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.

**After:**
> Her views have been cited in The New York Times and the BBC.

Keep a citation when the source explains what the person said and where. Do not invent that context to make the citation useful.

---

### 3. Superficial analyses with -ing endings

**Words to watch:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

**Problem:** AI writing adds an -ing phrase to make a simple fact sound deeper than it is.

**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.

**After:**
> The temple is painted blue, green, and gold, colors meant to evoke Texas bluebonnets and the Gulf of Mexico.

---

### 4. Promotional and advertisement-like language

**Words to watch:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning

**Problem:** AI writing sounds like an advertisement, especially about places, culture, products, and organizations.

**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.

**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia.

The result is shorter and duller. That is correct. If the founder wants a real selling point here, ask them for one. Do not supply it yourself.

---

### 5. Vague attributions and weasel words

**Words to watch:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few are cited)

**Problem:** AI writing assigns a claim to unnamed experts, critics, reports, or observers.

**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.

**After:**
> Researchers and conservationists study the Haolai River for its unusual characteristics.

Name a real source when the source text gives one. Otherwise remove the unsupported claim. Never invent a source.

---

### 6. Formulaic challenges and outlook sections

**Words to watch:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

**Problem:** AI writing adds a stock section about challenges, future prospects, or continued growth. The section repeats vague claims instead of adding facts.

**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.

**After:**
> Korattur has recurring traffic congestion and water shortages.

---

## LANGUAGE AND GRAMMAR PATTERNS

### 7. Overused AI vocabulary

**High-frequency AI words:** actually, additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, gate/gated/gating (figurative only, keep real technical use), highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, quietly, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

**Problem:** AI writing uses these words far more often than most people do, and often in groups.

**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.

**After:**
> Somali cuisine also includes camel meat. Pasta dishes, introduced during Italian colonization, remain common.

---

### 8. Avoidance of "is" and "are"

**Words to watch:** serves as/stands as/marks/represents [a], boasts/features/offers [a]

**Problem:** AI writing replaces simple verbs such as is, are, and has with longer phrases.

**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.

**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

---

### 9. Negative parallelisms and clipped negative endings

**Problem:** AI writing overuses "Not only...but..." and "It's not just X, it's Y." It also ends sentences with a clipped negative fragment instead of a clear clause.

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.

**After:**
> The heavy beat adds to the aggressive tone.

**Before (clipped ending):**
> The options come from the selected item, no guessing.

**After:**
> The options come from the selected item, so the user does not have to guess.

---

### 10. Rule of three overuse

**Problem:** AI writing forces ideas into groups of three to sound complete.

**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.

**After:**
> The event includes talks and panels. There is also time for informal networking.

---

### 11. Synonym cycling and repeated sentence openings

**Problem:** AI writing handles repetition by rule instead of by ear. It renames the same person or thing. It also starts several sentences with the same subject.

Use one clear name for one subject. For repeated openings, merge sentences, change the subject, or start with the action.

**Before (synonym cycling):**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.

**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.

**Before (repeated openings):**
> She noted the door. She noted the lock on it. She filed both away.

**After:**
> She noted the door and its lock, then filed both away.

Do not ban the repeated word. Fix the repeated sentence pattern. The remaining sentence may still start with "She."

---

### 12. False ranges

**Problem:** AI writing uses "from X to Y" when X and Y do not form a real range.

**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.

**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.

---

### 13. Passive voice and missing subjects

**Problem:** AI writing hides who acts, or drops the subject entirely. Use the active voice when it makes the actor clearer.

**Before:**
> No configuration file needed. The results are preserved automatically.

**After:**
> You do not need a configuration file. The system preserves the results automatically.

---

## STYLE PATTERNS

### 14. Em dashes and en dashes

**Rule:** The final text must contain no em dashes (—) and no en dashes (–), unless the writer's sample uses them. Replace the dash with a period, a comma, a colon, or parentheses, or rewrite the sentence. Check also for spaced dashes and double hyphens (--) used as dashes.

**Before:**
> The term is primarily promoted by Dutch institutions—not by the people themselves. You don't say "Netherlands, Europe" as an address—yet this mislabeling continues—even in official documents.

**After:**
> The term is primarily promoted by Dutch institutions, not by the people themselves. You don't say "Netherlands, Europe" as an address, yet this mislabeling continues in official documents.

**Before:**
> The new policy — announced without warning — affects thousands of workers. The changes -- long overdue according to critics -- will take effect immediately.

**After:**
> The new policy, announced without warning, affects thousands of workers. The changes, long overdue according to critics, will take effect immediately.

Before you return the rewrite, search it for — and –. Remove each one. If `ABOUT-ME.md` shows the writer uses them, match the writer's rate instead.

---

### 15. Overuse of boldface

**Problem:** AI writing bolds words and phrases without a clear reason.

**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.

**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

---

### 16. Lists with bold mini-headings

**Problem:** AI writing uses vertical lists where every item starts with a bold label and a colon.

**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

**After:**
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

---

### 17. Title case in headings

**Problem:** AI writing capitalizes every main word in a heading.

**Before:**
> ## Strategic Negotiations And Global Partnerships

**After:**
> ## Strategic negotiations and global partnerships

---

### 18. Emojis

**Problem:** AI writing decorates headings and list items with emojis.

**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting

**After:**
> The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.

---

### 19. Curly quotation marks

**Problem:** ChatGPT uses curly quotes (“...”) where the writer or the target format uses straight quotes ("...").

**Before:**
> He said “the project is on track” but others disagreed.

**After:**
> He said "the project is on track" but others disagreed.

---

## CHATBOT PATTERNS

### 20. Chatbot text left in the answer

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., Want me to...?, Should I continue?, let me know, here is a...

**Problem:** A chatbot greeting, offer, or closing stays in text that should stand on its own.

**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

---

### 21. Knowledge-limit disclaimers and speculative gap-fill

**Words to watch:** as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information, not publicly available, maintains a low profile, keeps personal details private, likely [grew up/studied/began], it is believed that

**Problem:** The model says it could not find a source, then fills the gap with a plausible guess. State what the source does not show, or delete the sentence. Never present a guess as a fact.

**Before (cutoff disclaimer):**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.

**After:**
> The company's founding date is not documented in the available sources.

Or cut the sentence. State a date only when a source gives you one.

**Before (speculative gap-fill):**
> Information about her early life is not publicly available, suggesting she maintains a low profile and keeps personal details private. She likely grew up in a middle-class household, which shaped her later interest in education reform.

**After:**
> Her early life is not documented in the available sources.

---

### 22. Sycophantic tone

**Problem:** AI writing praises the user or agrees before it answers.

**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.

**After:**
> The economic factors you mentioned are relevant here.

---

## FILLER AND HEDGING

### 23. Filler phrases

**Before → After:**
- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"

---

### 24. Excessive hedging

**Phrases to watch:** to be fair, it's also possible, could potentially, might arguably, in some cases it may, this is an inference

**Problem:** Repeated editing stacks one qualifier on another until every claim sounds uncertain. Keep a qualifier only when the source supports it and the meaning needs it.

**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.

**After:**
> The policy may affect outcomes.

---

### 25. Generic positive conclusions

**Problem:** AI writing ends with vague optimism instead of the last useful fact.

**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.

**After:**
> Cut the paragraph. End on the last concrete fact in the text. If the source states real plans, use those instead.

---

### 26. Too many hyphenated word pairs

**Words to watch:** third-party, cross-functional, client-facing, data-driven, decision-making, well-known, high-quality, real-time, long-term, end-to-end

**Problem:** AI writing hyphenates these pairs everywhere. Keep the hyphen before a noun. Drop it after the noun.

**Before:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross-functional, the report is high-quality, and the methodology is data-driven.

**After:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross functional, the report is high quality, and the methodology is data driven.

---

## RHETORIC PATTERNS

These patterns catch what models write today. The older patterns catch obvious slop. These catch text that sounds like a confident blogger and still is not.

### 27. Pretending to reveal a deeper truth

**Phrases to watch:** the real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter

**Problem:** These phrases make an ordinary point sound like a hidden truth.

**Before:**
> The real question is whether teams can adapt. At its core, what really matters is organizational readiness.

**After:**
> The question is whether teams can adapt. That mostly depends on whether the organization is ready to change its habits.

---

### 28. Announcing the next point

**Phrases to watch:** let's dive in, let's explore, let's break this down, here's what you need to know, now let's look at, without further ado, heads up, quick note, before I forget

**Problem:** AI writing announces the next point instead of stating it. A casual version such as "one thing that bit me" has the same problem. Remove the announcement, not only its formal tone.

**Before:**
> Let's dive into how caching works in Next.js. Here's what you need to know.

**After:**
> Next.js caches data at several layers, including request memoization, the data cache, and the router cache.

**Before (casual register):**
> One thing that bit me hard, so pay attention to this part: the webpack dev server doesn't send the CORS header by default.

**After:**
> The webpack dev server doesn't send the CORS header by default.

---

### 29. A heading repeated in the first sentence

**Problem:** AI writing follows a heading with a sentence that only repeats the heading. Delete the repeated sentence.

**Before:**
> ## Performance
> Speed matters.
>
> When users hit a slow page, they leave.

**After:**
> ## Performance
> When users hit a slow page, they leave.

---

### 30. Writing about the previous version

**Problem:** Documentation and comments should describe current behavior. Mention the old version only in changelogs, release notes, and migration guides.

**Before:**
> This function was added to replace the previous approach of iterating through all items, which caused O(n²) performance.

**After:**
> This function uses a hash map for O(1) lookups, avoiding the O(n²) cost of naive iteration.

---

### 31. Forced punchlines and dramatic fragments

**Problem:** AI writing turns each sentence into a dramatic closing line. One short sentence adds emphasis. A row of short fragments feels forced.

**Before:**
> Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.

**After:**
> AlphaEvolve changed the search because it did not favor symmetry or human-looking designs. That made some of the older assumptions less useful.

---

### 32. Formulaic sayings

**Phrases to watch:** X is the Y of Z, X becomes a trap, X is not a tool but a mirror, the language of, the currency of, the architecture of

**Problem:** AI writing turns an ordinary claim into a saying that sounds deep and adds no detail. Replace the saying with the specific claim.

**Before:**
> Symmetry is the language of trust. Efficiency becomes a trap when teams forget the human layer.

**After:**
> Symmetric layouts often feel more predictable to users. Teams can over-optimize workflows and miss how people actually use them.

---

### 33. Fake-candid openings

**Phrases to watch:** Honestly?, Look, Here's the thing, The thing is, Let's be honest, Real talk

**Problem:** AI writing starts with a staged pause or a claim of honesty before it makes a routine point. State the point directly.

**Before:**
> Is it worth the price? Honestly? It depends on how often you'll use it.

**After:**
> Whether it's worth the price depends on how often you'll use it.

This applies to the standalone opener only. "Honestly" and "look" in the middle of a casual sentence are normal.

---

### 34. Answering objections nobody raised

**Phrases to watch:** This isn't (mainly/really) about, I'm not saying/arguing/trying to, To be clear, Don't get me wrong, This is not to say, You could argue... but, Some might say... but

**Problem:** AI writing answers an objection that never appears in the text. Watch for an unattributed statement about what the writer does not mean.

**Before:**
> This isn't mainly about prompt length, and I'm not arguing that documentation doesn't matter. You could categorize the problem another way, but the issue is whether the agent can use the instruction when it acts.

**After:**
> The issue is whether the agent can use the instruction when it acts.

Remove only the unsupported defense. If it contains a real claim, state that claim directly. A direct claim such as "the API is not thread-safe" is not this pattern.

---

### 35. Rejecting fake alternatives

**Phrases to watch:** A tempting option/approach would be, One might be tempted to, An obvious approach would be, You might think... but, It would be easy to just, Some would suggest

**Problem:** AI writing introduces an option no reader would consider, rejects it in a clause, and never mentions it again. Remove the fake option and state the real constraint.

**Before:**
> Session tokens are rotated every 24 hours. A tempting approach would be to rotate them by restarting the auth service on a cron job, but that would drop every active session. Rotation happens in place, and clients refresh transparently.

**After:**
> Session tokens are rotated every 24 hours, in place, and clients refresh transparently.

One rejected option can be valid. Several short, unrelated rejections are a stronger sign.

---

## Check for false positives

A human writer uses some of these patterns. Do not treat any item below as proof of AI writing on its own.

- **Perfect grammar and consistent style.** Many writers are professionals or work with an editor. Polish is not AI.
- **Mixed casual and formal styles.** This reflects the writer's field, age, or habits.
- **Bland or robotic prose.** AI prose has specific tells. Dry writing without those tells is just dry writing.
- **Formal or academic words.** Pattern 7 lists specific overused words. Do not simplify every formal word.
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
