import random
playing = True
number = (random.randint(10, 25))
print("I will generate a number from 10 to 25, and you have to guess it. (You have unlimited attempts)")
print("The game ends when you get my number right.")
while playing:
    guess = int(input("Give me your best guess! \n"))
    if number == guess:
        print("You Win! You got the number right!")
        print("The number was",number)
        break
    else:
        print("Your guess isn't quite right. Try again. \n")

