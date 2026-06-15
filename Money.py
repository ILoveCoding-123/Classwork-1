Amount = int(input("Please Enter the Amount for Withdrawal :"))
Note1 = Amount//100
Note2 = (Amount%100)//50
Note3 = ((Amount%100)%50)//10
Note4 = (((Amount%100)%50)%10)//1 
print("The number of 100 dollar notes is", Note1)
print("The number of 50 dollar notes is", Note2)
print("The number of 10 dollar notes is", Note3)
print("The number of 1 dollar notes is", Note4)