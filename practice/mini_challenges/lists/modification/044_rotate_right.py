# Rotate the list right by one position

numbers = [23, 7, 41, 18, 56, 9, 32, 14]

saved_num = numbers[-1]

for index in range(len(numbers) - 1, -1, -1):
    numbers[index] = numbers[index - 1] 

numbers[0] = saved_num

print(numbers)