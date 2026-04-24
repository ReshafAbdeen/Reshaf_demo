# My fisrt self made game

import random

def get_choices():
    player_choice = input("Enter your choice(rock, paper, scissors) = ")
    optin = ["rock", "paper", "scissor"]
    computer_choice = random.choice(optin)
    choice = {"player" : player_choice, "computer" : computer_choice}
    return choice

def check_win(player, computer):
    print(f"You choose {player}, Computer choose {computer}")

    if player == computer:
      return "Match is tie"
    elif player == "rock":
      if computer == "scissor":
       return "You choose Rock! You Win"
      else:
         return "You choose Paper! You loos"
    

    elif player == "paper":
      if computer == "rock":
        return "You choose Paper! You Win"
      else:
         return "You choose Scissor! You loos"
      
      
    elif player == "scissor":
      if computer == "paper":
        return "You choose Scissor! You Win"
      else:
         return "You choose Rock! You loos"
      
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)