# Question:
# Ask the user to enter numbers, store them in a list, and find the second largest number.

print('Enter 0 to End the List: ')

numbers = []

is_running = True

while is_running:
    num = int(input('Enter Number: '))
    if num == 0:
        is_running = False
    numbers.append(num)

numbers.pop(-1)

largest_number = numbers[0]
second_largest = numbers[1]

print(f'List: {numbers}')

for num in numbers:
    if num > largest_number:
        largest_number = num

print(f'Largest Number: {largest_number}')

for num in numbers:
    if num != largest_number:
        second_largest = num

for num in numbers:
    if num == largest_number:
        continue
    if num > second_largest:
        second_largest = num

print(second_largest)

print(f'Second Largest: {second_largest}')
