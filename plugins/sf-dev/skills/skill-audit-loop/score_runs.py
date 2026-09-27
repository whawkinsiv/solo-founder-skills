#!/usr/bin/env python3
"""Score every run against the case's checks.

Two kinds of check:

  rule  -- a shell command run in the finished working directory. Exit 0 passes.
           Deterministic, free, and the only checks you can fully trust. Use one
           wherever one is possible.
  judge -- a question answered by a `claude -p` call reading a summary of the
           run's trace. For behaviour no rule can express: whether a prerequisite
           was actually read, whether steps happened in the documented order,
           whether a claim was verified before being written.

Scoring is where audit budgets quietly go. 30 runs x 4 judges is 120 model calls,
each reading a trace, and that can cost more than the runs it is grading. Three
guardrails, all on by default:

  * All of a run's judge checks go in ONE call, not one call each.
  * Runs already scored against the same checks are skipped, not re-billed.
  * Judges default to a small model, with per-check escalation for criteria that
    genuinely need judgement rather than retrieval.

Judges see the trace summary and the question. They do not see the arm name or
the other arms' results. Every judge returns a rationale, not a verdict alone --
a bare pass/fail tells you a check failed but not which sentence of the skill to
fix, and the rationale is the whole reason this loop can propose an edit.

The batching trade-off, stated plainly: criteria graded together can bleed into
each other, where a bad impression of the run colours every verdict. The prompt
pushes against it and the cost saving is roughly 4x. Set "batch_judges": false in
the suite if a criterion is load-bearing enough that you want it graded alone.
"""

import argparse
import hashlib
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import budget as bg
import trace as tr

BATCH_SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "verdicts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "verdict": {"type": "string", "enum": ["pass", "fail", "unclear"]},
                    "rationale": {"type": "string"},
                },
                "required": ["id", "verdict", "rationale"],
            },
        }
    },
    "required": ["verdicts"],
})

PROMPT = """You are grading one run of a coding agent against {n} independent criteria.

Below is a condensed record of everything the agent did: user turns, its own
messages, and every tool call in order with the arguments that identify it.

Grade each criterion separately and on its own terms. They are unrelated -- a
failure on one is not evidence about another, and a general impression of the run
must not decide them all the same way. Judge only what each criterion asks. If the
record does not contain enough to decide one, return "unclear" for that one rather
than guessing.

Your rationale is the part that matters. Say what in the record decided it --
which turn, which tool call, what was missing. "Did not follow instructions" is
useless. "Wrote report.md at turn 4 without ever reading config.yaml" is what
someone needs to fix the underlying instructions.

CRITERIA:
{criteria}

RECORD:
{record}

Return JSON: {{"verdicts": [{{"id": ..., "verdict": "pass"|"fail"|"unclear", "rationale": ...}}]}}
with exactly one entry per criterion id above."""


def fingerprint(checks):
    """Identity of the check set, so a rerun can tell "already graded this" from
    "the criteria changed and this needs regrading"."""
    payload = json.dumps(
        [[c.get("id"), c.get("type"), c.get("cmd"), c.get("ask"), c.get("model")]
         for c in checks], sort_keys=True)
    return hashlib.sha256(payload.encode()).hexdigest()[:12]


def run_rule(check, workdir):
    try:
        proc = subprocess.run(check["cmd"], shell=True, cwd=workdir,
                              capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        return {"verdict": "fail", "rationale": "rule check timed out"}
    out = ((proc.stdout or "") + (proc.stderr or "")).strip()[:600]
    return {
        "verdict": "pass" if proc.returncode == 0 else "fail",
        "rationale": f"exit {proc.returncode}" + (f": {out}" if out else ""),
    }


def call_judge(checks, record, model, timeout):
    """One call, N criteria. Returns {check_id: outcome} and the call's cost."""
    criteria = "\n".join(f"- id: {c['id']}\n  question: {c['ask']}" for c in checks)
    prompt = PROMPT.format(n=len(checks), criteria=criteria, record=record)
    cmd = ["claude", "-p", prompt, "--bare", "--output-format", "json",
           "--json-schema", BATCH_SCHEMA, "--model", model]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True,
                              timeout=timeout, check=False)
    except subprocess.TimeoutExpired:
        return {c["id"]: {"verdict": "unclear", "rationale": "judge timed out"}
                for c in checks}, 0.0
    except FileNotFoundError:
        raise SystemExit("`claude` not on PATH")

    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {c["id"]: {"verdict": "unclear",
                          "rationale": f"judge output unparseable: {proc.stdout[:160]}"}
                for c in checks}, 0.0

    cost = payload.get("total_cost_usd") or 0.0
    structured = payload.get("structured_output") or {}
    by_id = {}
    for v in structured.get("verdicts", []):
        if isinstance(v, dict) and v.get("id"):
            by_id[v["id"]] = {"verdict": v.get("verdict", "unclear"),
                              "rationale": v.get("rationale", "")}
    out = {c["id"]: by_id.get(c["id"], {
        "verdict": "unclear",
        "rationale": "judge returned no verdict for this criterion",
    }) for c in checks}
    return out, cost


def judge_groups(judges, default_model, batch):
    """Group judge checks into calls. One call per model normally; one call per
    check when batching is off."""
    if not batch:
        return [(c.get("model") or default_model, [c]) for c in judges]
    groups = {}
    for c in judges:
        groups.setdefault(c.get("model") or default_model, []).append(c)
    return list(groups.items())


def score_run(run_dir, case, defaults, force):
    meta = json.loads((run_dir / "meta.json").read_text())
    checks = [c for c in case.get("checks", [])
              if not c.get("arms") or meta["arm"] in c["arms"]]
    fp = fingerprint(checks)

    scores_path = run_dir / "scores.json"
    if not force and scores_path.exists():
        try:
            prev = json.loads(scores_path.read_text())
            if prev.get("checks_fingerprint") == fp:
                return {**prev, "reused": True}, 0.0
        except json.JSONDecodeError:
            pass

    results, spend = [], 0.0

    # Rules first: free and deterministic.
    for check in checks:
        if check.get("type") == "rule":
            results.append({"id": check["id"], "type": "rule",
                            **run_rule(check, run_dir / "workdir")})

    judges = [c for c in checks if c.get("type", "judge") != "rule"]
    if judges and meta["status"] in ("ok", "turn_capped"):
        record = tr.summarize(run_dir / "trace.jsonl",
                              max_chars=defaults["trace_chars"],
                              tool_result_chars=defaults["result_chars"])
        if not record.strip():
            for c in judges:
                results.append({"id": c["id"], "type": "judge",
                                "verdict": "unclear", "rationale": "trace was empty"})
        else:
            for model, group in judge_groups(judges, defaults["model"],
                                             defaults["batch"]):
                outcomes, cost = call_judge(group, record, model, defaults["timeout"])
                spend += cost or 0.0
                for c in group:
                    results.append({"id": c["id"], "type": "judge", "model": model,
                                    **outcomes[c["id"]]})
    elif judges:
        for c in judges:
            results.append({"id": c["id"], "type": "judge", "verdict": "unclear",
                            "rationale": f"run status was {meta['status']}"})

    order = {c["id"]: i for i, c in enumerate(checks)}
    results.sort(key=lambda r: order.get(r["id"], 999))
    scored = {**meta, "checks": results, "checks_fingerprint": fp,
              "judge_cost_usd": round(spend, 5)}
    scores_path.write_text(json.dumps(scored, indent=2))
    return scored, spend


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--suite", required=True)
    ap.add_argument("--runs", required=True)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--judge-model", default=None,
                    help="default model for judges (suite judge_model, else haiku)")
    ap.add_argument("--judge-timeout", type=int, default=300)
    ap.add_argument("--trace-chars", type=int, default=None,
                    help="trace summary budget per run; the main lever on judge cost")
    ap.add_argument("--no-batch", action="store_true",
                    help="one call per criterion instead of one per run. ~4x the cost; "
                         "use when a criterion must not be influenced by its neighbours")
    ap.add_argument("--rescore", action="store_true",
                    help="regrade runs already scored against the same checks")
    ap.add_argument("--budget", type=float, default=None,
                    help="stop grading once judge calls have cost this much")
    args = ap.parse_args()

    suite = json.loads(Path(args.suite).read_text())
    cases = {c["id"]: c for c in suite["cases"]}
    defaults = {
        "model": args.judge_model or suite.get("judge_model", "haiku"),
        "timeout": args.judge_timeout,
        "trace_chars": args.trace_chars or suite.get("judge_trace_chars", 12000),
        "result_chars": suite.get("judge_result_chars", 160),
        "batch": suite.get("batch_judges", True) and not args.no_batch,
    }
    runs_root = Path(args.runs).resolve()

    targets = []
    for meta_path in sorted(runs_root.glob("*/*/rep*/meta.json")):
        case_id = json.loads(meta_path.read_text())["case"]
        if case_id in cases:
            targets.append((meta_path.parent, cases[case_id]))
    if not targets:
        raise SystemExit(f"no runs found under {runs_root}")

    n_judges = sum(1 for _, c in targets
                   for ch in c.get("checks", []) if ch.get("type", "judge") != "rule")
    print(f"scoring {len(targets)} runs, default judge model {defaults['model']}")
    if defaults["batch"]:
        print(f"{n_judges} judge criteria, batched to roughly one call per run "
              f"instead of {n_judges}")
    else:
        print(f"{n_judges} judge criteria, batching off -- that is {n_judges} calls")

    cap = bg.Budget(args.budget if args.budget is not None
                    else suite.get("judge_budget_usd"))
    scored = []

    def work(target):
        if cap.exhausted():
            cap.skip()
            return None
        result, spend = score_run(target[0], target[1], defaults, args.rescore)
        cap.charge(spend)
        return result

    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        for result in pool.map(work, targets):
            if result:
                scored.append(result)

    (runs_root / "scores.json").write_text(json.dumps(scored, indent=2))
    if cap.spent:
        bg.record(runs_root, "judges", cap.spent, {"runs": len(scored)})
    total, _ = bg.total_so_far(runs_root)

    reused = sum(1 for s in scored if s.get("reused"))
    unclear = sum(1 for s in scored for c in s["checks"] if c["verdict"] == "unclear")
    print(f"\nwrote {runs_root / 'scores.json'}")
    if reused:
        print(f"{reused} run(s) reused from a previous scoring pass (--rescore to redo)")
    print(f"judges: {cap.summary()} | audit to date: ${total:.2f}")
    if cap.skipped:
        print(f"{cap.skipped} run(s) left ungraded at the judge budget ceiling. "
              f"Pass rates are computed over what was graded, so treat them as partial.")
    if unclear:
        print(f"{unclear} check(s) came back unclear. Read those rationales before "
              f"trusting the pass rates -- usually the criterion is ambiguous rather "
              f"than the run being bad. If a small judge model returns unclear often, "
              f"set \"model\" on that specific check instead of raising it for all.")


if __name__ == "__main__":
    main()
