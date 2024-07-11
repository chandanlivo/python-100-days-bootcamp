print("Welcome to the rollercoster...!")
height = int(input("Enter your height in cms: "))
bill = 0
if height > 120:
    print("You can ride  the rollercoster..")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("child tickets are $5")
    elif age <= 18:
        bill = 7
        print("teenagers tickets are $7")
    else:
        bill = 12
        print("adult tickets are $12")
    
    #Photo requirement
    want_photo = input("Do you want photo? 'Y' or 'N' ")
    if want_photo == 'Y' or 'y':
        bill += 3
    print(f"Your final bill is {bill}")

else:
    print("You can't ride the rollercoster:(")