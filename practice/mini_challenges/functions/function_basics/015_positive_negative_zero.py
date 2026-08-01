# Return positive, negative, zero

def is_positive_negative_zero(number):
    if number > 0:
        return 'Positive'
    elif number < 0:
        return 'Negative'
    else:
        return 'Zero'

is_positive = is_positive_negative_zero(10)
is_negative = is_positive_negative_zero(-10)
is_zero = is_positive_negative_zero(0)

print(is_positive)
print(is_negative)
print(is_zero)