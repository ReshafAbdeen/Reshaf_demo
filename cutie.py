import random
def play_rpg():
    print("--- Mini Text RPG ---")
    hp, gold = 20, 0
    while hp > 0:
        print(f"\nHP: {hp} | Gold: {gold}")
        print("1. Explore  2. Rest  3. Quit")
        choice = input("Choose action: ")
        if choice == '3':
            break
        elif choice == '2':
            heal = random.randint(2, 5)
            hp += heal
            print(f"You rested and gained {heal} HP.")
        elif choice == '1':
            event = random.choice(['monster', 'treasure', 'nothing'])
            if event == 'monster':
                dmg = random.randint(3, 8)
                hp -= dmg
                print(f"A monster attacked! You lost {dmg} HP.")
            elif event == 'treasure':
                coin = random.randint(10, 20)
                gold += coin
                print(f"You found a chest with {coin} gold!")
            else:
                print("You wandered safely but found nothing.")
        else:
            print("Invalid choice!")
    print(f"\nGame Over! Final Gold: {gold}")
play_rpg()import random
def play_rpg():
    print("--- Mini Text RPG ---")
    hp, gold = 20, 0
    while hp > 0:
        print(f"\nHP: {hp} | Gold: {gold}")
        print("1. Explore  2. Rest  3. Quit")
        choice = input("Choose action: ")
        if choice == '3':
            break
        elif choice == '2':
            heal = random.randint(2, 5)
            hp += heal
            print(f"You rested and gained {heal} HP.")
        elif choice == '1':
            event = random.choice(['monster', 'treasure', 'nothing'])
            if event == 'monster':
                dmg = random.randint(3, 8)
                hp -= dmg
                print(f"A monster attacked! You lost {dmg} HP.")
            elif event == 'treasure':
                coin = random.randint(10, 20)
                gold += coin
                print(f"You found a chest with {coin} gold!")
            else:
                print("You wandered safely but found nothing.")
        else:
            print("Invalid choice!")
    print(f"\nGame Over! Final Gold: {gold}")
play_rpg()