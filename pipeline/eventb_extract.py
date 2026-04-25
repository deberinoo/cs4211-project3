import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional


def load_multiple_json_objects(text: str) -> List[Dict[str, Any]]:
    """
    Event-B JSON dumps in the assignment sometimes contain multiple JSON objects
    concatenated together. This parser reads them sequentially.
    """
    decoder = json.JSONDecoder()
    objs = []
    idx = 0
    n = len(text)
    while idx < n:
        # skip whitespace
        while idx < n and text[idx].isspace():
            idx += 1
        if idx >= n:
            break
        obj, end = decoder.raw_decode(text, idx)
        if not isinstance(obj, dict):
            raise ValueError("Top-level JSON object is not a dictionary.")
        objs.append(obj)
        idx = end
    return objs


def fmt_list(xs: List[str]) -> str:
    return ", ".join(xs) if xs else "-"


def md_escape(s: str) -> str:
    # keep it simple; most predicates are fine in markdown as-is
    return s.replace("\n", " ").strip()


def render_context(ctx: Dict[str, Any]) -> str:
    name = ctx.get("CONTEXT", "(unknown)")
    extends = ctx.get("EXTENDS", [])
    sets_ = ctx.get("SETS", [])
    consts = ctx.get("CONSTANTS", [])
    axioms = ctx.get("AXIOMS", [])

    out = []
    out.append(f"### Context: `{name}`")
    out.append("")
    out.append(f"- Extends: {fmt_list(extends)}")
    out.append(f"- Sets: {fmt_list(sets_)}")
    out.append(f"- Constants: {fmt_list(consts)}")
    out.append("")
    if axioms:
        out.append("**Axioms**")
        out.append("")
        out.append("| Label | Predicate |")
        out.append("|---|---|")
        for a in axioms:
            out.append(f"| `{a.get('label_name','')}` | {md_escape(a.get('predicate',''))} |")
        out.append("")
    return "\n".join(out)


def render_machine(m: Dict[str, Any], max_events: Optional[int] = None) -> str:
    name = m.get("MACHINE", "(unknown)")
    refines = m.get("REFINES", [])
    sees = m.get("SEES", [])
    variables = m.get("VARIABLES", [])
    invariants = m.get("INVARIANTS", [])
    events = m.get("EVENTS", [])

    out = []
    out.append(f"### Machine: `{name}`")
    out.append("")
    out.append(f"- Refines: {fmt_list(refines)}")
    out.append(f"- Sees: {fmt_list(sees)}")
    out.append("")

    # Variables
    out.append("**Variables**")
    out.append("")
    out.append("| Variable |")
    out.append("|---|")
    for v in variables:
        out.append(f"| `{v}` |")
    out.append("")

    # Invariants
    if invariants:
        out.append("**Invariants (requirements candidates)**")
        out.append("")
        out.append("| Label | Predicate |")
        out.append("|---|---|")
        for inv in invariants:
            out.append(f"| `{inv.get('label_name','')}` | {md_escape(inv.get('predicate',''))} |")
        out.append("")

    # Initialisation (special event)
    init_event = None
    for e in events:
        if e.get("event_name") == "INITIALISATION":
            init_event = e
            break

    if init_event:
        out.append("**Initialisation (from `INITIALISATION` event)**")
        out.append("")
        out.append("| Action | Assignment |")
        out.append("|---|---|")
        for act in init_event.get("THEN", []):
            out.append(f"| `{act.get('label_name','')}` | {md_escape(act.get('assignment',''))} |")
        out.append("")

    # Events
    out.append("**Events (guards and actions)**")
    out.append("")
    out.append("| Event | Params (ANY) | Guards (WHERE) | Actions (THEN) |")
    out.append("|---|---|---|---|")

    event_list = [e for e in events if e.get("event_name") != "INITIALISATION"]
    if max_events is not None:
        event_list = event_list[:max_events]

    for e in event_list:
        ename = e.get("event_name", "")
        params = e.get("ANY", [])
        guards = e.get("WHERE", [])
        actions = e.get("THEN", [])

        guard_str = "<br>".join(
            [f"`{g.get('label_name','')}`: {md_escape(g.get('predicate',''))}" for g in guards]
        ) if guards else "-"

        act_str = "<br>".join(
            [f"`{a.get('label_name','')}`: {md_escape(a.get('assignment',''))}" for a in actions]
        ) if actions else "-"

        out.append(f"| `{ename}` | {md_escape(fmt_list(params))} | {guard_str} | {act_str} |")

    if max_events is not None and len([e for e in events if e.get("event_name") != "INITIALISATION"]) > max_events:
        out.append("")
        out.append(f"> Note: Only the first {max_events} events are shown. Re-run without `--max-events` to export all events.")

    out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Extract Event-B JSON (contexts/machines) into Markdown tables.")
    ap.add_argument("input", help="Path to Event-B JSON file (may contain multiple JSON objects).")
    ap.add_argument("-o", "--output", help="Output markdown file path. Default: <input>_extraction.md")
    ap.add_argument("--max-events", type=int, default=None, help="Optional limit for number of events shown (excluding INITIALISATION).")
    args = ap.parse_args()

    in_path = Path(args.input)
    text = in_path.read_text(encoding="utf-8")
    objs = load_multiple_json_objects(text)

    contexts = [o for o in objs if "CONTEXT" in o]
    machines = [o for o in objs if "MACHINE" in o]

    out_lines = []
    out_lines.append(f"# Event-B Extraction Output: `{in_path.name}`")
    out_lines.append("")
    out_lines.append("This file is auto-generated from the provided Event-B JSON artefacts.")
    out_lines.append("")

    if contexts:
        out_lines.append("## Contexts")
        out_lines.append("")
        for c in contexts:
            out_lines.append(render_context(c))
            out_lines.append("")

    if machines:
        out_lines.append("## Machines")
        out_lines.append("")
        for m in machines:
            out_lines.append(render_machine(m, max_events=args.max_events))
            out_lines.append("")

    if not contexts and not machines:
        raise ValueError("No CONTEXT or MACHINE objects found in input JSON.")

    out_path = Path(args.output) if args.output else in_path.with_name(in_path.stem + "_extraction.md")
    out_path.write_text("\n".join(out_lines).strip() + "\n", encoding="utf-8")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()