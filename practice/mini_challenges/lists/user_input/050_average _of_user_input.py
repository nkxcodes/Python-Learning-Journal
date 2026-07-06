# Question:
# Ask the user to enter numbers, store them in a list, and calculate the average.

print('Enter 0 to End the list: ')

numbers = []

is_running = True

sum = 0

while is_running:
    num = int(input('Enter Number: '))
    if num == 0:
        is_running = False
    numbers.append(num)

numbers.pop(-1)

for num in numbers:
    sum += num

average = sum / len(numbers)

print(f'Average: {average}')