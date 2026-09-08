import functools
import time


def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


start = time.perf_counter()
print(f"Fibonacci(35) result: {fibonacci(35)}")
first_run_time = time.perf_counter() - start
print(f"First run time: {first_run_time:.6f} seconds")

start = time.perf_counter()
print(f"Fibonacci(35) cached: {fibonacci(35)}")
second_run_time = time.perf_counter() - start
print(f"Second run time: {second_run_time:.6f} seconds")