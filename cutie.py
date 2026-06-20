from contextlib import contextmanager

@contextmanager
def managed_file(filename, mode):
    """Safely opens and closes a file, handling potential errors."""
    print(f" Opening {filename}...")
    file_obj = open(filename, mode)
    try:
        yield file_obj 
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
    finally:
        print(f" Closing {filename}...")
        file_obj.close()

with managed_file("sample.txt", "w") as f:
    f.write("Hello from an intermediate Python script!")