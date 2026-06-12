#The Mind Reader Game

import random
print("\033[1m" + "=== Welcome to the Mind Reader Game ===" + "\033[0m\n")
secret_number = random.randint(1, 20)
print("Maine 1 se 20 ke beech ek number socha hai Guess karo konsa hai ???")
lifeline = 7
sahiGuess = False

while lifeline > 0 and not sahiGuess:
    print()
    print(f"Aapke ke pass {lifeline} moke hai.")
    user = int(input("Enter Your Guess number : "))
    
    

    if user == secret_number:
        print("Wahhh1 Bhai sahi tum to genius ho...")
        sahiGuess = True
        
    elif user < secret_number:
        print("Bhai thoda bara number guess karo..")
        lifeline -= 1

    elif user < 1 or user > 20 :
        print("Warning !!!!  Bhai 1 se 20 ke beech hi number guess karo.. ")
        lifeline -= 1

    else:
        print("THoda chota number guess karo..")
        lifeline -= 1


if sahiGuess:
    print("\n\033[1;36m" + "Aap Jeet Gaye! Kya Mind Reading ki hai!" + "\033[0m")
else:
    print("\n\033[1;31m" + f"Lifelines Khatam! Game Over bhaiya. Sahi number {secret_number} tha!" + "\033[0m")

print("\033[1m" + "=== Game Over !!! ===" + "\033[0m\n")