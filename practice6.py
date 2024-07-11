height = input("Enter your height\n")
weight = input("Enter your weight\n")
w = int(weight)
h = float(height)
bmi = w/h**2 #bmi = w/(h*h)

print(bmi)

if bmi <18.5 :
    print("You are underwieight.")
elif bmi < 25:
    print("You have normal weight")
elif bmi < 30:
    print("You are slightly overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")