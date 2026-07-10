# The Live "Hacker" Matrix Graph

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation

print("\033[1m" + "==Algorithmic Trading: Live Crypto Data Fetcher=="+ "\033[0m\n")

ticker = "BTC-USD"
print(f"Server se {ticker} ka 1-Minute data pull kiya ja raha hai... Please Wait...\n")

btc_data = yf.download(ticker, period='1d', interval="1m")
df = pd.DataFrame(btc_data)

print(f"Total Live Ticks Fetched: {len(df)}")
print("Live Window Open Ho rhi hai. Check karo....")

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 6))

x_data, y_data = [], []

def animate(i):
    if i < len(df):
        x_data.append(df.index[i])
        y_data.append(df['Close'].iloc[i].item())
        ax.clear()
        ax.plot(x_data, y_data, color='lime', linewidth=2)
        ax.set_title("LIVE: Bitcoin Intradya Tracker(1-Minut Intervals)", color='white', fontweight='bold', fontsize=14)
        ax.set_ylabel("Price In USD ($)", color='lightgrey', fontsize=14)
        ax.grid(True, linestyle='--', alpha=0.5, color='gray')

ani = FuncAnimation(fig, animate, frames=len(df), interval=10, repeat=False)

plt.show()