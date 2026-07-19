# Caesar Cipher (Message Encryptor & Decryptor)

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result
print("--- Caesar Cipher Program ---")
while True:
    print("\n1. Encrypt  2. Decrypt  3. Exit")
    choice = input("Enter choice (1/2/3): ")
    if choice == '3':
        print("Exiting...")
        break
    elif choice in ['1', '2']:
        mode = 'encrypt' if choice == '1' else 'decrypt'
        message = input("Enter your message: ")
        try:
            shift_val = int(input("Enter shift value (number): "))
            output = caesar_cipher(message, shift_val, mode)
            print(f"Result: {output}")
        except ValueError:
            print("Shift value must be a number!")
    else:
        print("Invalid choice, please try again.")