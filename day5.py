import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
              'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
                'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', "#", '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '~']

print("Welcome to password generator")
nr_letters = int(input("How many letters would you like in your password.?"))
nr_numbers = int(input("How many numbers would you like in your password.?"))
nr_symbols = int(input("How many symbols would you like in your password.?"))

# Easy level 
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# print(password)

#Hard level
password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
print(password_list)
random.shuffle(password_list)
print(password_list)
print('\n')

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")