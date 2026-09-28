---
name: domain-name
description: "Use this skill when the user needs to name a product or company and find a domain for it. Also use when the user says 'name my product,' 'what should I call it,' 'help me pick a domain,' 'is this a good name,' 'find me a domain,' 'my domain is taken,' 'check if this name is available,' or pastes a list of candidate names for an opinion. Scores names against ten rules, then verifies domain availability with DNS and RDAP. Do NOT use for buying a domain or pointing DNS at your host once the name is chosen (use deploy), for visual brand identity such as colors, logos, or typography (use brand-identity-generator), for positioning and messaging (use niche-advantage), or for writing headlines and page copy (use copywriting)."
metadata:
  version: 1.0.1
---

# Naming a product and getting the domain

Naming fails in two different ways, and they need different work. A name can be a bad
name, or it can be a good name you cannot have. Judge the concept first, then test
availability. Running availability checks on a weak shortlist wastes the founder's time
on names they should not want.

## Optimise in this order

```
great concept  →  great name  →  acceptable domain
```

**Never the reverse.** The failure mode is subtle and almost automatic: one pattern
starts returning free domains, so you generate more of that pattern, and within two
rounds availability is choosing the concept. You will not notice it happening. The
symptom is a candidate list where most names share a word or a shape.

A great name with an acceptable domain beats a mediocre name with a pristine one:

- `Foothold` → `getfoothold.com` — **works.** The name is doing the work.
- `Social Engagement Automation` → `socialengagementautomation.com` — **still mediocre.**
  A perfect domain cannot rescue a dead name.

So when a strong name's exact domain is gone, do not discard the name. Try the
variants in the rule 10 ladder first. Discard a name for being *weak*, never for being
*taken*.

Work in three phases. Do not skip ahead to phase 3 — a founder who picks from an
unrefined list picks the first name they recognise, which is usually the most generic
one.

**Read `references/scorecard.md` before scoring anything.** It holds the ten rules, the
test for each, and worked examples.

---

## Phase 1 — Generate the initial list

No availability checks yet. Domains are cheap to check and expensive to get attached to.

### Step 1: Get the raw material

Ask for whatever is missing, in one message:

1. **Every distinct job the product does. Number them. Do not compress to one
   sentence.** A three-job product described in one sentence loses two jobs, and
   whichever job survives becomes the entire naming territory by accident.
2. **What unifies those jobs.** If the product does find → join → publish, the
   unifying idea is working a defined set of people over time. **The unifying idea is
   the naming territory, not any single job.**
3. **The outcome the customer gets.** This matters more than the features. `Traction`
   works because it names what an early-stage product wants.
4. Who it is for.
5. Any word they already like, or any they have ruled out.
6. Whether `.com` is a hard requirement.

If `ABOUT-ME.md` or `MY-ICP.md` exist in the project, read them first and ask only for
what they do not answer.

### Step 2: Build word pools

Write out the pools before you write any names. Names invented directly tend to cluster
around one idea.

**First, one pool per job, plus a unifying pool.** This step is what stops a multi-job
product from being named after whichever job you thought about first.

| Pool | Contains | Example — a tool that plans your meals, builds the list, and orders the food |
|---|---|---|
| Job 1 | Vocabulary for the first job | plan, menu, spread, course |
| Job 2 | Vocabulary for the second job | list, tally, cart, basket |
| Job 3 | Vocabulary for the third job | order, deliver, stock, fill |
| **Unifying** | **Words covering every job at once** | **pantry, larder, table, kitchen** |

**The name usually comes from the unifying pool.** A journalist's *beat* is the people
they cover, the conversations they follow, and the stories they publish — one word for
three jobs.

Then cut across those with the lexical pools:

| Pool | Contains | Example for a habit tracker |
|---|---|---|
| Outcome | What the customer ends up with | streak, momentum, traction, foothold |
| Object | Concrete things in the domain | ledger, anchor, compass, thread |
| Action | What the user does | tally, mark, log, keep |
| Metaphor | One conceptual leap away | ratchet, flywheel, cairn, tide |

Before you write a single name, check that some word in your pools touches **every**
job. If every word serves one job, stop and rebuild the pools. That is the most common
way this skill fails, and everything downstream inherits the error.

### Step 3: Produce 20-30 candidates

Cover all five kinds deliberately. Do not let one kind dominate — each fails
differently, and a list of one kind inherits that kind's weakness.

| Kind | What it is | Examples |
|---|---|---|
| **Adjacent concept** | An ordinary word one step from the product. Not descriptive, not a riddle. | Stripe, Notion, Linear, Buffer |
| **Plain compound** | Two real words naming the thing you get | Basecamp, Mailchimp, Dropbox |
| Outcome word | Names what the customer ends up with | Traction, Foothold |
| **Coined** | Invented, but spellable on first hearing | Typefully, Taplio, Calendly |
| Metaphor | One conceptual leap | Buffer, for scheduling |

### Generate the obvious name first, and check it before you reach

**Before any other kind, build the plain compounds from the product's own nouns** —
the words its landing page already repeats — and check those domains immediately.

Take the noun for who it serves, the noun for what it hands them, and put them
together. Then do it again with the next pair. Produce a dozen of these before you
generate anything clever.

If one of them is free and literally true, **you may already be finished.** Reaching
past an available, accurate, plain name is the single most expensive mistake in this
skill: it costs rounds, and it usually ends back where it started.

Only once the obvious names are generated and checked do you move to the kinds below.

**Adjacent concept is the highest-yield kind and the easiest to skip.** Stripe is not
a payments pun. Notion does not describe notes. Linear does not describe issue
tracking. Each is a common word picked for sound and a faint thematic link, with no
puzzle for the listener to solve. Generate at least eight of these before anything
else.

**Coined is not the same as misspelled.** `Typefully` and `Calendly` are coinages — a
listener spells them right on first hearing. `Flickr` and `Lyft` are respellings of
real words and score 0 on rule 2. Coin by adding a clean suffix (`-ly`, `-io`, `-a`)
to a real word, or by fusing two real words. Never by dropping vowels.

**Warning on plain compounds.** They read clearly and score 0 on rule 5, because
`GrowthPlatform` is anonymous. A compound earns its place when it names the product's
actual output — `Dropbox` is a box you drop things into — not when it merely labels a
category.

### Step 4: Score and present

Score each on the ten rules. Present the top 12 as a table, highest first. **Every row
carries both a pro and a con.** Never one without the other.

| Name | Score | Pro | Con |
|---|---|---|---|
| Foothold | 17 | Vivid mental object, distinctive, expandable | Common word — the search landscape needs checking |
| Basecamp | 16 | Names the thing you get; two real words, both true | "Camp" is well used; search is crowded |

A row carrying only a con reads as a rejection you have already made on the founder's
behalf. A row carrying only a pro is a sales pitch. They need both halves, because
they are the one judging.

**Cover every kind in generation. Do not cap any kind in the results.**

Before scoring, confirm you produced real candidates from all five kinds. If you
skipped one because another was going well, go back — that is a lapse in generation,
and the list you are about to score is missing its best option.

But once you have covered the kinds honestly, **let the winners win.** If one pattern
takes eight of the top twelve after a fair fight, that is a finding about the product,
not a bias to correct. Diluting a strong list to look varied hands the founder worse
options and hides the real signal. Say plainly that the pattern dominated and why.

The failure to guard against is **generating** narrowly — usually because one pattern
starts returning free domains and availability quietly takes over the brief. It is not
a list that ends up concentrated on merit.

**Done when** the founder has a scored list of 12 and has told you which names they
react to. Move to phase 2.

---

## Phase 2 — Refine to a shortlist and check availability

### Step 5: Cut to 5-8

Keep the names the founder reacted to plus any scoring 16+. Drop anything scoring under
12 — a name with three structural failures does not get rescued.

For each survivor, try two variants to fix its weakest rule. A name losing on "short"
often has a shorter root inside it.

### Step 6: First pass — DNS

Build the domain list. For each name pick the two or three extensions worth having, not
all of them. Then:

```bash
python3 scripts/check-availability.py \
  foothold.dev traction.com momentum.app
```

Or for a longer list, one domain per line:

```bash
python3 scripts/check-availability.py \
  --file candidates.txt
```

The path is relative to the folder that holds this SKILL.md, not to your project. If your agent reports `No such file or directory`, it used the wrong working directory: prefix the path with the folder this file was loaded from.

The script runs DNS first because a nameserver record proves a domain is taken in
milliseconds, for free. Most candidates die here, and that is the cheapest place to die.

### Step 7: Second pass — RDAP

The same script does this automatically for any domain that survives DNS. RDAP is the
registry's own record and the official successor to WHOIS. It needs no key and no
account.

Read the three verdicts precisely. They are not interchangeable:

| Verdict | Means | Do |
|---|---|---|
| `TAKEN` | Registered. | Drop it, or check if it is parked and for sale. |
| `LIKELY FREE` | No nameservers and no registry record. | Real candidate. Confirm at a registrar. |
| `UNVERIFIABLE` | The script cannot answer. | Search it at a registrar by hand. |

**`UNVERIFIABLE` is not a soft yes.** It appears for two reasons. Either the TLD runs no
RDAP server — `.io`, `.co`, `.me` and `.sh` do not, so a 404 from them is meaningless —
or the request was rate-limited. Treat it as unknown. Never present it to the founder as
available.

**`LIKELY FREE` is not a purchase.** DNS and RDAP can both lag a fresh registration.
Only a registrar's checkout is final. Say so.

### Step 8: Check the non-domain half of ownable

The domain is necessary and not sufficient. For each surviving name:

1. Search the bare word. Is a larger company using it in an adjacent market? If yes, cut
   it, even with the domain free. You would compete for your own name forever.
2. Check the handle on the **one** channel the founder will actually use.
3. Check for a trademark collision in their category. A name containing another
   company's product name — `Tweet`, `Slack`, `GPT` — is a risk, not just a ceiling.

**Done when** 3-5 names have a confirmed-free domain and no larger brand collision.

---

## Phase 3 — Give the founder what they need to decide

**The founder chooses the name. You do not.** They will say it ten thousand times,
defend it to customers, and live with it for years. That endorsement cannot be
delegated, and a name the founder merely accepted is one they will second-guess
forever.

Your job is to make the decision **easy**, not to make it. A founder stalls when the
options look interchangeable. They stall less when the real differences are sharp and
the cost of each choice is named out loud. Sharpen, then hand over.

### Step 9: Force the comparison

Put the finalists in one table with the three rules that actually differ between them.
Drop the rules where they all score the same — those carry no information.

### Step 10: Run the three tests that break ties

Run the first two yourself before you show the founder anything. They eliminate
finalists, so a name that fails them never reaches a tie-break.

1. **The scope test.** Read the job list from Step 1 back. Does the name cover every
   job, or one of them? Cut any finalist that names a single job of several. A name
   can pass every other test and still describe a third of the product — and it will
   feel apt while doing it, because it *is* apt, for that third.
2. **The copy test.** Read the product's real landing page or pitch, not your summary
   of it. Does the name agree with the voice, or does it name the objection the copy
   works to answer? A tool whose FAQ asks "could this get my account banned?" must not
   be called something that means interrupting.

Then ask the founder directly:

3. **The phone test.** Say the name and the extension aloud. Would a stranger type it
   correctly with no spelling?
4. **The invoice test.** Picture the name on an invoice to their most sceptical customer.
   Which one holds up?
5. **The second-product test.** Name a product they might build in two years. Which name
   still fits?

### Step 11: Hand over the decision

Give the founder, for each finalist:

1. **What it gives and what it costs — both halves, every finalist.** One line each.
   The strength, then the tradeoff: the spelling correction on every podcast, the
   crowded search, the type-in traffic that will reach somebody else. A tradeoff the founder
   discovers later feels like a mistake. One you named up front is a choice they made.
   Never list a con without its pro; that is a verdict wearing a table's clothes.
2. **The one question that separates it from the others.** Not a score. A question only
   they can answer, such as "do you mind explaining the name once per conversation?"
3. **Your reading, offered as a reading.** You may say which you find strongest and
   why — that is useful signal. Say it once, in a sentence, and label it as your view.

**Present factors as factors. Never name one as the deciding criterion.** Saying "X is
what really matters here" is the decision itself wearing the clothes of analysis: it
forecloses the founder's judgment while appearing to inform it, and it is easy to do
by accident after you have removed the explicit recommendation.

List what each option gives and costs, say which way each factor cuts, and leave the
weighting alone. How much a founder cares about brand purity, how often they will say
the name aloud, how much they mind losing type-in traffic, what they intend
to spend later — these are facts about their business and their taste. The scorecard
does not hold them and neither do you.

Then ask which one they want, and stop. Do not repeat the recommendation, do not
re-rank after they answer, and do not argue with their choice. If they pick the one
you scored lowest, that is a legitimate outcome — they know things about their
business, their customers, and their own taste that no scorecard holds.

The one thing to press on: **register it before the session ends.** Availability
decays, and that is a fact about the world rather than an opinion about the name.

### Step 12: Save the decision

Ask the founder how they want the session saved. The default is a Markdown (`.md`) file in a directory the founder names. Do not choose the directory yourself, because the founder decides where their files live. If the founder does not want it saved, skip this step.

Record the finalists, their scores, the chosen name, and the reason. A founder who revisits the name
in six months should get their own reasoning back rather than starting over.

**Done when** one name is chosen, the domain is registered, and the decision is saved or the founder
chose not to save it.

---

## Examples

### Example 1: Founder has an idea and no name

User says: "I'm building a tool that helps freelancers chase unpaid invoices. No idea
what to call it."

Actions:
1. Ask for the outcome. They say "getting paid without feeling like a debt collector."
2. Build pools — outcome: `settled, cleared, paid, current`; object: `ledger, nudge,
   receipt`; action: `chase, remind, follow`; metaphor: `tide, ratchet`.
3. Generate 24 candidates, score them, present the top 12.
4. They react to `Settled` and `Nudge`.
5. Check `settled.app`, `getsettled.com`, `nudge.dev`. `Nudge` turns out to be a larger
   HR product — cut on rule 10 despite the domain being free.
6. Recommend `Settled` on `settled.app`: names the outcome, one syllable of meaning,
   passes the invoice test. Tradeoff — the exact `.com` is parked.

### Example 2: Founder has a list and wants an opinion

User says: "Which of these is best — TaskFlowPro, Cadence, Brisk, or getdone.io?"

Actions:
1. Score all four without checking domains first.
2. `TaskFlowPro` scores 6 — fails memorable, distinctive, and credible. `getdone.io`
   scores 7 — the `get` prefix fails looks-good. Say so plainly and drop both.
3. `Cadence` 16, `Brisk` 17. Check availability on both.
4. `cadence.com` is taken by a large EDA company — cut on rule 10.
5. Recommend `Brisk`. Run the phone test to confirm.

### Example 3: The name is good and the domain is gone

User says: "I want Foothold but foothold.com is taken."

Actions:
1. Confirm the name itself scores well. It does — 17.
2. Check `foothold.dev`, `foothold.app`, `foothold.io`. Report each verdict precisely,
   including any `UNVERIFIABLE`.
3. Explain that exact `.com` is no longer mandatory for software, and that
   `foothold.dev` beats `getfoothold.com` on rule 7.
4. If every extension for one good name is gone, go back to phase 2 with variants.
   But if a whole **territory** is dead — twenty or more names from the same concept
   all taken — that says something about the concept, not about luck. Go back to
   phase 1 and check the pools cover every job. Digging deeper into an exhausted seam
   produces a name that is available because nobody wanted it.

---

## Troubleshooting

### Every candidate comes back `TAKEN`

**Cause:** the names are common single dictionary words in `.com`. Nearly all are
registered.

**Solution:** move to `.dev`, `.app`, or `.ai`, where exact-match single words are still
available. Or shift from single words to two-word compounds, which the scorecard treats
as the practical sweet spot anyway.

### A domain reads `LIKELY FREE` but the registrar says it is taken

**Cause:** DNS and RDAP lag. A domain registered in the last few hours has no
nameservers and may not yet appear in RDAP. Premium and reserved names also show as
unregistered while being unbuyable.

**Solution:** the registrar is correct. This is why the script says "likely" and why
step 7 tells the founder to confirm at checkout.

### Everything on `.io` reads `UNVERIFIABLE`

**Cause:** working as intended. `.io` has no RDAP server, so registration cannot be
confirmed programmatically. The script refuses to guess rather than report a false free.

**Solution:** search those names at a registrar by hand. Do not report them as
available.

### `warning: could not reach IANA bootstrap`

**Cause:** no network, or `data.iana.org` is blocked. Without the bootstrap the script
cannot tell which TLDs it can trust, so it marks everything `UNVERIFIABLE`.

**Solution:** check the connection and re-run. DNS verdicts are still valid, so `TAKEN`
results remain trustworthy.

### `RDAP rate-limited; re-run this one in a minute`

**Cause:** `rdap.org` throttles bursts. The script already pauses between requests and
retries once.

**Solution:** re-run just the affected domains. Keep lists under about 20 domains per
run.

### The founder loves a name that scores 8

**Cause:** the story behind it means something to them. Rule 6 exists for this.

**Solution:** do not overrule them, and do not pretend the score is fine. Name the
specific rules it fails and what each one will cost — spelling questions on every
podcast, or a name that caps the company at one feature. Then let them decide. It is
their company.
