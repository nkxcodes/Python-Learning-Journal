# Question:
# Ask the user to enter a sentence, split it into words, and sort the words based on their length.

sentence = input('Enter a Sentence: ')

words_list = sentence.split()

words_list.sort(key=len)

print(words_list)