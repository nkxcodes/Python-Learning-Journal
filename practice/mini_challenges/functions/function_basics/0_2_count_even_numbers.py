# Count even numbers

def even_numbers(u_list):
    even_numbers = 0

    for element in u_list:
        if element % 2 == 0:
            even_numbers += 1
    
    return even_numbers

result = even_numbers([1, 2, 3, 4, 5, 6])

print(result)