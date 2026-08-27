import asyncio
import time

# Async Worker Task
async def fetch_data(task_id: int, delay: int):
    print(f"[Task {task_id}] Fetching data... (takes {delay}s)")
    await asyncio.sleep(delay)  # Non-blocking I/O sleep
    print(f"[Task {task_id}] Completed!")
    return {"task_id": task_id, "status": "Success"}

# Async Main Controller
async def main():
    start_time = time.time()
    
    # 3 tasks ko concurrently schedule karein
    tasks = [
        fetch_data(task_id=1, delay=3),
        fetch_data(task_id=2, delay=1),
        fetch_data(task_id=3, delay=2),
    ]
    
    # Run all tasks in parallel using gather
    results = await asyncio.gather(*tasks)
    
    elapsed = time.time() - start_time
    print(f"\nAll tasks finished in {elapsed:.2f} seconds!")
    print(f"Results: {results}")

# Execution
if __name__ == "__main__":
    asyncio.run(main())