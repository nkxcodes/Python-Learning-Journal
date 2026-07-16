# Question:
# Ask the user to enter a sentence, split it into words, and remove duplicate words while keeping only one occurrence of each word.

sentence = input('Enter a Sentence: ')

words_list = sentence.split()

unique_words = []

for word in words_list:
    if word in unique_words:
        continue
    unique_words.append(word)

print(f'List: {unique_words}')