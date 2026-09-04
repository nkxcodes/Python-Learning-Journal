# Write a function that counts the number of digits in an integer.

def count_digits(integer):
    count = 0
    number = str(integer)

    if number[0] == '-':
        number = number[1::]

    for digits in number:
        count += 1

    return count

result = count_digits(-9811)

print(result)