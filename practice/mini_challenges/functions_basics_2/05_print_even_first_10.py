# Write a function that prints the first 10 even numbers.

def first_10_even_numbers():
    for num in range(1, 21):
        if num % 2 == 0:
            print(num)

first_10_even_numbers()