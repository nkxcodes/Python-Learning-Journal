# Write a function that checks whether a character is a vowel.

def is_vowel(char):
    if len(char) > 1:
        return 'Character cannot be more than 1.'

    if (char == 'a' or
        char == 'e' or
        char == 'i' or
        char == 'o' or
        char == 'u'):
        return True
    else:
        return False 

result = is_vowel('a')

print(result)