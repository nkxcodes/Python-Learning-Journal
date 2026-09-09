# Write a function that counts spaces in a string.

def count_spaces(u_string):
    count = 0
    for ch in u_string:
        if ch == ' ':
            count += 1
    return count

result = count_spaces('P R O G R A M M I N G')

print(result)