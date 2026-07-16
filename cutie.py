quiz_data = {
    "What is 5 + 7?": "12",
    "What is the capital of France?": "paris",
    "Which language is this code written in?": "python"
}
def run_quiz():
    score = 0
    print("--- Welcome to the Mini Quiz ---")
    print("Answer the following 3 questions:\n")
    for question, correct_answer in quiz_data.items():
        print(question)
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == correct_answer:
            print("Correct! +1 point.\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}\n")
    return score
if __name__ == "__main__":
    final_score = run_quiz()
    total_qs = len(quiz_data)
    print(f"Quiz Complete! Your score: {final_score}/{total_qs}")
    if final_score == total_qs:
        print("Excellent! You got all of them right.")
    elif final_score > 0:
        print("Good effort! Keep learning.")
    else:
        print("Oops! Better luck next time.")
# Quiz module finished successfully
print("Thank you for playing!")