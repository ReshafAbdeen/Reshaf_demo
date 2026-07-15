# Secure Password Generator

import random
import string
def generate_password(length, digits, symbols):
    characters = string.ascii_letters
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    if length < 4:
        return "Error: Length must be at least 4!"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password
print("--- Secure Password Generator ---")
while True:
    try:
        pwd_len = int(input("Enter length: "))
        inc_num = input("Numbers? (y/n): ").lower() == 'y'
        inc_sym = input("Symbols? (y/n): ").lower() == 'y'
        final_pwd = generate_password(pwd_len, inc_num, inc_sym)
        print(f"\nGenerated Password: {final_pwd}")
        print("Make sure to save it securely!")
        break
    except ValueError:
        print("Invalid input! Please enter a number.")
    print("Try again...")
# Security is important in today's digital world.
# End of Generator Script
print("Thank you for using the generator!")