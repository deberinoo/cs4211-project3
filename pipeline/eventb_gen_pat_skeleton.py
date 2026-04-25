import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


def load_multi_json(text: str) -> List[Dict[str, Any]]:
    """Parse multiple JSON objects concatenated in one file."""
    dec = json.JSONDecoder()
    i, n = 0, len(text)
    objs = []
    while i < n:
        while i < n and text[i].isspace():
            i += 1
        if i >= n:
            break
        obj, j = dec.raw_decode(text, i)
        objs.append(obj)
        i = j
    return objs


def find_machine(objs: List[Dict[str, Any]]) -> Dict[str, Any]:
    machines = [o for o in objs if isinstance(o, dict) and "MACHINE" in o]
    if not machines:
        raise ValueError("No MACHINE object found in JSON.")
    return machines[0]


def sanitize_event_name(name: str) -> str:
    return "".join(ch if ch.isalnum() or ch == "_" else "_" for ch in name)


def gen_event_loop_csp(machine_name: str, events: List[str], per_line: int = 3) -> str:
    """
    Generate a readable multi-line CSP event-scheduler loop.
    per_line controls how many choices appear per line.
    """
    events = [sanitize_event_name(e) for e in events]
    choices = [f"{e} -> System()" for e in events]

    # Build multi-line with [] prefixes
    lines: List[str] = []
    for i, ch in enumerate(choices):
        prefix = "    " if i == 0 else " [] "
        # Put each choice on its own line (most readable)
        lines.append(f"{prefix}{ch}")

    body = "\n".join(lines) if lines else "    Skip"

    return f"""// Auto-generated PAT CSP skeleton for {machine_name}
// Style: generic event-scheduler loop (control-flow template)

System() =
(
{body}
);

#assert System() deadlockfree;
"""


def gen_checks_csp(events: List[str], k: int = 3) -> str:
    events = [sanitize_event_name(e) for e in events]
    sample = events[:k]
    lines = [
        "// Auto-generated check templates",
        "#assert System() deadlockfree;"
    ]
    for e in sample:
        lines.append(f"#assert System() |= <> {e};")
    lines.append("")
    lines.append("// Note: <> event means 'eventually on all executions', not mere reachability.")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="Event-B JSON file (may contain multiple JSON objects).")
    ap.add_argument("--outdir", default=".", help="Output directory.")
    ap.add_argument("--k", type=int, default=3, help="Number of sample events for liveness templates.")
    args = ap.parse_args()

    text = Path(args.input).read_text(encoding="utf-8")
    objs = load_multi_json(text)
    m = find_machine(objs)

    machine_name = m.get("MACHINE", "unknown_machine")
    raw_events = [e.get("event_name", "") for e in m.get("EVENTS", [])]
    events = [e for e in raw_events if e and e != "INITIALISATION"]

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    model_path = outdir / f"{machine_name}_skeleton.csp"
    checks_path = outdir / f"{machine_name}_checks.csp"

    model_path.write_text(gen_event_loop_csp(machine_name, events), encoding="utf-8")
    checks_path.write_text(gen_checks_csp(events, k=args.k), encoding="utf-8")

    print(f"Wrote: {model_path}")
    print(f"Wrote: {checks_path}")


if __name__ == "__main__":
    main()