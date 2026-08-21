# School Snack Counter: Sets and Arrays Assignment

# 1. Create snack boxes using sets
# (Sets automatically handle unique items)
box_a = {"apple", "banana", "popcorn", "juice"}
box_b = {"granola bar", "banana", "chips", "popcorn"}

print("Initial Snack Boxes:")
print(f"Box A: {box_a}")
print(f"Box B: {box_b}\n")

# 2. Add new snacks to the sets
box_a.add("pretzels")
box_b.add("grapes")

print("After Adding New Snacks:")
print(f"Box A updated: {box_a}")
print(f"Box B updated: {box_b}\n")

# 3. Find shared snacks (Intersection of two sets)
shared_snacks = box_a.intersection(box_b)
print(f"Shared snacks between Box A and Box B: {shared_snacks}\n")

# 4. Create an array (list) of snack counts
# Let's track how many snacks are in various boxes or daily distributions
snack_counts = [4, 5, 4, 6, 5]
print(f"Initial snack counts array: {snack_counts}")

# 5. Add values to the array
snack_counts.append(7)
snack_counts.append(5)
print(f"Snack counts after adding new values: {snack_counts}\n")

# 6. Use count() and reverse() to explore the final result
# Count how many times a specific snack count (e.g., 5) appears
target_count = 5
occurrences = snack_counts.count(target_count)
print(f"The snack count '{target_count}' appears {occurrences} times in the array.")

# Reverse the array elements in place
snack_counts.reverse()
print(f"Reversed snack counts array: {snack_counts}")
