# Remove duplicate elements

numbers = [
    12, 5, 8, 12, 3, 5, 19, 8, 7, 3,
    12, 25, 19, 5, 30, 7, 8, 25, 14, 3,
    9, 14, 5, 18, 30, 9, 12, 21, 18, 7,
    25, 5, 3, 9, 14, 12, 30, 8, 21, 19,
    7, 18, 25, 5, 14, 9, 30, 3, 12, 8
]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)