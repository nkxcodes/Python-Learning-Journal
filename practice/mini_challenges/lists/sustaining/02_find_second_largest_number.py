# Question:
# Find second largest number

numbers = [4, 7, 2, 9, 7, 9, 5]

second_largest = numbers[0]

for element in numbers:
    if element < second_largest:
        second_largest = element

print(f'Second Largest: {second_largest}')