# Number Guessing Game# 2. NUMBER GUESSING GAME (30 Lines)
import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome! I am thinking of a number between 1 and 100.")

    while True:
        user_input = input("Take a guess: ").strip()
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(user_input)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You found it in {attempts} attempts.")
            break

if __name__ == "__main__":
    guessing_game()