def greet_customer():
    print("Welcome to my very own Lemonade Stand!")
    print("We sell the best lemonade in the world!")

greet_customer()

price_per_cup = float(input("How much would you like to charge per cup of lemonade? $"))
cups_sold = int(input("How many cups of lemonade did you sell today? "))

def calculate_total(price, cups):
    total = price * cups
    return total

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)

amount_paid = float(input("How much money did the customer pay you? $"))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def Thank_You_Message(cups):
    if cups >=5:
        print("Thank you for your purchase! You bought a lot of lemonade today!")
    else:
        print("Thank you for your purchase! Enjoy your lemonade!")

Closing_Message = Thank_You_Message(cups_sold)


print("")
print("=================Lemonade Stand Receipt=================")
print("Price per cup: $", price_per_cup)
print("Cups sold: ", cups_sold)
print("Total Cost: $", rounded_total)
print("Amount Paid: $", amount_paid)
print("Change Due: $", rounded_change)
print(Closing_Message)
print("========================================================")