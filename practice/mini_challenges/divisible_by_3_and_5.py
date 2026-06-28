# Divisible by 3 and 5
#
# Description:
# Check whether a number is divisible by both 3 and 5.
#
# Example:
# Enter a number: 45
#
# Output:
# 45 is divisible by both 3 and 5.

number = int(input('Enter a Number: '))

is_divisible_by_3 = False
is_divisible_by_5 = False

if number % 3 == 0 and number % 5 == 0:
    is_divisible_by_3 = True 
    is_divisible_by_5 = True
elif number % 3 == 0:
    is_divisible_by_3 = True
elif number % 5 == 0:
    is_divisible_by_5 = True

if is_divisible_by_3 and is_divisible_by_5:
    print(f'{number} is divisible by both 3 and 5')
elif is_divisible_by_3:
    print(f'{number} is only divsible by 3')
elif is_divisible_by_5:
    print(f'{number} is only divisible by 5')
else:
    print(f'{number} is not divisible by neither 3 nor 5')