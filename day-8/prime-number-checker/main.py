# create a prime number checker

# define function and parameter
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# define argument and call function
n = int(input("Check this number:\n"))
prime_checker(number=n)