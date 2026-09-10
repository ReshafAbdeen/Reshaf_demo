import queue
import time


class TaskQueue:

    def __init__(self):
        self.task_queue = queue.PriorityQueue()

    def add_task(self, name, priority):
        # Priority Queue processes lowest numbers first (1 = highest priority)
        self.task_queue.put((priority, name))
        print(f"Enqueued task: '{name}' with priority {priority}")

    def process_all(self):
        print("\n--- Processing Tasks in Priority Order ---")
        while not self.task_queue.empty():
            priority, name = self.task_queue.get()
            print(f"Processing '{name}' (Priority {priority})...")
            time.sleep(0.1)
            self.task_queue.task_done()
        print("All tasks completed!")


tq = TaskQueue()
tq.add_task("Send daily report", priority=3)
tq.add_task("Fix critical security bug", priority=1)
tq.add_task("Update documentation", priority=4)
tq.add_task("Review pull requests", priority=2)

tq.process_all()