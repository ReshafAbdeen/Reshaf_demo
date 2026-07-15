# Command-Line To-Do List

tasks = []
def show_tasks():
    print("\n--- To-Do List ---")
    if not tasks:
        print("No tasks available.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("------------------")
while True:
    show_tasks()
    print("\nOptions: 1. Add 2. Remove 3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        new_task = input("Enter task: ")
        tasks.append(new_task)
        print("Task added!")
    elif choice == '2':
        try:
            t_num = int(input("Task number: "))
            removed = tasks.pop(t_num - 1)
            print(f"Removed: {removed}")
        except (ValueError, IndexError):
            print("Invalid number!")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
# End of Program
print("Run again to manage tasks.")