# Create a function that accepts three numbers and returns the largest.

def largest_number(num1, num2, num3):
    numbers = [num1, num2, num3]
    largest_number = 0
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return largest_number

largest_number = largest_number(9, 10, 34)

print(largest_number)
