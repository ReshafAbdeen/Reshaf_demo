import csv
from datetime import datetime
from pathlib import Path
from typing import Generator, Dict, Any


def stream_large_csv(file_path: Path) -> Generator[Dict[str, Any], None, None]:
    """Generator that yields rows one by one to save memory."""
    if not file_path.exists():
        raise FileNotFoundError(f"Target file missing: {file_path}")

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row


def clean_and_validate(row: Dict[str, str]) -> Dict[str, Any]:
    """Parses types, cleans strings, and handles malformed data."""
    try:
        return {
            "transaction_id": int(row["id"].strip()),
            "amount": float(row["amount"].replace("$", "").strip()),
            "date": datetime.strptime(row["date"].strip(), "%Y-%m-%d").date(),
            "status": row["status"].upper().strip(),
        }
    except (ValueError, KeyError) as e:
        return {"transaction_id": None, "error": f"Data corruption: {e}"}


def main():
    data_file = Path("./transactions.csv")
    
    if not data_file.exists():
        data_file.write_text("id,amount,date,status\n1, $150.50, 2026-06-01, pending\n2, bad_data, 2026-06-02, paid\n3, $99.00, 2026-06-03, paid\n")

    total_revenue = 0.0
    corrupted_count = 0

    print("Processing stream...")
    for raw_row in stream_large_csv(data_file):
        processed = clean_and_validate(raw_row)
        
        if processed.get("error"):
            corrupted_count += 1
            continue
            
        if processed["status"] == "PAID":
            total_revenue += processed["amount"]

    print(f"\n--- Processing Summary ---")
    print(f"Total Valid Revenue: ${total_revenue:.2f}")
    print(f"Skipped Corrupted Rows: {corrupted_count}")


if __name__ == "__main__":
    main()