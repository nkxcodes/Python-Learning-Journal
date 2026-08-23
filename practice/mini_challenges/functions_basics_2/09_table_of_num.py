# Write a function that prints a multiplication table of any number.

def table_of(num):
    for number in range(1, 11):
        print(f'{num} x {number} = {num * number}')

table_of(2)