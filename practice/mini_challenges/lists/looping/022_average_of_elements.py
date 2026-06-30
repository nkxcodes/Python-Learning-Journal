# Find the average of all numbers

numbers = [18, 42, 7, 95, 31, 64, 12, 87, 53, 29, 76, 10, 44, 68, 21]

total = 0

for number in numbers:
    total += number

average = total / len(numbers)

print(f'Average: {average}')