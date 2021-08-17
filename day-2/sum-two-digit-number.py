# write a program that adds the digits in a 2 digit number.

# the user inputs a two digit number
number = input("Type a two digit number: \n")

# assign a variable to each number
string_first_number = number[0]
string_second_number = number[1]

# convert from string to integer
first_number = int(string_first_number)
second_number = int(string_second_number)

# prints the sum and gives the ouput
print("Adding the two digits, gives a total of:", first_number + second_number)