#!/usr/bin/env bash
# Install Solo Founder Skills into a coding agent that reads the Agent Skills format.
#
# Claude Code users do not need this script. Use the plugin marketplace instead:
#   /plugin marketplace add whawkinsiv/solo-founder-skills
#   /plugin install sf-strategy@solo-founder-skills-marketplace
#
# Every other agent (Codex CLI, Gemini CLI, Cursor, Copilot) reads a plain folder of
# skills. This script copies the skills you ask for into the folder your agent watches.
#
# Usage:
#   ./install.sh --codex  sf-strategy sf-copy    -> ~/.codex/skills/
#   ./install.sh --agents sf-strategy            -> ./.agents/skills/
#   ./install.sh --claude sf-strategy            -> ~/.claude/skills/
#   ./install.sh --dest ~/somewhere sf-strategy  -> a folder you name
#   ./install.sh --list                          -> show plugins and their skills

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST=""
TARGET=""
PLUGINS=()

# Codex loads every installed skill's name and description at startup. That list is
# capped at 2% of the model's context window, or 8,000 characters when the window is
# unknown. Past the cap it shortens descriptions and can drop skills without telling
# you much. All 61 skills total about 25,000 characters, so install the plugins you
# need rather than everything.
BUDGET=8000

usage() { sed -n '2,17p' "$0" | sed 's/^# \{0,1\}//'; exit "${1:-0}"; }

list_plugins() {
  printf '%-14s %s\n' "PLUGIN" "SKILLS"
  for d in "$REPO"/plugins/*/; do
    local name skills
    name="$(basename "$d")"
    skills="$(find "$d/skills" -maxdepth 1 -mindepth 1 -type d -exec basename {} \; 2>/dev/null | sort | tr '\n' ' ')"
    printf '%-14s %s\n' "$name" "$skills"
  done
  echo
  echo "sf-dev holds skill-authoring tools. Founders do not need it."
}

# Sum name + description length for the skills about to be installed.
describe_cost() {
  python3 - "$@" <<'PY'
import re, sys
from pathlib import Path
total = 0
for skill in sys.argv[1:]:
    p = Path(skill) / "SKILL.md"
    if not p.is_file():
        continue
    m = re.match(r"^---\n(.*?)\n---\n", p.read_text(), re.S)
    if not m:
        continue
    d = re.search(r"description:\s*(.*?)(?=\n[a-z-]+:|\Z)", m.group(1), re.S)
    total += len(Path(skill).name) + (len(d.group(1).strip().strip('"\'')) if d else 0)
print(total)
PY
}

while [ $# -gt 0 ]; do
  case "$1" in
    --codex)  TARGET="Codex CLI";  DEST="$HOME/.codex/skills" ;;
    --agents) TARGET="agents";     DEST="./.agents/skills" ;;
    --claude) TARGET="Claude Code"; DEST="$HOME/.claude/skills" ;;
    --dest)   shift; [ $# -gt 0 ] || { echo "--dest needs a path" >&2; exit 1; }
              TARGET="custom"; DEST="$1" ;;
    --list)   list_plugins; exit 0 ;;
    -h|--help) usage 0 ;;
    -*)       echo "Unknown option: $1" >&2; usage 1 >&2 ;;
    *)        PLUGINS+=("$1") ;;
  esac
  shift
done

[ -n "$DEST" ] || { echo "Pick a target: --codex, --agents, --claude, or --dest PATH" >&2; usage 1 >&2; }
[ "${#PLUGINS[@]}" -gt 0 ] || { echo "Name at least one plugin. Run --list to see them." >&2; exit 1; }

# Collect the skill folders before copying anything, so a bad plugin name fails early.
SKILLS=()
for plugin in "${PLUGINS[@]}"; do
  dir="$REPO/plugins/$plugin/skills"
  [ -d "$dir" ] || { echo "No such plugin: $plugin. Run --list to see them." >&2; exit 1; }
  while IFS= read -r s; do SKILLS+=("$s"); done \
    < <(find "$dir" -maxdepth 1 -mindepth 1 -type d | sort)
done

cost="$(describe_cost "${SKILLS[@]}")"
echo "Installing ${#SKILLS[@]} skills from ${#PLUGINS[@]} plugin(s) into $DEST"
echo "Startup description cost: ${cost} characters"
if [ "$cost" -gt "$BUDGET" ]; then
  cat >&2 <<EOF

Warning: ${cost} characters is over the ${BUDGET}-character floor some agents use for
the startup skill list. Codex shortens descriptions past that point and can leave skills
out. If your agent stops finding a skill, install fewer plugins at once.

EOF
fi

mkdir -p "$DEST"
for s in "${SKILLS[@]}"; do
  name="$(basename "$s")"
  rm -rf "$DEST/$name"
  cp -R "$s" "$DEST/$name"
  echo "  $name"
done

echo
echo "Done. Start a new session in your agent so it picks up the new skills."
echo "To remove one: rm -rf \"$DEST/<skill-name>\""
