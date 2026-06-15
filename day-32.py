import json
import os

DATA_FILE = "todo_list.json"

def load_tasks():
    """Loads tasks from a JSON file. Returns an empty list if file doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error reading data file. Starting with an empty list.")
        return []

def save_tasks(tasks):
    """Saves the current tasks list to a JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print("Error saving tasks to file.")

def add_task(tasks):
    """Adds a new task to the list."""
    title = input("\nEnter task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print(f"Task '{title}' added!")
    else:
        print("Task description cannot be empty.")

def view_tasks(tasks):
    """Displays the list of tasks with their status."""
    if not tasks:
        print("\nYour todo list is empty!")
        return

    print("\n--- Your Todo List ---")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} [{status}]")

def mark_completed(tasks):
    """Marks a specific task as completed."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("\nEnter the number of the task to mark complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[choice - 1]['title']}' marked as completed!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_completed(tasks):
    """Removes all completed tasks using a list comprehension."""
    initial_count = len(tasks)
    tasks[:] = [task for task in tasks if not task["completed"]]
    
    if len(tasks) < initial_count:
        save_tasks(tasks)
        print(f"🧹 Cleared {initial_count - len(tasks)} completed task(s).")
    else:
        print("\nNo completed tasks to clear.")

def main():
    """Main loop for the application."""
    tasks = load_tasks()

    while True:
        print("\n=== TODO MANAGER ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Clear Completed Tasks")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            clear_completed(tasks)
        elif choice == "5":
            print("\nGoodbye! 👋")
            break
        else:
            print("⚠️ Invalid choice. Please pick a number from 1 to 5.")

if __name__ == "__main__":
    main()