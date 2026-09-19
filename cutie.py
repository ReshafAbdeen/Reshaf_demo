import string
from pathlib import Path

def check_password_strength(password: str) -> dict:
    """Evaluates the strength of a given password and returns a score and feedback."""
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters long")

    if any(char in string.ascii_lowercase for char in password):
        score += 1
    else:
        feedback.append("Missing lowercase letter")

    if any(char in string.ascii_uppercase for char in password):
        score += 1
    else:
        feedback.append("Missing uppercase letter")

    if any(char in string.digits for char in password):
        score += 1
    else:
        feedback.append("Missing number")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Missing special character")

    return {"score": score, "feedback": feedback}

def process_password_file(input_path: str, output_path: str) -> None:
    """Reads passwords from a file, evaluates them, and writes a report."""
    input_file = Path(input_path)
    
    if not input_file.exists():
        print(f"Error: {input_path} could not be found.")
        return

    passwords = input_file.read_text(encoding="utf-8").splitlines()
    report_lines = []

    for idx, pwd in enumerate(passwords, start=1):
        clean_pwd = pwd.strip()
        if not clean_pwd:
            continue
            
        result = check_password_strength(clean_pwd)
        status = "Strong" if result["score"] == 5 else "Needs Improvement"
        
        report_lines.append(f"Password {idx}: Score {result['score']}/5 [{status}]")
        if result["feedback"]:
            report_lines.append(f"  -> Suggestions: {', '.join(result['feedback'])}")
        report_lines.append("-" * 40)

    Path(output_path).write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Analysis complete! Report saved to '{output_path}'.")

if __name__ == "__main__":
    # Create a dummy input file for testing purposes
    sample_data = "weakpass\nCorrectHorseBatteryStaple!\nAdmin123!"
    Path("passwords.txt").write_text(sample_data, encoding="utf-8")

    # Run the batch processor
    process_password_file("passwords.txt", "password_report.txt")