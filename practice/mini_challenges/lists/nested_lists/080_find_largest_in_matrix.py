# Question:
# Create a 3×3 matrix and find the largest element.

matrix_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

largest_element = 0

for row in matrix_list:
    for element in row:
        if element > largest_element:
            largest_element = element

print(f'Largest Element: {largest_element}')