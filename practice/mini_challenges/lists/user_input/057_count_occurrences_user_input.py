# Question:
# Ask the user to enter numbers, then count how many times a user-specified 

print('Enter 0 to End the List: ')

numbers = []

is_running = True

while is_running:
    num = int(input('Enter Number: '))
    if num == 0:
        is_running = False
    numbers.append(num)

numbers.pop(-1)

number = int(input('Enter a Number to Count: '))
count = 0

for num in numbers:
    if num == number:
        count += 1

print(f'{number} appeared {count} times in list')
