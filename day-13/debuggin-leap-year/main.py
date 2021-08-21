#new code, the input takes the input as a string data type
#by adding int() before the input, the code is fixed
#can also use type() function to find what data type
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

#old code, includes a bug
#year = input("Which year do you want to check?")

#if year % 4 == 0:
#  if year % 100 == 0:
#    if year % 400 == 0:
#      print("Leap year.")
#    else:
#      print("Not leap year.")
#  else:
#    print("Leap year.")
#else:
#  print("Not leap year.")
  