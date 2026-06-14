import random

def guess_game():
    secret_number = random.randint(1, 20)
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Awesome job! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Oops! Please enter a valid number.")

guess_game()