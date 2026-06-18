import pandas as pd
import numpy as np
import os

def clean_data(input_path):
    df = pd.read_csv(input_path)
    
    for col in ["kast", "hs_percent", "cl_percent"]:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace("%", "", regex=False)
                .astype(float) / 100
            )

    df['cl_percent'] = df['cl_percent'].fillna(0)

    numeric_cols = [
        "series_result", "rds_played", "rating", "acs", "kd", "kast", "adr", "kpr", "apr", "fkpr", "fdpr", "hs_percent", "cl_percent"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    input_path = os.path.join(BASE_DIR, "raw_data", "indi_by_series.csv")
    output_path = os.path.join(BASE_DIR, "clean_data", "indi_by_series.csv")

    df_clean = clean_data(input_path)
    df_clean.to_csv(output_path, index=False)