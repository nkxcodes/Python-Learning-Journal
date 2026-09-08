# Write a function that counts consonants in a string.

def count_consonants(u_string):
    count = 0
    for ch in u_string:
        if ch not in ['a', 'e', 'i', 'o', 'u',
                      'A', 'E', 'I', 'O', 'U']:
                      count += 1
    return count

result = count_consonants('Programming')

print(result)