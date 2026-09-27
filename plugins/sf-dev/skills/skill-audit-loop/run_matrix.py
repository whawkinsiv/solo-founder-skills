#!/usr/bin/env python3
"""Run every case against every arm, several times, in isolated directories.

Isolation is the point. Each run gets a fresh copy of the case fixture as its
working directory, and the skill under test is staged into a private directory
passed with --add-dir.

Two ways to get an uncontaminated baseline arm:

  "auth": "api_key" + "bare": true
      --bare skips auto-discovery of hooks, skills, plugins, MCP servers,
      memory and CLAUDE.md. Cleanest isolation, but bare mode never reads
      OAuth credentials, the keychain, or CLAUDE_CODE_OAUTH_TOKEN, so it needs
      ANTHROPIC_API_KEY and bills per token. It also carries a smaller tool set.

  "auth": "subscription" + "bare": false + "config_dir": "~/.claude-audit"
      A dedicated CLAUDE_CONFIG_DIR is a separate Claude Code profile with its
      own credentials, settings, skills, hooks and MCP servers. Log into it
      once with `CLAUDE_CONFIG_DIR=~/.claude-audit claude auth login` and runs
      are both isolated and covered by your subscription. Costs rate limits
      rather than dollars, and competes with your own interactive sessions.

Run --smoke first either way. It executes one case, one arm, one rep and prints
the tool list from the session, which catches both a broken auth setup and a
tool the skill needs but the session doesn't have.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import budget as bg
import trace as tr


def load_suite(path):
    suite = json.loads(Path(path).read_text())
    suite.setdefault("reps", 3)
    suite.setdefault("model", "sonnet")
    suite.setdefault("max_turns", 25)
    suite.setdefault("permission_mode", "acceptEdits")
    suite.setdefault("allowed_tools", "Read,Write,Edit,Bash,Grep,Glob")
    suite.setdefault("timeout_seconds", 900)
    suite.setdefault("bare", True)
    suite.setdefault("auth", "api_key")
    suite.setdefault("config_dir", None)
    suite.setdefault("budget_usd", None)
    suite.setdefault("max_runs", 60)
    if suite["auth"] == "subscription" and suite["bare"]:
        raise SystemExit(
            "auth 'subscription' cannot be combined with bare mode -- bare mode never "
            "reads OAuth credentials, the keychain, or CLAUDE_CODE_OAUTH_TOKEN.\n"
            "Set \"bare\": false and give \"config_dir\" a dedicated profile directory "
            "for isolation instead."
        )
    if not suite.get("arms"):
        raise SystemExit("suite needs an 'arms' list")
    if not suite.get("cases"):
        raise SystemExit("suite needs a 'cases' list")
    return suite


def stage(run_dir, case, arm, suite_dir):
    """Build the run's working directory and skill host from scratch."""
    workdir = run_dir / "workdir"
    if workdir.exists():
        shutil.rmtree(workdir)
    fixture = case.get("fixture")
    if fixture:
        src = (suite_dir / fixture).resolve()
        if not src.exists():
            raise SystemExit(f"fixture not found: {src}")
        shutil.copytree(src, workdir)
    else:
        workdir.mkdir(parents=True)

    host = None
    skill_dir = arm.get("skill_dir")
    if skill_dir:
        src = Path(skill_dir).expanduser().resolve()
        if not src.exists():
            raise SystemExit(f"skill_dir not found: {src}")
        host = run_dir / "skillhost"
        dest = host / ".claude" / "skills" / src.name
        if host.exists():
            shutil.rmtree(host)
        dest.parent.mkdir(parents=True)
        shutil.copytree(src, dest)
    return workdir, host


def build_cmd(suite, case, host):
    cmd = ["claude", "-p", case["prompt"],
           "--output-format", "stream-json", "--verbose",
           "--model", suite["model"],
           "--max-turns", str(suite["max_turns"]),
           "--permission-mode", suite["permission_mode"]]
    if suite["allowed_tools"]:
        cmd += ["--allowedTools", suite["allowed_tools"]]
    if suite["bare"]:
        cmd.append("--bare")
    if host:
        cmd += ["--add-dir", str(host)]
    cmd += list(suite.get("extra_args", []))
    return cmd


def run_env(suite):
    """Environment for the child claude process.

    A dedicated CLAUDE_CONFIG_DIR gives an isolated Claude Code profile --
    its own credentials, settings, skills, hooks and MCP servers -- which is
    how you get a clean baseline arm while still authenticating with a
    subscription. Log into that profile once before the first run:

        CLAUDE_CONFIG_DIR=~/.claude-audit claude auth login

    ANTHROPIC_API_KEY is stripped when the suite asks for subscription auth,
    because a key present in the environment takes precedence over a
    subscription and will silently bill per token instead.
    """
    env = dict(os.environ)
    config_dir = suite.get("config_dir")
    if config_dir:
        env["CLAUDE_CONFIG_DIR"] = str(Path(config_dir).expanduser())
    if suite.get("auth") == "subscription":
        env.pop("ANTHROPIC_API_KEY", None)
    return env


def already_done(run_dir):
    """A finished run is a sunk cost. Never pay for it twice -- interrupted
    suites and re-invocations are common, and silently redoing 20 sessions is
    the single easiest way to waste money here."""
    meta = run_dir / "meta.json"
    if not meta.exists():
        return None
    try:
        prev = json.loads(meta.read_text())
    except json.JSONDecodeError:
        return None
    return prev if prev.get("status") == "ok" else None


def one_run(suite, suite_dir, case, arm, rep, out_root, verbose, budget, force):
    run_dir = out_root / case["id"] / arm["name"] / f"rep{rep}"
    run_dir.mkdir(parents=True, exist_ok=True)

    if not force:
        prev = already_done(run_dir)
        if prev:
            if verbose:
                print(f"  {case['id']}/{arm['name']}/rep{rep}: reusing existing run",
                      flush=True)
            return {**prev, "reused": True}

    if budget.exhausted():
        budget.skip()
        meta = {"case": case["id"], "arm": arm["name"], "rep": rep,
                "status": "skipped_budget", "error": "budget cap reached before this run",
                "session_id": None, "cost_usd": None, "num_turns": None,
                "duration_s": 0, "is_error": None, "tools_available": None,
                "skill_staged": bool(arm.get("skill_dir")), "cmd": []}
        (run_dir / "meta.json").write_text(json.dumps(meta, indent=2))
        return meta

    workdir, host = stage(run_dir, case, arm, suite_dir)
    cmd = build_cmd(suite, case, host)
    trace_path = run_dir / "trace.jsonl"

    started = time.time()
    status, err = "ok", ""
    with open(trace_path, "w") as tf, open(run_dir / "stderr.txt", "w") as ef:
        try:
            proc = subprocess.run(
                cmd, cwd=workdir, stdout=tf, stderr=ef, env=run_env(suite),
                timeout=suite["timeout_seconds"], check=False,
            )
            if proc.returncode != 0:
                status = f"exit{proc.returncode}"
        except subprocess.TimeoutExpired:
            status = "timeout"
        except FileNotFoundError:
            raise SystemExit("`claude` not on PATH -- install the CLI or add it to PATH")
    elapsed = time.time() - started

    entries = list(tr.iter_entries(trace_path))
    result = tr.result_line(entries) or {}
    init = next((e for e in entries if e.get("type") == "system"
                 and e.get("subtype") == "init"), {})
    if not entries:
        status, err = "empty", Path(run_dir / "stderr.txt").read_text()[:400]

    turns = result.get("num_turns")
    if status == "ok" and isinstance(turns, int) and turns >= suite["max_turns"]:
        # A run that hits the turn cap was almost certainly looping. Its output
        # is not evidence about the skill, and re-running the case unchanged
        # buys another one exactly like it.
        status = "turn_capped"

    meta = {
        "case": case["id"], "arm": arm["name"], "rep": rep,
        "status": status, "error": err,
        "session_id": result.get("session_id") or init.get("session_id"),
        "cost_usd": result.get("total_cost_usd"),
        "num_turns": result.get("num_turns"),
        "duration_s": round(elapsed, 1),
        "is_error": result.get("is_error"),
        "tools_available": init.get("tools"),
        "skill_staged": bool(host),
        "cmd": cmd,
    }
    budget.charge(meta["cost_usd"])
    (run_dir / "meta.json").write_text(json.dumps(meta, indent=2))
    if verbose:
        print(f"  {case['id']}/{arm['name']}/rep{rep}: {status} "
              f"{meta['num_turns']} turns ${meta['cost_usd']}", flush=True)
    return meta


def preflight(suite, n_jobs):
    """Warn about the two ways this quietly goes wrong: no auth at all, and
    auth that is not the one you think you are using."""
    def warn(msg):
        print(f"warning: {msg}", file=sys.stderr)

    if suite["auth"] == "api_key":
        if not os.environ.get("ANTHROPIC_API_KEY"):
            warn("auth is 'api_key' but ANTHROPIC_API_KEY is not set")
    else:
        if os.environ.get("ANTHROPIC_API_KEY"):
            warn("ANTHROPIC_API_KEY is set and takes precedence over a subscription; "
                 "it will be stripped from the child environment for these runs")
        if not suite["config_dir"]:
            warn("no config_dir set, so runs inherit your real ~/.claude -- every "
                 "installed skill, hook and MCP server leaks into the baseline arm. "
                 "Point config_dir at a dedicated profile and log into it once with "
                 "`CLAUDE_CONFIG_DIR=<dir> claude auth login`.")
        else:
            path = Path(suite["config_dir"]).expanduser()
            if not path.exists():
                warn(f"{path} does not exist yet -- run "
                     f"`CLAUDE_CONFIG_DIR={path} claude auth login` before the suite, "
                     f"or every run will fail on authentication")
        if n_jobs > 12:
            warn(f"{n_jobs} runs on subscription auth draw down your rate limits and "
                 f"compete with your own sessions; keep --jobs low or use an API key")

    if not suite["bare"] and not suite["config_dir"]:
        warn("bare mode is off and no config_dir is set: the baseline arm is not "
             "actually skill-free. Keep the skill under test out of ~/.claude/skills "
             "at minimum, or the comparison measures nothing.")


def project(out_root, n_jobs, budget_cap):
    """Estimate this iteration from what this suite has actually cost before.

    A general figure per run would be useless: cost is dominated by how much
    work the cases ask for, and that varies by an order of magnitude between
    suites. Your own earlier runs are the only estimate worth quoting.
    """
    per_run, sample = bg.observed_cost_per_run(out_root)
    spent, _ = bg.total_so_far(out_root)
    lines = []
    if spent:
        lines.append(f"this audit has already cost ${spent:.2f} across earlier phases")
    if per_run is None:
        lines.append(f"{n_jobs} runs planned. No cost data yet -- run --smoke first "
                     f"and this becomes a real projection instead of a guess.")
    else:
        proj = per_run * n_jobs
        lines.append(f"{n_jobs} runs planned. Past runs averaged ${per_run:.3f} "
                     f"(n={sample}), so expect roughly ${proj:.2f}.")
        if budget_cap and proj > budget_cap:
            lines.append(f"That is over the ${budget_cap:.2f} budget_usd cap -- the run "
                         f"will stop partway. Cut cases or raise the cap deliberately.")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--suite", required=True)
    ap.add_argument("--out", required=True, help="iteration directory, e.g. runs/iter-1")
    ap.add_argument("--jobs", type=int, default=2,
                    help="parallel runs. Low by default: on a subscription these "
                         "compete with your own sessions for the same rate limits")
    ap.add_argument("--smoke", action="store_true",
                    help="one case, one arm, one rep -- verify auth and tools, and "
                         "establish a cost-per-run figure, before committing to a suite")
    ap.add_argument("--estimate", action="store_true",
                    help="project the cost from earlier runs and exit without spending")
    ap.add_argument("--budget", type=float, default=None,
                    help="override the suite's budget_usd ceiling for this invocation")
    ap.add_argument("--case", default=None, help="run a single case id")
    ap.add_argument("--force", action="store_true",
                    help="re-run runs that already completed (they are reused by default)")
    ap.add_argument("--yes", action="store_true", help="skip the cost confirmation")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    suite_path = Path(args.suite).resolve()
    suite = load_suite(suite_path)
    suite_dir = suite_path.parent
    out_root = Path(args.out).resolve()
    out_root.mkdir(parents=True, exist_ok=True)

    cases = suite["cases"]
    arms = suite["arms"]
    reps = suite["reps"]
    if args.case:
        cases = [c for c in cases if c["id"] == args.case]
        if not cases:
            raise SystemExit(f"no case with id {args.case!r} in the suite")
    if args.smoke:
        cases, arms, reps = cases[:1], arms[:1], 1

    jobs = [(c, a, r) for c in cases for a in arms for r in range(1, reps + 1)]
    cap = args.budget if args.budget is not None else suite["budget_usd"]

    if args.estimate:
        print(project(out_root, len(jobs), cap))
        return

    if len(jobs) > suite["max_runs"] and not args.yes:
        raise SystemExit(
            f"{len(jobs)} runs exceeds max_runs ({suite['max_runs']}). A suite this "
            f"large rarely changes the conclusion and always changes the bill. Cut "
            f"cases, or raise max_runs in the suite if you mean it."
        )

    preflight(suite, len(jobs))
    reusable = sum(1 for c, a, r in jobs
                   if not args.force
                   and already_done(out_root / c["id"] / a["name"] / f"rep{r}"))
    print(f"{len(jobs)} runs: {len(cases)} case(s) x {len(arms)} arm(s) x {reps} rep(s)")
    if reusable:
        print(f"{reusable} already complete and will be reused (--force to redo)")
    print(project(out_root, len(jobs) - reusable, cap))
    if cap:
        print(f"budget ceiling: ${cap:.2f} -- new runs stop once it is reached")

    if not args.yes and not args.smoke:
        prompt = ("these runs draw on your subscription rate limits. continue? [y/N] "
                  if suite["auth"] == "subscription"
                  else "each run is a billed agent session. continue? [y/N] ")
        if input(prompt).strip().lower() != "y":
            sys.exit("aborted")

    budget = bg.Budget(cap)
    metas = []
    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        futures = [pool.submit(one_run, suite, suite_dir, c, a, r, out_root,
                               not args.quiet, budget, args.force)
                   for c, a, r in jobs]
        for f in futures:
            metas.append(f.result())

    (out_root / "runs.json").write_text(json.dumps(metas, indent=2))
    shutil.copy(suite_path, out_root / "suite.json")

    fresh = [m for m in metas if not m.get("reused")]
    costs = [m["cost_usd"] for m in fresh if isinstance(m["cost_usd"], (int, float))]
    if costs:
        bg.record(out_root, "matrix", sum(costs), {"runs": len(fresh)})
    total, _ = bg.total_so_far(out_root)

    bad = [m for m in metas if m["status"] not in ("ok",)]
    print(f"\ndone. {len(metas)} runs ({len(fresh)} new), {len(bad)} not ok")
    print(f"this phase: {budget.summary()} | audit to date: ${total:.2f}")

    capped = [m for m in metas if m["status"] == "turn_capped"]
    if capped:
        print(f"\n{len(capped)} run(s) hit the {suite['max_turns']}-turn cap. Those were "
              f"looping, not working -- their output is not evidence, and re-running the "
              f"case unchanged buys another one just like it. Fix the case or the skill "
              f"before the next iteration.")
    if budget.skipped:
        print(f"{budget.skipped} run(s) skipped at the budget ceiling. Results are "
              f"partial -- do not compare arms until the suite completes.")

    if args.smoke and metas:
        print("\ntools in session:", metas[0].get("tools_available"))
        print("If a tool the skill needs is missing, switch to "
              "auth=subscription + bare=false + config_dir.")
        print("Now run with --estimate to project the full suite from this.")
    for m in bad:
        print(f"  {m['status'].upper()} {m['case']}/{m['arm']}/rep{m['rep']}: "
              f"{(m.get('error') or '')[:200]}")


if __name__ == "__main__":
    main()
