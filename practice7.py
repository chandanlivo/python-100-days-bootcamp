year = int(input())
if year %2 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Its a leap year")
        else:
            print("Its not leap year")
    else:
        print("Its a leap year")
else:
    print("Its not a leap year")