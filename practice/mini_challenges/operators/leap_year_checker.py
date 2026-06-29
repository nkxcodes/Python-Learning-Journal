# Leap Year Checker
#
# Description:
# Determine whether a given year is a leap year using logical operators.
#
# Example:
# Enter a year: 2024
#
# Output:
# 2024 is a leap year.

year = int(input('Enter a year: '))

leap = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True
else:
    leap = False

if leap:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')