import json
from pathlib import Path

episodes = json.loads(Path("data/episodes.json").read_text(encoding="utf-8"))
errors = []

for i, ep in enumerate(episodes, start=1):
    for field in ["episode_id", "podcast_id", "title", "phase_id", "main_topic", "language", "apple_url", "verification_status"]:
        if not ep.get(field):
            errors.append(f"Episode {i}: missing {field}")
    if ep.get("language") != "es":
        errors.append(f"{ep.get('episode_id')}: language must be es")
    if ep.get("verification_status") == "verified_apple":
        url = ep.get("apple_url", "")
        if "podcasts.apple.com" not in url or "?i=" not in url:
            errors.append(f"{ep.get('episode_id')}: verified Apple URL must include podcasts.apple.com and ?i=")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print("-", e)
    raise SystemExit(1)

print(f"OK: {len(episodes)} episodes validated")
