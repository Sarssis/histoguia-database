import json
from pathlib import Path
episodes = json.loads(Path("data/episodes.json").read_text(encoding="utf-8"))
errors = []
for ep in episodes:
    if ep.get("language") != "es":
        errors.append(f"{ep['id']}: language is not es")
    url = ep.get("apple_url", "")
    if ep.get("verification_status") == "verified_apple" and ("podcasts.apple.com" not in url or "?i=" not in url):
        errors.append(f"{ep['id']}: invalid Apple episode URL")
if errors:
    print("VALIDATION FAILED")
    print("\n".join(errors))
    raise SystemExit(1)
print(f"OK: {len(episodes)} Phase 1 episodes validated")
