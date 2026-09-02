# Write a function that returns the sum of even number from 1 to n

def sum_of_odd(n):
    total_sum = 0
    for num in range(1, n + 1):
        if num % 2 != 0:
            total_sum += num
    return total_sum

result = sum_of_odd(20)

print(result)