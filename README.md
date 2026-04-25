# CS4211 Project 3 — Event-B to PAT (DOORS & CAR)

This repository contains our CS4211 Project 3 deliverables: manual PAT models for two Event-B systems (**90_DOORS** and **2_CAR**) and a semi-automated prototype pipeline that helps extract structured summaries and generate PAT skeleton templates.

## Systems
- **90_DOORS**: access-request protocol  
  `CARD → accept/refuse → ACCEPT/REFUSE → PASS/OFF_* → ACKN → Idle`
- **2_CAR (m3)**: single-lane bridge traffic controller with sensors, lights, counters, and capacity constraint `d`.

## What we built
1) **Manual PAT models (CSP style)**  
   - Control-flow abstraction using phases/states and event-labelled transitions
   - Verification checks (deadlock, safety, liveness insights) with counterexample traces where applicable

2) **Semi-automated prototype pipeline**  
   - Parses provided Event-B JSON artefacts
   - Auto-generates extraction outputs (tables for variables/init/invariants/events)
   - Auto-generates runnable PAT CSP skeleton templates + basic check templates  
   - Final verified models are produced by manually refining the generated skeletons (abstraction decisions, tightening assumptions, and interpreting verification results)

## Repository structure
- `artefacts/`  
  Event-B JSON inputs (`doors.json`, `car.json`)
- `pipeline/`  
  Prototype scripts for extraction and skeleton generation:
  - `eventb_extract.py` — outputs extraction tables
  - `eventb_gen_pat_skeleton.py` — generates PAT skeleton + check templates
  - `core.py` — shared helpers
- `pat_models/`
  - `doors/` — generated skeleton/checks for DOORS  
  - `car/` — generated skeleton/checks for CAR  
  - `final/` — final refined models used for verification (`doors.csp`, `CAR.csp`)
- `evidence/`
  - `doors/verification_outputs/` — screenshots/logs for DOORS verification
  - `car/verification_outputs/` — screenshots/logs for CAR verification
  - `pipeline/` — optional pipeline artefacts / before-after materials

## How to run the prototype (table extraction)
From the repo root:

```bash
python3 pipeline/eventb_extract.py artefacts/doors.json --out evidence/doors/appendix_doors_extraction.md
python3 pipeline/eventb_extract.py artefacts/car.json   --out evidence/car/appendix_car_extraction.md
