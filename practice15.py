student_scores = input().split()
for n in range(0, len(student_scores)):   # running the loop to convert the input values into integer values
    student_scores[n]= int(student_scores[n])

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score is {highest_score}")