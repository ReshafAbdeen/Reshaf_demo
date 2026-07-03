import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    attempts = 0
    print("Maine 1 se 20 ke beech ek number socha hai. Guess karo!")

    while attempts < 5:
        guess = int(input("Apna guess dalo: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Thoda bada number try karo.")
        elif guess > secret_number:
            print("Too high! Thoda chota number try karo.")
        else:
            print(f"Waah! Aapne {attempts} attempts me sahi guess kiya!")
            return

    print(f"Game Over! Sahi number {secret_number} tha.")

guess_the_number()