# Question:
# Find and print the common elements between two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 9]

for number in list1:
    if number in list2:
        print(number)