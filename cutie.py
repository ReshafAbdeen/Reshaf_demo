#Digital Stopwatch

import time
def stop_watch():
    print("--- Simple Stopwatch ---")
    print("Press Enter to start, Ctrl+C to stop.")
    try:
        input("Ready? Press Enter...")
        print("Stopwatch started! Running...")
        start_time = time.time()
        while True:
            elapsed = time.time() - start_time
            mins, secs = divmod(int(elapsed), 60)
            ms = int((elapsed - int(elapsed)) * 100)
            timer = f"{mins:02d}:{secs:02d}.{ms:02d}"
            print(f"\rElapsed Time: {timer}", end="")
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\n\nStopwatch stopped!")
        end_time = time.time()
        total = end_time - start_time
        m, s = divmod(int(total), 60)
        ms_final = int((total - int(total)) * 100)
        print(f"Final Time: {m:02d}:{s:02d}.{ms_final:02d}")
if __name__ == "__main__":
    while True:
        stop_watch()
        again = input("\nRun again? (y/n): ")
        if again.lower() != 'y':
            break
print("Exiting Stopwatch...")
print("Goodbye!")