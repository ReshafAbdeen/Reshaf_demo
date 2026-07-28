import time
def pomodoro_timer():
    print("--- Pomodoro Timer ---")
    try:
        w_time = int(input("Work time (seconds for demo): "))
        b_time = int(input("Break time (seconds for demo): "))
        cycles = int(input("Number of cycles: "))
        for i in range(1, cycles + 1):
            print(f"\n[Cycle {i}/{cycles}] Work for {w_time}s!")
            for w in range(w_time, 0, -1):
                print(f"\rWork time remaining: {w}s   ", end="")
                time.sleep(1)
            print("\nBEEP! Time for a break!")
            if i < cycles:
                print(f"Take a {b_time}s break.")
                for b in range(b_time, 0, -1):
                    print(f"\rBreak time remaining: {b}s   ", end="")
                    time.sleep(1)
                print("\nBEEP! Break is over!")
        print("\nPomodoro session completed! Great focus.")
    except ValueError:
        print("\nError: Please enter numbers only!")
    except KeyboardInterrupt:
        print("\nTimer stopped by the user.")
if __name__ == "__main__":
    pomodoro_timer()
# Boost your productivity!
print("Thank you for using the timer.")
# Goodbye!
# End of code