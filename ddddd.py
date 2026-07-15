# Number Guessing Game

import random
def play_guessing_game():
    print("--- Number Guessing Game ---")
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    print(f"Guess a number (1-100). Max attempts: {max_attempts}")
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Keep it between 1 and 100!")
            elif guess < secret_number:
                print("Too low! Try higher.")
            elif guess > secret_number:
                print("Too high! Try lower.")
            else:
                print(f"You win! Guessed in {attempts} tries!")
                return
        except ValueError:
            print("Enter a valid integer!")
    print(f"Game Over! The number was {secret_number}.")
print("Starting game module...")
if __name__ == "__main__":
    play_guessing_game()
    replay = input("Play again? (y/n): ")
    if replay.lower() == 'y':
        play_guessing_game()
print("Thanks for playing!")