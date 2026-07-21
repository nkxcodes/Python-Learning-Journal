# Question:
# Find and print all unique elements in a list (elements that appear only once).

numbers = [10, 20, 30, 40, 50, 60, 70, 10, 30, 40, 50, 40, 99, 980]

original_numbers = []

duplicate_numbers = []

for number in numbers:
    if number in original_numbers:
        duplicate_numbers.append(number)
    else:
        original_numbers.append(number)

print(original_numbers)