# ==========================================================
# Question 61
# Ask the user to enter a sentence.
#
# Count and print:
# - Number of uppercase letters
# - Number of lowercase letters
#
# Example:
# Input:
# Hello WORLD
#
# Output:
# Uppercase: 6
# Lowercase: 4
#
# Goal:
# Practice looping through strings and checking
# individual characters.
# ==========================================================

sentence = input('Enter a Sentence: ')

uppercase = 0
lowercase = 0

for char in sentence:
    if char.isupper() == True:
        uppercase += 1
    else:
        lowercase += 1


print(f'Uppercase: {uppercase}')
print(f'Lowercase: {lowercase}')