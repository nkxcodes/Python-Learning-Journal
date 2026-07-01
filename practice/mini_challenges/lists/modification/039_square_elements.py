# Square every element

numbers = [4, 9, 15, 2, 11, 7, 20, 13, 6, 18]

squared_numbers = []

for number in numbers:
    squared_numbers.append(number ** 2)

print(squared_numbers)

# Square every element in same list

numbers_2 = [4, 9, 15, 2, 11, 7, 20, 13, 6, 18]

for index in range(0, len(numbers_2)):
    numbers_2[index] **= 2

print(numbers_2)