history = []
def calculate(num1, op, num2):
    if op == '+': return num1 + num2
    if op == '-': return num1 - num2
    if op == '*': return num1 * num2
    if op == '/': return num1 / num2 if num2 != 0 else "Error: Div by 0"
    return "Invalid operator"
print("--- Python Calculator ---")
while True:
    print("\nOptions: 'c' to calculate, 'h' for history, 'q' to quit")
    choice = input("Enter choice: ").lower()
    if choice == 'q':
        break
    elif choice == 'h':
        print("History:", history if history else "Empty")
    elif choice == 'c':
        try:
            n1 = float(input("Enter first number: "))
            opr = input("Enter operator (+, -, *, /): ")
            n2 = float(input("Enter second number: "))
            res = calculate(n1, opr, n2)
            print(f"Result: {res}")
            if isinstance(res, float):
                history.append(f"{n1} {opr} {n2} = {res}")
        except ValueError:
            print("Please enter valid numbers!")
    else:
        print("Unknown command!")
# Save output or clear it based on session.
print("Calculator session ended.")