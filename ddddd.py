# Rock, Paper, Scissors Game

import random
def play_rps():
    choices = ['rock', 'paper', 'scissors']
    u_score, c_score = 0, 0
    print("--- Rock, Paper, Scissors ---")
    while True:
        print(f"\nScore -> You: {u_score} | Comp: {c_score}")
        user = input("rock, paper, scissors (or 'q' to quit): ").lower()
        if user == 'q':
            break
        if user not in choices:
            print("Invalid input!")
            continue
        comp = random.choice(choices)
        print(f"Computer chose: {comp}")
        if user == comp:
            print("It's a tie!")
        elif (user == 'rock' and comp == 'scissors') or \
             (user == 'paper' and comp == 'rock') or \
             (user == 'scissors' and comp == 'paper'):
            print("You win this round!")
            u_score += 1
        else:
            print("Computer wins this round!")
            c_score += 1
    print(f"Final -> You: {u_score} | Computer: {c_score}")
if __name__ == "__main__":
    play_rps()
    print("Game Over!")
print("Bye!")