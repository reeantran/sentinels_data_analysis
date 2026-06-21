import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("../../clean_data/vod_review.csv")
kickoff = df[(df['event'] == 'amer_kickoff_2026')]
kickoff = kickoff[(kickoff['side'] == 't')]
stage_1 = df[(df['event'] == 'amer_stage_1_2026')]
stage_1 = stage_1[(stage_1['side'] == 't')]

