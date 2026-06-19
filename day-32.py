import time
from contextlib import contextmanager


@contextmanager
def execution_timer(block_name: str):
    """Timer that automatically measures the execution of a 'with' block."""
    print(f"⏱️ [Entering] Starting timer for: '{block_name}'")
    start_time = time.perf_counter()

    try:
        yield
    finally:
        end_time = time.perf_counter()
        print(
            f"[Exiting] '{block_name}' took {end_time - start_time:.4f} seconds.\n"
        )


if __name__ == "__main__":
    with execution_timer("Heavy Calculation"):
        print("Processing data...")
        _ = [x**2 for x in range(5_000_000)]

    with execution_timer("Network Delay Simulation"):
        print("Simulating a slow network request...")
        time.sleep(0.5)