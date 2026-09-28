"""Spend ceilings and a running ledger.

Two things worth knowing about the numbers here. `total_cost_usd` from a run is
a client-side estimate, not your bill, and it is reported whether you are on an
API key or a subscription -- on a subscription it is what the run *would* have
cost, which is still the best available proxy for how hard you are leaning on
your rate limits.

The ledger exists because the expensive failure mode of an audit loop is not one
costly run. It is six iterations of a suite nobody re-estimated, where each round
felt cheap and the total did not.
"""

import json
import threading
import time
from pathlib import Path


class Budget:
    """A ceiling that stops new work rather than reporting the overrun later.

    Charges land as runs finish, so the cap is approximate: work already in
    flight when the ceiling is hit still completes. With a small --jobs that
    overshoot is a run or two.
    """

    def __init__(self, cap_usd=None):
        self.cap = cap_usd
        self.spent = 0.0
        self.skipped = 0
        self._lock = threading.Lock()

    def charge(self, amount):
        if not isinstance(amount, (int, float)):
            return
        with self._lock:
            self.spent += amount

    def exhausted(self):
        if self.cap is None:
            return False
        with self._lock:
            return self.spent >= self.cap

    def skip(self):
        with self._lock:
            self.skipped += 1

    def summary(self):
        if self.cap is None:
            return f"${self.spent:.2f} (no cap set)"
        return (f"${self.spent:.2f} of ${self.cap:.2f} cap"
                + (f", {self.skipped} run(s) skipped after the cap" if self.skipped else ""))


def ledger_path(out_root):
    """One ledger per audit, sitting beside the iteration directories."""
    return Path(out_root).resolve().parent / "spend.jsonl"


def record(out_root, phase, amount, detail=None):
    entry = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "iteration": Path(out_root).name,
        "phase": phase,
        "usd": round(amount, 4) if isinstance(amount, (int, float)) else None,
    }
    if detail:
        entry.update(detail)
    path = ledger_path(out_root)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "a") as fh:
            fh.write(json.dumps(entry) + "\n")
    except OSError:
        pass
    return entry


def total_so_far(out_root):
    """Everything spent on this audit across every iteration and phase."""
    path = ledger_path(out_root)
    if not path.exists():
        return 0.0, []
    entries = []
    for line in path.read_text(errors="replace").splitlines():
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    total = sum(e["usd"] for e in entries if isinstance(e.get("usd"), (int, float)))
    return total, entries


def observed_cost_per_run(out_root):
    """Mean cost of a completed run from any earlier iteration of this audit.

    Projecting from your own suite beats any general figure: cost per run is
    dominated by how much work the cases ask for, which varies enormously.
    """
    parent = Path(out_root).resolve().parent
    costs = []
    for runs_json in sorted(parent.glob("*/runs.json")):
        try:
            for m in json.loads(runs_json.read_text()):
                if m.get("status") == "ok" and isinstance(m.get("cost_usd"), (int, float)):
                    costs.append(m["cost_usd"])
        except (OSError, json.JSONDecodeError):
            continue
    return (sum(costs) / len(costs), len(costs)) if costs else (None, 0)
