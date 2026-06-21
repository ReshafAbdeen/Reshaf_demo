import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs) 
        end_time = time.time()
        print(f"'{func.__name__}' took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def heavy_calculation(n):
    return sum([i**2 for i in range(n)])
heavy_calculation(5000000)