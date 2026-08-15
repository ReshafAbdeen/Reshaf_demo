from collections import Counter, defaultdict

# --- Counter: Easily count occurrences of items ---
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)

print(f"Top 2 words: {word_counts.most_common(2)}")
# Output: Top 2 words: [('apple', 3), ('banana', 2)]

# --- defaultdict: Handle missing dictionary keys gracefully ---
# Instead of throwing a KeyError, it automatically creates a default value (e.g., an empty list)
student_grades = [('Alice', 85), ('Bob', 90), ('Alice', 92), ('Charlie', 78)]
grade_book = defaultdict(list)

for name, grade in student_grades:
    grade_book[name].append(grade)

print("Grade Book:", dict(grade_book))
# Output: {'Alice': [85, 92], 'Bob': [90], 'Charlie': [78]}