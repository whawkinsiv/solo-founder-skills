#!/usr/bin/env python3
"""Register (or remove) the SessionEnd capture hook for a skill.

Merges into the existing settings file rather than replacing it, and prints the
diff before writing. Never edit someone's settings.json silently -- it holds
their permissions and other hooks, and a clobbered one is a bad afternoon.
"""

import argparse
import json
import shutil
from pathlib import Path

EVENT = "SessionEnd"


def settings_path(scope):
    if scope == "user":
        return Path.home() / ".claude" / "settings.json"
    return Path.cwd() / ".claude" / "settings.json"


def build_entry(skill, script):
    return {
        "hooks": [{
            "type": "command",
            "command": f"SKILL_AUDIT_SKILL={skill} python3 {script}",
            "async": True,
        }]
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--skill", required=True)
    ap.add_argument("--scope", choices=["user", "project"], default="user")
    ap.add_argument("--remove", action="store_true")
    ap.add_argument("--yes", action="store_true")
    args = ap.parse_args()

    script = (Path(__file__).parent / "capture_session.py").resolve()
    path = settings_path(args.scope)
    settings = {}
    if path.exists():
        try:
            settings = json.loads(path.read_text())
        except json.JSONDecodeError:
            raise SystemExit(f"{path} is not valid JSON -- fix it before running this")

    hooks = settings.setdefault("hooks", {})
    entries = hooks.setdefault(EVENT, [])
    marker = f"SKILL_AUDIT_SKILL={args.skill} "
    entries[:] = [
        e for e in entries
        if not any(marker in (h.get("command") or "") for h in e.get("hooks", []))
    ]
    if not args.remove:
        entries.append(build_entry(args.skill, script))
    if not entries:
        hooks.pop(EVENT, None)
    if not hooks:
        settings.pop("hooks", None)

    print(f"{path}:\n{json.dumps(settings.get('hooks', {}), indent=2)}")
    if not args.yes and input("write this? [y/N] ").strip().lower() != "y":
        raise SystemExit("aborted")

    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        shutil.copy(path, path.with_suffix(".json.bak"))
        print(f"backed up to {path.with_suffix('.json.bak')}")
    path.write_text(json.dumps(settings, indent=2) + "\n")
    print("written. run /hooks in Claude Code to confirm it registered.")


if __name__ == "__main__":
    main()
