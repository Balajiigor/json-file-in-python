import json

f = open("/home/balaji/Documents/output of json/input server data.json")

data = json.load(f)

for i in data["Emp1"]:
    print(i)
f.close()
