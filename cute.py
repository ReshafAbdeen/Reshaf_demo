import sys


def display_menu():
    """Prints the available options to the user."""
    print("\n" + "=" * 30)
    print("      TASK MANAGER MENU")
    print("=" * 30)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Exit")
    print("=" * 30)


def view_tasks(tasks):
    """Displays the current list of tasks."""
    if not tasks:
        print("\nYour task list is empty! Enjoy your free time.")
        return

    print("\n--- YOUR TASKS ---")
    for task_id, task_info in tasks.items():
        status = "✅ Done" if task_info["completed"] else "❌ Pending"
        print(f"[{task_id}] {task_info['name']} - Status: {status}")


def add_task(tasks):
    """Adds a new task to the dictionary."""
    task_name = input("\nEnter the task description: ").strip()
    if task_name:
        # Generate a simple incremental ID
        new_id = len(tasks) + 1
        tasks[new_id] = {"name": task_name, "completed": False}
        print(f"Success: '{task_name}' has been added.")
    else:
        print("Error: Task description cannot be empty.")


def complete_task(tasks):
    """Marks a specific task as completed."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_id = int(input("\nEnter the ID of the task you completed: "))
        if task_id in tasks:
            if tasks[task_id]["completed"]:
                print("That task is already marked as complete!")
            else:
                tasks[task_id]["completed"] = True
                print(f"Great job! '{tasks[task_id]['name']}' is marked complete.")
        else:
            print("Error: Invalid Task ID.")
    except ValueError:
        print("Error: Please enter a valid number.")


def main():
    """Main application loop."""
    # Seed data to start with
    todo_list = {
        1: {"name": "Buy groceries", "completed": False},
        2: {"name": "Read a book chapter", "completed": True},
    }

    print("Welcome to your personal productivity tracker.")

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            complete_task(todo_list)
        elif choice == "4":
            print("\nGoodbye! Stay productive.")
            sys.exit()