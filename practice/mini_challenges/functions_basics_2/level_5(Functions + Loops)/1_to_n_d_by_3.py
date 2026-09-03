# Write a function that counts how many numbeers from 1 to n are divisible by 3.

def divisible_by_3(n):
    count = 0
    for num in range(1, n + 1):
        if num % 3 == 0:
            count += 1
    return count

result = divisible_by_3(20)

print(result)