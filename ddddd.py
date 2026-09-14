import time
from functools import wraps


class RateLimiterTokenBucket:

    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_update = time.time()

    def _refill(self):
        now = time.time()
        delta = now - self.last_update
        self.tokens = min(self.capacity, self.tokens + delta * self.refill_rate)
        self.last_update = now

    def consume(self, tokens: int = 1) -> bool:
        self._refill()
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False


bucket = RateLimiterTokenBucket(capacity=5, refill_rate=2.0)

print("Consuming 5 tokens initially:")
for i in range(1, 6):
    print(f"Token {i} consumed: {bucket.consume()}")

print(f"\nConsuming 6th token immediately: {bucket.consume()}")

time.sleep(1.0)
print(f"\nConsuming token after 1 second refill: {bucket.consume()}")