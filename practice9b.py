print("Thank you for choosing python pizza")
size = input()
add_pepperoni = input()
add_cheese = input()
bill =0

if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
else:
    bill += 25

if add_pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

if add_cheese == 'y':
    bill += 1

print(f"Your final bill is {bill}")
