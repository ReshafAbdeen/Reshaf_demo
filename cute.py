class FibonacciIterator:
    def __init__(self, limit: int):
        self.limit = limit
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.a > self.limit:
            raise StopIteration  
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current

print(f"Fibonacci up to 50: {[num for num in FibonacciIterator(50)]}")