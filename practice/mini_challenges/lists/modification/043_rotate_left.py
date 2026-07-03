# Rotate the list left by one position

numbers = [14, 27, 35, 8, 19, 42, 6, 51]

saved_num = numbers[0]

for index in range(0, len(numbers) - 1):
    numbers[index] = numbers[index + 1]

last_position = len(numbers) - 1
numbers[last_position] = saved_num

print(numbers)