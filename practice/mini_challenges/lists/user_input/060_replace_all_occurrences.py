# Question:
# Ask the user to enter numbers, then replace every occurrence of one user-specified number with another.

print('Enter 0 to Enter the list: ')

numbers = []

is_running = True

while is_running:
    num = int(input('Enter Number: '))
    if num == 0:
        is_running = False
    numbers.append(num)

numbers.pop(-1)

print(numbers)

number_to_replace = int(input('Enter the number to replace: '))
new_number = int(input('Enter the new number: '))

for index in range(0, len(numbers)):
    if numbers[index] == number_to_replace:
        numbers[index] = new_number

print(numbers)