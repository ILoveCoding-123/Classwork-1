class Pet:
    # The __init__ constructor initializes the object's attributes
    def __init__(self, name, breed, age, owner_name):
        self.name = name          # Stores pet's name
        self.breed = breed        # Stores pet's breed
        self.age = age            # Stores pet's age
        self.owner_name = owner_name  # Stores owner's name

    # Method to display the pet's full profile information
    def display_profile(self):
        print("\n--- 🐾 PET PROFILE 🐾 ---")
        print(f"Pet Name:   {self.name}")
        print(f"Breed:      {self.breed}")
        print(f"Age:        {self.age} years old")
        print(f"Owner:      {self.owner_name}")
        print("------------------------")


# --- Main Program Execution ---
def main():
    print("Welcome to the Pet Profile Builder!")
    print("Please enter the pet details below:\n")

    # Collecting input from the user
    name = input("Enter Pet's Name: ")
    breed = input("Enter Pet's Breed: ")
    age = input("Enter Pet's Age: ")
    owner = input("Enter Owner's Name: ")

    # Instantiating a new Pet object with the provided data
    my_pet = Pet(name, breed, age, owner)

    # Calling the method to show the profile
    my_pet.display_profile()


# Ensures the script runs when executed directly
if __name__ == "__main__":
    main()
