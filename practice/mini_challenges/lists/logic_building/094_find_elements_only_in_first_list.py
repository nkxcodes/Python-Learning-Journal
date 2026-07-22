# Question:
# Find and print the elements that are present only in the first list.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7]

for element in list1:
    if element not in list2:
        print(element)

list1 = [10, 20, 30, 40]
list2 = [20, 50]

for element in list1:
    if element not in list2:
        print(element)

list1 = ["apple", "banana", "mango", "grapes"]
list2 = ["banana", "orange", "grapes"]

for element in list1:
    if element not in list2:
        print(element)

list1 = [2, 4, 6]
list2 = [2, 4, 6, 8]

found = False

for element in list1:
    if element not in list2:
        print(element)
        found = True 

if not found:
    print('No elements found.')

list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = [2, 5]

processed = []

for element in list1:
    if element not in list2:
        if element in processed:
            continue
        else:
            print(element)
            processed.append(element)