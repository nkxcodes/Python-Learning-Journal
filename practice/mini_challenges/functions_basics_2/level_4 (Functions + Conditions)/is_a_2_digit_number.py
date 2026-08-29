# Write a function that checks whether a number is a two digit number.

def is_two_digit_number(number):
    if number < 0:
        number = str(number)
        number =  number[1:]
    else:
        number = str(number)
    if len(number) == 2:
        return "It's a two digit number"
    else:
        return "It's not a two digit number"


result = is_two_digit_number(-24)

print(result)