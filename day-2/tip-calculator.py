# build a tip calculator
# printed a welcome message
print("Welcome to the tip calculator!")

# asked the user for inputs, changed data types and assigned variables
bill = float(input("What was the total bill? "))
percentage = float(input("What percentage tip would you like to give? "))
split_number = int(input("How many people to split the bill? "))

# calculated the percentage of the total
percentage_total = bill * (percentage/100)

# calculated the total bill plus the percentage
total_plus_percentage = percentage_total + bill

# calculated the total split and rounded to 2 decimal places
final_total_split = round(total_plus_percentage / split_number, 2)
final_total_split = "{:.2f}".format(final_total_split)

# printed the result and used f-strings
print(f"Each person should pay: {final_total_split}€")