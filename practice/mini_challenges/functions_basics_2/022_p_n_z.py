# Write a function that takes a number and prints whether it is positive, negative, or zero.

def number_status(number):
    if number == 0:
        return 'Zero'
    if number > 0:
        return 'Positive'
    if number < 0:
        return 'Negative'

result = number_status(-1)

print(result)