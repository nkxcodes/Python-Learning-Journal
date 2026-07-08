# Question:
# Ask the user to enter numbers, then insert a new number at a position chosed by the user.

print('Enter 0 to End the List: ')

numbers = []

is_running = True

while is_running:
    num = int(input('Enter Number: '))
    if num == 0:
        is_running = False
    numbers.append(num)

print(numbers)

new_number = int(input('Enter a new number at a position: '))
insert_index = int(input('Enter index in which have to insert: '))

numbers.insert(insert_index, new_number)

print(numbers)