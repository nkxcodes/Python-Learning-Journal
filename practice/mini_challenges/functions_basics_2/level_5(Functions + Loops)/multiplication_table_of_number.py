# Write a function that prints the multiplication table of a number.

def multiplication_of(n):
    for num in range(1, 11):
        print(f'{n} x {num} = {n * num}')

multiplication_of(5)