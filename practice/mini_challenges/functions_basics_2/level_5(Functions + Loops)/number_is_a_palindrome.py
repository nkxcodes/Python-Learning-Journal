# Write a function that checks whether a number is a palindrome.

def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while original_number > 0:
        reversed_number = reversed_number * 10
        reversed_number += original_number % 10
        original_number = original_number // 10

    return number == reversed_number

result = is_palindrome(1111)

print(result)