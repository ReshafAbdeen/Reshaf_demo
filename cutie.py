import string
def check_password(password):
    score = 0
    if len(password) >= 8: score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    return score
print("--- Password Strength Checker ---")
while True:
    pwd = input("\nEnter password (or 'q' to quit): ")
    if pwd == 'q':
        print("Exiting tool...")
        break
    s = check_password(pwd)
    print("Strength: ", end="")
    if s == 5:
        print("Very Strong! 💪")
    elif s == 4:
        print("Strong! 👍")
    elif s >= 2:
        print("Weak! ⚠️")
    else:
        print("Very Weak! ❌")
    print(f"Score: {s}/5")
# Security matters
# Use a password manager
print("Goodbye!")
# End of Script