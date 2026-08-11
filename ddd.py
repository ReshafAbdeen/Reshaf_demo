def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)
def binary_to_text(binary):
    try:
        return ''.join(chr(int(b, 2)) for b in binary.split())
    except ValueError:
        return "Error: Invalid binary input!"
def main():
    print("--- Text <-> Binary Converter ---")
    while True:
        print("\n1. Text to Binary  2. Binary to Text  3. Exit")
        choice = input("Enter choice (1-3): ")
        if choice == '1':
            txt = input("Enter text: ")
            print(f"Binary: {text_to_binary(txt)}")
        elif choice == '2':
            bin_str = input("Enter binary: ")
            print(f"Text: {binary_to_text(bin_str)}")
        elif choice == '3':
            print("Exiting Converter...")
            break
        else:
            print("Invalid choice, try again.")
if __name__ == "__main__":
    main()
# Binary logic is fundamental to computers.
# String conversions are easy in Python.
print("Thanks for using!")
# Goodbye!
# End of code