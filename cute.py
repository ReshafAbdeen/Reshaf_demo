import requests

amount_usd = 100
url = "https://open.er-api.com/v6/latest/USD"
data = requests.get(url).json()

if data["result"] == "success":
    rate = data["rates"]["EUR"]
    amount_eur = amount_usd * rate
    print(f"--- Currency Converter ---")
    print(f"${amount_usd} USD = {amount_eur:.2f} EUR (Rate: {rate:.4f})")
else:
    print("Error fetching exchange rates.")