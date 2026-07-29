# Question:
# Remove every third element from the list

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for index in range(len(list1) - 1, 1, -3):
    print(f"Removing index {index}, value {list1[index]}")
    list1.pop(index)

print(list1)