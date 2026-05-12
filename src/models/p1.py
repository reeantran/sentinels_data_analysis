import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/sen_data_clean.csv")

controller = df.loc[df['role'] == 'controller']
# cmap = controller['map']
controller = controller.reset_index(drop=True)
controller['x'] = controller.index

stats = ['rating', 'acs', 'plus_minus', 'kast', 'adr', 'hs_perc', 'plus_minus_f', 'clutches', 'kd_ratio', 'assists']
for category in stats:
    plt.figure(category)
    plt.scatter(controller['x'], controller[category], c=['green' if result=='w' else 'red' for result in controller['result']], s=100)
    plt.xticks(controller['x'], controller['player'], rotation=90)
    # plt.boxplot(controller['player'], labels=['TenZ', 'bang', 'johnqt'])
    plt.title("Controller " + category + " Comparison")

plt.show()