import random
import time
responses = [
    "It is certain.", "Without a doubt.", "You may rely on it.",
    "Yes, definitely.", "It is decidedly so.", "As I see it, yes.",
    "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
    "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
    "Cannot predict now.", "Concentrate and ask again.",
    "Don't count on it.", "My reply is no.", "My sources say no.",
    "Outlook not so good.", "Very doubtful."
]
def magic_8_ball():
    print("--- Magic 8 Ball Fortune Teller ---")
    while True:
        question = input("\nAsk a Yes/No question (or 'q' to quit): ")
        if question.lower() == 'q':
            print("The spirits bid you farewell...")
            break
        if not question.strip():
            print("You must ask a question!")
            continue
        print("Thinking", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print(f"\nAnswer: {random.choice(responses)}")
if __name__ == "__main__":
    magic_8_ball()
# Trust the magic 8 ball!
print("Goodbye!")