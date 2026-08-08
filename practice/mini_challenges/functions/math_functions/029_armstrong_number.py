# Check Armstrong number

def is_armstrong(u_number):
    original_number = u_number
    total_digits = 0
    working_number = 0

    while u_number > 0:
        original_number = original_number // 10
        total_digits += 1

    while u_number > 0:
        working_number = u_number % 10 ** total_digits
        u_number = u_number // 10

    if working_number == u_number:
        return True
    else:
        return False

result = is_armstrong(153)

print(result)