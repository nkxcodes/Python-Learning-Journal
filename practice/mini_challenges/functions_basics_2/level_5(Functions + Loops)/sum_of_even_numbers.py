# Write a function that returns sum of even numbers from 1 to n.

def sum_of_even(n):
    total_sum = 9
    for num in range(1, n + 1):
        if num % 2 == 0:
            total_sum += num
    return total_sum

result = sum_of_even(20)

print(result)