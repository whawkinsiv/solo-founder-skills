"""Parse Claude Code traces into something small enough to judge.

Handles two shapes with the same code:
  * stream-json emitted by `claude -p --output-format stream-json --verbose`
  * session transcripts under ~/.claude/projects/**/*.jsonl

Both wrap Anthropic-format messages in an envelope with a `type` field. The
envelope gains fields between Claude Code versions, so everything here is
written to tolerate keys it has never seen and to skip lines it cannot parse
rather than dying on them.
"""

import json
from pathlib import Path

TOOL_ARG_PREVIEW = 160


def iter_entries(path):
    """Yield one dict per line, silently skipping unparseable lines."""
    with open(path, "r", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(obj, dict):
                yield obj


def blocks(entry):
    """Content blocks of an entry, normalising the string-content shortcut."""
    msg = entry.get("message")
    if not isinstance(msg, dict):
        return []
    content = msg.get("content")
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    if isinstance(content, list):
        return [b for b in content if isinstance(b, dict)]
    return []


def is_tool_result(entry):
    return any(b.get("type") == "tool_result" for b in blocks(entry))


def text_of(entry):
    parts = [b.get("text", "") for b in blocks(entry) if b.get("type") == "text"]
    return "\n".join(p for p in parts if p).strip()


def user_turns(entries):
    """Real user messages, in order. Tool results are excluded: they arrive as
    user-role entries but are the environment talking, not the person."""
    out = []
    for i, e in enumerate(entries):
        if e.get("type") != "user" or is_tool_result(e):
            continue
        t = text_of(e)
        if t:
            out.append({"index": i, "text": t, "timestamp": e.get("timestamp")})
    return out


def tool_calls(entries):
    out = []
    for i, e in enumerate(entries):
        if e.get("type") != "assistant":
            continue
        for b in blocks(e):
            if b.get("type") == "tool_use":
                out.append({"index": i, "name": b.get("name", "?"), "input": b.get("input", {})})
    return out


def result_line(entries):
    """The final `result` event from stream-json, if present."""
    for e in reversed(entries):
        if e.get("type") == "result":
            return e
    return None


def _arg_preview(inp):
    if not isinstance(inp, dict):
        return str(inp)[:TOOL_ARG_PREVIEW]
    for key in ("file_path", "path", "command", "pattern", "url", "prompt", "skill"):
        if key in inp:
            return f"{key}={str(inp[key])[:TOOL_ARG_PREVIEW]}"
    return json.dumps(inp)[:TOOL_ARG_PREVIEW]


def summarize(path, max_chars=12000, text_preview=500, tool_result_chars=160):
    """Compact, ordered account of what happened, for a judge to read.

    Keeps every tool call name and its distinguishing argument, because the
    sequence of actions is usually where a skill failure is visible. Truncates
    prose and tool output hard, because those are rarely where it is and they
    are almost all of the bytes. This is the main lever on judge cost -- the
    summary is what every judge call pays to read.
    """
    entries = list(iter_entries(path))
    lines = []
    for e in entries:
        etype = e.get("type")
        if etype == "system" and e.get("subtype") == "init":
            tools = e.get("tools") or []
            lines.append(f"[init] model={e.get('model','?')} tools={','.join(map(str, tools))[:400]}")
        elif etype == "user" and not is_tool_result(e):
            t = text_of(e)
            if t:
                lines.append(f"[user] {t[:text_preview]}")
        elif etype == "user" and is_tool_result(e):
            for b in blocks(e):
                if b.get("type") != "tool_result":
                    continue
                content = b.get("content")
                if isinstance(content, list):
                    content = " ".join(
                        c.get("text", "") for c in content if isinstance(c, dict)
                    )
                flag = " ERROR" if b.get("is_error") else ""
                lines.append(f"  [result{flag}] {str(content)[:tool_result_chars]}")
        elif etype == "assistant":
            for b in blocks(e):
                if b.get("type") == "text" and b.get("text", "").strip():
                    lines.append(f"[assistant] {b['text'][:text_preview]}")
                elif b.get("type") == "tool_use":
                    lines.append(f"  [tool] {b.get('name','?')}({_arg_preview(b.get('input'))})")
        elif etype == "result":
            lines.append(f"[end] turns={e.get('num_turns','?')} cost_usd={e.get('total_cost_usd','?')}")

    out = "\n".join(lines)
    if len(out) > max_chars:
        head = out[: int(max_chars * 0.6)]
        tail = out[-int(max_chars * 0.35) :]
        out = f"{head}\n\n...[{len(out) - len(head) - len(tail)} chars elided]...\n\n{tail}"
    return out


def mentions(path, needles):
    """True if any needle appears anywhere in the raw file. Deliberately dumb:
    skill loading shows up differently across Claude Code versions, so a raw
    substring search on the skill name and path is more durable than matching
    a specific tool-call shape."""
    needles = [n for n in needles if n]
    if not needles:
        return False
    try:
        blob = Path(path).read_text(errors="replace")
    except OSError:
        return False
    return any(n in blob for n in needles)
