# Algorithmic Trading Volatility Tracker (The Finance Tech)

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation
print("\033[1m" + "==Algorithmic Trading: Live Crypto Data Fetcher=="+ "\033[0m\n")

ticker = "BTC-USD"

print(f"Srever Se {ticker} Ka Live data pull kiya ja rha hai....Please Wait..")

btc_data = yf.download(ticker, period="6mo")

df = pd.DataFrame(btc_data)
print("=======Raw Market Data (First 5 Days)=======")
print(df.head())
df['SMA_20'] = df['Close'].rolling(window=20).mean()

print("\n===Data Info===")
print(f"Total Raw & Columns {df.shape}")

plt.style.use('dark_background')
plt.figure(figsize=(10, 5))

plt.plot(df.index, df['Close'], color='orange', linewidth=2, label='Bitcoin (BTC) Price')
plt.plot(df.index, df['SMA_20'], color='cyan', linewidth=2, label='20 Days Trend (SMA)')

plt.title("Bitcoin Trend - Last 6 Month", fontsize=14, fontweight='bold')
plt.xlabel("Date", fontsize=14)
plt.ylabel("Price in USD ($)", fontsize=14, color='lightgrey')

plt.grid(True, linestyle=':', alpha=0.5, color='gray')
plt.legend()

plt.show()