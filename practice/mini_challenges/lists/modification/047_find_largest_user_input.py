# Question:
# Ask the user to enter numbers, store them in a list, and find the largest number.

numbers =  []

count = 1
largest_number = 0

while count <= 5:
    num = int(input('Enter Number: '))
    numbers.append(num)
    count += 1

for num in numbers:
    if num > largest_number:
        largest_number = num

print(numbers)
print(f'Largest Number: {largest_number}')