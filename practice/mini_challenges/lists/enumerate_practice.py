# ==========================================================
# Question 1
# Print the index and value of every element using enumerate().
#
# Example Output:
# 0 Apple
# 1 Mango
# 2 Banana
# ==========================================================

print('Question_1: ')

fruits = ['Apple', 'Mango', 'Banana']

for index, fruit in enumerate(fruits, start=0):
    print(f'{index} {fruit}')

# ==========================================================
# Question 2
# Start counting from 1 instead of 0 using enumerate().
#
# Example Output:
# 1 Apple
# 2 Mango
# 3 Banana
# ==========================================================

print('Question_2: ')

fruits_2 = ['Apple', 'Mango', 'Banana']

for index, fruit in enumerate(fruits, start=1):
    print(f'{index} {fruit}')

# ==========================================================
# Question 3
# Print only the indexes of every element.
#
# Example Output:
# 0
# 1
# 2
# 3
# ==========================================================

print('Question_3: ')

fruits_3 = ['Apple', 'Mango', 'Banana']

for index, fruit in enumerate(fruits_3, start=0):
    print(index)

# ==========================================================
# Question 4
# Print only the values using enumerate().
#
# (Do not remove enumerate() even though it isn't necessary.)
# ==========================================================

print('Question_4: ')

students = ["Rahul", "Priya", "Aman", "Neha", "Riya", "Karan"]

for index, student in enumerate(students, start=0):
    print(student)

# ==========================================================
# Question 5
# Print each item like this:
#
# Item 1: Apple
# Item 2: Mango
# Item 3: Banana
#
# Use enumerate(start=1).
# ==========================================================

print('Question_5: ')

students = ["Rahul", "Priya", "Aman", "Neha", "Riya", "Karan"]

for index, student in enumerate(students, start=1):
    print(f'Student {index}: {student}')

# ==========================================================
# Question 6
# Print only the elements that are at even indexes.
#
# Example:
# Index 0 -> Apple
# Index 2 -> Banana
# Index 4 -> Kiwi
# ==========================================================

print('Question_6: ')

students = ["Rahul", "Priya", "Aman", "Neha", "Riya", "Karan"]

for index, student in enumerate(students, start=0):
    if index % 2 == 0:
        print(f'Index {index} -> {student}')

# ==========================================================
# Question 7
# Print only the elements that are at odd indexes.
# ==========================================================

print('Question_7: ')

students = ["Rahul", "Priya", "Aman", "Neha", "Riya", "Karan"]

for index, student in enumerate(students, start=0):
    if index % 2 != 0:
        print(f'Index {index} -> {student}')