# Valorant Weapons Shop Manager

print("\033[1m" + "== Valorant Weapons Shop Manager ==" + "\033[0m\n")

def buy_weapon(budget, gun_name):
    if gun_name == "Vandal":
        if budget >= 2900: 
            budget -= 2900
            return f"Vandal Bought! {budget}$ left in your Account."
        else:
            return f"Bhai sirf {budget}$ hain, Vandal nahi aayegi. Pistol le le!"
            
    elif gun_name == "Operator":
        if budget >= 4700: 
            budget -= 4700
            return f"Operator Bought! {budget}$ left in your Account."
        else:
            return f"Bhai Operator 4700 ki aati hai, paise kam hain!"
            
    else:
        return f"Bhai Valorant hai, '{gun_name}' yahan nahi milti!"

while True:
    print("-" * 30)
    budget_input = int(input("Enter Your Budget (ya exit ke liye 0 likho): "))
    
    if budget_input == 0:
        print("Shop Closed! GG!")
        break
        
    gun_input = input("Enter Gun Name (Vandal/Operator): ")

    final_result = buy_weapon(budget_input, gun_input)

    print(final_result)


