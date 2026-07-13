# The def Keyword (Custom Functions)

print("\033[1m" + "===  Valorant AI: Rank Predictor Function ===" + "\033[0m\n")

def predict_rank(Player_name, kills, deaths):
    if deaths == 0:
        deaths == 1

    kd_ratio = round(kills / deaths, 2)

    if kd_ratio >= 2.5:
        rank = "Radiant"
    elif kd_ratio >= 1.5:
        rank = "Ascendant"
    elif kd_ratio >= 1:
        rank = "Gold"
    else:
        rank = "Iron (Thoda Aim sahi karo bhai)"

    report = f"Player {Player_name} | K/D : {kd_ratio} | Predict Rank : {rank}"
    return report 
print("System Active! You Want to exit type Quit...\n")

while True:

    name_input = input("Enter Your Name : ")
    if name_input.lower() == "quit":
        print("System sutting down...Go")
        break
    kill_input = int(input("Enter Your kill : "))
    deaths_input = int(input("Enter Your Deaths : "))

    final_result = predict_rank(name_input, kill_input, deaths_input)
    print(final_result)


    



player1 = predict_rank("Zaynul", 12, 2)