# Return total odd numbers.

def find_total_odd_numbers(u_list):
    odd_numbers = 0
    for element in u_list:
        if element % 2 != 0:
            odd_numbers += 1
    return odd_numbers

result = find_total_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(result)