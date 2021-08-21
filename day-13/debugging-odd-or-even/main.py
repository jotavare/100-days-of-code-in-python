#new code, the if statement was missing another '='
#by adding "==" we are checking if the result is equal to 0
#if we used "=" we are saying that its 0!
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#old code, includes a bug
#number = int(input("Which number do you want to check? "))

#if number % 2 = 0:
#  print("This is an even number.")
#else:
#  print("This is an odd number.")