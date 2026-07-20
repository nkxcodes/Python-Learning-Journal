# Question:
# Create a 3×3 matrix and print its transpose.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row = []

for column_index in range(0, len(matrix)):
    for row_index in range(0, len(matrix)):
        row.append(matrix[row_index][column_index])
    print(row)
    row = []