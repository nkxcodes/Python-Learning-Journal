# Return second largest element

def find_second_largest_element(u_list):
    largest_element = 0
    second_largest = 0
    for element in u_list:
        if element > largest_element:
            largest_element = element
    for element in u_list:
        if element == largest_element:
            continue
        if element > second_largest:
            second_largest = element
    return second_largest

result = find_second_largest_element([1, 2, 3, 4, 5])

print(result)