# Remove all even numbers

numbers = [12, 7, 0, 19, 24, -5, 8, 13, -10, 21, 4, 17, 30, 9, -2, 15, 26, 11]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
print(numbers)

# Remove all even numbers from same list with letting elements to be skipped

numbers = [12, 7, 0, 19, 24, -5, 8, 13, -10, 21, 4, 17, 30, 9, -2, 15, 26, 11]

for index in range(len(numbers) - 1, -1, -1):
    if numbers[index] % 2 == 0:
        numbers.pop(index)

print(numbers)