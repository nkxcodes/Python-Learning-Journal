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

# ==========================================================
# Question 8
# Find the index of a given value using enumerate().
#
# Example:
# Find "Orange"
#
# Output:
# Orange found at index 3
# ==========================================================

print('Question_8: ')

students = ["Rahul", "Priya", "Aman", "Neha", "Riya", "Karan"]

find = input('Find: ')
founded = False
find_index = 0

for index, student in enumerate(students, start=0):
    if student == find:
        founded = True
        find_index = index

if founded:
    print(f'{find} found at index {find_index}')
else:
    print(f'{find} not found in the list')

# ==========================================================
# Question 9
# Count how many elements are longer than 5 characters.
#
# Use enumerate() while looping.
# ==========================================================

print('Question_9: ')

students = ["Rahul", "Priya", "Aman", "Neha", "Riya", "Karan"]

count = 0

for index, student in enumerate(students, start=0):
    if len(student) >= 5:
        count += 1

print(f'{count} elements are longer than 5 characters')

# ==========================================================
# Question 10
# Replace every negative number in a list with 0.
#
# Hint:
# enumerate() gives both the index and the value.
# ==========================================================

print('Question_10: ')

numbers = [18, -7, 0, 45, -12, 9, -3, 27, 14, -25, 6, -1, 33, -18, 50]

for index, number in enumerate(numbers, start=0):
    if number < 0:
        numbers[index] = 0

print(numbers)

# ==========================================================
# Question 11
# Multiply every element by 2 using enumerate()
# and store the result back into the same list.
# ==========================================================


print('Question_11: ')

numbers = [12, 45, 7, 89, 23, 56, 91, 18, 34, 5]

for index, number in enumerate(numbers, start=0):
    numbers[index] = number * 2

print(numbers)

# ==========================================================
# Question 12
# Print all indexes where the value is even.
#
# Example Output:
# Even number at index 1
# Even number at index 4
# ==========================================================

print('Question_12: ')

numbers = [13, 24, 7, 18, 45, 60, 9, 32, 11, 50, 27, 14, 3, 22, 19]

for index, number in enumerate(numbers, start=0):
    if number % 2 == 0:
        print(f'Even number at Index {index}')

# ==========================================================
# Question 13
# Find the largest number and print both:
# - its value
# - its index
#
# Do not use list.index().
# ==========================================================

print('Question_13: ')

numbers = [18, 42, 7, 91, 35, 12, 64, 29, 56, 83, 15, 77]

largest_number = 0
index = 0

for index_2, number in enumerate(numbers, start=0):
    if number > largest_number:
        largest_number = number
        index = index_2

print(f'Largest Number: {largest_number}')
print(f'Index: {index}')

# ==========================================================
# Question 14
# Find the smallest number and print both:
# - its value
# - its index
#
# Do not use list.index().
# ==========================================================

numbers = [18, 42, 7, 91, 35, 12, 64, 29, 56, 83, 15, 77]

smallest_number = numbers[0]
index = 0

for index_2, number in enumerate(numbers, start=0):
    if number < smallest_number:
        smallest_number = number
        index = index_2

print(f'Smallest Number: {smallest_number}')
print(f'Index: {index}')