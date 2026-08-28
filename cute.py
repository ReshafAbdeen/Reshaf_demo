import json, os

FILENAME = "tasks.json"

def load_tasks():
    return json.load(open(FILENAME)) if os.path.exists(FILENAME) else []

def save_tasks(tasks):
    json.dump(tasks, open(FILENAME, "w"), indent=2)

def show_tasks(tasks):
    print("\n--- YOUR TASKS ---")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")

def main():
    tasks = load_tasks()
    while True:
        show_tasks(tasks)
        choice = input("\n[a]dd, [d]one, [q]uit: ").strip().lower()
        if choice == "a":
            tasks.append({"title": input("Task: ").strip(), "done": False})
        elif choice == "d":
            idx = int(input("Task #: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
        elif choice == "q":
            save_tasks(tasks)
            break

main()