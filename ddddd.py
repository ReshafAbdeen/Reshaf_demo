expenses = []
def add_expense(item, amount):
    expenses.append({"item": item, "amount": amount})
    print(f"Added: {item} - ${amount}")
def view_expenses():
    total = 0
    print("\n--- Expense List ---")
    for exp in expenses:
        print(f"{exp['item']}: ${exp['amount']}")
        total += exp['amount']
    print(f"Total Spent: ${total}\n--------------------")
while True:
    print("1. Add Expense  2. View  3. Exit")
    choice = input("Select option: ")
    if choice == '1':
        item_name = input("Enter item name: ")
        try:
            cost = float(input("Enter amount: "))
            add_expense(item_name, cost)
        except ValueError:
            print("Invalid amount!")
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        print("Exiting Tracker...")
        break
    else:
        print("Invalid choice, try again.")
# Expense tracker closed.
print("Have a great day!")