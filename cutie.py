menu = {
    "A1": {"name": "Cola", "price": 1.50},
    "A2": {"name": "Chips", "price": 2.00},
    "B1": {"name": "Candy", "price": 1.00},
    "B2": {"name": "Water", "price": 1.25}
}
def vending_machine():
    print("--- Virtual Vending Machine ---")
    for code, item in menu.items():
        print(f"{code}: {item['name']} - ${item['price']:.2f}")
    balance = 0.0
    while True:
        print(f"\nCurrent Balance: ${balance:.2f}")
        choice = input("Enter code (or 'd' deposit, 'q' quit): ").upper()
        if choice == 'Q':
            if balance > 0: print(f"Refunding ${balance:.2f}")
            break
        elif choice == 'D':
            try:
                amt = float(input("Insert money: $"))
                if amt > 0: balance += amt
            except ValueError:
                print("Invalid amount!")
        elif choice in menu:
            if balance >= menu[choice]['price']:
                balance -= menu[choice]['price']
                print(f"Dispensing {menu[choice]['name']}! Enjoy.")
            else: print("Not enough money! Deposit more.")
        else: print("Invalid code! Try again.")
vending_machine()