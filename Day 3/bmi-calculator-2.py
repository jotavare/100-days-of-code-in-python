# write a program that interprets the Body Mass Index (BMI) based on a user's weight and height

# ask for the user height and weight and convert to a float
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# calculate the bmi and round to a 1 decimal number
bmi = weight / (height*height)
round_bmi = round(bmi,1)

# print the user bmi score
print("Your BMI is", round_bmi)

# print the user bmi interpretation 
if bmi < 18.5:
  print("You are underweight.")
elif bmi < 25:
  print("You have normal weight.")
elif bmi < 30:
  print("You are slightly overweight.")
elif bmi < 35:
  print("You are obese.")
else:
  print("You are clinically obese.")





