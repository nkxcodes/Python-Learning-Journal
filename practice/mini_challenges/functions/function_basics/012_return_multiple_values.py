# Return quotient and remainder together.

def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

quotient, remainder = divide(24, 4)

print(f'Quotient: {quotient}')
print(f'Remainder: {remainder}')