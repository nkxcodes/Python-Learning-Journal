# Find smallest number

def smallest_number(u_list):
    smallest_number = u_list[0]

    for element in u_list:
        if element < smallest_number:
            smallest_number = element

    return smallest_number

result = smallest_number([0, 1, 2, 3, 4, 5, 6])

print(result)