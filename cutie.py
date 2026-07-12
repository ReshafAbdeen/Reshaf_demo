# Simple Todo List Application


# 1. SIMPLE TODO LIST APPLICATION (30 Lines)
def show_menu():
    print("\n--- TODO MENU ---")
    print("1. Add Task\n2. View Tasks\n3. Exit")

def todo_app():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            task = input("Enter the task: ").strip()
            if task:
                tasks.append(task)
                print(f"'{task}' added successfully!")
        elif choice == "2":
            if not tasks:
                print("Your todo list is empty!")
            else:
                print("\n--- YOUR TASKS ---")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    todo_app()