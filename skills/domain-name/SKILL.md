---
name: domain-name
description: "Use this skill when the founder needs to name a product or company and find a domain: 'name my product,' 'what should I call it,' 'help me pick a domain,' 'is this a good name,' 'my domain is taken,' 'check if this name is available,' or a pasted list of candidate names. Scores names against ten rules, then checks domain availability with DNS and RDAP. Not for pointing DNS at a host once the name is chosen (use go-live) or for writing page copy (use landing-page)."
metadata:
  version: 2.0.0
---

# Naming a product and getting the domain

A name can fail in two ways: it is a bad name, or it is a good name you cannot have. Judge the concept first. Test availability second.

## Optimize in this order

```
great concept  →  great name  →  acceptable domain
```

**Never the reverse.** The failure is subtle: one pattern starts returning free domains, so you generate more of that pattern, and within two rounds availability is choosing the concept. The symptom is a list where most names share a word or a shape.

A great name with an acceptable domain beats a mediocre name with a perfect one. `Foothold` on `getfoothold.com` works. `socialengagementautomation.com` is still a dead name. When a strong name's exact domain is gone, try other suffixes in the acceptable set and the `get`/`use` + one word wrapper (rules 7 and 10 in the scorecard) before dropping the name. Drop a name for being weak, never for being taken.

**Read `references/scorecard.md` before scoring anything.** It holds the ten rules, the test for each, and worked examples.

## Phase 1: Generate

No availability checks in this phase, except the obvious names in Step 3.

### Step 1: Get the raw material

Ask for what is missing, in one message:
1. **Every distinct job the product does, numbered.** Do not compress them to one sentence. A three-job product described in one sentence loses two jobs, and the surviving job becomes the whole naming territory by accident.
2. **What unifies those jobs.** The unifying idea is the naming territory, not any single job.
3. **The outcome the customer gets.** `Traction` works because it names what an early product wants.
4. Who it is for.
5. Words they like, and words they have ruled out.
6. Whether `.com` is a hard requirement.

Read ABOUT-ME.md and the project README first, if they exist. Ask only what they do not answer.

### Step 2: Build word pools

Write the pools before any names. Names invented directly cluster around one idea.

**First, one pool per job, plus a unifying pool.** For a tool that plans meals, builds the list, and orders the food: Job 1 `plan, menu, course`; Job 2 `list, tally, basket`; Job 3 `order, deliver, stock`; **Unifying `pantry, larder, table, kitchen`**. The name usually comes from the unifying pool.

Then cut across with lexical pools: **Outcome** (streak, momentum, foothold), **Object** (ledger, anchor, compass), **Action** (tally, mark, keep), **Metaphor** (ratchet, flywheel, cairn).

Check that some word in the pools touches **every** job. If every word serves one job, rebuild the pools. This is the most common way this skill fails.

### Step 3: Produce 20–30 candidates

Work in this order:

1. **Obvious names first.** Build a dozen plain compounds from the product's own nouns: who it serves plus what it hands them. Check these domains now. If one is free and literally true, you may be finished. Reaching past an available, accurate, plain name is the most expensive mistake in this skill.
2. **Then at least eight adjacent concepts.** An ordinary word one step from the product, picked for sound and a faint link: Stripe, Notion, Linear. This is the highest-yield kind and the easiest to skip.
3. **Then the other kinds:** outcome words (Traction), coined words that are spelled right on first hearing (Calendly, Typefully), and metaphors (Buffer).

Coined is not misspelled. `Flickr` and `Lyft` are respellings and score 0 on rule 2. Coin by adding a clean suffix or by fusing two real words, never by dropping vowels. A plain compound earns its place only when it names the product's actual output (`Dropbox`), not a category (`GrowthPlatform`).

### Step 4: Score and present

Score each name on the ten rules. Present the top 12 as a table, highest first. **Every row has both a pro and a con.** A row with only a con is a rejection made for the founder. A row with only a pro is a sales pitch.

Cover every kind during generation. Do not cap any kind in the results. If one pattern takes eight of the top twelve after a fair fight, say so: that is a finding about the product.

**Done when** the founder has a scored list and has said which names they react to.

## Phase 2: Shortlist and check availability

### Step 5: Cut to 5–8

Keep the names the founder reacted to, plus any scoring 16 or more. Drop anything under 12. For each survivor, try two variants that fix its weakest rule.

### Step 6: Run the checker

Pick the two or three suffixes worth having for each name, from the acceptable set. Then run the script. The path is relative to the folder that holds this SKILL.md:

```bash
python3 scripts/check-availability.py foothold.dev traction.com momentum.app
python3 scripts/check-availability.py --file candidates.txt
```

The script checks DNS first (a nameserver record proves a domain is taken, fast and free), then the registry's RDAP record for anything that survives. Keep lists under about 20 domains per run.

| Verdict | Means | Do |
|---|---|---|
| `TAKEN` | Registered | Drop it, or check whether it is parked and for sale |
| `LIKELY FREE` | No nameservers and no registry record | Real candidate. Confirm at a registrar checkout |
| `UNVERIFIABLE` | The script cannot tell | Search it at a registrar by hand. Never present it as available |

`UNVERIFIABLE` appears when a suffix has no RDAP server (`.io`, `.co`, `.me`, `.sh`) or when the request was rate-limited. `LIKELY FREE` is not a purchase: DNS and RDAP can lag a fresh registration, and premium names look free but are not for sale.

### Step 7: Check the rest of "ownable"

For each survivor:
1. Search the bare word. If a larger company uses it in a nearby market, cut it, even with the domain free.
2. Check the handle on the **one** channel the founder will use.
3. Check for a trademark clash in their category. A name containing another product's name (`Tweet`, `Slack`, `GPT`) is a risk.

**Done when** 3–5 names have a likely-free domain and no larger brand collision.

## Phase 3: The founder decides

**The founder chooses the name. You do not.** They will say it ten thousand times and defend it to customers. Your job is to make the decision easy, not to make it.

### Step 8: Run the cutting tests yourself

1. **Scope test.** Read the job list from Step 1 back. Cut any finalist that names only one job of several. It will feel apt, because it is apt for that one job.
2. **Copy test.** Read the product's real landing page or pitch. Cut any name that names the objection the copy works to answer.

### Step 9: Hand over

Put the finalists in one table with the three rules that actually differ between them. Then give, for each finalist:
1. What it gives and what it costs, in one line each.
2. The one question that separates it from the others, which only the founder can answer. For example: "Do you mind explaining the name once per conversation?"
3. Optionally, your own reading, said once and labeled as your view.

Ask the founder to run three tests: say it aloud (would a stranger spell it?), picture it on an invoice to their most skeptical customer, and imagine it on a product they might build in two years.

Present factors as factors. Never call one factor "what really matters": that is the decision, dressed as analysis. Then ask which they want, and stop. Do not re-rank after they answer. If they pick the name you scored lowest, that is a valid outcome.

Press on one thing: **register it before the session ends.** Availability decays.

### Step 10: Save the decision

Ask how the founder wants the session saved. The default is a Markdown file in a folder the founder names. Record the finalists, scores, the chosen name, and the reason.

## Examples

**No name yet.** "A tool that helps freelancers chase unpaid invoices." The outcome is "getting paid without feeling like a debt collector." Build the pools, generate 24, present 12. The founder reacts to `Settled` and `Nudge`. `Nudge` is a larger HR product, so cut it on rule 10. Present `Settled` (`settled.app`) and the other finalists with their pros, cons, and separating questions. The founder picks.

**A list for an opinion.** "TaskFlowPro, Cadence, Brisk, or getdone.io?" Score all four before checking domains. `TaskFlowPro` fails memorable, distinctive, and credible. `getdone.io` sits on a country-code suffix outside the acceptable set, and "done" alone is not distinctive. `cadence.com` belongs to a large company, so cut it on rule 10. Present the survivors with pros and cons. The founder decides.

**Good name, domain gone.** "I want Foothold but foothold.com is taken." Confirm the name scores well. Check `foothold.dev`, `foothold.app`, and `getfoothold.com`. Prefer the exact match on another suffix over the wrapped `.com`. If twenty names from one concept are all taken, the territory is exhausted. Go back to Step 2 and check that the pools cover every job.

## Troubleshooting

- **Every candidate is `TAKEN`:** the names are common single words on `.com`. Move to another suffix in the acceptable set, or to two-word compounds.
- **`LIKELY FREE`, but the registrar says taken:** the registrar is right. DNS and RDAP lag, and reserved names look free.
- **Everything on `.io` is `UNVERIFIABLE`:** working as intended. `.io` has no RDAP server. Check by hand.
- **`could not reach IANA bootstrap`:** no network. `TAKEN` results from DNS are still valid.
- **`RDAP rate-limited`:** re-run only those domains a minute later.
- **The founder loves a name that scores 8:** do not overrule them. Name the rules it fails and what each one will cost, then let them decide.
