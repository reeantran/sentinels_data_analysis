import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/sen_data_clean.csv")

flex = df.loc[df['role'] == 'flex']
plt.figure(4)
plt.scatter(flex['date'], flex['kd_ratio'])
plt.title("Flex Comparison")
plt.xticks(rotation=45)

plt.show()