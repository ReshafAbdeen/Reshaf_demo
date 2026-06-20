import time
from functools import wraps

def timer_decorator(func):
    """A decorator that prints the execution time of a function."""
    @wraps(func)  
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"'{func.__name__}' took {execution_time:.6f} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def heavy_calculation(n):
    return sum(i * i for i in range(n))

result = heavy_calculation(1_000_000)