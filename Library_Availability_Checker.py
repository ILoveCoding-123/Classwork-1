# Library Book Availability Checker: Advanced Python Functions

# 1. Pair book names with copy counts
# Creating initial lists for books and their available inventory counts
book_names = ["The Great Gatsby", "To Kill a Mockingbird", "1884", "Moby Dick", "Pride and Prejudice"]
copy_counts = [3, 0, 5, 2, 4]

# 2. Combine values with zip() 
# Creating a dictionary or list of tuples to pair the items together
book_inventory = list(zip(book_names, copy_counts))
print("Current Library Inventory:")
for book, count in book_inventory:
    print(f"- {book}: {count} copies available")
print("\n" + "="*40 + "\n")

# 3. Filter available books
# Extract only the books that have at least 1 copy available
available_books = [book for book, count in book_inventory if count > 0]
print("Available Books in Library:")
print(available_books)
print("\n" + "="*40 + "\n")

# 4. Update late fees using map()
# Let's say we have an initial list of standard late fees for overdue members
current_fees = [2.50, 5.00, 0.00, 1.75, 10.50]

# Standard fee increase function (e.g., adding a flat $1.50 fine increase)
def apply_fine_increase(fee):
    return fee + 1.50

# Applying map() to update all late fees simultaneously
updated_fees = list(map(apply_fine_increase, current_fees))
print("Updated Member Late Fees:")
print(f"Old Fees: {current_fees}")
print(f"New Fees: {updated_fees}")
print("\n" + "="*40 + "\n")

# 5. Stop the program early when a chosen book is unavailable
# Let's simulate a user trying to check out a specific book sequence
requested_books = ["1884", "To Kill a Mockingbird", "Moby Dick"]

print("Processing Checkout Requests:")
for book in requested_books:
    # Look up the inventory count for the requested book
    # Finding the index or matching it via dictionary lookup
    book_index = book_names.index(book)
    copies_left = copy_counts[book_index]
    
    if copies_left == 0:
        print(f"🛑 CRITICAL ERROR: '{book}' is unavailable! Halting checkout program immediately.")
        break # Stops the program loop early
        
    print(f"✅ Success: '{book}' is available. Processing loan...")