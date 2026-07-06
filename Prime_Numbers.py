Lower = int(input("Enter a lower range: "))
Upper = int(input("Enter an upper range: "))

print("Prime numbers between", Lower, "and", Upper, "are:")
for num in range(Lower, Upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)