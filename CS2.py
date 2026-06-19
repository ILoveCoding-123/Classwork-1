actual_cost = float(input("Enter the Actual Product Price: "))
sale_amount = float(input("Enter the Sales Amount: "))

if (sale_amount < actual_cost):
    amount = actual_cost - sale_amount
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit!!!!")