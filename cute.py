import time
def print_pattern():
    print("--- Text Pattern Generator ---")
    while True:
        print("\n1. Pyramid  2. Square  3. Diamond  4. Quit")
        choice = input("Select a pattern (1-4): ")
        if choice == '4':
            print("Exiting Generator...")
            break
        try:
            size = int(input("Enter size (e.g., 5): "))
            if choice == '1':
                for i in range(1, size + 1):
                    print(" " * (size - i) + "*" * (2 * i - 1))
            elif choice == '2':
                for i in range(size):
                    print("*" * size)
            elif choice == '3':
                for i in range(1, size + 1):
                    print(" " * (size - i) + "*" * (2 * i - 1))
                for i in range(size - 1, 0, -1):
                    print(" " * (size - i) + "*" * (2 * i - 1))
            else:
                print("Invalid choice!")
            time.sleep(0.5)
        except ValueError:
            print("Please enter a valid number!")
if __name__ == "__main__":
    print_pattern()
print("Goodbye!")