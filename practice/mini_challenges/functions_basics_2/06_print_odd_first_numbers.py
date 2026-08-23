# Write a function that prints the first 10 odd numbers.

def first_10_odd_numbers():
    for num in range(1, 21):
        if num % 2 != 0:
            print(num)

first_10_odd_numbers()