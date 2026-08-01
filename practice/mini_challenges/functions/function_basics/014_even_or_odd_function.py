# Return whether a number is even or odd

def check_even_or_odd(number):
    if number % 2 != 0:
        return 'Odd'
    else:
        return 'Even'

is_even = check_even_or_odd(23)

print(is_even)