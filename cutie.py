import time
import random
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a fun and powerful programming language.",
    "Practice makes perfect when it comes to coding."
]
def typing_test():
    print("--- Typing Speed Tester ---")
    text = random.choice(sentences)
    print("\nType this exactly:")
    print(f"'{text}'")
    input("Press Enter when you are ready to start...")
    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()
    time_taken = end_time - start_time
    words = len(user_input.split())
    wpm = (words / time_taken) * 60 if time_taken > 0 else 0
    if user_input.strip() == text:
        print(f"\nPerfect! Time: {time_taken:.2f} seconds.")
        print(f"Your Speed: {wpm:.2f} WPM (Words Per Minute)")
    else:
        print("\nYou made some typos. Focus on accuracy!")
        print(f"Speed: {wpm:.2f} WPM. Keep practicing!")
if __name__ == "__main__":
    while True:
        typing_test()
        if input("\nTry again? (y/n): ").lower() != 'y': break
print("Keep typing to improve your speed!")