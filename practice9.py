print("Welcome to Python Pizza :)")
print("Choose the size of the pizza: S, M, L, ")
size = input()
bill = 0
if size == 's':
    bill = 15
    print("Price of small pizza is $15")
    print("would you like to add pepperoni($3)")
    add_pepperoni = input()
    if add_pepperoni == 'y':
        bill += 2
    print(f"Your bill is {bill}")

    print("would you like to add cheese($1)")
    add_cheese = input()
    if add_cheese == 'y':
        bill += 1
    print(f"Your final bill is {bill}")
elif size == 'm':
    bill = 20
    print("Price of medium pizza is $20")
    print("would you like to add pepperoni($3)")
    add_pepperoni = input()
    if add_pepperoni == 'y':
        bill += 3
    print(f"Your bill is {bill} ")

    print("would you like to add cheese($1)")
    add_cheese = input()
    if add_cheese == 'y':
        bill += 1
    print(f"Your final bill is {bill}")
else:
    bill = 25
    print("Price of large pizza is $25")
    print("would you like to add pepperoni($3)")
    add_pepperoni = input()
    if add_pepperoni == 'y':
        bill += 3
    print(f"Your bill is {bill}")

    print("would you like to add cheese($1)")
    add_cheese = input()
    if add_cheese == 'y':
        bill += 1
    print(f"Your final bill is {bill}")
print("Thank you for choosing PYTHON pizza")