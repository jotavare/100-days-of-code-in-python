#the print function should not have '[]'
#the first 'if' should have and instead of or
#and after the first 'if', the other ones should be 'elif'
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

#old code, includes bugs
#for number in range(1, 101):
#  if number % 3 == 0 or number % 5 == 0:
#    print("FizzBuzz")
#  if number % 3 == 0:
#    print("Fizz")
#  if number % 5 == 0:
#    print("Buzz")
#  else:
#    print([number])