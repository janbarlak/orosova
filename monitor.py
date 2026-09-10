import json
import urllib.request

URL = "https://prixi.sk/professional/10/schedule_uid/5003255a-e77f-41be-bc14-96520975aace"

with urllib.request.urlopen(URL) as r:
    data = json.loads(r.read().decode())

print("Response:")
print(data)

if isinstance(data, list) and len(data) == 0:
    print("NO_FREE_SLOTS")
else:
    print("FREE_SLOTS_FOUND")
