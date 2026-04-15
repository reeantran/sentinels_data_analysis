import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/sen_data_clean.csv")

controller = df.loc[df['role'] == 'controller']
plt.figure(3)
plt.scatter(controller['date'], controller['kd_ratio'])
plt.title("Controller Comparison")
plt.xticks(rotation=45)

plt.show()