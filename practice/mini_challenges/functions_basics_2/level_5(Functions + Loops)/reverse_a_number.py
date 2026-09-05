# Write a function reverses a number.

def reverse(number):
    original_number = number
    reverse_number = 0
    is_negative = False

    if original_number < 0:
        is_negative = True
        original_number = abs(original_number)

    if original_number == 0:
        return original_number

    while original_number > 0:
        reverse_number = reverse_number * 10
        reverse_number += original_number % 10
        original_number = original_number // 10
    
    if is_negative:
        return reverse_number * (-1)
    else:
        return reverse_number

result = reverse(-9811)

print(result)