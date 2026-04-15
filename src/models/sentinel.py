import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/sen_data_clean.csv")

sentinel = df.loc[df['role'] == 'sentinel']
plt.figure(5)
plt.scatter(sentinel['date'], sentinel['kd_ratio'])
plt.title("Sentinel Comparison")
plt.xticks(rotation=45)

plt.show()