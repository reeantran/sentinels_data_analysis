import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("../../clean_data/vod_review.csv")
kickoff = df[(df['event'] == 'amer_kickoff_2026')]
kickoff = kickoff[(kickoff['side'] == 'ct')]
stage_1 = df[(df['event'] == 'amer_stage_1_2026')]
stage_1 = stage_1[(stage_1['side'] == 'ct')]

players_k = ['johnqt', 'reduxx', 'cortezia', 'kyu', 'n4rrate']
players_s1 = ['johnqt', 'reduxx', 'cortezia', 'jonahp', 'jerrwin']

rows = []

for player in players_k:
    col = f'{player}_k_post'

    rows.append({
        'player': f'{player} (K)',
        'alive_winrate': kickoff.loc[kickoff[col].notna(), 'round_win'].mean(),
        'dead_loserate': 1 - kickoff.loc[kickoff[col].isna(), 'round_win'].mean()
    })

for player in players_s1:
    col = f'{player}_k_post'

    rows.append({
        'player': f'{player} (S1)',
        'alive_winrate': stage_1.loc[stage_1[col].notna(), 'round_win'].mean(),
        'dead_loserate': 1 - stage_1.loc[stage_1[col].isna(), 'round_win'].mean()
    })

plot_df = pd.DataFrame(rows)

plot_df_long = plot_df.melt(
    id_vars='player',
    value_vars=['alive_winrate', 'dead_loserate'],
    var_name='side',
    value_name='rate'
)

plt.figure(figsize=(6, 4))
sns.barplot(data=plot_df_long, x='player', y='rate', hue='side')
plt.ylabel('Round Result Rate')
plt.title('Player Alive During Retake Win Rate vs Player Dead During Retake Lose Rate')
plt.ylim(0, 1)
plt.xticks(rotation=45)
plt.legend(title='')
plt.tight_layout()
plt.show()