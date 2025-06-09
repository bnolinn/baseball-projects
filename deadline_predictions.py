from pybaseball import standings, team_pitching
from sklearn.ensemble import RandomForestRegressor

df_standings = standings(2025)
print(df_standings)

df_pitching = team_pitching(2025)
print(df_pitching)