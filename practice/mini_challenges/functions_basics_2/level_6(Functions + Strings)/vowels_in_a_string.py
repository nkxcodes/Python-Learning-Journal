# Write a function that counts vowels in a string.

def count_vowels(u_string):
    count = 0
    for ch in u_string:
        if (ch == 'a' or
            ch == 'A' or
            ch == 'e' or
            ch == 'E' or
            ch == 'i' or
            ch == 'I' or
            ch == 'o' or
            ch == 'O' or
            ch == 'u' or
            ch == 'U'):
            count += 1
    return count

result = count_vowels('Programming')

print(result)