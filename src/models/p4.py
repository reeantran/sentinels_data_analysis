import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/sen_data_clean.csv")

scan = df.loc[df['role'] == 'scan']
plt.figure(2)
plt.scatter(scan['date'], scan['kd_ratio'])
plt.title("Scan Comparison")
plt.xticks(rotation=45)

plt.show()