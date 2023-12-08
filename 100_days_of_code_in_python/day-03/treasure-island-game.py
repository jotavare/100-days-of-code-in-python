print('''
▓▓▓▓████████████████████████████
▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
████████████████████████████████████
██▓▓__▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓__▓▓██
██▓▓__▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓__▓▓██
██▓▓__▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓__▓▓██
████████████████████████████████████
██▓▓__██▒▒░░░░__▒▒▒▒__░░░░▒▒██__▓▓██
██▓▓__██░░░░░░__▒▒▒▒__░░░░░░██__▓▓██
██▓▓__██░░░░░░________░░░░░░██__▓▓██
██▓▓__██▒▒░░░░░░░░░░░░░░░░▒▒██__▓▓██
████████████████████████████████████
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 

# ask the user for the input (answer 1) and convert it to upper case
print("1 - You wake up in a forest and the first thing you see is a bear. What do you decide to do?")
print("'A' - Give the bear a hug.")
print("'B' - Run away!")
str_answer1 = input("Write 'A' or 'B'= ")
answer1 = str_answer1.upper()

# use the if and elif statements to decide the outcome message
if answer1 == "A":
  print("\nYou try to hug the bear but he chopped your head off!")
  print("Just to be sure, dont hug a bear in real life.")
  print("Game Over!")
elif answer1 == "B":
  print("You run away, but the bear is running after you!\n")

# ask the user for the input (answer 2) and convert it to upper case
  print("2 - While you're running, you find the way out of the forest. What do you decide to do?")
  print("'A' - Get out of the forest!")
  print("'B' - Continue running in circles inside the forest.")
  str_answer2 = input("Write 'A' or 'B'= ")
  answer2 = str_answer2.upper()

# use the if and elif statements to decide the outcome message
  if answer1 == "B":
    if answer2 == "A":
      print("\nYou try to get out of the forest, but you slip and fall in a cave breaking your legs.\n")
      print("To your suprise the bear runs away, but you hear steps and a big sound echoes through the cave... 'ROAAAAARRR'. A lion appears and kills you!")
      print("Game Over! Sorry :/")
    elif answer2 == "B":
      print("As you continue running, you find a old house, and inside you see a bright light.\n")

# ask the user for the input (answer 3) and convert it to upper case
      print("3 - You decide to run to the house and hide there.\nInside you find 3 doors. One 'red', one 'yellow' and one 'blue'.\nWhich colour do you choose?")
      str_answer3 = input("Write 'Red', 'Yellow', 'Blue' = ")
      answer3 = str_answer3.upper()

# use the if and elif statements to decide the outcome message
      if answer2 == "B":
        if answer3 == "RED":
          print("\nYou open the red door and decide to inspect inside, you see a light switch.")
          print("You decide to turn it on. It's a room full of beasts!")
          print("As you try to run away you see the bear, you have no where to escape.")
          print("Game Over!")
        elif answer3 == "YELLOW":
          print("\nYou open the yellow door and decide to inspect inside, you see a light switch.")
          print("You decide to turn it on. It's the treasure!")
          print("Inside you find a map of the forest and a gun. You can escape now.")
          print("Congratulations!")
          print("PS: Don't hug bears in real life.")
        elif answer3 == "BLUE":
          print("\nYou open the blue door and decide to inspect inside, you see a light switch.")
          print("You decide to turn it on but the door closes behind you!")
          print("The room starts filling with water. You have no where to escape. You die trying to breath underwater.")
          print("Game Over!")
        else:
          print("Not a valid input")
    else:
      print("Not a valid input")
else:
  print("Not a valid input")