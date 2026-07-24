# 1. Find the largest element in a list

list1 = [10, 20, 30, 40, 50, 60]

largest_element = 0

for element in list1:
    if element > largest_element:
        largest_element = element

print(f'Largest Element: {largest_element}')


list2 = [10, 20, 30, 40, 50, 60]

smallest_element =  list2[0]

for element in list2:
    if element < smallest_element:
        smallest_element = element

print(f'Smallest Element: {smallest_element}')

list3 = [10, 20, 30, 40, 50, 60]

total = 0

for element in list3:
    total += element

print(f'Total: {total}')