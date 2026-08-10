import time
import sys
def display_progress_bar():
    print("--- Terminal Progress Bar ---")
    total_tasks = 50
    bar_length = 30
    print("Starting task processing...\n")
    for i in range(total_tasks + 1):
        percent = 100 * (i / float(total_tasks))
        filled = int(bar_length * i // total_tasks)
        bar = '█' * filled + '-' * (bar_length - filled)
        sys.stdout.write(f"\rProgress: |{bar}| {percent:.1f}% Complete")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n\nTask processing finished successfully!")
def spinning_cursor():
    print("\nLoading data, please wait...")
    spinner = ['|', '/', '-', '\\']
    for _ in range(20):
        for char in spinner:
            sys.stdout.write(f"\rLoading... {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    print("\rLoading... Done!   ")
if __name__ == "__main__":
    display_progress_bar()
    spinning_cursor()
# CLI UI elements make apps look pro.
print("All tasks completed.")
print("Goodbye!")