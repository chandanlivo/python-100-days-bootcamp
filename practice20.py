def prime_number(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Its a prime number") 
    else:
        print("Its not a prime number")

n = int(input())
prime_number(number= n)