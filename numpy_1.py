#Data Smoother

import pandas as pd 

print("\033[1m" + "Advance Pandas : Ping Smoother "+ "\033[0m")

data = {
    "Match_no" : [1, 2, 3, 4, 5, 6, 7, 8],
    'Raw_Ping_ms': [25, 30, 180, 22, 28, 500, 35, 49]
}

df = pd.DataFrame(data)
print("--Raw Data (With Lag Spike)")
print(df)


df['Smoother_Ping (3-Match Avg)'] = df['Raw_Ping_ms'].rolling(window=3).mean()
print("\n---Data After Rolling Average Magic---")
print(df)