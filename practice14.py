student_heights= input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f"The total height = {total_height}")
print(f"The total number of students = {len(student_heights)}")
# print(f"The avg height = {int(total_height/len(student_heights))}")
avg_height = int(total_height/len(student_heights))
print(f"The avg height = {avg_height}")
