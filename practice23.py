student_scores = {
    'Ram' : 91,
    'Shyam' : 90,
    'Veer' : 87,
    'vidhya' : 77,
    'varash' : 69
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)