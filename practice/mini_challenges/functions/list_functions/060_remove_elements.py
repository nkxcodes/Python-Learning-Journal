# Return all occurences of an element.

def remove_element(u_list, r_element):
    new_list = []
    for element in u_list:
        if element == r_element:
            continue
        else:
            new_list.append(element)
    return new_list

result = remove_element([10, 20, 30, 20, 40, 20, 50], 20)

print(result)