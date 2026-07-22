# Question:
# Check whether two lists contain exactly the same elements in the same order.

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

same = True

if len(list1) != len(list2):
    print('The lists are different.')
    same = False
else:
    for list_1_index in range(0, len(list1)):
        if list1[list_1_index] == list2[list_1_index]:
            continue
        else:
            same = False
            break

if same:
    print('The lists are the same.')