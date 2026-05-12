import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/sen_data_clean.csv")

duelist = df[df['role'] == 'duelist']
i = 0
stats = ['rating', 'acs', 'plus_minus', 'kast', 'adr', 'hs_perc', 'plus_minus_f', 'clutches', 'kd_ratio']
for category in stats:
    plt.figure(category)
    plt.scatter(duelist['date'], duelist[category], c=['green' if result=='w' else 'red' for result in duelist['result']], marker='D', s=100)
    plt.title("Duelist " + category + " Comparison")
    plt.xticks(duelist['date'], duelist['event'], rotation=90)
    for event, group in duelist.groupby('event'):
        xmin = group['date'].min()
        xmax = group['date'].max()
        
        plt.axvline(x=xmax, color='black', linestyle='--', alpha=0.7)

plt.show()