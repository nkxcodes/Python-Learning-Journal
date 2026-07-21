# Question:
# Find and print all duplicate elements in a list.

numbers = [10, 20, 30, 40, 50, 60, 70, 10, 30, 40, 50, 40, 99, 980]

original_numbers = []

dup_numbers = []

for number in numbers:
    if number in original_numbers:
        dup_numbers.append(number)
    else:
        original_numbers.append(number)

print(dup_numbers)