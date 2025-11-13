from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd

# Get player name from user
name = input("Enter NBA player name: ")

# Search player ID
player_dict = players.find_players_by_full_name(name)

if not player_dict:
    print("Player not found. Check the spelling.")
else:
    player = player_dict[0]
    print(f"Found player: {player['full_name']} (ID: {player['id']})")

    # Get career stats
    career = playercareerstats.PlayerCareerStats(player_id=player["id"])
    df = career.get_data_frames()[0]

    # Show last 3 seasons
    print(df.tail(3))

    # Save as CSV
    filename = f"{player['full_name'].replace(' ', '_')}_career_stats.csv"
    df.to_csv(filename, index=False)
    print(f"\n✅ Data saved as '{filename}' in your project folder!")
