# Print all odd numbers from 1 to n.

def odd_numbers(n):
    if n == 0:
        return
    
    odd_numbers(n - 1)
    if n % 2 != 0:
        print(n)

odd_numbers(10)