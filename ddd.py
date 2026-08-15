import concurrent.futures
import time

def fake_download(file_id):
    """Simulates a task that takes time, like downloading a file."""
    print(f"Starting download for file {file_id}...")
    time.sleep(1.5) # Simulating network delay
    return f"File {file_id} data"

file_ids = [1, 2, 3, 4, 5]

start_time = time.time()

# Using a ThreadPoolExecutor to run downloads simultaneously
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Map applies the function to every item in the list concurrently
    results = executor.map(fake_download, file_ids)

    for result in results:
        print(f"Completed: {result}")

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds") 
# Will take ~1.5 seconds instead of 7.5 seconds!