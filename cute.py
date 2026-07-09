# Custom Context Manager (OOP & Magic Methods)import os

class SafeFileHandler:
    """Context manager for safely opening files and handling errors."""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        if self.file:
            self.file.close()
            print(f"Closed file: {self.filename}")
        if exc_type is not None:
            print(f"An error occurred and was safely caught: {exc_val}")
        return True 

if __name__ == "__main__":
    file_name = "test_log.txt"
    
    with SafeFileHandler(file_name, 'w') as f:
        f.write("Logging some intermediate Python data...\n")
        print("Data written successfully.")
        raise ValueError("Oops! A simulated error occurred.")

    if os.path.exists(file_name):
        os.remove(file_name) #