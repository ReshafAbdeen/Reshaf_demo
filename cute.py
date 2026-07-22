# Mock Currency Converter


# Mock Currency Converter
rates = {"USD": 1.0, "EUR": 0.85, "INR": 83.0, "GBP": 0.75}
def convert(amount, from_curr, to_curr):
    if from_curr not in rates or to_curr not in rates:
        return None
    usd_amount = amount / rates[from_curr]
    return usd_amount * rates[to_curr]
print("--- Mock Currency Converter ---")
while True:
    print(f"Available: {', '.join(rates.keys())}")
    print("Enter 'q' to quit at any time.")
    f_curr = input("From Currency: ").upper()
    if f_curr == 'Q': break
    t_curr = input("To Currency: ").upper()
    if t_curr == 'Q': break
    try:
        amt = float(input("Enter Amount: "))
        res = convert(amt, f_curr, t_curr)
        if res is not None:
            print(f"{amt} {f_curr} = {res:.2f} {t_curr}\n")
        else:
            print("Invalid Currency Code!\n")
    except ValueError:
        print("Invalid amount!\n")
# Converter module finished.
print("Currency rates are just mock values.")
print("Thanks for using!")
# Always verify real rates online.
# Stay updated!
# End of Program