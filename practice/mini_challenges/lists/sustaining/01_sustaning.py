# 1. Find the largest element in a list

list1 = [10, 20, 30, 40, 50, 60]

largest_element = 0

for element in list1:
    if element > largest_element:
        largest_element = element

print(f'Largest Element: {largest_element}')