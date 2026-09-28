#!/usr/bin/env python3
"""Audit every skill against the Agent Skills spec and this repo's portability rules.

Replaces the hand-maintained "Known gaps" table that used to sit in SKILL-STANDARD.md.
A stored count goes stale silently. This measures on demand instead.

    python3 scripts/audit.py           # report, exit 1 on any FAIL
    python3 scripts/audit.py --quiet   # only FAILs and the summary

Spec: https://agentskills.io/specification
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# The Agent Skills spec allows exactly these frontmatter keys. Anything else is a
# Claude Code extension and makes the skill non-portable: claude.ai and the Skills
# API reject unknown keys outright.
SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}

DESC_MAX = 1024        # spec hard cap
LINE_SOFT = 500        # spec recommendation
TOKEN_SOFT = 5000      # spec recommendation for the body

# A skill body that names one vendor's variables cannot run in another agent.
VENDOR_PATTERNS = [
    (r"\$\{?CLAUDE_PLUGIN_ROOT\}?", "$CLAUDE_PLUGIN_ROOT is Claude Code only"),
    (r"\$\{?CLAUDE_SKILL_DIR\}?", "$CLAUDE_SKILL_DIR is Claude Code only"),
    (r"^\s*when_to_use\s*:", "when_to_use is not in the spec"),
]


def tracked_skills():
    out = subprocess.run(
        ["git", "ls-files", "plugins/*/skills/*/SKILL.md"],
        cwd=REPO, capture_output=True, text=True, check=True).stdout
    paths = [REPO / line for line in out.split() if line]
    # Include a skill that exists but is not committed yet, so work in progress is
    # audited too rather than silently skipped.
    for p in sorted(REPO.glob("plugins/*/skills/*/SKILL.md")):
        if p not in paths:
            paths.append(p)
    return sorted(paths)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None


def field(fm, key):
    m = re.search(rf"^{key}:\s*(.*?)(?=\n[A-Za-z0-9_-]+:|\Z)", fm, re.S | re.M)
    return m.group(1).strip().strip("\"'") if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true", help="only FAILs and the summary")
    args = ap.parse_args()

    fails, warns = [], []
    counts = {"scripts": 0, "references": 0, "assets": 0}
    skills = tracked_skills()

    for skill_md in skills:
        d = skill_md.parent
        rel = d.relative_to(REPO)
        name = d.name
        text = skill_md.read_text()

        fm = frontmatter(text)
        if fm is None:
            fails.append(f"{rel}: no YAML frontmatter")
            continue

        # --- spec: name ---
        declared = field(fm, "name")
        if not declared:
            fails.append(f"{rel}: no name field")
        elif declared != name:
            fails.append(f"{rel}: name '{declared}' does not match its directory")
        elif not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
            fails.append(f"{rel}: name is not 1-64 chars of kebab-case")

        # --- spec: description ---
        desc = field(fm, "description")
        if not desc:
            fails.append(f"{rel}: no description field")
        elif len(desc) > DESC_MAX:
            fails.append(f"{rel}: description is {len(desc)} chars, over the {DESC_MAX} cap")

        # --- portability: frontmatter keys ---
        extra = {k for k in re.findall(r"^([A-Za-z0-9_-]+):", fm, re.M)} - SPEC_FIELDS
        if extra:
            fails.append(f"{rel}: non-spec frontmatter {sorted(extra)} breaks portability")

        # --- portability: vendor-locked bodies ---
        for pattern, why in VENDOR_PATTERNS:
            if re.search(pattern, text, re.M):
                fails.append(f"{rel}: {why}")

        # --- spec recommendations ---
        n_lines = len(text.splitlines())
        n_tokens = int(len(text.split()) / 0.75)
        if n_lines > LINE_SOFT:
            warns.append(f"{rel}: {n_lines} lines, over the {LINE_SOFT}-line guidance")
        if n_tokens > TOKEN_SOFT:
            warns.append(f"{rel}: ~{n_tokens:,} tokens, over the {TOKEN_SOFT:,} guidance")

        # --- support files must be reachable ---
        for f in sorted(d.rglob("*")):
            if f.is_dir() or f.name == "SKILL.md" or "__pycache__" in f.parts:
                continue
            ref = f.relative_to(d).as_posix()
            if ref not in text and f.name not in text:
                # A file another support file calls is still reachable.
                siblings = [g for g in d.rglob("*")
                            if g.is_file() and g != f and g.suffix in (".md", ".py")]
                if not any(f.name in g.read_text(errors="ignore") for g in siblings):
                    warns.append(f"{rel}: {ref} is never referenced, so it never loads")

        for sub in counts:
            if (d / sub).is_dir():
                counts[sub] += 1

    if not args.quiet:
        for w in warns:
            print(f"WARN  {w}")
    for f in fails:
        print(f"FAIL  {f}")

    print()
    print(f"{len(skills)} skills audited")
    print(f"  scripts/ {counts['scripts']}   references/ {counts['references']}   "
          f"assets/ {counts['assets']}")
    print(f"  {len(fails)} fail, {len(warns)} warn")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
