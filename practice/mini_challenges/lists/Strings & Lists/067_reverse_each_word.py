# Question:
# Ask the user to enter a sentence, split it into words, and reverse every individual word while keeping the word order the same.

sentence = input('Enter a Sentence: ')

words_list = sentence.split()

for index in range(0, len(words_list)):
    words_list[index] = words_list[index][::-1]

print(f'Reserve words list: {words_list}')