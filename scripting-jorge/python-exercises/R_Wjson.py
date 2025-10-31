import json

# Read JSON
with open("../files/data.json") as f:
    data = json.load(f)

print(data)

data["age"] = 43

print(data)

# # Write JSON
with open("../files/output.json", "w") as f:
    json.dump(data, f, indent=2)
