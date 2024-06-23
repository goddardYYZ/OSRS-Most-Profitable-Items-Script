import requests

# Function to get the price of an item by its ID
def get_item_price(item_id, item_names):
    try:
        url = f"https://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item={item_id}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price_str = data["item"]["current"]["price"]
        
        if isinstance(price_str, str):
            price = float(price_str.replace("m", "000000").replace("k", "000").replace(",", ""))
        else:
            price = float(price_str)
        
        return price
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Error fetching price for item ID {item_id}: {e}")
        item_names[item_id]["enabled"] = False
        save_items("items.txt", item_names)
        return None

# Function to calculate the profit for an item
def calculate_profit(cost_price, sell_price):
    return round(sell_price - cost_price, 2)

# Function to load items from a file
def load_items(file_name):
    items = {}
    with open(file_name, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            item_id = int(parts[0])
            item_name = parts[1]
            item_enabled = parts[2].lower() == "true"
            items[item_id] = {"name": item_name, "enabled": item_enabled}
    return items

# Function to save items to a file
def save_items(file_name, items):
    with open(file_name, "w") as file:
        for item_id, item_data in items.items():
            file.write(f"{item_id},{item_data['name']},{item_data['enabled']}\n")

# Initialize the item names dictionary with items from the file
item_names = load_items("items.txt")

# Function to add items to the list
def add_item(item_id, item_name):
    if item_id in item_names:
        print("Error: Item ID already exists in the list.")
    elif item_name in [item["name"] for item in item_names.values()]:
        print("Error: Item name already exists in the list.")
    else:
        item_names[item_id] = {"name": item_name, "enabled": True}
        save_items("items.txt", item_names)
        print("Item added successfully.")

# Function to remove items from the list
def remove_item():
    item_id = int(input("Enter the item ID to remove: "))
    if item_id in item_names:
        del item_names[item_id]
        save_items("items.txt", item_names)
        print("Item removed successfully.")
    else:
        print("Error: Item ID not found in the list.")

# Function to enable or disable items
def toggle_item():
    print("Items in the list:")
    for item_id, item_data in item_names.items():
        print(f"Name: {item_data['name']}, ID: {item_id}, Enabled: {item_data['enabled']}")
    print("0. Cancel")
    item_id = int(input("Enter the item ID to toggle (or 0 to cancel): "))
    if item_id == 0:
        return
    if item_id in item_names:
        try:
            item_names[item_id]["enabled"] = not item_names[item_id]["enabled"]
            save_items("items.txt", item_names)
            print("Item toggled successfully.")
        except Exception as e:
            print(f"Error toggling item ID {item_id}: {e}")
    else:
        print("Error: Item ID not found in the list.")

# Menu loop
while True:
    print("\nMenu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Toggle item")
    print("4. Calculate profits")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item(int(input("Enter the item ID: ")), input("Enter the item name: "))
    elif choice == "2":
        remove_item()
    elif choice == "3":
        toggle_item()
    elif choice == "4":
        # Dictionary to store item names, prices, and profits
        items = {}

        # Fetch prices for each enabled item ID in the dictionary
        for item_id, item_data in item_names.items():
            if item_data["enabled"]:
                cost_price = get_item_price(item_id, item_names)
                if cost_price is not None:
                    sell_price = cost_price * 1.05  # Assuming a 5% markup for selling
                    profit = calculate_profit(cost_price, sell_price)
                    items[item_data["name"]] = {
                        "cost_price": round(cost_price, 2),
                        "sell_price": round(sell_price, 2),
                        "profit": profit
                    }

        # Sort items by profit in descending order
        sorted_items = sorted(items.items(), key=lambda x: x[1]["profit"], reverse=True)

        # Print the items sorted by profit
        for rank, (item_name, item_data) in enumerate(sorted_items, start=1):
            print(f"{rank}. Item: {item_name}, Profit: {item_data['profit']}, Cost Price: {item_data['cost_price']}, Sell Price: {item_data['sell_price']}")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
