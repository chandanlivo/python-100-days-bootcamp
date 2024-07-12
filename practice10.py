print("Love calculator is calculating your score...")
name1 = input()
name2 = input()

combined_names = name1 + name2
final_name = combined_names.lower()

t = final_name.count('t')
r = final_name.count('r')
u = final_name.count('u')
e = final_name.count('e')
first_digit = t + r + u + e

l = final_name.count('l')
o = final_name.count('o')
v = final_name.count('v')
e = final_name.count('e')
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit)) 

if(score < 10) or (score > 90):
    print(f"Your love score is {score}, you go together like coke and mentos...")
elif(score >= 40) and (score <= 50):
    print(f"Your love score is {score}, you are alright together..")
else:
    print(F"Your love score is {score}, and forget her")

