# Check Perfect Number.

def is_perfect(u_number):
    total = 0

    for divisor in range(1, u_number):
        if u_number % divisor == 0:
            total += divisor

    if total == u_number:
        return True
    else:
        return False

result = is_perfect(12)

print(result)