# Return common elements.

def find_common_elements(u_list_1, u_list_2):
    common_elements = []
    for element in u_list_1:
        if element in u_list_2:
            common_elements.append(element)
    return common_elements

result = find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])

print(result)