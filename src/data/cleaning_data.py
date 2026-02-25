import pandas as pd
import numpy as np
import os

def clean_data(input_path):
    # read the path
    df = pd.read_csv(input_path)
    
    # clean the column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # remove the '/' from the deaths
    df["deaths"] = (
        df["deaths"]
        .astype(str)
        .str.replace("/", "", regex=False)
        .str.strip()
    )
    
    # turning % into float decimals
    for col in ["kast", "hs_perc"]:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace("%", "", regex=False)
                .astype(float) / 100
            )

    numeric_cols = [
        "year", "rating", "acs", "kills", "deaths", "assists", "plus_minus_kd", "kast", "adr", "hs_perc", "first_kills", "first_deaths", "plus_minus_fkd", "clutches"
    ]

    # making sure these are numeric values and not strings
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    
    # adding df column kd_ratio and era
    df["kd_ratio"] = df["kills"] / df["deaths"].replace(0, np.nan)
    df["era"] = df["year"].apply(
        lambda y: 1 if y == 2026 else 0
    )

    return df

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    input_path = os.path.join(BASE_DIR, "data", "sen_data_raw.csv")
    output_path = os.path.join(BASE_DIR, "data", "sen_data_clean.csv")

    df_clean = clean_data(input_path)

    os.makedirs("data", exist_ok=True)
    df_clean.to_csv(output_path, index=False)