#!/usr/bin/env python3
"""Render the paste-ready build prompt from config/agent.conf.

Emits a PROMPT for the agent, not a script for your machine. Paste the output
into the agent's first message; it configures itself with its own tools.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF = os.path.join(ROOT, "config", "agent.conf")
SPEC = os.path.join(ROOT, "build", "BUILD_SCRIPT.md")


def load_conf(path):
    if not os.path.exists(path):
        sys.exit("no %s - copy config/agent.conf.example and edit it first"
                 % os.path.relpath(path, ROOT))
    conf, key = {}, None
    for raw in open(path):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Z0-9_]+)\s*=\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            conf[key] = [val] if val else []
        elif key and line.startswith((" ", "\t")):
            conf[key].append(line.strip())
    return {k: (v[0] if len(v) == 1 else v) for k, v in conf.items()}


def extract(spec, start, end=None):
    """Pull a fenced code block that follows a heading."""
    i = spec.find(start)
    if i < 0:
        sys.exit("could not find %r in BUILD_SCRIPT.md" % start)
    seg = spec[i:spec.find(end, i)] if end else spec[i:]
    m = re.search(r"```\n(.*?)\n```", seg, re.S)
    if not m:
        sys.exit("no fenced block after %r" % start)
    return m.group(1)


def main():
    c = load_conf(CONF)
    spec = open(SPEC).read()

    need = ["AGENT", "OPERATOR", "TIMEZONE", "LAYER0_ROLES", "CHAMBERS", "ROSTER_PATH"]
    missing = [k for k in need if not c.get(k)]
    if missing:
        sys.exit("config is missing: %s" % ", ".join(missing))

    path = str(c["ROSTER_PATH"]).strip().upper()
    if path not in ("A", "B"):
        sys.exit("ROSTER_PATH must be A or B, got %r" % path)

    n = str(c["CHAMBERS"]).strip()
    if not n.isdigit() or not (1 <= int(n) <= 99):
        sys.exit("CHAMBERS must be 1-99, got %r" % n)

    if path == "A":
        titles = c.get("CHAMBER_LIST") or []
        if isinstance(titles, str):
            titles = [titles]
        if len(titles) != int(n):
            sys.exit("CHAMBERS is %s but CHAMBER_LIST has %d entries - they must "
                     "match exactly, or the agent has to guess which is right"
                     % (n, len(titles)))
        block = extract(spec, "## PATH A", "## PATH B")
        block = block.replace(
            "  01  <discipline>\n  02  <discipline>\n  ...\n  {{N}}  <discipline>",
            "\n".join("  %02d  %s" % (i + 1, t) for i, t in enumerate(titles)))
    else:
        if not c.get("TARGET"):
            sys.exit("ROSTER_PATH is B, so TARGET is required")
        block = extract(spec, "## PATH B — THE MASTER NAMES THE TARGET",
                        "## WHY PATH B NEEDS THE STOP")
        block = block.replace("{{TARGET}}", str(c["TARGET"]))

    body = extract(spec, "## PASTE EVERYTHING BELOW THIS LINE", "## END OF PASTE")
    for k, v in (("{{AGENT}}", c["AGENT"]), ("{{TAGLINE}}", c.get("TAGLINE", "")),
                 ("{{OPERATOR}}", c["OPERATOR"]), ("{{TZ}}", c["TIMEZONE"]),
                 ("{{LAYER0_ROLES}}", c["LAYER0_ROLES"]), ("{{N}}", n),
                 ("{{ROSTER_BLOCK}}", block)):
        body = body.replace(k, str(v))
    body = body.replace("{{N}}", n)          # placeholders inside the injected block

    left = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", body)))
    if left:
        sys.exit("unsubstituted placeholders remain: %s" % ", ".join(left))

    sys.stderr.write(
        "\n%s | %s chambers | PATH %s | %s\n"
        "%d characters (%d bytes UTF-8). Paste everything below into the agent's FIRST message.\n"
        "%s\n\n" % (c["AGENT"], n, path, c["TIMEZONE"], len(body),
           len(body.encode()), "-" * 68))
    print(body)


if __name__ == "__main__":
    main()
