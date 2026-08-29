import random
import time


class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0

    def attack(self, target):
        damage = random.randint(10, 25)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def heal(self):
        amount = random.randint(15, 30)
        self.health = min(100, self.health + amount)
        print(f"{self.name} heals for {amount} HP! Current HP: {self.health}")


hero = Player("Hero")
monster = Player("Goblin")
monster.health = 80

print("--- Mini Arena Battle ---")
while hero.health > 0 and monster.health > 0:
    action = input("Choose action: [a]ttack or [h]eal: ").strip().lower()
    if action == "a":
        hero.attack(monster)
    elif action == "h":
        hero.heal()
    else:
        print("Invalid move, lost turn!")

    if monster.health > 0:
        time.sleep(0.5)
        monster.attack(hero)

    print(f"Status -> {hero.name}: {hero.health} HP | {monster.name}: {monster.health} HP\n")

print("Game Over!")
print(f"{'Hero won!' if hero.health > 0 else 'Monster won!'}")