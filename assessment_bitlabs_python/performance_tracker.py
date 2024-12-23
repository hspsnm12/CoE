def average(marks):
    return sum(marks) / len(marks)

def top_performer(students):
    averages = {name: average(marks) for name, marks in students.items()}
    top_student = max(averages, key=averages.get)
    return averages, top_student

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
averages, top_student = top_performer(students)

print(f"Average Marks: {averages}")
print(f"Top Performer: \"{top_student}\"")
