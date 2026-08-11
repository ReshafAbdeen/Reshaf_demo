import os
import datetime
def diary_app():
    print("--- Personal Diary App ---")
    filename = "my_diary.txt"
    while True:
        print("\n1. Write Entry  2. Read Diary  3. Exit")
        choice = input("Choose option (1-3): ")
        if choice == '1':
            entry = input("Write your thought: ")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            with open(filename, 'a') as f:
                f.write(f"[{timestamp}] {entry}\n")
            print("Entry saved successfully!")
        elif choice == '2':
            if os.path.exists(filename):
                print("\n--- Your Diary Entries ---")
                with open(filename, 'r') as f:
                    print(f.read().strip())
                print("-" * 26)
            else:
                print("Diary is empty. Write something first!")
        elif choice == '3':
            print("Exiting Diary App...")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    diary_app()
print("Goodbye!")