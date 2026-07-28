# Question:
# Move all negative numbers to the beginning of the list while keeping the order of the remaining elements unchanged.

list1 = [5, -2, 8, -7, 3, -1, 10, 4]

negative_numbers = []
positive_numbers = []

for index in range(len(list1)):
    if list1[index] < 0:
        negative_numbers.append(list1[index])
    elif list1[index] >= 0:
        positive_numbers.append(list1[index])

list1 = negative_numbers + positive_numbers

print(list1)