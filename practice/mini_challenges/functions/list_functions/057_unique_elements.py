# Return unique elements.

def find_unique_elements(u_list):
    unique_elements = []
    count = 0
    for element in u_list:
        for index in range(0, len(u_list)):
            if element == u_list[index]:
                count += 1
        if count == 1:
            unique_elements.append(element)
        count = 0
    return unique_elements

result = find_unique_elements([10, 20, 20, 30, 40, 40, 50])

print(result)