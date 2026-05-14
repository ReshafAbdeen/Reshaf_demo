#MY FIRST PASSWORD GENERATOR PROGRAMM

import random
import string

def generate_password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(char)

    return password
    

try:
    size = int(input("Kitna lamba password dalna hai :"))
    
    if size < 4:
        print("Password 4 ank ka hona chahiye:")

    else:
        result = generate_password(size)
        print(f"Aapka password ye rha {result}")

except ValueError:
    print("Invald syntax ! Phirse try rakhe.")