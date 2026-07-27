# Question:
# Find the element that appears the least number of times in a list.

list1 = ["apple", "banana", "apple", "mango", "apple", "banana"]

count = 0

processed = []

least_appeared_count = 10

least_appeared_element = ''

for index in range(0, len(list1)):
    if list1[index] in processed:
        continue
    else:
        for index_2 in range(0, len(list1)):
            if list1[index] == list1[index_2]:
                count += 1

        if count < least_appeared_count:
            least_appeared_count = count
            least_appeared_element = list1[index]

        count = 0
        processed.append(list1[index])  

print(f'Least Appeared Element: {least_appeared_element}')
print(f'Appeared: {least_appeared_count} times')