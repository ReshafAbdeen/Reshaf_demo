import threading
import time


class ThreadSafeCounter:

    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            current = self.value
            time.sleep(0.001)  # Simulate non-atomic operation
            self.value = current + 1


counter = ThreadSafeCounter()
threads = []

for _ in range(10):
    t = threading.Thread(target=lambda: [counter.increment() for _ in range(5)])
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter value (expected 50): {counter.value}")