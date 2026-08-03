# Return total vowels

def total_vowels_in(u_string):
    splited_string = u_string.split()
    print(splited_string)
    total_vowels = 0
    for word in splited_string:
        if (word == 'a' or 
            word == 'e' or
            word == 'i' or
            word == 'o' or
            word == 'u'):
            total_vowels += 1
    return total_vowels

total_vowels_in_programming = total_vowels_in('programming')

print(f'Total Vowels: {total_vowels_in_programming}')
