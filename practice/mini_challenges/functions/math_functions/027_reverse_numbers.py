# Return reversed digits

def reverse_number(u_number):
    reversed_number = 0

    while u_number > 0:
        reversed_number = reversed_number * 10
        reversed_number += u_number % 10
        u_number = u_number // 10

    return reversed_number

result = reverse_number(908)

print(result)