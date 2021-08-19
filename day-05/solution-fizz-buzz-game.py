# write a program that automatically prints the solution to the FizzBuzz game
# number divisible by 3 = "Fizz"
# number divisible by 5 = "Buzz"
# number divisible by 3 and 5 = "FizzBuzz"

# used the for, range(), and if statements to create the conditions and print the ouput
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")   
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)