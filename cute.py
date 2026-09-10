import time


class RateLimiter:

    def __init__(self, max_requests: int, time_window: float):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []

    def allow_request(self) -> bool:
        now = time.time()
        # Drop timestamps older than the time window
        self.requests = [
            t for t in self.requests if now - t < self.time_window
        ]
        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False


limiter = RateLimiter(max_requests=3, time_window=1.0)

print("Attempting 5 rapid API requests:")
for i in range(1, 6):
    allowed = limiter.allow_request()
    status = "200 OK" if allowed else "429 Too Many Requests"
    print(f"Request {i}: {status}")

print("\nWaiting for rate limit window to expire...")
time.sleep(1.1)

allowed = limiter.allow_request()
print(f"Request 6 (after cooldown): {'200 OK' if allowed else '429 Too Many Requests'}")