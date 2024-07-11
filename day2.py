print("Welcome to bill calculator")
bill = input("What was the total bill $ ")
tip = input("How much tip would you like to give ? 10, 12 or 15 %")
person = input("How many people would you like to split ")

tip = int(bill)*(float(int(tip)/100))

bill = int(bill)+ float(tip)

final_bill = bill/int(person)

final_bill = "{:.2f}".format(final_bill)   # Formatting to 2 decimal places 33.60

print(f"Each person should pay: ${final_bill} ")  # F-string