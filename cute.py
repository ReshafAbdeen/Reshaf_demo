from contextlib import contextmanager
import time

@contextmanager
def temporary_timer(label):
    """A context manager that times a specific block of code."""
    print(f"Starting block: {label}")
    start = time.time()
    try:
        # Code inside the 'with' block runs here
        yield 
    finally:
        # This always runs, even if the block throws an error
        end = time.time()
        print(f"Finished block: {label} (Took {end - start:.3f}s)\n")

# Using the custom context manager
with temporary_timer("Heavy Computation"):
    # Everything inside this block is timed
    total = sum(x**2 for x in range(1_000_000))
    print(f"Computation complete. Total digits: {len(str(total))}")