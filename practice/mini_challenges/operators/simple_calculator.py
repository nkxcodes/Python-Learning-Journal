# Simple Calculator
#
# Description:
# Create a calculator that performs addition, subtraction,
# multiplication, division, floor division, modulus, and exponentiation.
#
# Example:
# Enter first number: 10
# Enter second number: 3
# Choose operator: //
#
# Output:
# Result: 3

first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))

choosed_operator = input('Choose Operator: ')
result = 0

if choosed_operator == '+':
    result = first_num + second_num
elif choosed_operator == '-':
    result = first_num - second_num
elif choosed_operator == '*':
    result = first_num * second_num
elif choosed_operator == '/':
    if second_num == 0:
        print('Cannot divide by zero')
    else:
        result = first_num / second_num
elif choosed_operator == '//':
    if second_num == 0:
        print('Cannot divide by zero')
    else:
        result = first_num // second_num
elif choosed_operator == '%':
    result = first_num % second_num
elif choosed_operator == '**':
    result = first_num ** second_num
else:
    print('Invalid Operator')

print(f'Result: {result}')

    