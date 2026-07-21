# Question:
# Find and print the common elements between two lists.

num_1 = [10, 20, 30, 40, 50, 5, 6]
num_2  = [1, 2, 3, 4, 5, 5, 6]

for index in range(0, len(num_1)):
    if num_1[index] == num_2[index]:
        print(num_1)