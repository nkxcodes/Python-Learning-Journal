# Rotate list by k positions.

def rotate_list(u_list, k):
    rotated_list = u_list[-k:] + u_list[:-k]
    return rotated_list

result = rotate_list([10, 20, 30, 40, 50], 2)

print(result)