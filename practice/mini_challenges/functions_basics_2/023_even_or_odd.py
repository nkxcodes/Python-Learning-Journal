# Write a function that takes a number and prints whether it is even or odd.

def even_or_odd(number):
    if number % 2 != 0:
        return 'Odd'
    else:
        return 'Even'

result = even_or_odd(18)

print(result)