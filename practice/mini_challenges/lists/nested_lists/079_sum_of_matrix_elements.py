# Question:
# Create a 3×3 matrix and calculate the sum of all its elements.

matrix_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

total = 0

for row in matrix_list:
    for element in row:
        total += element

print(f'Total of Elements: {total}')