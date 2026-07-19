# Question:
# Count the total number of elements in a nested list.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

count = 0

for row in matrix:
    for elements in row:
        count += 1

print(f'Total Elements: {count}')