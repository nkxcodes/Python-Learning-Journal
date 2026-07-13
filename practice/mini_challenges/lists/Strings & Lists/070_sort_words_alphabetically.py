# Question:
# Ask the user to enter a sentence, split it into words, and sort the words in alphabetical order.

sentence = input('Enter a Sentence: ')

words_list = sentence.split()

words_list.sort()

print(f'Sorted List: {words_list}')