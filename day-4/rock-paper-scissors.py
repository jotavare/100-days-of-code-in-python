rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# create a random generated rock, paper, scissors game
# import random Module
import random

# can also create a list, but didn't use it
choices = [rock, paper, scissors]

# welcome message plus ask the user for the input number
print("Welcome to the Rock, Paper, Scissors game!")
print("What do you choose?")
user_result = float(input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# get a random number between 0 and 2
python_result = int(random.randint(0,2))

# print rock, paper, scissors based on the input and random number
print("\nYou chose:")
if user_result >= 3 or user_result < 0.9 and user_result != 0:
  print("Invalid choice!\nYou lose!\n")
if user_result == 0:
  print(rock)
elif user_result == 1:
  print(paper)
elif user_result == 2:
  print(scissors)

print("Computer chose:")
if python_result == 0:
  print(rock)
elif python_result == 1:
  print(paper)
elif python_result == 2:
  print(scissors)

# who won? and print the result

if user_result == 0:
  if python_result == 0:
    print("Draw!")
  elif python_result == 1:
    print("You lose!")
  elif python_result == 2:
    print("You Win!")

if user_result == 1:
  if python_result == 0:
    print("You Win!")
  elif python_result == 1:
    print("Draw!")
  elif python_result == 2:
    print("You lose!")

if user_result == 2:
  if python_result == 0:
    print("You lose!")
  elif python_result == 1:
    print("You Win!")
  elif python_result == 2:
    print("Draw!")