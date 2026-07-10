# ==========================================================
# Question 64
# Ask the user to keep entering numbers.
#
# Stop when the user enters 0.
#
# Then print:
# - Total numbers entered (excluding 0)
# - Largest number
# - Smallest number
# - Average
#
# Goal:
# Practice loops, user input,
# variables, and mathematical calculations.
# ==========================================================

print('Enter 0 to End the list: ')

numbers = []

is_running = True

while is_running:
    num = int(input('Enter Number: '))
    if num == 0:
        is_running = False
    numbers.append(num)

numbers.pop(-1)

total = len(numbers)

largest_number = 0

smallest_number = numbers[0] or numbers[1]

average = sum(numbers) / len(numbers)

for number in numbers:
    if number > largest_number:
        largest_number = number

for number in numbers:
    if number < smallest_number:
        smallest_number = number

print(f'Total: {total}')
print(f'Largest Number: {largest_number}')
print(f'Smallest Number: {smallest_number}')
print(f'Average: {average}')    