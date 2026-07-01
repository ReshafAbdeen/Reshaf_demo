import time
from functools import lru_cache

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)  # Execute the actual function
        print(f"[{func.__name__}] Execution time: {time.perf_counter() - start_time:.6f}s")
        return result
    return wrapper

@timer_decorator
@lru_cache(maxsize=32)
def compute_heavy_math(n: int) -> int:
    return sum(i * i for i in range(n))

run1 = compute_heavy_math(5_000_000)
run2 = compute_heavy_math(5_000_000)  