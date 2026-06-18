import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

kickoff_df = pd.read_csv("../../clean_data/regional_team_stats_kickoff.csv")
stage_1_df = pd.read_csv("../../clean_data/regional_team_stats_s1.csv")

kickoff_df["event"] = "amer_kickoff_2026"
stage_1_df["event"] = "amer_stage_1_2026"

