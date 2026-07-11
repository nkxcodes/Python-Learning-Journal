# Question:
# Ask the user to enter a sentence, convert it into a list of words, and count the total number of words.

sentence = input('Enter a Sentence: ')

words_list = []

count = 0

for word in sentence:
    words_list.append(word)

for word in sentence:
    count += 1

print(f'Words: {count}')