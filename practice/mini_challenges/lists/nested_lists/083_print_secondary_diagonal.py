# Question:
# Create a 3×3 matrix and print the elements on the secondary diagonal.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row_index in range(0, len(matrix)):
    for column_index in range(len(matrix[row_index]) - 1, -1, -1):
        if row_index + column_index == 2:
            print(matrix[row_index][column_index])
