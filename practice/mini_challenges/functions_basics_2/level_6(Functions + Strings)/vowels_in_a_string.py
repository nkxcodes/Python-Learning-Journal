# Write a function that counts vowels in a string.

def count_vowels(u_string):
    count = 0

    for ch in u_string:
        if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            count += 1

    return count

result = count_vowels('Programming')

print(result)