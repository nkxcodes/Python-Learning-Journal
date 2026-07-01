# Multiply every element by 2

list1 = [12, 45, 7, 89, 23, 56, 91]

doubled_list = []

for number in list1:
    doubled_list.append(number * 2)

print(doubled_list)

# Multiply every element by 2 in same list

list2 = [12, 45, 7, 89, 23, 56, 91]

for index in range(0, len(list2)):
    list2[index] *= 2

print(list2)