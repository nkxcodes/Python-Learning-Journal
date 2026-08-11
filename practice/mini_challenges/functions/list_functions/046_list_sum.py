# Return sum of list.

def sum_of_list(u_list):
    total_sum = 0
    for element in u_list:
        total_sum += element
    return total_sum

result = sum_of_list([1, 2, 3, 4, 5])

print(result)