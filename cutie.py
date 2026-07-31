def mad_libs_game():
    print("--- Mad Libs Story Generator ---")
    print("Provide some words to create a funny story!\n")
    name = input("Enter a person's name: ").strip().title()
    adj1 = input("Enter an adjective (e.g., silly, huge): ").strip()
    noun1 = input("Enter a noun (e.g., car, monkey): ").strip()
    verb_past = input("Enter a past tense verb: ").strip()
    place = input("Enter a place: ").strip().title()
    adj2 = input("Enter another adjective: ").strip()
    animal = input("Enter an animal: ").strip()
    food = input("Enter a type of food: ").strip()
    print("\n" + "="*30)
    print("Here is your funny story:")
    print("="*30)
    story = (
        f"One day, {name} visited {place}. "
        f"The weather was {adj1}, perfect for a trip. "
        f"Suddenly, a {animal} appeared with a {noun1}! "
        f"{name} got scared and {verb_past} all the way home. "
        f"To calm down, they ate {adj2} {food}. "
    )
    print(story)
    print("="*30)
if __name__ == "__main__":
    while True:
        mad_libs_game()
        if input("\nPlay again? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break
# Fun and simple Python string formatting example.