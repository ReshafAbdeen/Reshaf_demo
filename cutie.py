def split_bill():
    print("--- Tip Calculator & Bill Splitter ---")
    while True:
        try:
            total_bill = float(input("\nEnter total bill amount: $"))
            if total_bill <= 0:
                print("Bill must be greater than zero.")
                continue
            tip_percent = float(input("Enter tip percentage (e.g., 10, 15, 20): "))
            people = int(input("How many people are splitting the bill? "))
            if people <= 0:
                print("Number of people must be at least 1.")
                continue
            tip_amount = total_bill * (tip_percent / 100)
            grand_total = total_bill + tip_amount
            per_person = grand_total / people
            print("\n--- Bill Summary ---")
            print(f"Initial Bill: ${total_bill:.2f}")
            print(f"Total Tip: ${tip_amount:.2f}")
            print(f"Grand Total: ${grand_total:.2f}")
            print(f"Each Person Pays: ${per_person:.2f}")
            print("--------------------")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
        again = input("Calculate another bill? (y/n): ")
        if again.lower() != 'y':
            print("Exiting Calculator...")
            break
if __name__ == "__main__":
    split_bill()