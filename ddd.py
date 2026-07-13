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

player1 = predict_rank("Zaynul", 12, 2)
player2 = predict_rank("Shoib", 4, 5)
player3 = predict_rank("Varish", 11, 4)

print(player1)
print(player2)
print(player3)