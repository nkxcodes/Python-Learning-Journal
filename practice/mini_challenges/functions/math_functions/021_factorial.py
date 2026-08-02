def factorial_of(number):
    factorial = 0
    for num in range(1, number):
        factorial += num

    return factorial

factorial_of_10 = factorial_of(10)

print(factorial_of_10)
