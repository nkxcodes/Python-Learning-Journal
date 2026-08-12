# Return minimum element.

def find_min_element(u_list):
    min_element = u_list[0]
    for element in u_list:
        if element < min_element:
            min_element = element
    return min_element

result = find_min_element([1, 2, 3, 4, 5])

print(result)