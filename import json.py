import json

with open("test2.json", "r") as f:
    data = json.load(f)

print(data["name"])





