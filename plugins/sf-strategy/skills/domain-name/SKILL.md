---
name: domain-name
description: "Use this skill when the user needs to name a product or company and find a domain for it. Also use when the user says 'name my product,' 'what should I call it,' 'help me pick a domain,' 'is this a good name,' 'find me a domain,' 'my domain is taken,' 'check if this name is available,' or pastes a list of candidate names for an opinion. Scores names against ten rules, then verifies domain availability with DNS and RDAP. Do NOT use for buying a domain or pointing DNS at your host once the name is chosen (use deploy), for visual brand identity such as colors, logos, or typography (use brand-identity-generator), for positioning and messaging (use niche-advantage), or for writing headlines and page copy (use copywriting)."
metadata:
  version: 1.0.0
---

# Naming a product and getting the domain

Naming fails in two different ways, and they need different work. A name can be a bad
name, or it can be a good name you cannot have. Judge the concept first, then test
availability. Running availability checks on a weak shortlist wastes the founder's time
on names they should not want.

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

1. What the product does, in one sentence.
2. **The outcome the customer gets.** This matters more than the features. `Traction`
   works because it names what an early-stage product wants.
3. Who it is for.
4. Any word they already like, or any they have ruled out.
5. Whether `.com` is a hard requirement.

If `ABOUT-ME.md` or `MY-ICP.md` exist in the project, read them first and ask only for
what they do not answer.

### Step 2: Build word pools

Write out four pools before you write any names. Names invented directly tend to cluster
around one idea.

| Pool | Contains | Example for a habit tracker |
|---|---|---|
| Outcome | What the customer ends up with | streak, momentum, traction, foothold |
| Object | Concrete things in the domain | ledger, anchor, compass, thread |
| Action | What the user does | tally, mark, log, keep |
| Metaphor | One conceptual leap away | ratchet, flywheel, cairn, tide |

### Step 3: Produce 20-30 candidates

Cover a range deliberately: single concrete words, two-word compounds, and a few
metaphors. Do not pad the list with variants of one idea.

### Step 4: Score and present

Score each on the ten rules. Present the top 12 as a table, highest first:

```
| Name | Score | Strongest | Weakest |
|---|---|---|---|
| Foothold | 17 | distinctive, expandable | common word, check search |
```

Then say which three you would keep and why. Founders need a call, not a menu.

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
python3 "$CLAUDE_PLUGIN_ROOT/skills/domain-name/scripts/check-availability.py" \
  foothold.dev traction.com momentum.app
```

Or for a longer list, one domain per line:

```bash
python3 "$CLAUDE_PLUGIN_ROOT/skills/domain-name/scripts/check-availability.py" \
  --file candidates.txt
```

If `$CLAUDE_PLUGIN_ROOT` is unset, use the path this SKILL.md was loaded from.

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

## Phase 3 — Decide on one

A founder who has reached three good options will stall. Your job is to end it.

### Step 9: Force the comparison

Put the finalists in one table with the three rules that actually differ between them.
Drop the rules where they all score the same — those carry no information.

### Step 10: Run the three tests that break ties

Ask the founder directly:

1. **The phone test.** Say the name and the extension aloud. Would a stranger type it
   correctly with no spelling?
2. **The invoice test.** Picture the name on an invoice to their most sceptical customer.
   Which one holds up?
3. **The second-product test.** Name a product they might build in two years. Which name
   still fits?

### Step 11: Recommend one

Name your pick, give the one reason that decided it, and name what they give up. Do not
present a ranked list and leave the decision open — that is how a founder ends up
holding three domains and no name.

Then tell them to register it now, before the session ends. Availability decays.

### Step 12: Archive the decision

Write the session to:

```
${SOLO_FOUNDER_CONFIG:-$HOME/.config/solo-founder}/domain-name/archive/<YYYY-MM-DD>-<slug>.md
```

Record the finalists, their scores, the chosen name, and the reason. Append a line to
`INDEX.md` in the same directory. A founder who revisits the name in six months should
get their own reasoning back rather than starting over.

If `${BUSINESS_BRAIN:-$HOME/business-brain}/` exists, write the chosen name and domain
to it following that repo's `AGENTS.md` — append, set `status: draft` and `updated:` to
today. Skip silently if it is absent. Never fail a run over it.

**Done when** one name is chosen, the domain is registered, and the decision is archived.

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
4. If every extension is gone, go back to phase 2 with variants — not to phase 1.

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
