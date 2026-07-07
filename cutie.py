#Command-Line To-Do List

def display_tasks(tasks):
    print("\n--- To-Do List ---")
    if not tasks:
        print("List is currently empty.")
    for i, t in enumerate(tasks, 1):
        status = "[x]" if t['done'] else "[ ]"
        print(f"{i}. {status} {t['name']}")

def main():
    tasks = []
    while True:
        display_tasks(tasks)
        print("\n1. Add Task  2. Mark Done  3. Quit")
        choice = input("Choice: ")
        
        if choice == '1':
            tasks.append({"name": input("Task: "), "done": False})
        elif choice == '2':
            try:
                idx = int(input("Task Number: ")) - 1
                tasks[idx]['done'] = True
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()