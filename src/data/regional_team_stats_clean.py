import pandas as pd
import numpy as np
import os

def clean_data(input_path):
    df = pd.read_csv(input_path)

    numeric_cols = [
        "wr", "t_wr", "ct_wr", "p_wr"
    ]

    for col in numeric_cols:
        if col in df.columns:
            frac = df[col].str.split("/", expand=True).astype(float)
            df[col] = frac[0] / frac[1] * 100

    return df

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    input_path = os.path.join(BASE_DIR, "raw_data", "reg_teams_s1.csv")
    output_path = os.path.join(BASE_DIR, "clean_data", "reg_teams_s1.csv")

    df_clean = clean_data(input_path)
    df_clean.to_csv(output_path, index=False)

    input_path = os.path.join(BASE_DIR, "raw_data", "reg_teams_kickoff.csv")
    output_path = os.path.join(BASE_DIR, "clean_data", "reg_teams_kickoff.csv")

    df_clean = clean_data(input_path)
    df_clean.to_csv(output_path, index=False)