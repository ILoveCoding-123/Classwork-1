def calculate_discount():
    while True:
        try:
            # 1. Take user inputs
            total_bill = float(input("Enter the total shopping bill amount: "))
            discount_percentage = float(input("Enter the discount percentage (0-100): "))

            # 2. Validate values to prevent logical errors
            if total_bill < 0 or discount_percentage < 0:
                raise ValueError("Values cannot be negative.")
            if discount_percentage > 100:
                raise ValueError("Discount percentage cannot exceed 100%.")

            # 3. Calculate results
            discount_amount = total_bill * (discount_percentage / 100)
            final_bill = total_bill - discount_amount

        except ValueError as ve:
            # Catches string inputs (e.g., 'abc') or custom raised negative/overflow values
            print(f"Error: Invalid numerical input. ({ve})")
            print("Please try entering the details again.\n")
            
        except Exception as e:
            # Catches any other unexpected runtime errors gracefully
            print(f"An unexpected error occurred: {e}")
            print("Please try again.\n")
            
        else:
            # Runs ONLY if no exceptions were raised
            print("\n--- Bill Summary ---")
            print(f"Original Bill: ${total_bill:.2f}")
            print(f"Discount Applied: {discount_percentage}% (-${discount_amount:.2f})")
            print(f"Final Amount Due: ${final_bill:.2f}")
            break # Breaks the loop because valid bill details were processed
            
        finally:
            # Runs every single loop execution regardless of success or failure
            print("Processing transaction attempt completed.")
            print("-" * 40)

if __name__ == "__main__":
    calculate_discount()
