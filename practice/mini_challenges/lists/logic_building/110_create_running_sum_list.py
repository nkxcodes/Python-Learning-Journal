# Question:
# Create a new list where each element is the running (cumulative) sum of the original list

list1 = [5, 3, 2, 7, 4]

running_total = []

total = 0

for index in range(0, len(list1)):
    total += list1[index]
    running_total.append(total)

print(running_total)