grades_db = {}
def manage_grades():
    print("--- Mini Student Gradebook ---")
    while True:
        print("\n1. Add/Update Grade  2. View Grades  3. Exit")
        choice = input("Enter choice (1-3): ")
        if choice == '1':
            name = input("Enter student name: ").strip().title()
            try:
                grade = float(input(f"Enter {name}'s grade (0-100): "))
                if 0 <= grade <= 100:
                    grades_db[name] = grade
                    print(f"Saved: {name} -> {grade}")
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == '2':
            if not grades_db:
                print("No grades recorded yet.")
            else:
                print("\n--- Class Records ---")
                for student, gr in grades_db.items():
                    print(f"Student: {student} | Grade: {gr}")
                avg = sum(grades_db.values()) / len(grades_db)
                print(f"Class Average: {avg:.2f}")
        elif choice == '3':
            print("Exiting Gradebook...")
            break
print("Thank you for using the Gradebook App!")
manage_grades()