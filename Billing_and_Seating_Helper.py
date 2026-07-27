def calculate_tiered_discount(amount, group_size, /):
    """Calculates total bill after applying recursive tiered discounts based on group size.

    Every 5 additional guests unlock an extra 5% discount (up to 20% max).

    Args:
        amount (float): The total initial bill amount.
        group_size (int): The total number of guests in the party.

    Returns:
        float: The final bill amount after applying the total discount percentage.
    """
    def _get_discount_rate(size, rate=0.0):
        # Base cases: group size exhausted or max discount reached (20%)
        if size < 5 or rate >= 0.20:
            return rate
        # Recursive step: add 5% discount for every tier of 5 guests
        return _get_discount_rate(size - 5, rate + 0.05)

    discount_rate = _get_discount_rate(group_size)
    final_amount = amount * (1.0 - discount_rate)
    return round(final_amount, 2)


# ==========================================
# 2. SEATING HELPER (RECURSIVE)
# ==========================================

def assign_seats_recursively(party_name, party_size, seats_per_row, /):
    """Recursively breaks down and assigns a large party into row seating allocations.

    Args:
        party_name (str): The name of the reservation party.
        party_size (int): Remaining count of people to seat.
        seats_per_row (int): Maximum capacity per row.

    Returns:
        list[str]: A list of row assignment messages for the party.
    """

    def _seat_helper(remaining_guests, current_row):
        # Base case: Everyone has been seated
        if remaining_guests <= 0:
            return []

        # Determine seating for the current row
        guests_in_this_row = min(remaining_guests, seats_per_row)
        current_assignment = (
            f"Row {current_row}: Seated {guests_in_this_row} guest(s) for '{party_name}'"
        )

        # Recursive call for remaining guests
        return [current_assignment] + _seat_helper(
            remaining_guests - guests_in_this_row, current_row + 1
        )

    return _seat_helper(party_size, current_row=1)


# ==========================================
# 3. MAIN WORKFLOW
# ==========================================

def main():
    """Runs the main demonstration in VS Code."""
    print("=" * 50)
    print("      BILLING AND SEATING HELPER DEMO      ")
    print("=" * 50)

    # Sample Data
    party_name = "Smith Family Reunion"
    party_size = 14
    initial_bill = 450.00
    seats_per_row = 5

    # 1. Billing Calculation
    # Note: These parameters are positional-only (defined with `/`),
    # passing them positionally as (initial_bill, party_size) works as expected.
    final_bill = calculate_tiered_discount(initial_bill, party_size)

    print(f"\n--- BILLING SUMMARY ---")
    print(f"Party Name:     {party_name}")
    print(f"Party Size:     {party_size} guests")
    print(f"Initial Bill:   ${initial_bill:.2f}")
    print(f"Discounted Bill: ${final_bill:.2f}")

    # 2. Seating Assignment
    seating_plan = assign_seats_recursively(party_name, party_size, seats_per_row)

    print(f"\n--- SEATING PLAN ---")
    for assignment in seating_plan:
        print(f"  [+] {assignment}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()