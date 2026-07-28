# Question:
# Split a list into two separate lists: one containing even numbers and the other containing odd numbers.

list1 = [12, 7, 4, 15, 8, 21, 10, 3, 6]

even_numbers = []
odd_numbers = []

for element in list1:
    if element % 2 == 0:
        even_numbers.append(element)
    else:
        odd_numbers.append(element)


print(even_numbers)
print(odd_numbers)