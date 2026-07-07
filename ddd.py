#Password Generator & Validator

import random
import string
import re

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def validate_password(password):
    if len(password) < 8:
        return False, "Password too short."
    if not re.search(r"[a-z]", password):
        return False, "Needs lowercase letter."
    if not re.search(r"[A-Z]", password):
        return False, "Needs uppercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Needs number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Needs special character."
    return True, "Strong password!"

if __name__ == "__main__":
    print("--- Password Tool ---")
    new_pass = generate_password(14)
    print(f"Generated Password: {new_pass}")
    
    test_pass = input("Enter a password to validate: ")
    is_valid, message = validate_password(test_pass)
    print(f"Result: {message}")