# Question:
# Create a new list containing only the palindrome numbers from the original list

list1 = [121, 45, 33, 123, 454, 67, 99, 101, 234, 1221]

palindrome_numbers = []


for index in range(0, len(list1)):
    is_palindrome = False
    original_number = list1[index]
    reversed_number = 0
    while original_number > 0:
        reversed_number = reversed_number * 10 # Make space for new digit
        reversed_number += original_number % 10 # Add last digit of original number
        original_number = original_number // 10 # Remove the last digit of original number

    if list1[index] == reversed_number:
        is_palindrome = True

    if is_palindrome:
        palindrome_numbers.append(list1[index])

print(palindrome_numbers)