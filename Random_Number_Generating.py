import random
import string

def generate_password(length=12):
    # Ensure the password has at least one of each required type
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    num = random.choice(string.digits)
    
    # Combine all valid character pools for the remaining characters
    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
    # Fill up the rest of the password length randomly
    remaining_length = length - 3
    remaining_chars = [random.choice(all_characters) for _ in range(remaining_length)]
    
    # Combine all characters into a list
    password_list = [lower, upper, num] + remaining_chars
    
    # Shuffle the list to mix the characters randomly
    random.shuffle(password_list)
    
    # Convert the list back into a single string
    password = "".join(password_list)
    return password

# Main program block
if __name__ == "__main__":
    print("--- Random Password Challenge ---")
    
    # Ask the user for their desired password length
    try:
        user_length = int(input("Enter the desired password length (minimum 6): "))
        if user_length < 6:
            print("Length is too short. Defaulting to 12 characters.")
            user_length = 12
    except ValueError:
        print("Invalid input. Defaulting to 12 characters.")