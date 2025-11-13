from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
import pandas as pd
import matplotlib.pyplot as plt

def get_player_id(player_name):
    """Get player ID by full name."""
    player_dict = players.find_players_by_full_name(player_name)
    if player_dict:
        return player_dict[0]['id']
    else:
        print(f"Player '{player_name}' not found.")
        return None

def get_player_career_data(player_name):
    """Fetch player career averages."""
    player_id = get_player_id(player_name)
    if player_id is None:
        return None

    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df = career.get_data_frames()[0]
    df["PLAYER_NAME"] = player_name
    df = df[["SEASON_ID", "PLAYER_NAME", "PTS", "AST", "REB"]]
    return df

def compare_players(player1, player2):
    """Compare two players' Points, Assists, and Rebounds per season."""
    df1 = get_player_career_data(player1)
    df2 = get_player_career_data(player2)

    if df1 is None or df2 is None:
        return

    # Ensure season IDs are strings for clean merging
    df1['SEASON_ID'] = df1['SEASON_ID'].astype(str)
    df2['SEASON_ID'] = df2['SEASON_ID'].astype(str)

    # Merge by season
    merged = pd.merge(df1, df2, on='SEASON_ID', suffixes=(f'_{player1}', f'_{player2}'))

    # Plot comparison
    plt.figure(figsize=(12, 7))

    # Points
    plt.plot(merged['SEASON_ID'], merged[f'PTS_{player1}'], label=f'{player1} PTS', marker='o')
    plt.plot(merged['SEASON_ID'], merged[f'PTS_{player2}'], label=f'{player2} PTS', marker='o')

    # Assists
    plt.plot(merged['SEASON_ID'], merged[f'AST_{player1}'], '--', label=f'{player1} AST')
    plt.plot(merged['SEASON_ID'], merged[f'AST_{player2}'], '--', label=f'{player2} AST')

    # Rebounds
    plt.plot(merged['SEASON_ID'], merged[f'REB_{player1}'], ':', label=f'{player1} REB')
    plt.plot(merged['SEASON_ID'], merged[f'REB_{player2}'], ':', label=f'{player2} REB')

    plt.xticks(rotation=45)
    plt.xlabel("Season")
    plt.ylabel("Per Game Average")
    plt.title(f"Career Comparison: {player1} vs {player2} (PTS, AST, REB)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    player1 = input("Enter first player name: ")
    player2 = input("Enter second player name: ")
    compare_players(player1, player2)

