# Find the smallest number.

numbers = [18, 42, 7, 95, 31, 64, 12, 87, 53, 29, 76, 10, 44, 68, 21]

smallest_value = numbers[0]

for number in numbers:
    if number < smallest_value:
        smallest_value = number

print(f'Smallest Number: {smallest_value}')