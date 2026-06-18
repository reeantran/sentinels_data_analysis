import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("../../clean_data/vod_review.csv")
kickoff = df[(df['event'] == 'amer_kickoff_2026')]
stage_1 = df[(df['event'] == 'amer_stage_1_2026')]
kickoff_t_wr = kickoff[(kickoff['side']) == 't']['round_win'].mean()
kickoff_ct_wr = kickoff[(kickoff['side']) == 'ct']['round_win'].mean()
s1_t_wr = stage_1[(stage_1['side']) == 't']['round_win'].mean()
s1_ct_wr = stage_1[(stage_1['side']) == 'ct']['round_win'].mean()

plot_df = pd.DataFrame({
    'event': ['Kickoff', 'Kickoff', 'Stage 1', 'Stage 1'],
    'side': ['T', 'CT', 'T', 'CT'],
    'win_rate': [kickoff_t_wr, kickoff_ct_wr, s1_t_wr, s1_ct_wr]
})

plt.figure(figsize=(6, 4))
sns.barplot(data=plot_df, x='event', y='win_rate', hue='side')
plt.ylabel('Round Win Rate')
plt.title('Round Win Rate: T vs CT')
plt.ylim(0, 1)
plt.legend(title='')
plt.tight_layout()
plt.show()