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
def calculator():
    num1 = int(input("Enter the first number "))

    for operator in operations: 
        print(operator)

    should_continue = True
    while should_continue:
        operator_symbol = input("Pick an operator ")
        num2 = int(input("Enter the next number "))
        calculation_function = operations[operator_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation  ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()




