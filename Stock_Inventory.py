def main():

    Box_Sizes = [50, 20, 10, 5, 1]
    Total_Boxes_Used = {size: 0 for size in Box_Sizes}
    print("Packaging Breakdown Program")
    print("Enter product details. Type 'exit' as the product name to finish.\n")

    while True:
        product_name = input("Enter product name (or 'exit'): ").strip()
        if product_name.lower() == 'exit':
            break
        try:
            quantity = int(input(f"Enter quantity for {product_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue    
            except ValueError:
            print("Invalid input. Please enter a whole number.\n")
            continue 
        print(f"\nPackaging breakdown for {product_name} ({quantity}units):")
        remaining_quantity = quantity
        size_index = 0
        while size_index < len(Box_Sizes):
            current_box_size = Box_Sizes[size_index]
            boxes_needed = 0
            while remaining_quantity >= current_box_size:
                remaining_quantity -= current_box_size
                boxes_needed += 1
            if boxes_needed > 0:
                print(f"    -Size {current_box_size}: box {boxes_needed}")
                Total_Boxes_Used[current_box_size] += boxes_needed
            size_index += 1
            if remaining_quantity > 0:
                print(f"  - Leftover Individual Items: {remaining_quantity}")
                print("-" * 35 + "\n")

        print("\n===================================")
        print("                Final Packaging Report                         ")
        print("===================================")    
        boxes_printed = False
        for size in Box_Sizes:
            count = Total_Boxes_Used[size]
            if count > 0:
                print(f"Size {size}: {count} box(es)")
                boxes_printed = True
    if not boxes_printed:
        print("No boxes were used.")
        print("===================================")
if __name__ == "__main__":
    main()