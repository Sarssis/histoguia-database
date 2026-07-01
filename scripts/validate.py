import json
from pathlib import Path

data = Path("data")
phases = json.loads((data/"phases.json").read_text(encoding="utf-8"))
subperiods = json.loads((data/"subperiods.json").read_text(encoding="utf-8"))
phase_ids = {p["id"] for p in phases}
errors = []
for s in subperiods:
    if s["phase_id"] not in phase_ids:
        errors.append(f"Subperiod {s['id']} has invalid phase_id {s['phase_id']}")
if errors:
    print("VALIDATION FAILED")
    print("\n".join(errors))
    raise SystemExit(1)
print(f"OK: {len(phases)} phases and {len(subperiods)} subperiods validated")
