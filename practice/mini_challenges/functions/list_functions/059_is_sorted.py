# Return True if list is sorted.

def is_sorted(u_list):
    sorted = True
    for index in range(0, len(u_list) - 1):
        if u_list[index] < u_list[index + 1]:
            continue
        else:
            sorted = False
    return sorted

result = is_sorted([1, 7, 8, 4, 5])

print(result)