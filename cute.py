import json
from datetime import datetime


class TaskManager:

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load()

    def load(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, title):
        task = {"title": title, "done": False, "created": str(datetime.now())}
        self.tasks.append(task)
        self.save()
        print(f"Added task: '{title}'")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{idx}. [{status}] {task['title']}")

    def toggle_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.save()
            print("Task status updated!")


manager = TaskManager()
manager.add_task("Learn Python")
manager.add_task("Build a mini project")
manager.list_tasks()
manager.toggle_task(0)
manager.list_tasks()