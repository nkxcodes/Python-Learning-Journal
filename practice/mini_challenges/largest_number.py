# Largest Number Finder
#
# Description:
# Compare two numbers and display the larger one.
#
# Example:
# Enter first number: 12
# Enter second number: 35
#
# Output:
# Largest number: 35

first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))

largest_number = 0

if first_number > second_number:
    largest_number = first_number
else:
    largest_number = second_number

print(f'Largest Number: {largest_number}')