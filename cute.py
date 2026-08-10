import random
def team_generator():
    print("--- Random Team Generator ---")
    names_input = input("Enter names separated by commas:\n")
    names = [n.strip() for n in names_input.split(",") if n.strip()]
    if not names:
        print("No valid names entered!")
        return
    try:
        num_teams = int(input("How many teams do you want? "))
        if num_teams < 1 or num_teams > len(names):
            print("Invalid number of teams!")
            return
        random.shuffle(names)
        teams = {i: [] for i in range(1, num_teams + 1)}
        for i, name in enumerate(names):
            teams[(i % num_teams) + 1].append(name)
        print("\n--- Generated Teams ---")
        for team_num, members in teams.items():
            print(f"Team {team_num}: {', '.join(members)}")
    except ValueError:
        print("Please enter a valid number!")
if __name__ == "__main__":
    while True:
        team_generator()
        again = input("\nGenerate again? (y/n): ")
        if again.lower() != 'y':
            break
print("Have fun with your teams!")
print("Goodbye!")