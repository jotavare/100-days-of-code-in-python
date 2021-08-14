# build an automatic pizza order program.
# ask the user the size and extra ingredients inputs
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

# yes or no for pepperoni and assign value - small pizza
if size == "S":
  bill = 15
  if add_pepperoni == "N":
    bill = 15
  elif add_pepperoni == "Y":
    bill += 2

# yes or no for pepperoni and assign value - medium pizza
elif size == "M":
  bill = 20
  if add_pepperoni == "N":
    bill = 20
  elif add_pepperoni == "Y":
    bill += 3

# yes or no for pepperoni and assign value - large pizza
elif size == "L":
  bill = 25
  if add_pepperoni == "N":
    bill = 25
  elif add_pepperoni == "Y":
    bill += 3

# yes or no for cheese, assign value and print final bill
if extra_cheese == "N":
  print(f"Your final bill is: {bill}€.")
elif extra_cheese == "Y":
  bill += 1
  print(f"Your final bill is: {bill}€.")




