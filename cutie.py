import time


class PomodoroTimer:

    def __init__(self, work_mins=25, break_mins=5):
        self.work_sec = work_mins * 60
        self.break_sec = break_mins * 60

    def countdown(self, seconds, label):
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            print(f"\r[{label}] {mins:02d}:{secs:02d}", end="")
            time.sleep(1)
            seconds -= 1
        print(f"\n{label} finished!")

    def start(self, cycles=1):
        for i in range(1, cycles + 1):
            print(f"\n--- Cycle {i}/{cycles} ---")
            self.countdown(self.work_sec, "Work Session")
            if i < cycles:
                self.countdown(self.break_sec, "Short Break")


# Configured with 5-second demos instead of full minutes
demo_timer = PomodoroTimer(work_mins=0.1, break_mins=0.05)
print("Starting Pomodoro Demo...")
demo_timer.start(cycles=2)
print("All cycles completed! Time for a long break.")