# ==========================================================
# Question 4: Multiplication Table
#
# Ask the user to enter a number.
# Print its multiplication table from 1 to 10.
#
# Example:
# Input:
# 7
#
# Output:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70
#
# Practice using a loop.
# ==========================================================

number = int(input('Enter a Number: '))

for multiply_with in range(1, 11):
    print(f'{number} x {multiply_with} = {number * multiply_with}')