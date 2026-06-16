class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to database: {self.db_name}")
        return self  

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Disconnecting from database: {self.db_name}")
        if exc_type:
            print(f"An error occurred: {exc_val}")

with DatabaseConnection("Production_DB") as db:
    print("Executing queries...")

