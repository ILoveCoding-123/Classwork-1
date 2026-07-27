try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is error!!")
except SyntaxError:
    print("The comma is missing. Enter your number separated by a comma like this : 1, 2")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("I WILL ALWAYS EXECUTE")

