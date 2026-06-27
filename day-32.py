import os
import time
import psutil

print("--- System Performance Monitor ---")
try:
    while True:
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu}% | RAM Usage: {ram}%", end="\r")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nMonitoring stopped.                      ")