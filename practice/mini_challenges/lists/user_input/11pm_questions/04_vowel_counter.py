# ==========================================================
# Question 7: Count the Vowels
#
# Ask the user to enter a word or sentence.
# Count how many vowels (a, e, i, o, u) are present.
#
# Example:
# Input:
# Education
#
# Output:
# Number of vowels = 5
#
# Hint:
# Check each character one by one.
# ==========================================================

sentence = input('Enter a Sentence: ')

count = 0

for char in sentence:
    if (char == 'a' or
        char == 'e' or
        char == 'i' or
        char == 'o' or
        char == 'u'):
        count += 1

print(f'Number of vowels = {count}')