def calculate_change(paid, price):
    change = paid - price
    return change

snack_price = 200
print("===== Snack Vending Machine =====")
print(f"All the snacks are {snack_price} cents.")
print("Accepted coins: 1, 2, 5, 10, 25")

total_inserted = 0
coins_inserted = 0


while True:
    coin = int(input("Insert a coin (1, 2, 5, 10, 25): "))


    if coin != 1 and coin != 2 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin. Please insert a valid coin.")
        continue

    total_inserted += coin
    coins_inserted += 1

    if total_inserted >= snack_price:
        print("Enough money inserted!\n")
        break

change_due = calculate_change(total_inserted, snack_price)

print("Dispensing your snack...")

if change_due == 0:
    pass
else:
    print(f"Here's your change: {change_due} cents")


print("\n======Snack Receipt=====")
print("Snack Price:", snack_price)
print("Coins Inserted:", coins_inserted)
print("Total Paid:",total_inserted)
print("Change Given:",change_due)
print("========================")
print("Thanks for your purchase!")
