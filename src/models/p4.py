import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../clean_data/individual_stats.csv")

p4 = df.loc[df['player_name'] == 'kyu' or df['player_name'] == 'jonahp']
stats = ["rds_played", "rating", "acs", "k/d", "kast", "adr", "kpr", "apr", "fkpr", "fdpr", "hs%", "cl%"]