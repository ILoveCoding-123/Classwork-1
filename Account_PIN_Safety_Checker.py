class AccountPINChecker:
    def __init__(self, username, pin):
        self.username = username
        # Encapsulation: Creating a private attribute for the PIN
        self.__pin = None
        
        # Initialize the PIN using our safe setter validation
        self.set_pin(pin)

    # Setter method to update and validate the private data safely
    def set_pin(self, new_pin):
        # Validation rule: PIN must be a string of exactly 4 digits
        if isinstance(new_pin, str) and new_pin.isdigit() and len(new_pin) == 4:
            self.__pin = new_pin
            print("✅ PIN updated successfully.")
        else:
            print("❌ Invalid PIN format! Must be a 4-digit numeric string.")

    # Special method to control how the object displays with print()
    def __str__(self):
        # Hide the actual PIN contents for safety display
        return f"Account User: {self.username} | PIN Security: [PROTECTED]"


# --- Test Cases to verify how private attributes behave ---
if __name__ == "__main__":
    print("--- 1. Creating Account ---")
    user_account = AccountPINChecker("Raju", "1234")

    print("\n--- 2. Printing the Object (__str__ method) ---")
    print(user_account)

    print("\n--- 3. Testing Direct External Access (Should fail/mangle) ---")
    try:
        # Trying to access the private attribute directly outside the class
        print(user_account.__pin)
    except AttributeError:
        print("🔒 Success: Cannot access '__pin' directly due to name mangling!")

    print("\n--- 4. Safely Updating Data using the Setter ---")
    user_account.set_pin("9876")      # Valid PIN update
    user_account.set_pin("abc1")      # Invalid PIN input
    user_account.set_pin("12345")     # Invalid length input

