# Write a function that checks whether a number is divisible by 5.

def is_divisible_by_5(number):
    if number % 5 == 0:
        return True
    else:
        return False

result = is_divisible_by_5(25)

print(result)