RowSize = int(input("Enter the number of rows: "))
if RowSize % 2 == 0:
    HalfDiamondRow = int(RowSize / 2)
else:
    HalfDiamondRow = int(RowSize/2) + 1
space = HalfDiamondRow - 1
for i in range(1, HalfDiamondRow + 1):
    for j in range(1, space + 1):
        print(end=" ")
    space -= 1
    num = 1
    for j in range(2*i - 1):
        print(end=str(num))
        num += 1
    print()
space = 1   
for i in range(1, HalfDiamondRow):
    for j in range(1, space + 1):
            print(end=" ")
    space += 1
    num = 1
    for j in range(1, 2 * (HalfDiamondRow - i)):
        print(end=str(num))
        num += 1
    print()
