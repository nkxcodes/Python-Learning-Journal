# Question:
# Find and print the common elements between two lists.

from multiprocessing import process


list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 9]

for number in list1:
    if number in list2:
        print(number)

list1 = [10, 20, 30, 40]
list2 = [20, 40, 60, 80]

for number in list1:
    if number in list2:
        print(number)

list1 = ["apple", "banana", "mango", "grapes"]
list2 = ["banana", "orange", "mango", "kiwi"]

for element in list1:
    if element in list2:
        print(element)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

found = False

for number in list1:
    if number in list2:
        print(number)
        found = True

if not found:
    print('No common elements found.')

list1 = [1, 2, 2, 3, 4, 5]
list2 = [2, 2, 4, 6]

processed = []

for number in list1:
    if number in list2:
        if number in processed:
            continue
        else:
            print(number)
            processed.append(number)