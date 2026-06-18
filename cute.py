import asyncio
import time


async def fetch_weather_data() -> dict:
    """Simulates a fast API call to a weather service."""
    print("Weather API: Starting request...")
    # asyncio.sleep simulates waiting for a network response without blocking Python
    await asyncio.sleep(1.5)
    print("Weather API: Data received!")
    return {"temp": "22°C", "condition": "Sunny"}


async def fetch_stock_prices() -> dict:
    """Simulates a slow API call to a financial service."""
    print("Stocks API: Starting request...")
    await asyncio.sleep(3.0)
    print("Stocks API: Data received!")
    return {"AAPL": 175.40, "TSLA": 210.15}


async def fetch_user_notifications() -> list:
    """Simulates a very fast database query for notifications."""
    print("Notifications: Querying database...")
    await asyncio.sleep(0.5)
    print("Notifications: Data received!")
    return ["New message from Bob", "Server update completed"]


async def main():
    start_time = time.time()
    print("Initializing Dashboard Data Fetch...\n")

    results = await asyncio.gather(
        fetch_weather_data(), fetch_stock_prices(), fetch_user_notifications()
    )

    weather, stocks, notifications = results

    print("\n================ DASHBOARD RESULTS ================")
    print(f"Weather: {weather['temp']}, {weather['condition']}")
    print(f"Stocks:  AAPL -> ${stocks['AAPL']}, TSLA -> ${stocks['TSLA']}")
    print(f"Alerts:  {len(notifications)} unread notifications")
    print("===================================================")

    total_time = time.time() - start_time
    print(f"⏱️ Total execution time: {total_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())