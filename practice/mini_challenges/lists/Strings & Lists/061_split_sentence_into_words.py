# Question:
# Ask the user to enter a sentence and convert it into a list of words.

sentence = input('Enter a Sentence: ')

char_list = []

for char in sentence:
    char_list.append(char)

print(char_list)