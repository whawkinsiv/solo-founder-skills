#!/usr/bin/env python3
"""Aggregate scored runs into report.md and results.csv.

Reports quality next to cost on purpose. A skill that lifts pass rate five
points while doubling tokens and turns is usually a bad trade, and nobody
notices unless the two numbers sit in the same table.
"""

import argparse
import csv
import json
import statistics as st
from collections import defaultdict
from pathlib import Path

import budget as bg


def mean_sd(values):
    vals = [v for v in values if isinstance(v, (int, float))]
    if not vals:
        return None, None
    return st.mean(vals), (st.stdev(vals) if len(vals) > 1 else 0.0)


def fmt(value, digits=2, prefix=""):
    return "-" if value is None else f"{prefix}{value:.{digits}f}"


def aggregate(scored):
    arms = sorted({s["arm"] for s in scored})
    checks = []
    for s in scored:
        for c in s["checks"]:
            if c["id"] not in checks:
                checks.append(c["id"])

    per_check = defaultdict(lambda: defaultdict(list))       # check -> arm -> verdicts
    per_case_check = defaultdict(lambda: defaultdict(list))  # (case,check) -> arm -> verdicts
    per_arm = defaultdict(lambda: defaultdict(list))         # arm -> metric -> values

    for s in scored:
        for metric in ("cost_usd", "num_turns", "duration_s"):
            per_arm[s["arm"]][metric].append(s.get(metric))
        per_arm[s["arm"]]["ok"].append(1 if s["status"] == "ok" else 0)
        for c in s["checks"]:
            per_check[c["id"]][s["arm"]].append(c["verdict"])
            per_case_check[(s["case"], c["id"])][s["arm"]].append(c["verdict"])
    return arms, checks, per_check, per_case_check, per_arm


def rate(verdicts):
    graded = [v for v in verdicts if v in ("pass", "fail")]
    if not graded:
        return None
    return sum(1 for v in graded if v == "pass") / len(graded)


def pct(value):
    return "-" if value is None else f"{100 * value:.0f}%"


def build(scored, previous=None, skill_path=None, runs_root=None):
    arms, checks, per_check, per_case_check, per_arm = aggregate(scored)
    lines = ["# Skill audit report", ""]
    lines += [f"{len(scored)} runs across {len(arms)} arm(s): {', '.join(arms)}.", ""]

    if skill_path and Path(skill_path).exists():
        n = len(Path(skill_path).read_text().splitlines())
        lines += [f"SKILL.md is **{n} lines**. Track this across iterations: a loop like",
                  "this ratchets toward bloat, and context spent is context lost.", ""]

    # The delta column tracks the arm that carries the skill. Comparing the
    # baseline across iterations is nearly useless -- it is the same no-skill
    # run every time, and any movement in it is noise you should not react to.
    staged = [s["arm"] for s in scored if s.get("skill_staged")]
    primary = max(set(staged), key=staged.count) if staged else arms[0]

    prev_rates = {}
    if previous:
        try:
            prev_scored = json.loads(Path(previous).read_text())
            _, _, prev_check, _, _ = aggregate(prev_scored)
            prev_rates = {c: {a: rate(v) for a, v in arms_d.items()}
                          for c, arms_d in prev_check.items()}
        except (OSError, json.JSONDecodeError):
            pass

    lines += ["## Pass rate by check", ""]
    header = ["check"] + arms + ([f"delta ({primary})"] if prev_rates else [])
    lines += ["| " + " | ".join(header) + " |",
              "|" + "---|" * len(header)]
    for check in checks:
        row = [f"`{check}`"] + [pct(rate(per_check[check].get(a, []))) for a in arms]
        if prev_rates:
            now = rate(per_check[check].get(primary, []))
            was = prev_rates.get(check, {}).get(primary)
            row.append("-" if now is None or was is None
                       else f"{100 * (now - was):+.0f} pts")
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")

    lines += ["## Cost of each arm", "",
              "| arm | runs ok | mean cost | mean turns | mean seconds |",
              "|---|---|---|---|---|"]
    for arm in arms:
        m = per_arm[arm]
        cost, _ = mean_sd(m["cost_usd"])
        turns, turns_sd = mean_sd(m["num_turns"])
        secs, _ = mean_sd(m["duration_s"])
        ok = f"{sum(m['ok'])}/{len(m['ok'])}"
        turn_str = "-" if turns is None else f"{turns:.1f} ± {turns_sd:.1f}"
        lines.append(f"| {arm} | {ok} | {fmt(cost, 3, '$')} | {turn_str} | {fmt(secs, 0)} |")
    lines.append("")

    lines += ["## Per case", "",
              "| case | check | " + " | ".join(arms) + " |",
              "|---|---|" + "---|" * len(arms)]
    for (case, check), by_arm in sorted(per_case_check.items()):
        row = [case, f"`{check}`"] + [pct(rate(by_arm.get(a, []))) for a in arms]
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")

    fails = [(s, c) for s in scored for c in s["checks"] if c["verdict"] == "fail"]
    lines += ["## Failure rationales", ""]
    if not fails:
        lines += ["No failures. If that happened on the first iteration, the checks are",
                  "too weak -- tighten them before believing the skill is finished.", ""]
    else:
        lines += ["Group these into clusters with a shared cause. One hypothesis and one",
                  "edit per cluster, then re-run the whole suite.", ""]
        by_check = defaultdict(list)
        for s, c in fails:
            by_check[c["id"]].append((s, c))
        for check, items in by_check.items():
            lines += [f"### `{check}` — {len(items)} failure(s)", ""]
            for s, c in items[:6]:
                lines.append(f"- **{s['case']} / {s['arm']} / rep{s['rep']}** — "
                             f"{c['rationale'].strip()}")
            lines.append("")

    unclear = [(s, c) for s in scored for c in s["checks"] if c["verdict"] == "unclear"]
    if unclear:
        lines += ["## Unclear", "",
                  "These could not be graded. Usually the criterion is ambiguous rather "
                  "than the run being bad -- fix the check, not the skill.", ""]
        for s, c in unclear[:10]:
            lines.append(f"- **{s['case']} / {s['arm']} / rep{s['rep']} / `{c['id']}`** — "
                         f"{c['rationale'].strip()[:300]}")
        lines.append("")

    capped = [s for s in scored if s.get("status") == "turn_capped"]
    skipped = [s for s in scored if s.get("status") == "skipped_budget"]
    if capped or skipped:
        lines += ["## Runs that did not produce evidence", ""]
        if capped:
            lines += [f"**{len(capped)} run(s) hit the turn cap.** Those were looping, "
                      f"not working. Their checks are graded but the results are not "
                      f"evidence about the skill, and re-running the case unchanged "
                      f"buys another one exactly like it — fix the case or the skill "
                      f"first.", ""]
            for s in capped[:6]:
                lines.append(f"- {s['case']} / {s['arm']} / rep{s['rep']}")
            lines.append("")
        if skipped:
            lines += [f"**{len(skipped)} run(s) skipped at the budget ceiling.** Pass "
                      f"rates below are computed over what actually ran, so the arms "
                      f"are not comparable until the suite completes.", ""]

    lines += ["## Spend", ""]
    matrix = sum(s["cost_usd"] for s in scored
                 if isinstance(s.get("cost_usd"), (int, float)))
    judges = sum(s.get("judge_cost_usd") or 0 for s in scored)
    lines += [f"- runs: ${matrix:.2f} across {len(scored)} run(s)",
              f"- judges: ${judges:.2f}"]
    total, entries = bg.total_so_far(runs_root) if runs_root else (0, [])
    if total:
        rounds = len({e.get("iteration") for e in entries})
        lines += [f"- **this audit to date: ${total:.2f}** across {rounds} iteration(s)"]
    lines += ["",
              "If the running total is climbing faster than the pass rates, stop and "
              "ask whether the remaining failures are worth it. Two rounds without "
              "improvement is the signal to stop, and it usually arrives before the "
              "budget does.", ""]

    lines += ["## How to read this", "",
              "- Arms within noise of each other: the skill is not doing anything. "
              "Consider deleting it rather than tuning it.",
              "- Baseline ahead of the skill: the skill is hurting. Read those traces "
              "before editing anything.",
              "- A check failing in every arm: the task may be wrong, not the skill.",
              "- Repetitions disagreeing with each other: that check is measuring noise. "
              "Either the criterion is vague or the behaviour is genuinely unstable.", ""]
    return "\n".join(lines)


def write_csv(scored, path):
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["case", "arm", "rep", "check", "type", "verdict",
                    "cost_usd", "num_turns", "duration_s", "status", "rationale"])
        for s in scored:
            for c in s["checks"]:
                w.writerow([s["case"], s["arm"], s["rep"], c["id"], c.get("type", ""),
                            c["verdict"], s.get("cost_usd"), s.get("num_turns"),
                            s.get("duration_s"), s.get("status"),
                            (c.get("rationale") or "").replace("\n", " ")])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs", required=True)
    ap.add_argument("--out", default=None)
    ap.add_argument("--previous", default=None, help="previous iteration's scores.json")
    ap.add_argument("--skill-md", default=None, help="path to SKILL.md, to track its length")
    args = ap.parse_args()

    runs_root = Path(args.runs).resolve()
    scored = json.loads((runs_root / "scores.json").read_text())
    md = build(scored, args.previous, args.skill_md, runs_root)

    out = Path(args.out) if args.out else runs_root / "report.md"
    out.write_text(md)
    csv_path = out.with_name("results.csv")
    write_csv(scored, csv_path)
    print(f"wrote {out}\nwrote {csv_path}")


if __name__ == "__main__":
    main()
