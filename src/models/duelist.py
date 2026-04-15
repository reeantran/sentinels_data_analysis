import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/sen_data_clean.csv")

duelist = df.loc[df['role'] == 'duelist']
plt.figure(1)
plt.scatter(duelist['date'], duelist['kd_ratio'])
plt.title("Duelist Comparison")
plt.xticks(rotation=45)
