# Return list without duplicates

def remove_duplicates(u_list):
    processed = []
    for index in range(len(u_list) - 1, -1, -1):
        if u_list[index] in processed:
            u_list.pop(index)
        else:
            processed.append(u_list[index])
    return u_list

result = remove_duplicates([1, 2, 3, 2, 4, 4, 5])

print(result)