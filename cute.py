import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
            
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
            return
            
    print(f"\nGame over! You've run out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()