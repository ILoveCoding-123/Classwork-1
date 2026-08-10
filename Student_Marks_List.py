# Student Marks List Analyzer

# 1. Create a list from user input
print("--- Student Marks List Analyzer ---")
user_input = input("Enter student marks separated by spaces (e.g., 85 92 78 90): ")

# Convert the input string into a list of floating-point numbers
marks = [float(mark) for mark in user_input.split()]

# Check if the list is empty to prevent errors
if not marks:
    print("No marks entered. Exiting program.")
else:
    # 2. Find the length of the list
    num_students = len(marks)
    
    # 3. Demonstrate Indexing and Slicing (as requested in the overview)
    print("\n--- Indexing & Slicing Examples ---")
    print(f"First student's mark (Index 0): {marks[0]}")
    print(f"Last student's mark (Index -1): {marks[-1]}")
    if num_students >= 3:
        print(f"Top 3 marks entered (Slicing [:3]): {marks[:3]}")

    # 4. Iterate through marks and calculate the summary metrics
    total_marks = 0
    smallest_mark = marks[0]
    largest_mark = marks[0]

    for mark in marks:
        total_marks += mark
        
        if mark < smallest_mark:
            smallest_mark = mark
            
        if mark > largest_mark:
            largest_mark = mark

    # Calculate average
    average_mark = total_marks / num_students

    # 5. Display the clear summary
    print("\n--- Performance Summary ---")
    print(f"Total Number of Students : {num_students}")
    print(f"Total Marks Combined : {total_marks:.2f}")
    print(f"Average Mark : {average_mark:.2f}")
    print(f"Smallest Mark : {smallest_mark:.2f}")
    print(f"Largest Mark : {largest_mark:.2f}")