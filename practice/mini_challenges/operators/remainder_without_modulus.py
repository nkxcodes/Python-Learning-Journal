# Remainder Without %
#
# Description:
# Calculate the remainder of two numbers without using the modulus (%)
# operator.
#
# Example:
# Enter dividend: 17
# Enter divisor: 5
#
# Output:
# Remainder: 2

dividend = int(input('Enter dividend: '))
divisor = int(input('Enter divisor: '))

remainder = dividend - (divisor * (dividend // divisor))

print(f'Remainder: {remainder}')