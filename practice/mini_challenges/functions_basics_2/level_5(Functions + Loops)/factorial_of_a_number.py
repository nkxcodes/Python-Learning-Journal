# Write a function that returns the factorial of a number.

def factorial_of(number):
    factorial = 0
    for num in range(10, 1, -1):
        factorial += number
    return factorial

result = factorial_of(10)

print(result)