from collections import Counter
import re

log_data = "INFO: User logged in\nERROR: Connection failed\nINFO: Page loaded\nERROR: Timeout"

try:
    errors = (line for line in log_data.split("\n") if "ERROR" in line)

    words = re.findall(r"\w+", " ".join(errors).lower())

    word_counts = Counter(words)

    print(f"Top Error Keywords: {word_counts.most_common(2)}")

except Exception as e:
    print(f"An error occurred during processing: {e}")