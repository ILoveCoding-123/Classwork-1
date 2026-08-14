student_data = {
    "id1": {"name": "Tyler", "grade": "6", "subject_integration": "english, math, science"},
    "id2": {"name": "Matthew", "grade": "7", "subject_integration": "english, math, science"},
    "id3": {"name": "Tyler", "grade": "6", "subject_integration": "english, math, science"},
    "id4": {"name": "Robert", "grade": "8", "subject_integration": "english, math, science"},
}


result = {}
seen_keys = []


for student_id, details in student_data.items():
    unique_key = (details["name"], details["grade"], details["subject_integration"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details



for k, v in result.items():
    print(k, ";", v)