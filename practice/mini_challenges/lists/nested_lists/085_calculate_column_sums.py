# Question:
# Create a 3×3 matrix and calculate the sum of each column.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

column_sum  = 0

for column_index in range(0, len(matrix)):
    for row_index in range(0, len(matrix)):
        column_sum += matrix[row_index][column_index]
    print(f'Column: {column_index}, Sum: {column_sum}')
    column_sum = 0