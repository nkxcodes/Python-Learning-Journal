# Password Checker
#
# Description:
# Build a simple password checker that validates a password using
# comparison, logical, and membership operators.
#
# Example:
# Enter password: Python@123
#
# Output:
# Password accepted.



password = input('Enter password: ')

minimun_length = 6
maximum_length = 20
specific_character = '@'

if password == '':
    print('Invalid Password')

if (
    len(password) > minimun_length 
    and len(password) < 20 
    and password.count(specific_character) == 1 
    and password[0].isalpha() 
    and password[0].isupper()
):
    print('Password Accepted')
else:
    print('Password Not Accepted')