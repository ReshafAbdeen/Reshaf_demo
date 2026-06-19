import json
import shutil
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path


class TransactionError(Exception):
    """Raised when a database transaction fails and requires a rollback."""

    pass


@dataclass
class UserRegistry:
    db_path: Path
    data: dict = field(default_factory=dict)

    def __post_init__(self):
        """Initializes the database file if it doesn't exist."""
        self.db_path = Path(self.db_path)
        if self.db_path.exists():
            self.load()
        else:
            self.save()

    def load(self) -> None:
        """Loads data directly from the JSON file."""
        with open(self.db_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def save(self) -> None:
        """Saves current state directly to the JSON file."""
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    @contextmanager
    def transaction(self):
        """Creates a temporary backup. Rolls back if any error occurs."""
        backup_path = self.db_path.with_suffix(".bak")
        shutil.copyfile(self.db_path, backup_path) 
        print("\n[Transaction Started] Backup created.")
        try:
            yield  
            self.save() 
            backup_path.unlink() 
            print("[Transaction Committed] Changes saved permanently.")
        except Exception as e:
            print(f"[Transaction Failed] Error: {e}. Rolling back...")
            shutil.copyfile(backup_path, self.db_path)
            backup_path.unlink()
            self.load() 
            raise TransactionError("Database rolled back to original state.") from e


if __name__ == "__main__":
    my_db_file = Path("user_store.json")
    registry = UserRegistry(db_path=my_db_file)

    with registry.transaction():
        registry.data["user_001"] = {"name": "Alice", "role": "Admin"}
        registry.data["user_002"] = {"name": "Bob", "role": "User"}

    print(f"Current DB State: {registry.data}")

    try:
        with registry.transaction():
            registry.data["user_003"] = {"name": "Charlie", "role": "Guest"}
            print("⚡ Simulating a sudden failure/crash mid-write...")
            raise KeyError("Simulated bad data payload structural error.")
    except TransactionError as e:
        print(f"Application Alert: {e}")

    print(f"Final Verified DB State: {registry.data}")

    if my_db_file.exists():
        my_db_file.unlink()