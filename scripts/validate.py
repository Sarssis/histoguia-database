import json
from pathlib import Path
episodes=json.loads(Path("data/episodes.json").read_text(encoding="utf-8"))
errors=[]
for e in episodes:
    if e.get("language")!="es": errors.append(f"{e['id']}: language must be es")
    for platform,status in e.get("verification",{}).items():
        url=e.get("links",{}).get(platform,"")
        if status=="verified" and not url: errors.append(f"{e['id']}: {platform} verified but URL missing")
        if platform=="apple" and status=="verified" and ("podcasts.apple.com" not in url or "?i=" not in url): errors.append(f"{e['id']}: invalid Apple episode URL")
if errors:
    print("VALIDATION FAILED"); print("\n".join(errors)); raise SystemExit(1)
print(f"OK: {len(episodes)} episodes validated")
