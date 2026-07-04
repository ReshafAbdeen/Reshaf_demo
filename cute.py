#Crypto Trend Analyzer

import pandas as pd

print("\033[1m" + "=== Crypto Time Series Analyzer ===" + "\033[0m\n")

market_data = {
    "Date": ["2026-07-01", "2026-07-02", "2026-07-03", "2026-07-04", "2026-07-05", "2026-07-06"],
    "Coin": ["Bitcoin", "Bitcoin", "Bitcoin", "Ethereum", "Ethereum", "Ethereum"],
    "Price_USD": [60500, 62000, 59000, 3100, 3250, 3050]
}

df = pd.DataFrame(market_data)
print("--- Raw Data (Date is Text) ---")
print(df)
print("\n---Datatype of Data Column :" , type(df['Date'][0]))


df['Date'] = pd.to_datetime(df['Date'])

df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month_name()
df['Weekday'] = df['Date'].dt.day_name()

print("\n==Smart Datetime Feature Extract Karne ke Baad==")
print(df)