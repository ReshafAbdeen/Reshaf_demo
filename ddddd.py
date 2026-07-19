# Advanced Dice Roller Simulator

import random
def roll_dice():
    print("--- Advanced Dice Roller ---")
    history = []
    while True:
        try:
            sides = int(input("\nEnter number of sides (e.g., 6) or 0 to quit: "))
            if sides == 0:
                break
            if sides < 2:
                print("A dice must have at least 2 sides!")
                continue
            rolls = int(input("How many times to roll? "))
            if rolls < 1:
                print("Must roll at least once!")
                continue
            current_rolls = [random.randint(1, sides) for _ in range(rolls)]
            history.extend(current_rolls)
            print(f"You rolled: {current_rolls}")
            print(f"Total sum of this roll: {sum(current_rolls)}")
        except ValueError:
            print("Please enter valid integers!")
    if history:
        print("\n--- Session Statistics ---")
        print(f"Total rolls made: {len(history)}")
        print(f"Sum of all rolls: {sum(history)}")
        print(f"Highest roll achieved: {max(history)}")
        print(f"Average roll: {sum(history)/len(history):.2f}")
    print("Thanks for rolling with us!")
roll_dice()