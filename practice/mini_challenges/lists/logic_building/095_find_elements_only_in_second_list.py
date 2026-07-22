# Question:
# Find and print the elements that are present only in the second list.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 6, 7]

for element in list2:
    if element not in list1:
        print(element)