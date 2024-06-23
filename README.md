# osrs-mk
# OSRS Most Profitable Items Script

This script fetches the prices of Old School RuneScape items from the Grand Exchange API, calculates the most profitable items, and lists the top items by profit. It also includes functionality to manage the item list, enabling and disabling items, and error handling for failed price checks.

## Features

- Fetches current item prices from the OSRS Grand Exchange API.
- Calculates profits based on a 5% markup for selling prices.
- Lists the most profitable items.
- Allows adding, removing, and toggling items in the list.
- Error handling for API request failures.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository or download the script files.
2. Install the required Python library:
    ```bash
    pip install requests
    ```

## Usage

1. **Generate the `items.txt` file**:
   Use the `genlist.py` script to generate the initial `items.txt` file. The `genlist.py` script should contain your base list of item IDs, names, and their enabled status.
2. **Run python osrs-mk.py**
   python osrs-mk.py
## Menu Options
1. Add item: Add a new item to the list by entering its ID and name.
2. Remove item: Remove an item from the list by entering its ID.
3. Toggle item: Enable or disable an item in the list by entering its ID.
4. Calculate profits: Fetch the prices for all enabled items, calculate their profits, and list the top items by profit.
5. Exit: Exit the script.
Example Output
When you select the option to calculate profits, the script will output the top profitable items:

## Example
1. Item: Blighted manta ray, Profit: 150.00, Cost Price: 1000.00, Sell Price: 1050.00
2. Item: Varrock teleport, Profit: 75.00, Cost Price: 500.00, Sell Price: 525.00
...
## Error Handling
If there is an error fetching the price for an item, the script will automatically disable the item and save the updated list to items.txt.

## Contributing
Contributions are welcome! Please fork this repository and submit pull requests to contribute improvements or bug fixes.
