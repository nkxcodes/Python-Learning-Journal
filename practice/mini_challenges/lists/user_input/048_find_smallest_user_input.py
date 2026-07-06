# Question:
# Ask the user to enter numbers, store them in a list, and find the smallest number.

print('Enter 0 to End the List: ')

numbers = []

is_running = True

while is_running:
    num = int(input('Enter Number: '))
    numbers.append(num)
    if num == 0:
        is_running = False

numbers.pop(-1)
smallest_number = numbers[0]

for num in numbers:
    if num < smallest_number:
        smallest_number = num

print(f'Smallest Number: {smallest_number}')