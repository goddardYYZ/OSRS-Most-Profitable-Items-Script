import requests
import re
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

# Initialize empty lists to store player counts and timestamps
player_counts = []
timestamps = []

def get_player_count():
    url = "http://www.runescape.com/player_count.js?varname=iPlayerCount&callback=jQuery000000000000000_0000000000&_=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Use regular expression to extract the player count
        match = re.search(r'\((\d+)\)', response.text)
        if match:
            player_count = int(match.group(1))
            return player_count
        else:
            print("Player count not found in response.")
            return None
    else:
        print("Error fetching player count.")
        return None

# def get_total_accounts():
#     url = "https://secure.runescape.com/m=account-creation-reports/rsusertotal.ws"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         total_accounts_match = re.search(r'"accounts":\s*(\d+)', response.text)
#         if total_accounts_match:
#             total_accounts = int(total_accounts_match.group(1))
#             return total_accounts
#         else:
#             print("Total accounts not found in response.")
#             return None
#     else:
#         print("Error fetching total accounts.")
#         return None

def update_graph(frame):
    global player_counts, timestamps
    # Get current player count
    player_count = get_player_count()
    # total_accounts = get_total_accounts()  # Disabled for now
    if player_count is not None:  # and total_accounts is not None:
        # Append player count and current timestamp to the lists
        player_counts.append(player_count)
        timestamps.append(datetime.now())
        # Trim lists to last 100 entries for better performance
        player_counts = player_counts[-100:]
        timestamps = timestamps[-100:]
        # Print debug information
        print(f"Player Count: {player_count}, Time: {timestamps[-1]}")
        # Update the plot
        ax.clear()
        ax.plot(timestamps, player_counts, marker='o', label='Player Count')
        # ax.set_ylim(0, total_accounts)  # Disabled for now
        ax.set_title('Player Count Over Time')
        ax.set_xlabel('Time')
        ax.set_ylabel('Player Count')
        ax.tick_params(axis='x', rotation=45)
        ax.legend()
        plt.tight_layout()
    else:
        print("Error: Could not update graph due to missing data.")

# Set up the figure and axis
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update_graph, interval=5000)  # Update every 5 seconds

# Show the plot
plt.show()
