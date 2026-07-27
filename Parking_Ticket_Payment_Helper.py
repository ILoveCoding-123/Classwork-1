class PaymentError(Exception):
    """Custom exception raised when a payment fails."""
    # Keyword: pass
    pass


# Keyword: def
def calculate_fine(violation_type, hours_overdue):
    """Calculates the fine amount based on violation type and overdue hours."""
    base_fine = 0.0

    # Keywords: if, elif, else, and, or
    if violation_type == "expired_meter" or violation_type == "meter":
        base_fine = 25.0
    elif violation_type == "handicap_zone":
        base_fine = 150.0
    elif violation_type == "no_parking_zone":
        base_fine = 75.0
    else:
        base_fine = 40.0  # Default fine for minor violations

    # Additional penalty for late payment
    # Keywords: if, and
    if hours_overdue > 24 and hours_overdue <= 72:
        base_fine += 20.0
    elif hours_overdue > 72:
        base_fine += 50.0

    # Keyword: return
    return base_fine


def apply_discount(fine_amount, promo_code):
    """Applies a discount code if valid."""
    # Keywords: is, None, not
    if promo_code is None or not promo_code:
        return fine_amount

    # Keywords: if, and, return
    if promo_code == "EARLYBIRD" and fine_amount >= 50.0:
        print("  [+] Applied 'EARLYBIRD' discount ($10.00 off).")
        return fine_amount - 10.0

    print("  [-] Invalid or non-applicable promo code.")
    return fine_amount


def process_payment(amount_due, payment_provided):
    """Validates and completes the transaction."""
    # Keywords: if, raise
    if payment_provided < amount_due:
        raise PaymentError(
            f"Insufficient payment! Required: ${amount_due:.2f}, Provided: ${payment_provided:.2f}"
        )

    change = payment_provided - amount_due
    # Keywords: return
    return change


def run_batch_processing(tickets):
    """Processes a batch of parking tickets using loop control keywords."""
    print("\n--- BATCH TICKET PROCESSING ---")

    # Keywords: for, in
    for ticket in tickets:
        ticket_id = ticket.get("id")
        is_paid = ticket.get("paid")

        # Keywords: if, is, True, continue
        if is_paid is True:
            print(f"Skipping Ticket #{ticket_id}: Already Paid.")
            continue

        # Keywords: if, is, False
        if is_paid is False:
            print(f"Processing Ticket #{ticket_id}...")
            # Keyword: break could be used here to halt processing on critical error

    # Keywords: return, True
    return True


def main():
    """Main workflow showcasing exception handling with keywords."""
    print("=" * 50)
    print("      PARKING TICKET PAYMENT HELPER      ")
    print("=" * 50)

    # Sample ticket data using Python literal keywords (None, True, False)
    violation_type = "handicap_zone"
    hours_overdue = 36
    promo_code = "EARLYBIRD"
    user_payment = 200.0

    print(f"Violation:     {violation_type}")
    print(f"Hours Overdue: {hours_overdue}")

    # Step 1: Calculate total fine
    total_fine = calculate_fine(violation_type, hours_overdue)
    print(f"Base Fine + Late Fees: ${total_fine:.2f}")

    # Step 2: Apply discount
    final_amount = apply_discount(total_fine, promo_code)
    print(f"Final Amount Due:      ${final_amount:.2f}")

    print("\nAttempting payment processing...")

    # Keywords: try, except, finally
    try:
        change = process_payment(final_amount, user_payment)
        print(f"  [ Success ] Payment accepted! Change returned: ${change:.2f}")

    except PaymentError as err:
        print(f"  [ Error ] Payment failed: {err}")

    finally:
        # Code in 'finally' ALWAYS executes regardless of errors
        print("\n[ Audit ] Ticket processing session closed.")

    # Demonstrating loop control keywords on a ticket batch
    batch_data = [
        {"id": 101, "paid": True},
        {"id": 102, "paid": False},
        {"id": 103, "paid": False},
    ]
    run_batch_processing(batch_data)


# Keywords: if, __name__
if __name__ == "__main__":
    main()