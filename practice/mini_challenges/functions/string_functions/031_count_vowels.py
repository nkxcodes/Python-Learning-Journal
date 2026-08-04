# Return total vowels

def total_vowels_in(u_string):
    total_vowels = 0
    for ch in u_string:
        if (ch == 'a' or 
            ch == 'e' or
            ch == 'i' or
            ch == 'o' or
            ch == 'u'):
            total_vowels += 1
    return total_vowels

total_vowels_in_programming = total_vowels_in('programming')

print(f'Total Vowels: {total_vowels_in_programming}')
