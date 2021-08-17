# import the random module
import random

# welcome message
print("Virtual Coin Toss Program")

# generate a random number and apply a variable
random_number = random.randint(0, 1)

# if the number is 1 = Heads and 0 = Tails
if random_number == 1:
  print("Heads")
elif random_number == 0:
  print("Tails")