import random
def guess_the_word():
    words = ["python", "hacker", "script", "server", "coding"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    print("--- Guess the Word Game ---")
    while attempts > 0 and "_" in guessed:
        print(f"\nWord: {' '.join(guessed)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single valid letter!")
            continue
        if guess in word:
            for i, char in enumerate(word):
                if char == guess:
                    guessed[i] = guess
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess!")
    if "_" not in guessed:
        print(f"\nCongratulations! Word was '{word}'.")
    else:
        print(f"\nGame Over! The word was '{word}'.")
if __name__ == "__main__":
    guess_the_word()
# End of Game
print("Play again later!")