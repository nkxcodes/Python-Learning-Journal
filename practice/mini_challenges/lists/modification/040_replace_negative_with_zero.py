# Replace negative numbers with 0.

numbers = [15, -8, 0, 27, -14, 6, -1, 42, -35, 19, -7, 3, -22, 11, -9]

for index in range(0, len(numbers)):
   if numbers[index] < 0:
    numbers[index] = 0

print(numbers)