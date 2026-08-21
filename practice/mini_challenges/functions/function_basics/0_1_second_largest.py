# Find second largest number.

def second_largest(u_list):
    second_largest = 0
    largest_number = 0

    for element in u_list:
        if element > largest_number:
            largest_number = element
    
    for element in u_list:
        if element == largest_number:
            continue
        if element > second_largest:
            second_largest = element

    return second_largest

result = second_largest([1, 2, 3, 45, 350])

print(result)