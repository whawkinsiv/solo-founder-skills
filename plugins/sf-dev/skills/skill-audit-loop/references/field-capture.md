# Continuous field capture

The batch loop runs when someone is paying attention. Between rounds, real usage keeps
producing better evidence than anything you can invent — and it disappears unless
something notes it down.

## What gets captured

```bash
python3 scripts/install_hook.py --skill <skill-name> --scope user
```

This registers a `SessionEnd` hook. Claude Code fires `SessionEnd` once when a session
ends and hands the hook a JSON payload on stdin containing `session_id`,
`transcript_path`, `cwd`, and `reason`.

`capture_session.py` checks whether that transcript references the named skill. If it
does, it appends one line to `~/.claude/skill-audit/<skill>.jsonl`:

```json
{"ts":"2026-08-27T14:02:11+00:00","skill":"my-skill","session_id":"...",
 "transcript_path":"/Users/you/.claude/projects/.../abc.jsonl",
 "cwd":"/Users/you/code/thing","reason":"exit","user_turns":7}
```

Pointers, not content. The transcript is already on disk; copying conversation text into
a second location buys nothing and creates a file nobody remembers agreeing to. If the
transcript gets deleted, the pointer goes stale, which is the correct behavior.

The hook is registered `async` and exits 0 unconditionally. A capture script that can
block or break a working session is worse than no capture script.

To remove it: `python3 scripts/install_hook.py --skill <name> --remove`. The installer
merges into `settings.json` rather than replacing it, and backs up the original first.

## Turning captures into cases

```bash
python3 scripts/scan_field.py --skill <name> --days 30 --out cases/field.md
```

`scan_field.py` reads session transcripts directly, so it works whether or not the hook
is installed — the hook just makes the pool easier to find and survives transcript
rotation.

For each session that loaded the skill, it extracts the user turns that came *after*, and
ranks them by how much they look like corrections.

The ranking is a hint, not a classifier. Read the output with the user and sort each turn
into:

- **failure** — the skill should have prevented this. Becomes a case.
- **drift** — the user changed their mind. Not a skill problem.
- **noise** — follow-up, unrelated question, thinking out loud.

That distinction is not recoverable from the text, which is why a person makes it. Getting
it wrong is expensive in a specific way: cases built from drift teach the skill to do
something nobody asked for, and they never stop passing, so they never get removed.

## Why corrections are worth more than invented cases

When someone types "no, I wanted it grouped by month," three things arrive at once: proof
the skill failed, the exact input that triggered the failure, and the correct answer in
the user's own words. Constructed cases have none of that — they test whether the agent
can solve a puzzle you wrote, which is a different question.

The most useful case in most suites is the prompt someone actually typed, in the casual,
underspecified way they actually typed it.

## What this deliberately does not do

The hook does not revise the skill. It would be easy to wire the loop so that every
session ending in a correction triggered an edit, and it would be a bad idea:

- One session is n=1. Agent runs vary enough that a single failure is often noise.
- The evidence is unverified — the "correction" may be the user changing direction.
- Nobody reviewed the edit, so the skill drifts somewhere nobody chose.
- There is no baseline, so there is no way to know whether the edit helped.

Capture is automatic. Revision is deliberate, measured against a suite, and signed off by
a person. That split is the entire design. Anything that collapses it trades a slow honest
loop for a fast one that quietly rots the skill.
