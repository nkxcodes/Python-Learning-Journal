# Question:
# Replace every negative number in a nested list with 0.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, -8, 9]
]

for row in matrix:
    for index in range(0, len(row)):
        if row[index] < 0:
            row[index] = 0

print(matrix)