import time
from functools import wraps

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {(end_time - start_time):.4f} seconds to execute.")
        return result
    return wrapper

@time_it
def compute_squares(n: int) -> list:
    return [i**2 for i in range(n)]

# Usage
squares = compute_squares(1_000_000)