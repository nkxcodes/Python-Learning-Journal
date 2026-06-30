# Count negative numbers

numbers = [18, -42, 0, 95, -31, 64, -12, 87, 53, -29, 76, 10, -44, 68, 21, 0, -7]

count = 0

for number in numbers:
    if number < 0:
        count += 1

print(f'Negative Numbers: {count}')