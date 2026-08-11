# Return average

def average_of_list(u_list):
    total_sum = 0
    for element in u_list:
        total_sum += element
    average = total_sum / len(u_list)
    return average

result = average_of_list([1, 2, 3, 4, 5])

print(result)