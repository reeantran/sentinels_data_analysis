import pandas as pd
import numpy as np
import os

def clean_data(input_path):
    df = pd.read_csv(input_path)

    numeric_cols = [
        "map_num", "t1_score", "t2_score", "t1_attack_w", "t1_defense_w", "t2_attack_w", "t1_defense_w", "t1_ot_w", "t2_ot_w", "t1_pistol_w", "t1_eco_w"
        , "t1_semi_eco_w", "t1_semi_buy_w", "t1_full_buy_w", "t2_pistol_w", "t2_eco_w", "t2_semi_eco_w", "t2_semi_buy_w", "t2_full_buy_w"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    input_path = os.path.join(BASE_DIR, "raw_data", "overall_team_stats.csv")
    output_path = os.path.join(BASE_DIR, "clean_data", "overall_team_stats.csv")

    df_clean = clean_data(input_path)

    os.makedirs("data", exist_ok=True)
    df_clean.to_csv(output_path, index=False)