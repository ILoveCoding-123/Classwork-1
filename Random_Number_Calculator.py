import math
import random


def show_menu():
    print("\n--- RANDOM FUN CALCULATOR ---")
    print("1. Generate a Lucky Number")
    print("2. Choose a Random Activity")
    print("3. Play a Number Guessing Game")
    print("4. Explore Math Module Functions")
    print("5. Exit")


def lucky_number():
    print("\n🍀 --- Lucky Number Generator ---")
    raw_num = random.uniform(10.0, 100.0)
    print(f"Generated raw decimal: {raw_num:.4f}")
    # Using math functions to format the lucky number
    print(f"Your lucky number (rounded up): {math.ceil(raw_num)}")
    print(f"Your lucky number (rounded down): {math.floor(raw_num)}")


def random_activity():
    print("\n🎯 --- Random Activity Picker ---")
    activities = [
        "Read a book for 15 minutes",
        "Do 20 jumping jacks",
        "Learn a new Python trick",
        "Drink a glass of water",
        "Listen to your favorite song",
        "Take a quick 5-minute walk",
    ]
    chosen = random.choice(activities)
    print(f"Your randomly selected activity is: '{chosen}'")


def guessing_game():
    print("\n🎲 --- Number Guessing Game ---")
    secret_number = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20. Can you guess it?")

    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(
                    f"🎉 Correct! You guessed the number in {attempts} attempts."
                )
                break
        except ValueError:
            print("Please enter a valid integer.")


def explore_math():
    print("\n📐 --- Exploring Math Module Functions ---")

    # 1. math.ceil() and math.floor()
    num = 7.3
    print(f"Original number: {num}")
    print(f" - math.ceil({num}) = {math.ceil(num)} (Rounds UP)")
    print(f" - math.floor({num}) = {math.floor(num)} (Rounds DOWN)")

    # 2. math.fabs()
    negative_num = -15.5
    print(
        f" - math.fabs({negative_num}) = {math.fabs(negative_num)} (Absolute Float Value)"
    )

    # 3. math.copysign()
    print(
        f" - math.copysign(50, -2) = {math.copysign(50, -2)} (Copies sign of second number to the first)"
    )

    # 4. math.gcd()
    a, b = 24, 36
    print(
        f" - math.gcd({a}, {b}) = {math.gcd(a, b)} (Greatest Common Divisor)"
    )


def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            lucky_number()
        elif choice == "2":
            random_activity()
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            explore_math()
        elif choice == "5":
            print("\nThank you for using the Random Fun Calculator! Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()