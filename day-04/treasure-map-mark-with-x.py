# write a program which will mark a spot with an X
# create a "map" and ask user for input
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\nChoose column and row number (e.g. 33)\n")

# assign a variable to the first and second number
first_number = int(position[0])
second_number = int(position[1])

# create if and elif statements to change the square for the x
# another way to these in less code
# [first_number -1][second_number -1] = X
if first_number == 1:
  if second_number == 1:
    row1[0] = "X"
  elif second_number == 2:
    row1[1] = "X"
  elif second_number == 3:
    row1[2] = "X"
  else:
    print("Invalid number")
if first_number == 2:
  if second_number == 1:
    row2[0] = "X"
  elif second_number == 2:
    row2[1] = "X"
  elif second_number == 3:
    row2[2] = "X"
  else:
    print("Invalid number")
if first_number == 3:
  if second_number == 1:
    row3[0] = "X"
  elif second_number == 2:
    row3[1] = "X"
  elif second_number == 3:
    row3[2] = "X"
  else:
    print("Invalid number")

# print the new "map" with "x"
print(f"{row1}\n{row2}\n{row3}")