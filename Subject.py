# -------------------------------------------------------------
# Student Subject Record Cleaner
# -------------------------------------------------------------

# Step 1: Create a dictionary of student records
# The dictionary stores data as key-value pairs (Student Name: Subject)
student_records = {
    "Alice": "Mathematics",
    "Bob": "Science",
    "Charlie": "History",
    "David": "Science", # Duplicate subject for removal testing
    "Eva": "Mathematics", # Duplicate subject for removal testing
    "Frank": "Art"
}
print("Original Student Records:")
print(student_records)
print("-" * 50)


# Step 2: Access values safely
# Using the .get() method prevents the program from crashing if a key does not exist
search_student = "Charlie"
subject = student_records.get(search_student, "Student not found")
print(f"Safely accessed {search_student}'s subject: {subject}")

# Testing safe access for a non-existent student
missing_student = "Grace"
subject_missing = student_records.get(missing_student, "Student not found")
print(f"Safely accessed {missing_student}'s subject: {subject_missing}")
print("-" * 50)


# Step 3: Add and update records
# Adding a brand new student record
student_records["Grace"] = "Geography"
print("Added Grace's record.")

# Updating an existing student's subject
student_records["Alice"] = "Advanced Calculus"
print("Updated Alice's subject.")
print("-" * 50)


# Step 4: Remove unwanted entries or duplicates
# Example A: Remove a specific unwanted entry using pop()
unwanted_student = "Frank"
if unwanted_student in student_records:
    removed_subject = student_records.pop(unwanted_student)
    print(f"Removed {unwanted_student} (Subject: {removed_subject}) from records.")

# Example B: Clean the dictionary by removing duplicate subject entries
# We keep only the first student who selected a specific subject
cleaned_records = {}
seen_subjects = set()

for student, sub in student_records.items():
    if sub not in seen_subjects:
        cleaned_records[student] = sub
        seen_subjects.add(sub)

student_records = cleaned_records
print("Cleaned records (removed duplicate subject entries).")
print("-" * 50)


# Step 5: Check the dictionary length
total_records = len(student_records)
print(f"Total number of unique student records: {total_records}")
print("-" * 50)


# Step 6: Iterate through the final records
print("Final Cleaned Student Subject Records:")
for student, sub in student_records.items():
    print(f"- Student: {student} | Subject: {sub}")