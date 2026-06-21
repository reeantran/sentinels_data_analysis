import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("../../clean_data/vod_review.csv")
kickoff = df[(df['event'] == 'amer_kickoff_2026')]
stage_1 = df[(df['event'] == 'amer_stage_1_2026')]

kickoff_adv = kickoff.dropna(subset=['fk_player'])
stage_1_adv = stage_1.dropna(subset=['fk_player'])
kickoff_disadv = kickoff.dropna(subset=['fd_player'])
stage_1_disadv = stage_1.dropna(subset=['fd_player'])

kickoff_adv_wr = kickoff_adv['round_win'].mean()
stage_1_adv_wr = stage_1_adv['round_win'].mean()
kickoff_disadv_wr = kickoff_disadv['round_win'].mean()
stage_1_disadv_wr = stage_1_disadv['round_win'].mean()

plot_df = pd.DataFrame({
    'event': ['Kickoff', 'Kickoff', 'Stage 1', 'Stage 1'],
    'side': ['Advantage', 'Disadvantage', 'Advantage', 'Disadvantage'],
    'win_rate': [kickoff_adv_wr, kickoff_disadv_wr, stage_1_adv_wr, stage_1_disadv_wr]
})

plt.figure(figsize=(6, 4))
sns.barplot(data=plot_df, x='event', y='win_rate', hue='side')
plt.ylabel('Round Win Rate')
plt.title('Round Win Rate: Advantage vs Disadvantage')
plt.ylim(0, 1)
plt.legend(title='')
plt.tight_layout()
plt.show()

# print("Kickoff Advantage Winrate: " + kickoff_adv_wr)
# print("Stage 1 Advantage Winrate: " + s1_adv_wr)
# print("Kickoff Disadvantage Winrate: " + kickoff_disadv_wr)
# print("Stage 1 Disadvantage Winrate: " + s1_disadv_wr)