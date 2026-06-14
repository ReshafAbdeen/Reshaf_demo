import json
import os

class Task:
    """Class to represent a single task."""
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.is_completed = False

    def mark_complete(self):
        self.is_completed = True

    def to_dict(self):
        """Convert object to dictionary for JSON saving."""
        return {
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed
        }

class ProjectManager:
    """Class to manage a collection of tasks and handle file I/O."""
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"✅ Task '{title}' added successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("\n📭 No tasks found.")
            return
        
        print("\n--- Current Tasks ---")
        for index, task in enumerate(self.tasks, start=1):
            status = "Done" if task.is_completed else "Pending"
            print(f"{index}. {task.title} [{status}]")
            print(f"   Description: {task.description}")

    def complete_task(self, index):
        try:
            self.tasks[index - 1].mark_complete()
            self.save_tasks()
            print(f"🎉 Task {index} marked as complete!")
        except IndexError:
            print("Invalid task number.")

    def save_tasks(self):
        """Saves the list of tasks to a JSON file."""
        with open(self.filename, 'w') as f:
            json_data = [task.to_dict() for task in self.tasks]
            json.dump(json_data, f, indent=4)

    def load_tasks(self):
        """Loads tasks from a JSON file if it exists."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                loaded_tasks = []
                for item in data:
                    task = Task(item['title'], item['description'])
                    task.is_completed = item['is_completed']
                    loaded_tasks.append(task)
                return loaded_tasks
        except Exception:
            print("Error loading saved tasks. Starting fresh.")
            return []

if __name__ == "__main__":
    manager = ProjectManager()
    
    print("--- Adding Tasks ---")
    manager.add_task("Learn Python OOP", "Understand classes, objects, and methods.")
    manager.add_task("Build a web app", "Use Flask or Django to make a backend.")
    
    manager.list_tasks()
    
    print("\n--- Completing a Task ---")
    manager.complete_task(1)
    
    manager.list_tasks()