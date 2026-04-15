import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/sen_data_clean.csv")

duelist = df[df['role'] == 'duelist']

plt.figure(1)
plt.scatter(duelist['date'], duelist['kd_ratio'])
plt.title("Duelist K/D Comparison")
plt.xticks(duelist['date'], duelist['event'], rotation=45)

plt.figure(2)
plt.scatter(duelist['date'], duelist['clutches'])
plt.title("Duelist Clutch Comparison")
plt.xticks(duelist['date'], duelist['event'], rotation=45)

plt.show()