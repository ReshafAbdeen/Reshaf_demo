import os
def manage_notes():
    print("--- Quick Notes App ---")
    file_name = "my_notes.txt"
    while True:
        print("\n1. Read Notes  2. Add Note  3. Clear  4. Exit")
        choice = input("Choose (1-4): ")
        if choice == '1':
            if os.path.exists(file_name):
                with open(file_name, 'r') as f:
                    content = f.read()
                    print("\n--- Your Notes ---")
                    print(content if content else "Empty!")
            else:
                print("No notes found. Add one first!")
        elif choice == '2':
            note = input("Write your note: ")
            with open(file_name, 'a') as f:
                f.write(note + "\n")
            print("Note saved successfully!")
        elif choice == '3':
            open(file_name, 'w').close()
            print("All notes cleared!")
        elif choice == '4':
            print("Exiting Notes App...")
            break
        else:
            print("Invalid choice, try again.")
if __name__ == "__main__":
    manage_notes()