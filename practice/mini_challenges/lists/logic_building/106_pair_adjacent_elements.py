# Question:
# Group every two adjacent elements of a list into pairs and display the resulting list of pairs.

list1 = [1, 2, 3, 4, 5, 6]

pairs = []

for index in range(0, len(list1), 2):
    pairs.append([list1[index], list1[index + 1]])

print(pairs)