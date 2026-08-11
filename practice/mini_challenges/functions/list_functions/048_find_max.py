# Return maximum element.

def find_max_element(u_list):
    max_element = 0
    for element in u_list:
        if element > max_element:
            max_element = element
    return max_element

result = find_max_element([1, 2, 3, 4, 5])

print(result)