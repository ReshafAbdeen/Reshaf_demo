#ATM Machine Simulator

def atm_simulator():
    balance = 1000.0
    print("--- Welcome to Python Bank ATM ---")
    if input("Enter your 4-digit PIN (1234): ") != "1234":
        return print("Incorrect PIN! Access Denied.")
    while True:
        print("\n1. Balance  2. Deposit  3. Withdraw  4. Exit")
        choice = input("Select an option (1-4): ")
        if choice == '1':
            print(f"Current Balance: ${balance:.2f}")
        elif choice == '2':
            try:
                amt = float(input("Deposit amount: $"))
                if amt > 0:
                    balance += amt
                    print(f"New Balance: ${balance:.2f}")
            except ValueError:
                print("Invalid input!")
        elif choice == '3':
            try:
                amt = float(input("Withdraw amount: $"))
                if 0 < amt <= balance:
                    balance -= amt
                    print(f"New Balance: ${balance:.2f}")
                else:
                    print("Insufficient funds!")
            except ValueError:
                print("Invalid input!")
        elif choice == '4':
            break