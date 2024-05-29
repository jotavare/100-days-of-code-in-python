# can't use len() and sum() functions, use loop functions
# calculate the avarege height
# ask the user for input (can't change the code bellow)
student_heights = input("Input a list of student heights in cm, separated by spaces.\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# use a loop to sum all the numbers inputed
total_height = 0

for height in student_heights:
  total_height = total_height + height

# can also simulate the len function with a loop
## number_of_students = 0
## for student in student_heights
##   number_of_students += 1

# calculate the average
average = round(total_height / (n+1))

# print a message with the average height
print(f"The average height of the list is {average} cm.")