# Write a function that checks whether a year is a leap year.

def is_leap_year(year):
    if year % 400 == 0:
        return True
    else:
        if year % 100 == 0:
            return False
        else:
            if year % 4 == 0:
                return True
            else:
                return False

result = is_leap_year(2009)

print(result)