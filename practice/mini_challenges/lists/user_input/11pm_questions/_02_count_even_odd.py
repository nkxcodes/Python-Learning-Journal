# ==========================================================
# Question 2: Count Even and Odd Numbers
#
# Create a list of integers.
# Count how many even numbers and how many odd numbers
# are present in the list.
#
# Example:
# numbers = [2, 7, 8, 5, 10]
#
# Output:
# Even = 3
# Odd = 2
#
# Hint:
# Use the modulus (%) operator.
# ==========================================================

numbers = [2, 7, 8, 5, 10]

even = 0
odd = 0

for number in numbers:
    if number % 2 != 0:
        odd += 1
    else:
        even += 1

print(f'Even = {even}')
print(f'Odd = {odd}')