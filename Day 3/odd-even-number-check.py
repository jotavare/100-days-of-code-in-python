# write a program that works out whether if a given number is an odd or even number

# asked the user for the input number
number = int(input("Which number do you want to check? "))

# if the remainder of the number == to 1 print odd else print even

if number % 2 == 1:
  print("This is an odd number")
else:
  print("This is an even number")
