
MyNumber = 28

Attempts = 5
while Attempts >= 0:
    Guess = int(input("Guess my number between 1 and 50(You have 5 attempts):"))
    if Guess == MyNumber:
        print("Congratulations! You guessed the correct number.")
    else:
        if Guess >= 29 and Guess < 35:
            print("Hot")
        if Guess >= 35 and Guess < 40:
            print("Warm")
        if Guess >= 40 and Guess < 45:
            print("Cold")
        if Guess >= 45 and Guess < 50:
            print("Ice Cold")
        if Guess < 28 and Guess > 20:
            print("Hot")
        if Guess < 20 and Guess > 15:
            print("Warm")
        if Guess < 15 and Guess > 10:
            print("Cold")
        if Guess < 10 and Guess >= 1:
            print("Ice Cold")

    if Guess != MyNumber:
        Attempts -= 1
        print(f"Wrong guess! You have {Attempts} attempts left.")
    elif Attempts == 0:
        print("Sorry, you've run out of attempts. The correct number was 28.")

