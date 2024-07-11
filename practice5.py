print("Welcome to the rollercoster...!")
height = int(input("Enter your height in cms: "))
if height > 120:
    print("You can ride  the rollercoster..")
    age = int(input("Enter your age: "))
    if age < 12:
        print("You have to pay $5")
    elif age <= 18:
        print("You have to pay $7")
    else:
        print("You have to pay $12")
else:
    print("You can't ride the rollercoster:(")