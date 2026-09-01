# Write a function that prints odd numbers from 1 to n.

def odd_to(n):
    for num in range(1, n + 1):
        if num % 2 != 0:
            print(num)

odd_to(20)