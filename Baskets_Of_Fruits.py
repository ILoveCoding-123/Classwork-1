Basket1 = {"apple", "banana", "mango", "apple", "grapes"}
Basket2 = {"mango", "kiwi", "banana", "grapes"}
print("Basket1:", Basket1)
print("Basket2:", Basket2)


Basket1.add("orange")
print("Basket1 after adding orange:", Basket1)


common_fruits = Basket1.intersection(Basket2)
print("Common fruits in both baskets:", common_fruits)


import array as arr
fruit_counts = arr.array('i', [3, 5, 2, 4])
print("Fruit counts after adding items:", fruit_counts)


count_of_4 = fruit_counts.count(4)
print("Number of times 4 appears:", count_of_4)


fruit_counts.reverse()
print("Reversed fruit counts array:", fruit_counts)


print("")
print("===== CLASS FRUIT BASKET ORGANIZER =====")
print("Basket 1:", Basket1)
print("Basket 2:", Basket2)
print("Common fruits in both baskets:", common_fruits)
print("Fruit counts:", fruit_counts)
print("========================================")