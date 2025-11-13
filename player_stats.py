from nba_api.stats.endpoints import playercareerstats
import pandas as pd

# Get LeBron James' career stats
lebron = playercareerstats.PlayerCareerStats(player_id='2544')  # LeBron's NBA ID
df = lebron.get_data_frames()[0]

# Show his most recent season
print("LeBron James - Latest Season Stats")
print(df.tail(1))
