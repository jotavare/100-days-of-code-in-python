# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# ask the user for the input (age)
age = input("What is your current age? ")

# convert user age to int and save as a new variable
age_as_int = int(age)

# calculate how many years are left until 90 using user age
years_left = 90 - age_as_int

# calculate how many days, weeks and months until 90
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

# print the result while using f-strings to convert data type
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left until 90 years old.")

