# Question:
# Ask the user to enter 5 numbers and store them in a list.

numbers = []

count = 1

while count <= 5:
    num = int(input('Enter Number: '))
    numbers.append(num)
    count += 1

print(numbers)