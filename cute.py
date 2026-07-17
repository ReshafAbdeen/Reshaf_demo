# Text File Analyzer

import os
def analyze_file(filename):
    if not os.path.exists(filename):
        print(f"Error: '{filename}' does not exist.")
        return
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            total_lines = len(lines)
            words = sum(len(line.split()) for line in lines)
            chars = sum(len(line) for line in lines)
        print("\n--- File Analysis Report ---")
        print(f"File Name: {filename}")
        print(f"Total Lines: {total_lines}")
        print(f"Total Words: {words}")
        print(f"Total Characters: {chars}")
        print("----------------------------\n")
    except Exception as e:
        print(f"An error occurred: {e}")
print("--- Text File Analyzer ---")
while True:
    path = input("Enter filename (or 'q' to quit): ")
    if path.lower() == 'q':
        print("Exiting Analyzer...")
        break
    analyze_file(path)
# End of Script
print("Run again to analyze more files.")
# Keep coding!
print("Goodbye!")