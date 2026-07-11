# Question:
# Ask the user to enter a sentence, split it into words, and find the shortest word.

sentence = input('Enter a Number: ')

words_list = sentence.split()

shortest_word_length = len(words_list[1])

shortest_word = ''

for word in words_list:
    word_length = len(word)
    if word_length <  shortest_word_length:
        shortest_word_length = word_length
        shortest_word = word

print(f'Shortest Word: {shortest_word}')