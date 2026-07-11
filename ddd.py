# Secure Password Generator & Strength Checker

import secrets
import string

def generate_secure_password(length=14):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-="
    
    all_chars = lower + upper + digits + symbols
    
    password = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]
    
    password += [secrets.choice(all_chars) for _ in range(length - 4)]
    
    secrets.SystemRandom().shuffle(password)
    final_password = "".join(password)
    
    strength = "Strong" if length >= 12 else "Moderate"
    
    return final_password, strength

pwd, strength = generate_secure_password(16)
print(f"Generated Password: {pwd}")
print(f"Password Strength:  {strength}")