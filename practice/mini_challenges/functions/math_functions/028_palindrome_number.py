# Return True if number is palindrome

def is_palindrome(number):
    original_number = number
    reversed_number = 0
    while original_number > 0:
        reversed_number = reversed_number * 10
        reversed_number += original_number % 10
        original_number = original_number // 10
    return number == reversed_number

is_232_is_palindrome = is_palindrome(232)

print(is_232_is_palindrome)
