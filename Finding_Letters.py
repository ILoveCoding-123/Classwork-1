User_Word = input("Enter a word: ")

letter_count = 0
index = 0

while index < len(User_Word):
    letter_count += 1
    index += 1

print(f"The word '{User_Word}' has {letter_count} letters.")