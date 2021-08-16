# can't use the max() and min () 
# need to calculate the highest score
# will first, ask the user for the input
student_scores = input("Input a list of student scores (seperate with spaces).\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# assign a value of 0 to a variable and used a loop and if statements to determine if it's a higher number or a lower number
highest_student = 0

for student in student_scores:
    if student > highest_student:
        highest_student = student

# after the loop finishes, print the highest number 
print(f"The highest score in the class is: {highest_student}.")