# Question:
# Ask the user to enter numbers, then delete element at a position chosen by the user.

print('Enter 0 to End the List: ')

numbers = []

is_running = True

while is_running:
    num = int(input('Enter Number: '))
    if num == 0:
        is_running = False
    numbers.append(num)

numbers.pop(-1)

print(numbers)

index_to_remove = int(input('Enter the position (index) to delete: '))

numbers.pop(index_to_remove)

print(numbers)