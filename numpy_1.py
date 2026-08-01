# Category-Based Quote Generator

import random
quotes = {
    "Motivation": ["Never give up.", "Believe in yourself.", "Keep pushing forward."],
    "Life": ["Life is beautiful.", "Enjoy every moment.", "Smile often."],
    "Coding": ["Code never lies.", "Bugs are features.", "Keep calm and code on."]
}
def generate_quote():
    print("--- Random Quote Generator ---")
    categories = list(quotes.keys())
    while True:
        print("\nCategories:")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        choice = input("Choose a category number (or 'q' to quit): ")
        if choice.lower() == 'q':
            print("Exiting Quote Generator...")
            break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(categories):
                cat = categories[idx]
                quote = random.choice(quotes[cat])
                print(f"\n-> {cat}: \"{quote}\"")
            else:
                print("Invalid number!")
        except ValueError:
            print("Please enter a number!")
if __name__ == "__main__":
    generate_quote()
print("Have a great day!")