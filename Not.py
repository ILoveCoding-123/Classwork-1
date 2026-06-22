a = 6
b = 14
c = 14
 
print(not (a == b))
print(not (b == c))

a = "Messi"
b = "Ronaldo"

if not (a == b):
    print("a, 'and' b, 'are different.'")

a = 10
b = 7

if not ((a == 10) == (b == 7)):
    print("Messi is the GOAT.")
     
a = int(input("Enter a number: "))

if not (a % 2 == 0):
    print(a, "is an odd number.")