Rows = int(input("Please enter the number of rows: "))
Number = 1
print("Floyd's Triangle")
for i in range(1, Rows + 1):
    for j in range(1, i + 1):
        print(Number, end=' ')
        Number += 1
    print()