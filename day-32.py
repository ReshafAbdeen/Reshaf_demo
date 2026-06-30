import asyncio
import random

async def fetch_api_data(endpoint_id: int) -> dict:
    print(f"Starting request to API #{endpoint_id}...")
    await asyncio.sleep(random.uniform(0.5, 1.5))
    return {"endpoint": endpoint_id, "status": "Success", "data": random.randint(100, 999)}

async def main():
    tasks = [fetch_api_data(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    print(f"\nAll data retrieved successfully:\n{results}")

asyncio.run(main())