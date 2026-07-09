# The Execution Time Decorator

import time
from functools import wraps

def time_it(func):
    """A decorator that prints the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds.")
        return result
    return wrapper

@time_it
def process_data(data_size):
    """Simulates a time-consuming data processing task."""
    print(f"Processing {data_size} records...")
    total = 0
    for i in range(data_size):
        total += i * 2
    return total

if __name__ == "__main__":
    result = process_data(5000000)
    print(f"Final Result: {result}")