import sys
import time

seconds = 10
print("--- Countdown Timer ---")

while seconds > 0:
    sys.stdout.write(f"\rTime remaining: {seconds} seconds")
    sys.stdout.flush()
    time.sleep(1)
    seconds -= 1

print("\rTime's up! Complete.       ")