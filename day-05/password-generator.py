#Password Generator Project

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# imported the random module
import random

# assigned all the letters, numbers and symbols to variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# asked the user for inputs and saved in integer variables
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# create a list with random characters
password_list = []

for letter in range(0, nr_letters):
    random_letter = letters [random.randint(0, (len(letters)-1))]
    password_list += random_letter

for symbol in range(0, nr_symbols):
    random_symbol = symbols [random.randint(0, (len(symbols)-1))]
    password_list += random_symbol

for number in range(0, nr_numbers):
    random_number = numbers [random.randint(0, (len(numbers)-1))]
    password_list += random_number

# shuffle the numbers because they were in order of input
random.shuffle(password_list)

# create a new list and print the output in one line as a string
random_password = ""

for character in password_list:
    random_password += character

print(f"Your password is:\n{random_password}")