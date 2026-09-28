#!/usr/bin/env python3
"""Find real sessions where a skill was loaded, and pull out what the user said
afterward.

The user turns that follow a skill load are the best evidence available about
whether the skill works, because corrections are free ground truth: the person
told you what the right answer was, in their own words, at the moment it
mattered.

This script extracts and ranks. It does not decide what counts as a failure --
the difference between "you got it wrong" and "I changed my mind" is not
recoverable from the text, so a human reads the output and says which is which.
"""

import argparse
import json
import os
import re
import time
from pathlib import Path

import trace as tr

# Ranking hints only. These bias ordering so the likely corrections surface
# first; they are not a classifier and must not be treated as one.
HINTS = [
    r"\bno[,.]", r"\bnot\b.{0,20}\bwhat i\b", r"\bactually\b", r"\binstead\b",
    r"\bshould have\b", r"\byou (missed|skipped|forgot|ignored)\b",
    r"\bagain\b", r"\bwrong\b", r"\bdon'?t\b", r"\bstop\b", r"\bwhy did you\b",
    r"\bi said\b", r"\bredo\b", r"\btry again\b", r"\bthat'?s not\b",
]
HINT_RE = [re.compile(h, re.I) for h in HINTS]


def session_files(roots, days):
    cutoff = time.time() - days * 86400
    seen = set()
    for root in roots:
        root = Path(root).expanduser()
        if not root.exists():
            continue
        for path in root.rglob("*.jsonl"):
            if path in seen:
                continue
            try:
                if path.stat().st_mtime < cutoff:
                    continue
            except OSError:
                continue
            seen.add(path)
            yield path


def score(text):
    return sum(1 for r in HINT_RE if r.search(text))


def scan(skill, skill_dir, roots, days, max_sessions):
    needles = [f"skills/{skill}", skill]
    if skill_dir:
        needles.append(str(skill_dir))

    found = []
    for path in session_files(roots, days):
        if not tr.mentions(path, needles):
            continue
        entries = list(tr.iter_entries(path))
        if not entries:
            continue

        # Where in the session did the skill first show up?
        first = None
        for i, e in enumerate(entries):
            if any(n in json.dumps(e, default=str) for n in needles):
                first = i
                break
        if first is None:
            continue

        after = [t for t in tr.user_turns(entries) if t["index"] > first]
        cwd = next((e.get("cwd") for e in entries if e.get("cwd")), None)
        found.append({
            "session": str(path),
            "mtime": time.strftime("%Y-%m-%d %H:%M", time.localtime(path.stat().st_mtime)),
            "cwd": cwd,
            "turns_after_skill": len(after),
            "candidates": sorted(
                ({"score": score(t["text"]), "text": t["text"]} for t in after),
                key=lambda c: -c["score"],
            )[:6],
        })
        if len(found) >= max_sessions:
            break

    found.sort(key=lambda s: -max([c["score"] for c in s["candidates"]] or [0]))
    return found


def to_markdown(skill, found):
    out = [f"# Field evidence for `{skill}`", ""]
    if not found:
        out += [
            "No local sessions in the window referenced this skill.",
            "",
            "That is itself a finding: either the skill is not being triggered in real use,",
            "or it has not been used recently. Check triggering before auditing output quality.",
        ]
        return "\n".join(out)

    out += [
        f"{len(found)} session(s) loaded this skill. For each, the user turns that came",
        "*after* the skill was loaded are listed, most suspicious first.",
        "",
        "Mark each one: **failure** (the skill should have prevented this), **drift**",
        "(the user changed their mind), or **noise**. Only failures become cases.",
        "",
    ]
    for i, s in enumerate(found, 1):
        out += [f"## {i}. {s['mtime']} — {s['cwd'] or 'unknown dir'}", ""]
        out += [f"`{s['session']}`", "", f"{s['turns_after_skill']} user turn(s) after the skill loaded.", ""]
        if not s["candidates"]:
            out += ["_No user turns after the skill loaded — one-shot session._", ""]
        for c in s["candidates"]:
            marker = "!" * min(c["score"], 3) or "-"
            text = c["text"].strip().replace("\n", "\n  > ")
            out += [f"- [{marker}] > {text}", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--skill", required=True, help="skill name, e.g. agent-citability-audit")
    ap.add_argument("--skill-dir", default=None, help="installed path, improves matching")
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--max-sessions", type=int, default=25)
    ap.add_argument("--roots", nargs="*", default=None,
                    help="transcript roots (default: ~/.claude/projects and the audit log dir)")
    ap.add_argument("--out", default=None, help="write markdown here")
    ap.add_argument("--json-out", default=None)
    args = ap.parse_args()

    roots = args.roots or [
        os.path.expanduser("~/.claude/projects"),
        os.path.expanduser("~/.config/claude/projects"),
    ]
    found = scan(args.skill, args.skill_dir, roots, args.days, args.max_sessions)
    md = to_markdown(args.skill, found)

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(md)
        print(f"wrote {args.out}")
    else:
        print(md)
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(found, indent=2))
        print(f"wrote {args.json_out}")


if __name__ == "__main__":
    main()
