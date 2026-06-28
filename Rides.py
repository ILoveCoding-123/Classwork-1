print("Select your ride: ")
print("1. Bike")
print("2. Car")


choice = int( input("Enter your choice: ") )

 
if( choice == 1 ): 
  print( "what type of bike? " )
  print("1.Electric Bike\n")
  print("2.Dirt Bike\n")


  choice2=int(input("Enter you choice: "))
  if choice2==1: 
    print("you have selected electric bike")
  else:
    print("you have selected dirt bike")

#User entering option 2
elif( choice == 2 ): 
  print( "what type of car?" )
  print("1.Gas Car")
  print("2.Electric Car")
  choice3=int(input("enter your choice: "))

  if choice3==1: 
    print("you have selected gas car")
  else:
    print("you have selected electric car")

else:
  print("Wrong choice!")