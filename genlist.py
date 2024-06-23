import requests

# URL of the JSON data
url = "https://www.osrsbox.com/osrsbox-db/items-summary.json"

# Fetch JSON data
response = requests.get(url)
data = response.json()

# Write data to items.txt
with open("items.txt", "w") as f:
    for item_id, item_data in data.items():
        name = item_data["name"]
        line = f"{item_id},{name},True\n"
        f.write(line)
