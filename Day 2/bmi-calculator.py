# Write a program that calculates the Body Mass Index (BMI)

# we ask for the ouput and assign a variable
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# convert the heigh and weight to float and integer types
height_float = float(height)
weight_int = int(weight)

# calculate the BMI (Body mass index)
bmi = weight_int / height_float ** 2

# print the text and the BMI as an integer type
print("Your BMI is:", int(bmi))
