import os
import sqlite3
from datetime import datetime


class DatabaseManager:
    """Handles all direct interactions with the SQLite database."""

    def __init__(self, db_name="todo_list.db"):
        self.db_name = db_name
        self.setup_database()

    def setup_database(self):
        """Creates the tasks table if it doesn't already exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    status TEXT DEFAULT 'Pending'
                )
            """
            )
            conn.commit()

    def run_query(self, query, params=()):
        """A helper method to execute queries and return results."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchall()


class TaskManager:
    """Handles the business logic of managing tasks."""

    def __init__(self):
        self.db = DatabaseManager()

    def add_task(self, title):
        if not title.strip():
            print("\nTask title cannot be empty!")
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        query = "INSERT INTO tasks (title, created_at) VALUES (?, ?)"
        self.db.run_query(query, (title, timestamp))
        print(f"\nTask '{title}' added successfully!")

    def view_tasks(self):
        query = "SELECT id, title, created_at, status FROM tasks"
        tasks = self.db.run_query(query)

        if not tasks:
            print("\n📝 Your todo list is empty.")
            return

        print(f"\n--- {'ID':<4} | {'Task':<30} | {'Created At':<17} | {'Status':<10} ---")
        for task in tasks:
            print(
                f"    {task[0]:<4} | {task[1]:<30} | {task[2]:<17} | {task[3]:<10}"
            )

    def mark_completed(self, task_id):
        # Check if ID exists
        check_query = "SELECT id FROM tasks WHERE id = ?"
        if not self.db.run_query(check_query, (task_id,)):
            print(f"\nError: Task ID {task_id} not found.")
            return

        query = "UPDATE tasks SET status = 'Completed' WHERE id = ?"
        self.db.run_query(query, (task_id,))
        print(f"\nTask #{task_id} marked as completed!")

    def delete_task(self, task_id):
        check_query = "SELECT id FROM tasks WHERE id = ?"
        if not self.db.run_query(check_query, (task_id,)):
            print(f"\nError: Task ID {task_id} not found.")
            return

        query = "DELETE FROM tasks WHERE id = ?"
        self.db.run_query(query, (task_id,))
        print(f"\nTask #{task_id} deleted.")


def main():
    manager = TaskManager()

    while True:
        print("\n=== INTERMEDIATE TODO MANAGER ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            manager.view_tasks()
        elif choice == "2":
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
                manager.mark_completed(task_id)
            except ValueError:
                print("\nPlease enter a valid numerical ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("\nPlease enter a valid numerical ID.")
        elif choice == "5":
            print("\nGoodbye! Thanks for staying organized.")
            break
        else:
            print("\nInvalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()