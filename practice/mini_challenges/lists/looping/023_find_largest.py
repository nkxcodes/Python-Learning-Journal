# Find the largest number.

numbers = [18, 42, 7, 95, 31, 64, 12, 87, 53, 29, 76, 10, 44, 68, 21]

largest_value = 0

for number in numbers:
    if number > largest_value:
        largest_value = number

print(f'Largest Number: {largest_value}')