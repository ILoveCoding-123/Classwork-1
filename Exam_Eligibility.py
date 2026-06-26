health_issues = input("Do you have any health issues or medical conditions? (Y/N): ").strip().upper()

if health_issues == 'Y':
    print("You are allowed to take the exam.")
else:
    attendance = int(input("Enter your attendance: "))
    if attendance >= 75:
        print("You are allowed to take the exam.")
    else:
        print("You are not allowed to take the exam.")