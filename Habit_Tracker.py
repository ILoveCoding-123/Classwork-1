# --- STEP 1: Creating Tuples ---
# Habit information tuple: (Habit Name, Target Days Per Week, Category)
habit_info = ("Exercise", 5, "Health")

# Weekly completion record tuple: (Day 1 to 7 status: 1 for done, 0 for not done)
# Let's say the user exercised on Mon, Wed, Fri, and Sat
completion_record = (1, 0, 1, 0, 1, 1, 0)

print("--- Habit Tracker Loaded ---")
print(f"Habit Details: {habit_info}")
print(f"Weekly Record (Mon-Sun): {completion_record}\n")


# --- STEP 2: Finding Tuple Length ---
# We use len() to find how many days are recorded
total_days_tracked = len(completion_record)
print(f"Total days tracked this week: {total_days_tracked} days")


# --- STEP 3: Accessing Values Using Indexing and Slicing ---
# Indexing: Get the status of the first day (Monday is index 0)
monday_status = completion_record[0]
print(f"Did you exercise on Monday? {'Yes' if monday_status == 1 else 'No'}")

# Slicing: Get the status for just the weekend (Saturday and Sunday are indices 5 and 6)
# Remember that the stop index in slicing is exclusive [start:stop]
weekend_status = completion_record[5:7]
print(f"Weekend completion record: {weekend_status}")

# Calculating total completed days using the sum() function
actual_days_completed = sum(completion_record)
print(f"Total days completed: {actual_days_completed} / {habit_info[1]}")


# --- STEP 4: Exploring Immutability (Why tuples cannot be changed directly) ---
print("\n--- Exploring Immutability ---")
print("Tuples are 'immutable', which means their values cannot be changed after creation.")
print("If we try to change Monday's status directly using: completion_record[0] = 0")

try:
    # This line will intentionally cause an error to prove tuples cannot be changed directly
    completion_record[0] = 0
except TypeError as error:
    print(f"❌ Python stopped us with a TypeError: {error}")
    print("To update a habit tracker dynamically, a developer would use a 'list' instead of a tuple.")
