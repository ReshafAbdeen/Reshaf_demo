import sys


class CircularBuffer:

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, item):
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        if self.size < self.capacity:
            self.size += 1
        else:
            self.head = (self.head + 1) % self.capacity

    def dequeue(self):
        if self.size == 0:
            return None
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def get_all(self):
        return [
            self.buffer[(self.head + i) % self.capacity]
            for i in range(self.size)
        ]


cb = CircularBuffer(3)
cb.enqueue("A")
cb.enqueue("B")
cb.enqueue("C")
print("Full Buffer:", cb.get_all())
cb.enqueue("D")  # Overwrites 'A'
print("After Overwrite:", cb.get_all())
print("Dequeued:", cb.dequeue())
print("Final State:", cb.get_all())