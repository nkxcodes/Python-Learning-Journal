# Write a function that calculates the sum of digits of a number.

def total_sum(integer):
    total_sum = 0
    number = str(integer)

    if number[0] == '-':
        number = number[1::]

    for char in number:
        total_sum += int(char)

    return total_sum

result = total_sum(9811)

print(result)