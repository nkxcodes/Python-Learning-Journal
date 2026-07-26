# Question: 
# Find the element that appears the most number of times in a list

list1 = ["apple", "banana", "apple", "mango", "apple", "banana"]

count = 0

processed = []

previous_most_count = 0

current_most_count = ''

for index in range(0, len(list1)):
    if list1[index] in processed:
        continue

    else:
        for index_2 in range(0, len(list1)):
            if list1[index] == list1[index_2]:
                count += 1

        if count > previous_most_count:
            previous_most_count = count
            current_most_count = list1[index]
        
        count = 0
        processed.append(list1[index])

print(f'Most Appeared: {current_most_count}')
print(f'Appeared: {previous_most_count} times')