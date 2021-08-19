# dictionary with all the students scores
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# create an empty dictionary
student_grades = {}

# for each score in student_scores change the to a message
for student in student_scores:
    score = student_scores[student]
    if score > 90 and score <= 100:
        student_grades[student] = "Outstanding"
    elif score > 80 and score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif score > 71 and score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# print the result
print(student_scores)
print(student_grades)
