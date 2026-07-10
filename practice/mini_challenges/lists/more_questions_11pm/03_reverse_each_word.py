# ==========================================================
# Question 65
# Ask the user to enter a sentence.
#
# Reverse every individual word while keeping
# the words in the same order.
#
# Example:
# Input:
# Python is fun
#
# Output:
# nohtyP si nuf
#
# Goal:
# Practice string slicing, loops,
# and building new strings.
# ==========================================================

sentence = input('Enter a Sentence: ')

sentence = sentence[::-1]

print(sentence)