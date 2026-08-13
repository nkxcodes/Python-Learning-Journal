# Return total even numbers.

def find_total_even_number(u_list):
    even_numbers = 0
    for element in u_list:
        if element % 2 == 0:
            even_numbers += 1
    return even_numbers

result = find_total_even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(result)