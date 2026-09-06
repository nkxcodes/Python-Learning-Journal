# Write a function that returns the length of a string.

def len_of(string):
    length = 0
    for ch in string:
        length += 1
    return length

result = len_of('Programming')

print(result)