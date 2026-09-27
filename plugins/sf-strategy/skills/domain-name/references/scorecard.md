# The ten rules, and how to score each one

Score every candidate 0, 1, or 2 on all ten. Maximum 20.

Each rule below gives a **test** — a question with an answer, not a feeling. Apply the
test rather than reacting to the name.

**Ownable is the only rule that can kill a name on its own.** You cannot buy what is
not for sale. A name scoring 19/20 with no obtainable domain is not a candidate. Every
other rule trades against the rest.

---

## 1. Memorable

*Someone should be able to recall it a day later. Concrete words beat generic
combinations.*

**Test:** does the name form a mental object or a concept you can picture? Say it once,
then try to write it from memory.

| Score | Meaning | Example |
|---|---|---|
| 2 | A clear object or concept. Sticks on one hearing. | Linear, Stripe, Buffer, Notion |
| 1 | Pronounceable and pleasant, but nothing to picture. | Zenvia, Kaleo |
| 0 | A generic compound that slides off. | GrowthPlatform, DataSync Pro |

Concrete beats abstract because a picture has a hook. "Stripe" is a thing you can see.
"Platform" is not.

---

## 2. Easy to say and spell

*If you say it aloud, the listener should know what to type.*

**Test:** say it to someone and have them type it. If they ask "how do you spell that?",
score 0.

Score 0 for any of these:
- Clever misspellings — `Flickr`, `Tumblr`, `Lyft` all pay a permanent tax
- Doubled letters at a seam — `bookkeeper`, `Appply`
- Ambiguous vowels — `Kolab` / `Collab`, `Symple` / `Simple`
- Awkward plurals — is it `Forms` or `Form`?
- Homophone traps — `Cite` / `Sight` / `Site`

This rule is close to a gate. A name failing it leaks users forever, in every podcast
mention and every word-of-mouth referral.

---

## 3. Conceptually relevant

*It should describe the product or express the outcome it creates.*

**Test:** name the product's outcome in one word. Does the name touch it?

| Score | Meaning |
|---|---|
| 2 | Names the outcome the customer wants. **Traction** is the model here — it describes nothing about the features and everything about what an early-stage product is trying to get. |
| 1 | A metaphor that connects with one small leap. **Buffer** for post scheduling. |
| 0 | Arbitrary. The name would fit any company in any industry. |

Naming the **outcome** outranks naming the **mechanism**. Outcomes stay true when the
mechanism changes.

---

## 4. Short

*Every extra syllable and word adds friction.*

**Test:** count syllables, not letters.

| Syllables | Score |
|---|---|
| 1-2 | 2 |
| 3 | 1 |
| 4+ | 0 |

One strong word is ideal. Two meaningful words are the practical sweet spot. Three
words is a sentence, not a name.

Short is not a virtue by itself — it is a proxy for low friction. `Linear` has three
syllables and works, because the word is common and the shape is clean. Judge friction,
and use syllable count as the first read.

---

## 5. Distinctive

*Searching the name should lead to you, not fifty unrelated companies.*

**Test:** search the bare word plus your category. Count how many unrelated companies
appear on page one.

| Score | Meaning | Example |
|---|---|---|
| 2 | The word is rare in a commercial context, so you can own the search. | Foothold |
| 1 | Common word, but few competitors in your category. | |
| 0 | Descriptive and anonymous. Nothing to grip. | GrowthPlatform, AppBuilder |

Descriptive and distinctive pull against each other. `GrowthPlatform` says exactly what
it does and is invisible. `Foothold` says less and is findable. Prefer findable, because
you can explain what you do in the tagline but you cannot buy your way out of anonymity.

---

## 6. No explanation required

*A user shouldn't have to ask "how do you spell that?" or "why is it called that?"*

**Test:** can a stranger hear the name and move on without a question?

A metaphor may require a tiny conceptual leap. It must not require a story. If the
answer to "why is it called that?" takes more than one sentence, score 0.

Founders routinely fail this rule because the story is meaningful **to them**. The
origin of the name is not an asset. Nobody asks.

---

## 7. Looks good written down

*Domains are visual objects.*

**Test:** write the full domain in lowercase. Look at the shape.

| Score | Meaning | Example |
|---|---|---|
| 2 | Scans cleanly. Word boundaries are obvious. | `socialgrowth.dev` |
| 1 | Readable but slightly cluttered. | |
| 0 | Prefixes, suffixes, or a jam of words. | `getyourtractionhq.com` |

Score 0 for: `get-` and `try-` prefixes, an `-hq` / `-app` / `-io` suffix bolted on,
hyphens, digits, or any string where two words collide into an accidental third
(`expertsexchange`).

The underlying words in `getyourtractionhq.com` are fine. The object is not.

---

## 8. Feels credible

*It should sound like something you'd trust with money, data, or your business.*

**Test:** would you put your customers' data in it? Would it look right on an invoice?

Score 0 for cute names, forced startup spelling, and gimmicky TLD puns where the name
runs into the extension (`cloud.ly`, `serious.biz`). Credibility matters more the closer
you get to money, health, or legal work.

---

## 9. Expandable

*Don't name the company after one narrow feature.*

**Test:** name the second product you might build. Does the name still fit?

`TweetReplyBot` becomes a liability the day you add LinkedIn, outreach, analytics, or
content planning. The name caps the company.

| Score | Meaning |
|---|---|
| 2 | Names a category, outcome, or concept. Fits products you haven't thought of. |
| 1 | Names a broad mechanism. Some room. |
| 0 | Names one feature, one platform, or one integration. |

Score 0 for any name containing another company's product name — `Tweet`, `Slack`,
`Notion`, `GPT`. Those are also a trademark risk, not only a ceiling.

---

## 10. Ownable — the gate

*You can get a sensible domain, handles, and search identity without fighting a much
larger brand.*

**Test, in order:**

1. Run `scripts/check-availability.py` on the candidate.
2. Search the bare word. Is there a larger company with the same name in an adjacent
   market? If yes, score 0 regardless of domain availability — you will compete for
   your own name forever.
3. Check the handle on the one channel you will actually use. Not all of them.

**Exact .com is useful but no longer mandatory for a software product.** A clean
`.dev`, `.app`, `.ai`, or `.io` beats a mangled `.com` every time. `foothold.dev` beats
`getfoothold.com`.

Ranked, best first:

1. Exact-match `.com`
2. Exact-match `.dev` / `.app` / `.ai` / `.io` — credible for software, and `.dev` and
   `.app` are HTTPS-only, which reads as modern
3. Exact match on a category TLD that fits — `.studio`, `.build`
4. A short, natural two-word `.com` — `usefoothold.com` only if `use` reads naturally
5. Anything with a hyphen, a digit, or a bolted-on `hq`

---

## Worked examples

| Name | Score | Read |
|---|---|---|
| **Stripe** | 19 | Concrete object, one syllable, credible, expandable. The metaphor (magnetic stripe) needs no explanation. |
| **Linear** | 18 | A concept you can picture, names the outcome (linear progress), scans clean. Common word, so distinctiveness came from execution. |
| **Traction** | 18 | The model for conceptual relevance. Names exactly what an early product wants. Common word, so check the search landscape hard. |
| **Foothold** | 17 | Strong identity, memorable, expandable. Beats `GrowthPlatform` on every rule that matters. |
| **Buffer** | 17 | One metaphor, one leap, no story needed. Expandable — it long outgrew post scheduling. |
| **GrowthPlatform** | 6 | Descriptive and anonymous. Fails memorable, distinctive, and looks-good. |
| **TweetReplyBot** | 4 | Fails expandable, credible, short, and carries trademark risk. |
| **getyourtractionhq.com** | 5 | Good root word destroyed by the wrapper. Fails looks-good, short, credible. |

---

## Reading a total

| Total | What to do |
|---|---|
| 16-20 | A real candidate. Take it to the availability check. |
| 12-15 | Fixable. Usually one rule is dragging it — find which, and try a variant. |
| Under 12 | Drop it. Do not try to rescue a name with three structural failures. |
| Any score, Ownable = 0 | Drop it. You cannot buy what is not for sale. |
