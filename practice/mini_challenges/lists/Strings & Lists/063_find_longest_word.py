# Question:
# Ask the user to enter a sentence, split it into words, and find the longest word.

sentence = input('Enter a Sentence: ')

words_list = sentence.split()

longest_word_length = 0

longest_word = ''

for word in words_list:
    word_length = len(word)
    if word_length > longest_word_length:
        longest_word_length = word_length
        longest_word = word

print(f'Longest Word: {longest_word}')