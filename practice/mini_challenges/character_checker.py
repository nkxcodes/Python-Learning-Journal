# Character Checker
#
# Description:
# Check whether a character exists inside a string.
#
# Example:
# Enter a word: Python
# Enter a character: y
#
# Output:
# Character found.

word = input('Enter a Word: ')
character = input('Enter a Character: ')

print('')

if character in word:
    print('Character found.')
else:
    print('Character not found.')