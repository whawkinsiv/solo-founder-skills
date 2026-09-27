#!/usr/bin/env python3
"""SessionEnd hook: note that a session used the skill.

Reads the hook payload on stdin, checks whether the session transcript
references the named skill, and appends one line to
~/.claude/skill-audit/<skill>.jsonl.

It stores pointers, not content. The transcript already exists on disk; copying
conversation text into a second location buys nothing and creates a file nobody
remembers agreeing to.

Exits 0 unconditionally. A capture script that can break someone's session is
worse than no capture script.
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return

    skill = os.environ.get("SKILL_AUDIT_SKILL")
    transcript = payload.get("transcript_path")
    if not skill or not transcript:
        return

    path = Path(transcript).expanduser()
    if not path.exists():
        return

    try:
        import trace as tr
        if not tr.mentions(path, [f"skills/{skill}", skill]):
            return
        entries = list(tr.iter_entries(path))
        turns_after = len(tr.user_turns(entries))
    except Exception:
        return

    log = Path.home() / ".claude" / "skill-audit"
    log.mkdir(parents=True, exist_ok=True)
    record = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "skill": skill,
        "session_id": payload.get("session_id"),
        "transcript_path": str(path),
        "cwd": payload.get("cwd"),
        "reason": payload.get("reason"),
        "user_turns": turns_after,
    }
    try:
        with open(log / f"{skill}.jsonl", "a") as fh:
            fh.write(json.dumps(record) + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
