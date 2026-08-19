# Print all even numbers from 1 to n.

def even_numbers(n):
    if n == 0:
        return

    even_numbers(n - 1)
    if n % 2 == 0:
        print(n)

even_numbers(10)