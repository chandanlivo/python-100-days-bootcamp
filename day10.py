def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))

for operator in operations: 
    print(operator)
operator_symbol = input("Pick an operator ")
calculation_function = operations[operator_symbol]
first_answer = calculation_function(num1, num2)
print(f"{num1} {operator_symbol} {num2} = {first_answer}")

operator_symbol = input("Pick another operator ")
num3 = int(input("What is the next number "))
calculation_function = operations[operator_symbol]
second_answer = calculation_function(first_answer, num3)
print(f"{first_answer} {operator_symbol} {num3} = {second_answer}")

