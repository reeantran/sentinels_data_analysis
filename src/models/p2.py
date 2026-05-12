import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../clean_data/individual_stats.csv")

p2 = df.loc[df['player_name'] == 'cortezia']
stats = ["rds_played", "rating", "acs", "k/d", "kast", "adr", "kpr", "apr", "fkpr", "fdpr", "hs%", "cl%"]