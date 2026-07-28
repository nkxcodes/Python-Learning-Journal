# Question:
# Move all zero values to the end of the list while keeping the order of the other elements unchanged.

list1 = [2, 0, 3, 0, 4, 0, 5, 0, 0, 0, 6, 7, 8]

spare_list = []

for index in range(len(list1) - 1, -1, -1):
    if list1[index] == 0:
        spare_list.append(list1[index])
        list1.remove(list1[index])

for index in range(len(spare_list) - 1, -1, -1):
    list1.append(spare_list[index])
    spare_list.pop(spare_list[index])

print(list1)
print(spare_list)