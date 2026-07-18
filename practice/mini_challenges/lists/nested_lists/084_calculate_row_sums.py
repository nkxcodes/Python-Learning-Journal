# Question:
# Create a 3×3 matrix and calculate the sum of each row.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sum = 0

for row in matrix:
    for element in row:
        row_sum += element
    print(f'Row: {row}, Total Sum: {row_sum}')
    row_sum = 0