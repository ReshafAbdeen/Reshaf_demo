import random

print("\033[1m" + "=== Welcome to the Ultimate HANGMAN Game ===" + "\033[0m\n")
guess_word = ["python", "coding", "gamer", "laptop", "cheating"]
secret_word = random.choice(guess_word)

display_word = ["_"] * len(secret_word)
chance = 6
khali_jagah = []

print(f"Guess karo konsa word hai {' '.join(display_word)}")

while chance > 0 and "_" in display_word:
    print(f"Aapke pass sirf {chance} chance hai..")
    print(f"Gues kiya hua letter : {khali_jagah}")

    guess = input("Ek letter guess karo bhai : ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Gaandu ek letter daal.....")
        continue

    if guess in khali_jagah:
        print("Loodu dobara kiun daal rha hai wahi letter....")
        continue
    khali_jagah.append(guess)
    
    if guess in secret_word:
        print("Wah sahi guess kiya.")

        for index in range(len(secret_word)):
            if secret_word[index]==guess:
                display_word[index]=guess
    else:
        print("Bhak galt letterr daala..")
        chance -= 1


    print(f"word abhi tak aisa dikh rha hai {' '.join(display_word)}")

if "_" not in display_word:
    print("\n\033[1;32m" + f"CHAK DE PHATTE! Aapne word '{secret_word}' guess kar liya! Genius ho!" + "\033[0m")
else:
    print("\n\033[1;31m" + f"Bhoot poora ban gaya! Game Over! Sahi word tha: '{secret_word}'" + "\033[0m")

print("\n=== Game Over !!! ===")


