# Question:
# Create a 3×3 matrix and print the elements on the main diagonal.

matrix = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
]

for row_index in range(0, len(matrix)):
    for column_index in range(0, len(matrix[row_index])):
        if row_index == column_index:
            print(matrix[row_index][column_index])