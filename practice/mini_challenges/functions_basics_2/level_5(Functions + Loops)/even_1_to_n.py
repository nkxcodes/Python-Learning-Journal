# Write a function that prints even numbers from 1 to n.

def even_to(n):
    for num in range(1, n+1):
        if num % 2 == 0:
            print(num)

even_to(20)