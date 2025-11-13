from nba_api.stats.endpoints import leaguedashplayerstats

# Fetch player stats for the 2023-24 season
data = leaguedashplayerstats.LeagueDashPlayerStats(season='2023-24')
df = data.get_data_frames()[0]

print(df.head())
