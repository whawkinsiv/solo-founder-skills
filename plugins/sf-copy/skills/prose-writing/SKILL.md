---
name: prose-writing
description: "Use this skill when the user wants to write long-form prose — blog posts, founder essays, build-in-public posts, About pages, newsletter intros, or origin stories. Also use when the user mentions 'blog post,' 'essay,' 'long-form,' 'founder voice,' 'build in public,' 'BIP post,' 'About page,' 'origin story,' or 'newsletter copy.' For microcopy and CTAs, see copywriting. For removing AI patterns from existing text, see humanize. For SEO articles, see seo-content. For content strategy and distribution, see content."
---

# Prose Writing

Founders write a lot of prose: blog posts, essays, build-in-public updates, About pages, newsletter intros. Hand the task to AI and you get slop — hedged, generic, three-item-list cadence, throat-clearing openings, "this highlights" tails. This skill is the proactive composition workflow: voice first, structure second, drafting third, edit last.

> **If `ABOUT-ME.md` exists in the project root**, read it before writing — it carries the founder's voice. **If `MY-ICP.md` exists**, read it for who the prose is talking to. The founder's voice delivers the customer's frame.

## Three principles of prose that doesn't sound like AI

- **Lead with a specific moment, claim, or number — not a category.** "I shipped a feature on Tuesday and lost two customers by Friday" beats "Building products comes with tradeoffs."
- **Trust the reader.** State what you mean. Don't gesture at significance ("This highlights an important point about…"). The reader can see the point if you make it.
- **Structure invisibly.** Every paragraph earns its place by moving the argument or story forward. If a paragraph could be deleted with no loss, delete it.

---

## Workflow

```
- [ ] Read ABOUT-ME.md and MY-ICP.md if they exist
- [ ] Build a voice card (once, reusable)
- [ ] Pick the format and state the one takeaway
- [ ] Write the opening line first
- [ ] Outline as 3–5 plain-English beats
- [ ] Draft fast, in voice. Don't edit while drafting.
- [ ] Edit pass: throat-clearing, "this highlights," ending
- [ ] Run humanize if it still sounds AI
```

---

## Voice discovery (do once, reuse forever)

Before writing in your voice, you need to know what your voice is. This is a 15-minute exercise.

1. Find 3 pieces of prose you wish you'd written. Blog posts, essays, threads. Not "good writing" in the abstract — writing that sounds like you on your best day.
2. For each piece, note:
   - **Sentence length pattern.** Mostly short? Mixed? Long sentences with short punches?
   - **Vocabulary register.** Plain ("we shipped this thing")? Mid ("we released the feature")? High ("we deployed the capability")?
   - **Opinion stance.** Stated directly? Hedged? Self-aware about uncertainty?
   - **Self in the prose.** First person constantly? Occasionally? Never?
   - **Humor.** Dry? Earnest? None?
3. Distill into a 5-line **voice card** you paste into every prompt:

```
Voice card:
- Sentence rhythm: [e.g., short punches with one longer setup per paragraph]
- Register: [e.g., plain, casual, no jargon unless naming a real thing]
- Opinions: [e.g., stated directly, qualified once if needed, never hedged twice]
- First person: [e.g., I/we present throughout — this is a person talking]
- What I never do: [e.g., listicles, "in conclusion," motivational closers, three-item lists]
```

Save this in `ABOUT-ME.md` so every skill in this plugin can use it.

**Tell AI:**
```
Help me build my voice card. I'll paste 3 pieces of writing I wish I'd written.
For each: identify sentence rhythm, register, opinion stance, first-person presence, humor.
Then distill into a 5-line voice card I can paste into prompts.
Don't flatten the differences — find what's consistent across all three.

Piece 1: [paste]
Piece 2: [paste]
Piece 3: [paste]
```

---

## Format: Blog post (800–1500 words)

**Shape:** hook → premise → 2–4 beats with examples → resolution that earns a takeaway.

- **Hook (first 1–3 sentences):** a specific moment, claim, or number. Not a definition. Not a question. Not "Imagine if…"
- **Premise (next paragraph):** the one thing this post argues or shows. State it.
- **Beats:** each beat = one point, one example, one paragraph (or two). Examples are concrete. If you find yourself writing "for instance, consider a scenario where…" delete and use a real one.
- **Resolution:** the post lands somewhere. Not a recap. Not "in conclusion." The strongest line you've got, placed last.

**Anti-pattern:** the listicle that's actually a content-marketing skeleton — H2 / paragraph / H2 / paragraph, all same-length, same-cadence, no argument moving through.

**Tell AI:**
```
Write a [800/1200/1500]-word blog post on [topic].
Voice: [paste voice card]
The one takeaway: [in one sentence, what the reader walks away believing]
Structure: hook with [specific moment / claim / number] → premise → [3–4] beats with concrete examples → resolution that lands on the strongest line.
Constraints:
- No "this highlights / underscores / demonstrates"
- No -ing analysis tails ("...marking a shift toward...")
- No three-item lists unless they're actually three things
- No "in conclusion" or "to summarize"
- End on a strong line, not a recap
- Read aloud test: cut anything I wouldn't say
```

---

## Format: Founder essay (1500–3000 words)

**Shape:** personal stake → tension or question → exploration → arrived-at view.

- **Personal stake:** why are you the one writing this? A specific experience, decision, mistake. Not a credential.
- **Tension:** the thing you didn't know, or got wrong, or are still working out. The whole essay turns on this.
- **Exploration:** you working through it. Multiple beats. It's allowed to wander a little — that's what makes it an essay and not a blog post.
- **Arrived-at view:** what you think now. Not a tidy thesis. Closer to "here's where I've landed, with these open questions."

**Anti-pattern:** the LinkedIn-influencer "lessons learned" cadence. "Lesson 1. Lesson 2. Lesson 3." If you find yourself bullet-pointing the takeaway, you've stopped writing an essay.

**Tell AI:**
```
Write a [1500/2000/2500]-word founder essay.
Voice: [paste voice card]
Personal stake: [the specific experience this essay turns on]
Tension: [what I didn't know, got wrong, or am still working out]
Where I've landed (roughly): [your current view, with open questions allowed]
Constraints:
- This is an essay, not a blog post. It can wander. It doesn't need a tidy thesis.
- No "lessons learned" or numbered takeaways
- No motivational closer ("the journey continues...")
- Open with the specific experience, not a setup
- End where my thinking actually ends — open questions are fine
```

---

## Format: Build-in-public update (200–500 words)

For threads, single posts, weekly recaps, monthly reviews.

**Shape:** the number or shipped thing → what was hard → what changed in your view.

- **Open with the specific.** "We hit $4K MRR last week" or "I shipped the new onboarding on Tuesday and pulled it back on Wednesday." Not "Here's an update on what we've been up to."
- **What was hard:** the actual hard part, not the polished version. If the hard part is "I almost gave up on Thursday," say that.
- **What changed in your view:** the small reframe. The thing you'll do differently. Specific.

**Anti-pattern:** the progress brag with no specifics ("Made tons of progress! Excited for what's next!"). Or the formulaic three-emoji-bullet recap.

**Tell AI:**
```
Write a build-in-public [thread / single post / weekly recap], [200/300/500] words.
Voice: [paste voice card]
The number / shipped thing: [specific]
What was hard: [the actual hard part]
What changed in my view: [the reframe or new decision]
Constraints:
- Open on the specific. No "Here's what I've been up to."
- Name the hard part honestly, not the polished version
- One reframe at the end, not three takeaways
- No celebratory emoji-bullets
```

---

## Format: About page / origin story (300–600 words)

**Shape:** the problem you ran into → why existing answers didn't work → what you're building → who it's for.

- **The problem you ran into:** a specific situation, not a market. "I was running invoicing for my agency in three spreadsheets" beats "Small businesses face complex billing challenges."
- **Why existing answers didn't work:** for *you*. Be specific about which ones and why. This is also positioning.
- **What you're building:** plain language. What it does, not what it represents.
- **Who it's for:** named, not "anyone who needs…"

**Anti-pattern:** the company-voice "we believe" prose. "We believe in the power of simplicity." Delete. Founders write About pages in first person, with a story, or they don't write them.

**Tell AI:**
```
Write an About page / origin story, [300/500] words.
Voice: [paste voice card]
The problem I ran into: [specific situation]
Why existing answers didn't work for me: [name the alternatives and the specific gap]
What I'm building: [plain description of what it does]
Who it's for: [named — be specific]
Constraints:
- First person. No "we believe."
- Open on the specific situation, not a market summary
- Name the alternatives I tried (this is positioning)
- End with who it's for, named — not "anyone who…"
```

---

## Format: Newsletter intro (100–250 words)

The 2–3 paragraphs at the top of a newsletter, before "Here's what's below."

**Shape:** the one thing on your mind this week → connection to what's below → invitation.

- **The one thing on your mind:** specific. A moment, a question you're sitting with, a thing you noticed.
- **Connection to what's below:** light touch. Don't summarize the whole issue.
- **Invitation:** read it, reply, share, whatever. One sentence.

**Anti-pattern:** "Hope you're having a great week!" filler openings. Cut.

**Tell AI:**
```
Write a newsletter intro, [150/200] words.
Voice: [paste voice card]
The one thing on my mind: [specific — a moment, question, or observation]
What's below in the issue: [1-line summary]
The invitation: [reply / share / read / etc.]
Constraints:
- No "Hope you're well" / "Happy Monday" openings
- Open on the specific thing on my mind
- Don't summarize the issue — point at it
- One invitation, not three
```

---

## Drafting workflow

1. **Pick the format. State the one takeaway.** One sentence. If you can't, you don't have a piece yet.
2. **Write the opening line first.** It sets the cadence for everything below. If your opening line is vague or generic, the rest will be too. Rewrite it three times before moving on.
3. **Outline as 3–5 plain-English beats.** Not headers. Just what each section does. "I introduce the problem with the spreadsheet story. I show why three other tools didn't work. I describe what we built. I name who it's for."
4. **Draft fast, in your voice. Don't edit while drafting.** Editing while drafting is how prose dies. Get to the end first.
5. **Read aloud.** Cut anything you wouldn't say. Mark anything that sounds stiff. Rewrite those sentences first.

---

## Editing pass

After the draft, three high-leverage edits — these alone catch 80% of AI-prose problems in long-form:

1. **Cut the throat-clearing first paragraph.** Most AI drafts (and most human first drafts) start with a paragraph of setup before the actual opening. Delete it. The post starts on what's now line 1.
2. **Replace every "this highlights / this underscores / this demonstrates" with the specific thing.** Find/replace through the draft. Each one is a place where you gestured at significance instead of stating it.
3. **Tighten the ending.** No "in conclusion." No "ultimately." No "the journey continues." Find the strongest single line in your last 200 words and move it to be the last line. Cut whatever was after it.

If the prose still sounds AI after these three passes, run **humanize** for the full pattern catalog. Don't try to memorize that catalog here — link out and use it.

---

## Common mistakes

| Default move | Better move |
|--------------|-------------|
| Open with a definition or category | Open with a specific moment, claim, or number |
| "Hope you're having a great week" | The one thing actually on your mind |
| Three-item lists for everything | Use 3 only when there are actually 3 |
| "This highlights / underscores / demonstrates" | State the specific thing |
| -ing analysis tails ("...marking a shift toward…") | End the sentence at the fact |
| Hedge every claim ("perhaps it might be that…") | State your view. Qualify once if needed. |
| "We believe" company voice on About pages | First person, specific story |
| End with a recap or "in conclusion" | End on the strongest line in the piece |
| "Lessons learned" numbered list at the end | Let the takeaway be implied by the writing |
| LinkedIn-influencer cadence (one-line paragraphs forever) | Vary paragraph length — some prose has paragraphs |
| "Imagine if…" hook | Use a real example you actually have |
| Adjective stacks ("a powerful, intuitive, beautiful tool") | Pick one. Or none. Show it instead. |
| Symmetric three-part rhythm in every sentence | Break the rhythm — short, long, fragment. |
| Polished generic tone | A bit of mess. A real opinion. A line you're slightly nervous to publish. |

---

## Voice calibration by format

- **Blog post:** the founder explaining something they've worked out. Confident, specific, willing to be wrong.
- **Founder essay:** the founder thinking on the page. More uncertainty allowed. Personal.
- **Build-in-public:** the founder mid-flight. Specific, honest about hard parts, not polished.
- **About page:** the founder introducing themselves. First person. Story-shaped.
- **Newsletter intro:** the founder writing a quick note to someone they like. Warm, specific, brief.

The voice card stays the same across formats. The register tilts.

---

## Quality check before publishing

```
- [ ] Opening line is specific (a moment, claim, or number) — not a category
- [ ] The piece has a single takeaway I can state in one sentence
- [ ] Every paragraph moves the argument or story forward
- [ ] No "this highlights / underscores / demonstrates"
- [ ] No -ing analysis tails
- [ ] Three-item lists are actually three things
- [ ] Ending is the strongest line, not a recap
- [ ] Reads aloud without anything I'd never say
- [ ] One opinion stated directly, not hedged twice
- [ ] Specific examples instead of "for instance, consider a scenario"
```

---

## Related Skills

- **humanize** — Remove AI patterns from an existing draft (29-pattern catalog). Use after this skill if needed.
- **copywriting** — Headlines, CTAs, microcopy, error messages. Different surface area.
- **seo-content** — SEO-driven articles where keyword and search intent shape structure.
- **content** — What to write about and where to publish. Content strategy upstream of this skill.
- **brand-identity-generator** — Voice and tone work upstream of writing, if you don't have a voice card yet.
- **landing-page** — Long-form sales-page prose has different rules; see that skill for the page-shaped version.
