import json
import os
file_path = "./log.json"
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
else:
    logs = []
with open("../data/raw_news/news_2025-04-24_22-37.json", "r") as f:
    data = json.load(f)
likes_highest = 0
url = None
for post in data["results"]:
    if post["votes"]["liked"] > likes_highest:
        url = post["url"]
        likes_highest = post["votes"]["liked"]
logs.append({"url": url})
with open(file_path, "w") as f:
    json.dump(logs, f, indent=2)
