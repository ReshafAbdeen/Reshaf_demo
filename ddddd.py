import string

def check_password_strength(password: str) -> dict:
    """Evaluates the strength of a given password and returns a score and feedback."""
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if any(char in string.ascii_lowercase for char in password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if any(char in string.ascii_uppercase for char in password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if any(char in string.digits for char in password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    return {"score": score, "feedback": feedback}

if __name__ == "__main__":
    test_password = "SecurePassword123!"
    result = check_password_strength(test_password)
    print(f"Password Score: {result['score']}/5")
    if result["feedback"]:
        print("Suggestions:", result["feedback"])
    else:
        print("Strong password!")