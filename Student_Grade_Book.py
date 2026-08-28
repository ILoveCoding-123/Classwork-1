# 1. Dictionary created with at least 5 student name-score pairs (5 marks)
grade_book = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88
}

# 2. A loop correctly calculates and prints the class average (10 marks)
total_score = 0
for name in grade_book:
    total_score += grade_book[name]

class_average = total_score / len(grade_book)
print(f"Class Average: {class_average:.2f}")

# 3. Highest and lowest scores and students identified using max() and min() (10 marks)
# Finding the student with the highest score
highest_student = max(grade_book, key=grade_book.get)
highest_score = grade_book[highest_student]

# Finding the student with the lowest score
lowest_student = min(grade_book, key=grade_book.get)
lowest_score = grade_book[lowest_student]

print(f"Top Scorer: {highest_student} with a score of {highest_score}")
print(f"Bottom Scorer: {lowest_student} with a score of {lowest_score}")

# 4 & 5. .get() used to look up student with a friendly message if missing (10 marks)
# input() lets the user search for a student
search_name = input("\nEnter a student's name to look up their grade: ")

# Using .get() with a default friendly message if the key is missing
student_grade = grade_book.get(search_name, "Not Found")

if student_grade != "Not Found":
    print(f"{search_name}'s score is: {student_grade}")
else:
    print(f"Sorry, '{search_name}' is not in the grade book. Please check the spelling and try again.")


