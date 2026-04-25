# Fig. C5: Prototype pipeline script excerpt (JSON → tables / skeleton)

import json

def load_multi_json(text: str):
    dec = json.JSONDecoder()
    i, objs = 0, []
    while i < len(text):
        while i < len(text) and text[i].isspace():
            i += 1
        if i >= len(text):
            break
        obj, j = dec.raw_decode(text, i)
        objs.append(obj)
        i = j
    return objs

def find_machine(objs):
    return next(o for o in objs if "MACHINE" in o)

text = open("car.json", "r", encoding="utf-8").read()
objs = load_multi_json(text)
m = find_machine(objs)

events = [e["event_name"] for e in m["EVENTS"] if e["event_name"] != "INITIALISATION"]

# Emit PAT CSP skeleton (control-flow template)
print("System() = (")
for idx, ev in enumerate(events):
    prefix = "    " if idx == 0 else " [] "
    print(f"{prefix}{ev} -> System()")
print(");")
print("#assert System() deadlockfree;")

