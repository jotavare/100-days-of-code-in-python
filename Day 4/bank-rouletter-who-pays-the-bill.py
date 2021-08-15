# select a random name to buy the meal
# import random module
import random

# ask for input and create a list seperated by a comma
names_string = input("Give me everybody's names, separated by a comma and a space. \n")
names = names_string.split(", ")

# use the len function to know how many names the user wrote
total_names = len(names)

# use a randomizer to choose a number betwee 0 and number of people input
random_number = random.randint(0, total_names - 1)

# print the random number as a name from the list
print(f"{names[random_number]} is going to buy the meal today!")

# we can also use random.choice() to get a random name
