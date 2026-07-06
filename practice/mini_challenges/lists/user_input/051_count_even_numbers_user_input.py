# Question:
# Ask the user to enter numbers, store them in a list, and count how many are even.

print('Enter 0 to End the list: ')

numbers = []

count = 0

is_running = True

while is_running:
    num = int(input('Enter Number: '))
    if num == 0:
        is_running = False
    numbers.append(num)

numbers.pop(-1)

for num in numbers:
    if num % 2 == 0:
        count += 1

print(f'Even Numbers: {count}')