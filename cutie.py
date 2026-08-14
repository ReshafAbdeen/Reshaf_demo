import time
from functools import wraps

# The decorator function
def time_execution(func):
    """A decorator that prints how long a function took to run."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        print(f"[{func.__name__}] executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Applying the decorator
@time_execution
def compute_squares(n):
    return [i * i for i in range(n)]

# When you call this, the decorator automatically times it
compute_squares(500_000)