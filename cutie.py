print("--- Student Grading System ---")
student_name = input("Enter Student Name: ")
subjects = ["Maths", "Science", "English"]
marks = []

for sub in subjects:
    score = float(input(f"Enter marks for {sub} (out of 100): "))
    marks.append(score)

total_marks = sum(marks)
percentage = (total_marks / (len(subjects) * 100)) * 100
grade = "A" if percentage >= 80 else "B" if percentage >= 60 else "C" if percentage >= 40 else "Fail"

print(f"\n--- Result for {student_name} ---")
print(f"Total Marks: {total_marks} / 300 | Percentage: {percentage:.2f}%")
print(f"Final Grade: {grade}")