import random
import string

length = 12
chars = string.ascii_letters + string.digits + string.punctuation
password = [random.choice(chars) for _ in range(length)]

random.shuffle(password)
final_password = "".join(password)

print("--- Secure Password Generator ---")
print(f"Your new password is: {final_password}")