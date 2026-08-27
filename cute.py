import argparse
import sys

def process_cli():
    parser = argparse.ArgumentParser(
        description="File Processing CLI Tool",
        epilog="Example: python app.py input.txt -o output.txt --verbose"
    )

    # Positional Argument (Required)
    parser.add_argument("filename", help="Path to the input file")

    # Optional Arguments (Flags)
    parser.add_argument("-o", "--output", help="Path to save output file", default="result.txt")
    parser.add_argument("-l", "--lines", type=int, help="Number of lines to read", default=10)
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable detailed console output")

    args = parser.parse_args()

    if args.verbose:
        print(f"[LOG] Processing file: {args.filename}")
        print(f"[LOG] Output will be saved to: {args.output}")
        print(f"[LOG] Line limit set to: {args.lines}")

    print(f"Executing operation on '{args.filename}'...")

# Terminal execution test wrapper
if __name__ == "__main__":
    # Test arguments simulate kar rahe hain (real setup me sys.argv use hota hai)
    sys.argv = ["app.py", "data.csv", "-o", "cleaned.csv", "-v"]
    process_cli()