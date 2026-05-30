from collections import Counter
import os

class LogEntry:
    """Represents a single log line parsed into structured data."""
    def __init__(self, timestamp, level, message):
        self.timestamp = timestamp
        self.level = level.strip()
        self.message = message.strip()

    def is_critical(self):
        """Simple business logic helper."""
        return self.level in ["ERROR", "CRITICAL"]


class LogAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.entries = []

    def load_logs(self):
        """Reads and parses the log file using exception handling."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Target log file '{self.file_path}' does not exist.")

        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    # Skip empty lines
                    if not line.strip():
                        continue
                    
                    parts = line.split(" - ", 2)
                    if len(parts) == 3:
                        self.entries.append(LogEntry(parts[0], parts[1], parts[2]))
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

    def generate_report(self):
        """Processes the loaded data using intermediate Python features."""
        if not self.entries:
            print("No logs to analyze. Did you load the file?")
            return

        print("=== LOG ANALYSIS REPORT ===")
        print(f"Total Log Entries Processed: {len(self.entries)}")

        level_counts = Counter(entry.level for entry in self.entries)
        print("\nLog Levels Breakdown:")
        for level, count in level_counts.items():
            print(f"  [{level}]: {count}")

        critical_errors = [entry.message for entry in self.entries if entry.is_critical()]
        
        print(f"\nTotal Critical Issues: {len(critical_errors)}")
        
        unique_criticals = sorted(list(set(critical_errors)), key=lambda x: x.lower())
        print("Unique Critical Issues (Sorted):")
        for issue in unique_criticals:
            print(f"  - {issue}")


# --- Demonstration Setup ---
if __name__ == "__main__":
    # 1. Create a dummy log file for testing purposes
    dummy_log_content = """2026-05-30 10:00:12 - INFO - User logged in
2026-05-30 10:01:45 - ERROR - Database connection failed
2026-05-30 10:02:30 - WARN - High memory usage detected
2026-05-30 10:05:12 - ERROR - Database connection failed
2026-05-30 10:06:01 - INFO - Dashboard loaded
2026-05-30 10:07:22 - ERROR - API Gateway Timeout"""

    sample_filename = "server.log"
    with open(sample_filename, "w") as f:
        f.write(dummy_log_content)

    # 2. Instantiate and run the analyzer
    analyzer = LogAnalyzer(sample_filename)
    
    try:
        analyzer.load_logs()
        analyzer.generate_report()
    except FileNotFoundError as e:
        print(e)
    finally:
        # Clean up the created file
        if os.path.exists(sample_filename):
            os.remove(sample_filename)