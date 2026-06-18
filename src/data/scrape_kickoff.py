import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

url = "https://www.vlr.gg/event/stats/2682/vct-2026-americas-kickoff"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_="wf-table mod-stats mod-scroll")

rows = []

for tr in table.find("tbody").find_all("tr"):
    tds = tr.find_all("td")

    if len(tds) < 12:
        continue

    row = {
        "player": tds[0].get_text(strip=True),
        "rating": tds[3].get_text(strip=True),
        "acs": tds[4].get_text(strip=True),
        "kd": tds[5].get_text(strip=True),
        "kast": tds[6].get_text(strip=True),
        "adr": tds[7].get_text(strip=True),
        "kpr": tds[8].get_text(strip=True),
        "apr": tds[9].get_text(strip=True),
        "fkpr": tds[10].get_text(strip=True),
        "fdpr": tds[11].get_text(strip=True),
        "hs_percent": tds[12].get_text(strip=True),
        "cl_percent": tds[13].get_text(strip=True),
    }

    rows.append(row)

df = pd.DataFrame(rows)

numeric_cols = [
    "rating", "acs", "kd", "kast", "adr", "kpr", "apr", "fkpr", "fdpr", "hs_percent", "cl_percent"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
output_path = os.path.join(BASE_DIR, "clean_data", "reg_players_kickoff.csv")
df.to_csv(output_path, index=False)