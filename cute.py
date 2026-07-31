cart = {}
def shopping_cart():
    print("--- Online Shopping Cart ---")
    while True:
        print("\n1. Add Item  2. Remove Item  3. View Cart  4. Checkout")
        choice = input("Enter choice (1-4): ")
        if choice == '1':
            item = input("Item name: ").title()
            try:
                price = float(input(f"Price: $"))
                cart[item] = cart.get(item, 0) + price
                print("Item added!")
            except ValueError:
                print("Invalid price!")
        elif choice == '2':
            item = input("Item to remove: ").title()
            if item in cart:
                del cart[item]
                print("Item removed.")
            else:
                print("Not in cart.")
        elif choice == '3':
            print("\n--- Cart ---")
            for k, v in cart.items():
                print(f"{k}: ${v:.2f}")
        elif choice == '4':
            print(f"\nTotal: ${sum(cart.values()):.2f}\nThanks!")
            break
if __name__ == "__main__":
    shopping_cart()