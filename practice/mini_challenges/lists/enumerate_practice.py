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