import json
import urllib.request
from pathlib import Path

URL = "https://prixi.sk/professional/10/schedule_uid/5003255a-e77f-41be-bc14-96520975aace"

with urllib.request.urlopen(URL) as r:
    data = json.loads(r.read().decode())

print("Response:")
print(data)

if isinstance(data, list) and len(data) == 0:
    print("NO_FREE_SLOTS")
else:
    print("FREE_SLOTS_FOUND")

    Path("issue.txt").write_text(
        "Objavil sa aspoň jeden voľný termín v systéme Prixi.\n\n"
        "https://prixi.sk/ordinacia/10/bot?fontSize=16&locale=sk"
    )
