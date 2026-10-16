#!/usr/bin/env python3
"""Compute the weighted total for the is-this-an-app matrix.

The matrix is in references/matrix.md. This script does arithmetic only. It
makes no decision about the form. Claude reads the directional signals in the
matrix and decides the form.

Two dimensions count in reverse: agent substitutability and distribution-context
fit. A high score on either one argues against a standalone app. The script
counts them as (5 - score). All other dimensions count as scored.

The total is 0-100. A higher total means the idea leans more toward a
standalone app.

Usage:
    python3 score.py --interface 1 --agent 5 --visual 1 --workflow 2 \\
        --background 0 --state 1 --integration 0 --device 1 --judgment 2 \\
        --collaboration 0 --latency 1 --distribution 5 --extensibility 0 --audit 0
"""
import argparse
import sys

# key, label, weight (percent). The weights add up to 100.
DIMENSIONS = [
    ("interface", "Interface essentiality", 15),
    ("agent", "Agent substitutability", 10),
    ("visual", "Visual / spatial dependence", 10),
    ("workflow", "Workflow ownership", 10),
    ("background", "Background / autonomous execution", 9),
    ("state", "Durable state requirement", 8),
    ("integration", "External integration dependence", 8),
    ("device", "Device / environment dependence", 7),
    ("judgment", "Human judgment / intervention frequency", 5),
    ("collaboration", "Collaboration / permission complexity", 5),
    ("latency", "Latency / interaction loop", 4),
    ("distribution", "Distribution-context fit", 4),
    ("extensibility", "Extensibility requirement", 3),
    ("audit", "Audit / control requirement", 2),
]
REVERSED = {"agent", "distribution"}


def main():
    p = argparse.ArgumentParser(description="Weighted total for the is-this-an-app matrix (14 dimensions, 0-5 each).")
    for key, label, weight in DIMENSIONS:
        p.add_argument(f"--{key}", type=int, required=True, metavar="0-5", help=f"{label} ({weight}%%)")
    a = p.parse_args()

    scores = {k: getattr(a, k) for k, _, _ in DIMENSIONS}
    bad = sorted(k for k, v in scores.items() if not 0 <= v <= 5)
    if bad:
        p.error(f"scores must be 0-5; out of range: {', '.join(bad)}")

    print("| Dimension | Weight | Score | Counted as | Points |")
    print("|---|---:|---:|---:|---:|")
    total = 0.0
    for key, label, weight in DIMENSIONS:
        counted = 5 - scores[key] if key in REVERSED else scores[key]
        points = weight * counted / 5
        total += points
        mark = " (reversed)" if key in REVERSED else ""
        print(f"| {label} | {weight}% | {scores[key]}/5 | {counted}/5{mark} | {points:.1f} |")
    print(f"| **Total** | 100% | | | **{total:.0f}/100** |")


if __name__ == "__main__":
    sys.exit(main())
