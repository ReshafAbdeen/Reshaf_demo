# Countdown Timerimport time
import sys
def countdown_timer():
    print("--- Countdown Timer ---")
    try:
        seconds = int(input("Enter time in seconds: "))
        if seconds <= 0:
            print("Please enter a positive number.")
            return
        print("Timer Started!")
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            sys.stdout.write(f"\rRemaining: {timer}")
            sys.stdout.flush()
            time.sleep(1)
            seconds -= 1
        print("\nTime's up! BEEP BEEP BEEP!")
    except ValueError:
        print("Invalid input! Enter an integer.")
    except KeyboardInterrupt:
        print("\nTimer stopped by user.")
if __name__ == "__main__":
    while True:
        countdown_timer()
        again = input("Set another timer? (y/n): ")
        if again.lower() != 'y':
            print("Exiting Timer App...")
            break
print("Goodbye!")