from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd
import matplotlib.pyplot as plt

# Choose player
name = input("Enter player name: ")

player_dict = players.find_players_by_full_name(name)

if not player_dict:
    print("Player not found.")
else:
    player = player_dict[0]
    print(f"Found player: {player['full_name']}")

    # Fetch data
    career = playercareerstats.PlayerCareerStats(player_id=player["id"])
    df = career.get_data_frames()[0]

    # Select columns
    df = df[['SEASON_ID', 'PLAYER_AGE', 'GP', 'PTS', 'AST', 'REB']]

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['SEASON_ID'], df['PTS'], label='Points', marker='o')
    plt.plot(df['SEASON_ID'], df['AST'], label='Assists', marker='s')
    plt.plot(df['SEASON_ID'], df['REB'], label='Rebounds', marker='^')

    plt.title(f"{player['full_name']} Career Stats Trend")
    plt.xlabel('Season')
    plt.ylabel('Average per Game')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
