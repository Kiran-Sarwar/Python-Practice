# Author = Kiran
# Date = 1st July, 2026
"""
Requirements:

Create a list of tuples, where each tuple = (name, marks) for at least 5 students.
Write code to:

Print the highest scoring student (name + marks)
Print the lowest scoring student (name + marks)
Add a new student to the list
Remove a student by name
Print the total number of students after changes


Bonus (optional, only if you want to flex a bit): calculate the average of all marks.
"""

list_of_students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 90), ("Eve", 88)]
print("List of students:", list_of_students)

# Find the highest scoring student
highest_student = max(list_of_students, key=lambda student: student[1])
print("Highest scoring student:", highest_student)

# Find the lowest scoring student
lowest_student = min(list_of_students, key=lambda student: student[1])
print("Lowest scoring student:", lowest_student)

# Add a new student
new_student = ("Frank", 95)
list_of_students.append(new_student)

# Remove a student by name
list_of_students.remove(("Charlie", 78))

# Print the total number of students after changes
total_students = len(list_of_students)
print("Total number of students after changes:", total_students)