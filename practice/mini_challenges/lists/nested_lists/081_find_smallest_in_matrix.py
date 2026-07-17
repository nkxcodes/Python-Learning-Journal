# Question:
# Create a 3×3 matrix and find the smallest element.

matrix_list = [[11, 12, 3], [4, 5, 6], [7, 8, 9]]

smallest_element = matrix_list[0][0]

for row in matrix_list:
    for element in row:
        if element < smallest_element:
            smallest_element = element

print(f'Smallest Element: {smallest_element}')