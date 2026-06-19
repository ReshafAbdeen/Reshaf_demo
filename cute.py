from datetime import datetime
from typing import Any, Dict, List, Optional


class ValidationError(Exception):
    """Raised when an incoming API request payload violates structural rules."""

    pass


class InventoryItemRequest:
    """Validates and structures a raw JSON payload for an inventory system."""

    def __init__(self, payload: Dict[str, Any]):
        self.raw_data = payload
        self.errors: List[str] = []

        # Extract, typecast, and validate properties safely
        self.item_id: str = self._validate_string("item_id", min_len=5)
        self.price: float = self._validate_numeric("price", min_val=0.01)
        self.quantity: int = int(self._validate_numeric("quantity", min_val=0))
        self.tags: List[str] = self._validate_tags()
        self.timestamp: datetime = self._validate_datetime()

        if self.errors:
            raise ValidationError(
                f"Validation Failed! Errors encountered: {self.errors}"
            )

    @property
    def total_valuation(self) -> float:
        """Calculates total value dynamically on demand."""
        return round(self.price * self.quantity, 2)

    def _validate_string(self, key: str, min_len: int) -> str:
        val = self.raw_data.get(key)
        if not isinstance(val, str) or len(val.strip()) < min_len:
            self.errors.append(
                f"'{key}' must be a string with at least {min_len} chars."
            )
            return ""
        return val.strip()

    def _validate_numeric(self, key: str, min_val: float) -> float:
        val = self.raw_data.get(key)
        if not isinstance(val, (int, float)) or val < min_val:
            self.errors.append(f"'{key}' must be a number >= {min_val}.")
            return 0.0
        return float(val)

    def _validate_tags(self) -> List[str]:
        tags = self.raw_data.get("tags", [])
        if not isinstance(tags, list) or not all(
            isinstance(t, str) for t in tags
        ):
            self.errors.append("'tags' must be a list of strings.")
            return []
        return [t.lower().strip() for t in tags]

    def _validate_datetime(self) -> datetime:
        ts_str = self.raw_data.get("timestamp", "")
        try:
            return datetime.fromisoformat(ts_str)
        except (ValueError, TypeError):
            self.errors.append(
                "'timestamp' must be a valid ISO 8601 string."
            )
            return datetime.min


if __name__ == "__main__":
    valid_payload = {
        "item_id": "PROD-9982X",
        "price": 249.99,
        "quantity": 12,
        "tags": ["Electronics ", " AUDIO "],
        "timestamp": "2026-06-19T22:40:00",
    }

    request = InventoryItemRequest(valid_payload)
    print(f"Success! Item ID: {request.item_id}")
    print(f"Normalized Tags: {request.tags}")
    print(f"Total Value on Hand: ${request.total_valuation:,}")

    malformed_payload = {
        "item_id": "PROD",  
        "price": -10.50,  
        "quantity": "Ten",  
        "timestamp": "Not-A-Date",
    }

    print("\nTrying to parse invalid payload...")
    try:
        InventoryItemRequest(malformed_payload)
    except ValidationError as e:
        print(f"Trapped Expected Request Failure:\n{e}")