import pandas as pd
import numpy as np
import os

def clean_data(input_path):
    df = pd.read_csv(input_path)

    numeric_cols = [
        "round", "spike_planted", "plant_time", "fk_time", "round_win", "johnqt_k_pre", "reduxx_k_pre", "cortezia_k_pre", "n4rrate_k_pre", "kyu_k_pre",
        "jonahp_k_pre", "victor_k_pre", "jerrwin_k_pre", "johnqt_k_post", "reduxx_k_post", "cortezia_k_post", "n4rrate_k_post", "kyu_k_post", "jonahp_k_post", 
        "victor_k_post", "jerrwin_k_post"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    input_path = os.path.join(BASE_DIR, "raw_data", "vod_review.csv")
    output_path = os.path.join(BASE_DIR, "clean_data", "vod_review.csv")

    df_clean = clean_data(input_path)
    df_clean.to_csv(output_path, index=False)