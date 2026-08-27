# Write a function that checks whether a number is divisible by both 3 and 5.

def is_divisible_by_3_and_5(number):
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False

result = is_divisible_by_3_and_5(15)

print(result)