# Valorant VCT Pro-Player Analytics Pipeline

import pandas as pd 
import numpy as np

print("\033[1m Valorant Esport: Advance AI Data Pipeline \033[0m\n")

vct_data = {
    'Match_Date': ['12-May-2026', '13-May-2026', '12-May-2026', '12-May-2026', '13-May-2026', '14-May-2026'],
    'Player': ['Tenz', 'Tenz', 'Tenz', "Forsaken", 'Forsaken', 'Forsaken'],
    "Kills": [25, 12, 30, 18, 22, 15],
    "Deaths": [10, 15, 12, 18, 14, 20],
    "Ping_ms": [20, 150, 22, 25, 24, 300]
}

df = pd.DataFrame(vct_data)
print("--Raw Server Data--")
print(df.head())

df["Match_Date"] = pd.to_datetime(df["Match_Date"])

df["KD_Ratio"] = round(df["Kills"] / df["Deaths"], 2)

df["Performance"] = np.where(df["KD_Ratio"] > 1.5 , "MVP Level", "Normal")

ping_bins = [0, 50, 150, 500 ]
ping_labels = ["Good", "Playable", "Extreme lag!"]
df["Srever_Health"] = pd.cut(df["Ping_ms"] , bins=ping_bins, labels=ping_labels)

df = df.sort_values(by=['Player', 'Match_Date'])
df["2-Match AVG Pings"] = df.groupby("Player")["Ping_ms"].transform(lambda x: x.rolling(2, min_periods=1).mean())

print("===Finala AI-Ready Pipeline Ready hai===")
print(df)