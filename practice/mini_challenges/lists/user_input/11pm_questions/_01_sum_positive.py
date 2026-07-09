# ==========================================================
# Question 1: Sum of Positive Numbers
#
# Create a list of numbers.
# Find the sum of only the positive numbers.
#
# Example:
# numbers = [5, -2, 8, -1, 3]
# Output:
# Sum of positive numbers = 16
#
# Hint:
# - Loop through the list.
# - Check if a number is positive.
# - Add it to the total.
# ==========================================================

numbers = [5, -2, 8, -1, 3]

total = 0

for number in numbers:
    if number > 0:
        total += number

print(f'Sum of positive numbers = {total}')