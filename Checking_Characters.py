String = input("Please enter your own word: ")
Char = input("Please enter your own letter: ")
i = 0
count = 0
while(i < len(String)):
    if String[i] == Char:
        count += 1
    i += 1
print("The number of times the letter", Char, "appears in the word", String, "is:", count)