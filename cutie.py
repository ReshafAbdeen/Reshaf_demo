import json, os
from datetime import datetime

FILENAME = "tasks.json"

def load_tasks():
    return json.load(open(FILENAME)) if os.path.exists(FILENAME) else []

def save_tasks(tasks):
    json.dump(tasks, open(FILENAME, "w"), indent=2)

def show_tasks(tasks):
    print("\n--- YOUR TASKS ---")
    today = datetime.now().date()
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else " "
        due = datetime.strptime(task["due"], "%Y-%m-%d").date()
        days_left = (due - today).days
        due_str = f"Due: {due} ({days_left}d left)" if days_left >= 0 else f"OVERDUE ({abs(days_left)}d ago)"
        print(f"{i}. [{status}] {task['title']} - {due_str}")

def main():
    tasks = load_tasks()
    while True:
        show_tasks(tasks)
        choice = input("\n[a]dd, [d]one, [q]uit: ").strip().lower()
        if choice == "a":
            title = input("Task title: ").strip()
            due = input("Due date (YYYY-MM-DD): ").strip()
            tasks.append({"title": title, "due": due, "done": False})
        elif choice == "d":
            idx = int(input("Task #: ")) - 1
            if 0 <= idx < len(tasks): tasks[idx]["done"] = True
        elif choice == "q":
            save_tasks(tasks); break

main()