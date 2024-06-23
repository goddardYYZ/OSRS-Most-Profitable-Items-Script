import requests
import re

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

def main():
    player_count = get_player_count()
    if player_count is not None:
        print(f"Current player count: {player_count:,}")
    else:
        print("Failed to retrieve player count.")

if __name__ == "__main__":
    main()
