import pandas as pd
import numpy as np
import os

def clean_data(input_path):
    df = pd.read_csv(input_path)

    numeric_cols = [
        "maps_played", "map_wins", "win%", "attack_r", "attack_r_w", "attack_r_w%", "defense_r", "defense_r_w", "defense_r_w%", "pistol_r", "pistol_r_w"
        , "pistol_r_w%"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    input_path = os.path.join(BASE_DIR, "raw_data", "regional_team_stats.csv")
    output_path = os.path.join(BASE_DIR, "clean_data", "regional_team_stats.csv")

    df_clean = clean_data(input_path)
    df_clean.to_csv(output_path, index=False)