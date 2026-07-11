# Question:
# Ask the user to enter numbers, store them in a list, and remove duplicate values.

print('Enter 0 to End the list: ')

numbers = []

new_numbers = []

is_running = True

while is_running:
    num = int(input('Enter Number: '))
    if num == 0:
        is_running = False
    numbers.append(num)

numbers.pop(-1)

for number in numbers:
    if number in new_numbers:
        continue
    else:
        new_numbers.append(number)

print(f'Original Numbers: {numbers}')
print(f'New Numbers: {new_numbers}')