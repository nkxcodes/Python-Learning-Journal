# Question:
# Check whether a list is sorted in ascending order.

list1 = [1, 2, 3, 4, 5]

is_sorted = True

for index in range(0, len(list1) - 1):
    if list1[index] <= list1[index + 1]:
        continue
    else:
        is_sorted = False
        break

if is_sorted:
    print('The list is sorted in ascending order.')
else:
    print('The list is not sorted in ascending order.')