print("Enter the grades of Tyler in his 4 subjects: ")
Math = int(input("Math: "))
Science = int(input("Science: "))   
Writing = int(input("Writing: "))
Reading = int(input("Reading: "))
Sum = Math + Science + Writing + Reading
print("The sum of all the grades is ", Sum)
Grade = (Sum/400)*100
print(end="His grade is ")
print(Grade)