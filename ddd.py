import sys
import time


class ProgressBar:

    def __init__(self, total, length=40, fill="█"):
        self.total = total
        self.length = length
        self.fill = fill

    def update(self, current, prefix="", suffix=""):
        percent = current / float(self.total)
        filled_len = int(self.length * current // self.total)
        bar = self.fill * filled_len + "-" * (self.length - filled_len)
        sys.stdout.write(
            f"\r{prefix} |{bar}| {percent:.1%} {suffix}"
        )
        sys.stdout.flush()
        if current == self.total:
            sys.stdout.write("\n")


items = list(range(0, 50))
progress = ProgressBar(len(items))

print("Starting Task Processing:")
for i, item in enumerate(items):
    time.sleep(0.05)
    progress.update(
        i + 1, prefix="Progress:", suffix=f"Completed {i + 1}/{len(items)}"
    )

print("Task Complete!")