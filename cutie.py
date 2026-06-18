import time
from collections.abc import Generator
from functools import wraps


def monitor_performance(func):
    """A decorator that measures execution time and memory scale."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[START] Executing '{func.__name__}'...")
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"[END] '{func.__name__}' finished in {duration:.6f} seconds.")
        return result

    return wrapper


def stream_sensor_readings(limit: int) -> Generator[dict, None, None]:
    """A generator that lazily yields millions of simulated telemetry packets."""
    for i in range(1, limit + 1):
        yield {
            "id": i,
            "timestamp": time.time(),
            "reading": (i * 0.105) % 100,
        }


@monitor_performance
def process_data_stream(total_records: int):
    """Processes a stream of data efficiently using the generator."""
    data_stream = stream_sensor_readings(total_records)

    alert_count = 0
    for record in data_stream:
        if record["reading"] > 85.0:
            alert_count += 1

    print(f"Processed {total_records:,} items. Flagged {alert_count} alerts.")


if __name__ == "__main__":
    process_data_stream(2_000_000)