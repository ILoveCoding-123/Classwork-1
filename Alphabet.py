Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
letter = input("Enter a letter from the alphabet, but if you enter anything that is not in the alphabet, it will not be accepted(only enter one letter): ")

if letter in Alphabet:
    print("You entered a letter or one letter from the alphabet.")
else:
    print("You did not enter a letter or one letter from the alphabet.")