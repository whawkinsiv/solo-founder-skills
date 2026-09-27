#!/usr/bin/env python3
"""Score a validation and return the verdict.

The six dimensions come from references/scorecard.md. Each is 1-5, scored from
evidence the founder actually has. A dimension with no evidence scores 1 and is
reported as a gap - it is never guessed at or averaged.

Why this is a script and not a paragraph of instructions: summing six numbers and
looking up a band is arithmetic, and arithmetic done in prose goes wrong quietly.
A verdict that does not match its own score is worse than no verdict, because the
founder cannot tell which half to trust.

Usage:
    python3 scripts/score.py --frequency 4 --intensity 3 --willingness 1 \\
                             --market 3 --advantage 5 --solutions 3
    python3 scripts/score.py ... --json
"""
import argparse
import json
import sys

DIMENSIONS = [
    ("frequency", "Problem frequency"),
    ("intensity", "Problem intensity"),
    ("willingness", "Willingness to pay"),
    ("market", "Market size"),
    ("advantage", "Your unique advantage"),
    ("solutions", "Current solutions"),
]

# Best to worst. Order matters - the willingness cap compares rank.
BANDS = [
    (25, 30, "Build", "Strong go. Scope the MVP."),
    (18, 24, "One more experiment", "Promising. Name the weakest dimension and design a test for it."),
    (12, 17, "Pivot the angle", "The problem may be real but this framing isn't working. Change audience or wedge, re-test."),
    (6, 11, "No-go", "Find a different problem. Archive the brief and move on."),
]
RANK = {b[2]: i for i, b in enumerate(BANDS)}


def band_for(total):
    for lo, hi, name, meaning in BANDS:
        if lo <= total <= hi:
            return name, meaning
    raise ValueError(f"total {total} outside 6-30")


def score(values):
    total = sum(values[k] for k, _ in DIMENSIONS)
    verdict, meaning = band_for(total)
    notes = []

    # Cap rule: no payment evidence means the verdict cannot be better than
    # "One more experiment", however strong everything else looks. Every other
    # dimension can be perfect and the business still fails if nobody pays.
    if values["willingness"] == 1 and RANK[verdict] < RANK["One more experiment"]:
        notes.append(
            f"Capped from '{verdict}' to 'One more experiment': willingness to pay "
            "scored 1, so there is no payment evidence yet."
        )
        verdict, meaning = "One more experiment", dict((b[2], b[3]) for b in BANDS)["One more experiment"]

    # Advisory: a strong unique advantage is a tiebreaker, not a foundation.
    if values["advantage"] >= 4 and total < 18:
        notes.append(
            "Unique advantage is strong but the total is low. Expertise does not "
            "rescue a weak idea - do not let it pull the verdict up."
        )

    gaps = [label for k, label in DIMENSIONS if values[k] == 1]
    weakest = min(DIMENSIONS, key=lambda d: values[d[0]])

    return {
        "scores": {k: values[k] for k, _ in DIMENSIONS},
        "total": total,
        "max": 30,
        "verdict": verdict,
        "meaning": meaning,
        "weakest_dimension": weakest[1],
        "weakest_score": values[weakest[0]],
        "gaps": gaps,
        "notes": notes,
    }


def main():
    p = argparse.ArgumentParser(description="Score a validation (six dimensions, 1-5 each).")
    for key, label in DIMENSIONS:
        p.add_argument(f"--{key}", type=int, required=True, metavar="1-5", help=label)
    p.add_argument("--json", action="store_true", help="machine-readable output")
    a = p.parse_args()

    values = {k: getattr(a, k) for k, _ in DIMENSIONS}
    bad = [k for k, v in values.items() if not 1 <= v <= 5]
    if bad:
        p.error(f"scores must be 1-5; out of range: {', '.join(sorted(bad))}")

    r = score(values)

    if a.json:
        print(json.dumps(r, indent=2))
        return

    width = max(len(label) for _, label in DIMENSIONS)
    for key, label in DIMENSIONS:
        print(f"  {label.ljust(width)}  {values[key]}/5")
    print(f"  {'TOTAL'.ljust(width)}  {r['total']}/30")
    print()
    print(f"  Verdict: {r['verdict']}")
    print(f"  {r['meaning']}")
    print(f"  Weakest: {r['weakest_dimension']} ({r['weakest_score']}/5) - aim the next experiment here.")
    if r["gaps"]:
        print(f"  No evidence yet for: {', '.join(r['gaps'])}")
    for n in r["notes"]:
        print(f"  Note: {n}")


if __name__ == "__main__":
    sys.exit(main())
