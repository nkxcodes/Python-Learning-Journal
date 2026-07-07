# Question:
# Ask the user to enter numbers, then search for a number entered by the user and report whether it exists.

print('Enter 0 to End the List: ')

numbers = []

is_running = True

while is_running:
    num = int(input('Enter Number: '))
    if num == 0:
        is_running = False
    numbers.append(num)

print('Search Number: ')

searched_number = int(input('Search Number: '))
number_exists = False

for num in numbers:
    if num == searched_number:
        number_exists = True

if number_exists:
    print(f'{searched_number} Exists in List')
else:
    print(f"{searched_number} Don't Exists in List")