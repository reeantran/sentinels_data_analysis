import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../../clean_data/vod_review.csv")

kickoff = df[df['event'] == 'amer_kickoff_2026']
stage_1 = df[df['event'] == 'amer_stage_1_2026']

players_k = ['johnqt', 'reduxx', 'cortezia', 'kyu', 'n4rrate']
players_s1 = ['johnqt', 'reduxx', 'cortezia', 'jonahp', 'jerrwin']

rows = []

for player in players_k:
    rows.append({
        'player': f'{player} (K)',
        'fk_winrate': kickoff.loc[
            kickoff['fk_player'] == player,
            'round_win'
        ].mean(),
        'fd_loserate': 1 - kickoff.loc[
            kickoff['fd_player'] == player,
            'round_win'
        ].mean()
    })

for player in players_s1:
    rows.append({
        'player': f'{player} (S1)',
        'fk_winrate': stage_1.loc[
            stage_1['fk_player'] == player,
            'round_win'
        ].mean(),
        'fd_loserate': 1 - stage_1.loc[
            stage_1['fd_player'] == player,
            'round_win'
        ].mean()
    })

plot_df = pd.DataFrame(rows)

plot_df_long = plot_df.melt(
    id_vars='player',
    value_vars=['fk_winrate', 'fd_loserate'],
    var_name='side',
    value_name='rate'
)

plt.figure(figsize=(6, 4))
sns.barplot(
    data=plot_df_long,
    x='player',
    y='rate',
    hue='side'
)
plt.ylabel('Round Result Rate')
plt.title('First Kill Win Rate vs First Death Lose Rate')
plt.ylim(0, 1)
plt.xticks(rotation=45)
plt.legend(title='')
plt.tight_layout()
plt.show()