# Write a function that checks whether a character is an alphabet.

def is_alphabet(char):
    if char.isalpha():
        return True
    else:
        return False

result = is_alphabet('9')

print(result)