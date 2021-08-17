# ask for the year and convert to integer
year = int(input("Which year do you want to check? "))

# if and else statements to calculate if leap or not leap year
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not a leap year.")
  else:
    print("Leap year.")
else:
  print("Not a leap year.")