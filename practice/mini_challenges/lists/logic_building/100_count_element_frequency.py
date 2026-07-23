# Question:
# Count and display how many times each element appears in a list.

list1 = ["apple", "banana", "apple", "mango", "banana", "apple"]

count = 0

processed = []

for element_1 in list1:
    if element_1 in processed:
        continue
    else:
        for element_2 in list1:
            if element_1 == element_2:
                count += 1

    print(f'{element_1} -> {count}')
    count = 0
    processed.append(element_1)