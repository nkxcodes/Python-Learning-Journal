# Even or Odd Checker
#
# Description:
# Ask the user for a number and determine whether it is even or odd
# using an operator.
#
# Example:
# Enter a number: 18
#
# Output:
# 18 is even.

number = int(input('Enter A Number: '))

if number % 2 == 0:
    print(f'{number} is Even')
else:
    print(f'{number} is Odd')