# Simple Alarm Clock


import time
import datetime
def set_alarm():
    print("--- Simple Alarm Clock ---")
    while True:
        alarm_time = input("Enter time in HH:MM (24-hour format) or 'q' to quit: ")
        if alarm_time.lower() == 'q':
            print("Exiting Alarm Clock...")
            break
        try:
            valid_time = datetime.datetime.strptime(alarm_time, "%H:%M")
            print(f"Alarm set for {alarm_time}. Waiting...")
            while True:
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M")
                if current_time == alarm_time:
                    print("\nWake up! BEEP BEEP BEEP!")
                    break
                time.sleep(10) # Check every 10 seconds
            break
        except ValueError:
            print("Invalid format! Use HH:MM like 07:30 or 14:45")
if __name__ == "__main__":
    set_alarm()
# Alarm clock module finished.
# Wake up early, be productive!
print("Run again to set a new alarm.")
# Stay punctual!
print("Goodbye!")
# End