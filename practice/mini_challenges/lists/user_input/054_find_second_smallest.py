# Question:
# Ask the user to enter numbers, store them in a list, and find the second smallest number.

print('Enter 0 to End the List: ')

numbers = []

is_running = True

while is_running:
    num = int(input('Enter Number: '))
    if num == 0:
        is_running = False
    numbers.append(num)

numbers.pop(-1)

smallest_number = numbers[0]
second_smallest = numbers[1]

for num in numbers:
    if num < smallest_number:
        smallest_number = num

for number in numbers:
    if num == smallest_number:
        continue
    if num < second_smallest:
        second_smallest = num

print(f'Second Smallest: {second_smallest}')