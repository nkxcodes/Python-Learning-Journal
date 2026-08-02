# Return sum of first N natural numbers.

def sum_of(numbers):
    sum = 0
    for num in range(numbers + 1):
        sum += num
    return sum

sum_of_10_natural_numbers = sum_of(10)

print(sum_of_10_natural_numbers)
