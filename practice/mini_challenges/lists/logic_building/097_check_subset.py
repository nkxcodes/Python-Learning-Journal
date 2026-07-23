# Question:
# Check whether one list is a subset of another list.

list1 = [2, 6]
list2 = [1, 2, 3, 4, 5]

is_subset = True

for element in list1:
    if element not in list2:
        is_subset = False
        break
        

if is_subset:
    print('List1 is a subset of list2.')
else:
    print('List1 is not a subset of list2.')