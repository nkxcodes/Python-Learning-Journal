# Write a function that takes three numbers and prints the largest.

def largest_number(n1, n2, n3):
    largest_number = n1

    if n2 > largest_number:
        largest_number = n2

    if n3 > largest_number:
        largest_number = n3

    return largest_number

result = largest_number(9, 7, 8)

print(result)    