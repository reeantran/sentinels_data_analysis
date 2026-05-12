import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../clean_data/individual_stats.csv")

p5 = df.loc[df['player_name'] == 'n4rrate' or df['player_name'] == 'victor' or df['player_name'] == 'jerrwin']
stats = ["rds_played", "rating", "acs", "k/d", "kast", "adr", "kpr", "apr", "fkpr", "fdpr", "hs%", "cl%"]