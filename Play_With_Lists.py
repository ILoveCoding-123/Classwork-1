L = [10, 12, 8, 16, 6, 18]
print("Original List :", L)

count = 0

for i in L:
    count += 1

avg = count/len(L)

print("sum = ", count)
print("Average = ", avg)


L.sort()

print("Smallest element in the list is :", L[0])

print("Largest element in the list is :", L[-1])