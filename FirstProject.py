import datetime


class LogSystem:

    def __init__(self, filename="app.log"):
        self.filename = filename

    def _write_log(self, level, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] [{level.upper()}] {message}"
        print(entry)
        with open(self.filename, "a") as f:
            f.write(entry + "\n")

    def info(self, message):
        self._write_log("INFO", message)

    def warning(self, message):
        self._write_log("WARN", message)

    def error(self, message):
        self._write_log("ERROR", message)

    def read_logs((self)):
        try:
            with open(self.filename, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            return []


logger = LogSystem()
logger.info("Application started successfully.")
logger.warning("High memory usage detected!")
logger.error("Failed to connect to database.")

print("\n--- Reading Log File ---")
print("".join(logger.read_logs()[-3:]))