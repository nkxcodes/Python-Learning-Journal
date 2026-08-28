# Write a function that checks whether a number is a multiple of 10.

def multiple_of_10(number):
    if number % 10 == 0:
        return True
    else:
        return False

result = multiple_of_10(14)

print(result)