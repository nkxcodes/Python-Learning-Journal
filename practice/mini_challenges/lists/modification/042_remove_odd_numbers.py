# Remove all odd nnumbers

numbers = [15, 8, -3, 22, 0, 17, -14, 9, 26, -7, 4, 11, 30, -12, 5, 18, -1, 24]

for index in range(len(numbers) - 1, -1, -1):
    if numbers[index] % 2 != 0:
        numbers.pop(index)

print(numbers)