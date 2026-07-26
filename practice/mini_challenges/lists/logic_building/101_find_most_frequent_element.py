# Question: 
# Find the element that appears the most number of times in a list

list1 = ["apple", "banana", "apple", "mango", "apple", "banana"]

count = 0

processed = []

previous_winner_count = 0

current_winner = ''

appeared_most = ''

for index in range(0, len(list1)):
    if list1[index] in processed:
        continue

    else:
        for index_2 in range(0, len(list1)):
            if list1[index] == list1[index_2]:
                count += 1

        if count > previous_winner_count:
            previous_winner_count = count
            current_winner = list1[index]
        
        count = 0
        processed.append(list1[index])

print(f'Winner: {current_winner}')
print(f'Appeared: {previous_winner_count}')