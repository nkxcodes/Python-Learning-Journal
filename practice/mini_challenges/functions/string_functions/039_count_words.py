# Return total words

def count(u_string):
    count = 0
    for ch in u_string:
        count += 1
    return count

result = count('Programming')

print(result)