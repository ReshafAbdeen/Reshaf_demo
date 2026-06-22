import time
import requests


def get_crypto_price(coin="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        return data[coin]["usd"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def main():
    print(f"--- Tracking Live Bitcoin Price (Press Ctrl+C to stop) ---")
    try:
        while True:
            price = get_crypto_price()
            if price:
                current_time = time.strftime("%H:%M:%S", time.localtime())
                print(f"[{current_time}] BTC: ${price:,.2f}")
            time.sleep(10)  
    except KeyboardInterrupt:
        print("\nTracker stopped.")


if __name__ == "__main__":
    main()